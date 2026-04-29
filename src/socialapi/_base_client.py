from __future__ import annotations

import asyncio
import logging
import random
import time
from typing import TYPE_CHECKING, Any, TypeVar, cast

import httpx

from socialapi._config import ClientConfig  # noqa: TC001
from socialapi._constants import USER_AGENT_PREFIX
from socialapi._exceptions import (
    APIConnectionError,
    APIStatusError,
    APITimeoutError,
)
from socialapi._version import __version__

if TYPE_CHECKING:
    from pydantic import BaseModel

    from socialapi._pagination import AsyncCursorPage, CursorPage

logger = logging.getLogger("socialapi")

T = TypeVar("T", bound="BaseModel")

# HTTP status codes that should be retried.
_RETRYABLE_STATUS_CODES: frozenset[int] = frozenset({408, 409, 429, 500, 502, 503, 504})

# Maximum seconds to honour from a Retry-After header.
_MAX_RETRY_AFTER: float = 60.0

# Exponential backoff parameters.
_BACKOFF_BASE: float = 0.5
_BACKOFF_MAX: float = 8.0


def _build_query_params(params: dict[str, Any] | None) -> dict[str, str]:
    """Flatten *params* into a ``str -> str`` mapping suitable for httpx.

    ``None`` values are dropped. ``bool`` is lowered to ``"true"``/``"false"``.
    ``list`` values are joined with commas (the convention used by the SocialAPI
    ``account_ids`` filter).
    """
    if not params:
        return {}
    out: dict[str, str] = {}
    for key, value in params.items():
        if value is None:
            continue
        if isinstance(value, bool):
            out[key] = "true" if value else "false"
        elif isinstance(value, list):
            out[key] = ",".join(str(v) for v in cast("list[Any]", value))
        else:
            out[key] = str(value)
    return out


def _calculate_retry_delay(retries_taken: int, response: httpx.Response | None) -> float:
    """Return seconds to sleep before the next retry attempt.

    Respects ``Retry-After`` when present (capped at 60 s), otherwise falls
    back to exponential backoff with full jitter.
    """
    if response is not None:
        retry_after = response.headers.get("retry-after")
        if retry_after is not None:
            try:
                delay = float(retry_after)
                return min(delay, _MAX_RETRY_AFTER)
            except ValueError:
                pass  # non-numeric Retry-After, fall through to backoff

    calculated = min(_BACKOFF_MAX, _BACKOFF_BASE * (2**retries_taken))
    return random.random() * calculated


def _should_retry_status(status_code: int) -> bool:
    """Return ``True`` if *status_code* is eligible for retry."""
    return status_code in _RETRYABLE_STATUS_CODES


# ---------------------------------------------------------------------------
# Sync client
# ---------------------------------------------------------------------------


class BaseSyncClient:
    """Shared HTTP logic for the synchronous client.

    Wraps ``httpx.Client``, injects auth headers, handles retries,
    and maps error responses to SDK exceptions.
    """

    _config: ClientConfig
    _client: httpx.Client

    def __init__(self, config: ClientConfig, *, http_client: httpx.Client | None = None) -> None:
        self._config = config
        if http_client is not None:
            self._client = http_client
        else:
            self._client = httpx.Client(
                timeout=httpx.Timeout(config.timeout),
            )

    # -- public helpers --------------------------------------------------------

    @property
    def base_url(self) -> str:
        return self._config.base_url

    @property
    def api_key(self) -> str:
        return self._config.api_key

    # -- header construction ---------------------------------------------------

    def _build_headers(self) -> dict[str, str]:
        return {
            "Authorization": f"Bearer {self._config.api_key}",
            "User-Agent": f"{USER_AGENT_PREFIX}/{__version__}",
            "Accept": "application/json",
        }

    # -- core request execution ------------------------------------------------

    def _request(
        self,
        method: str,
        path: str,
        *,
        params: dict[str, Any] | None = None,
        json_body: dict[str, Any] | None = None,
        timeout: float | None = None,
    ) -> httpx.Response:
        """Build, send and retry an HTTP request.  Returns the raw response."""
        url = f"{self._config.base_url}{path}"
        query = _build_query_params(params)
        headers = self._build_headers()

        request = self._client.build_request(
            method,
            url,
            params=query,
            json=json_body,
            headers=headers,
            timeout=httpx.Timeout(timeout) if timeout is not None else None,
        )

        if self._config.debug:
            logger.debug(
                "Request: %s %s headers=%s params=%s body=%s",
                method,
                url,
                headers,
                query,
                json_body,
            )

        retries_taken = 0
        max_retries = self._config.max_retries

        while True:
            response: httpx.Response | None = None
            try:
                response = self._client.send(request)
            except httpx.TimeoutException as exc:
                if retries_taken >= max_retries:
                    raise APITimeoutError(
                        f"Request timed out: {exc}",
                        request=request,
                    ) from exc
                delay = _calculate_retry_delay(retries_taken, None)
                if self._config.debug:
                    logger.debug("Timeout, retrying in %.2fs (attempt %d/%d)", delay, retries_taken + 1, max_retries)
                time.sleep(delay)
                retries_taken += 1
                continue
            except httpx.ConnectError as exc:
                if retries_taken >= max_retries:
                    raise APIConnectionError(
                        f"Connection error: {exc}",
                        request=request,
                    ) from exc
                delay = _calculate_retry_delay(retries_taken, None)
                if self._config.debug:
                    logger.debug(
                        "Connection error, retrying in %.2fs (attempt %d/%d)", delay, retries_taken + 1, max_retries
                    )
                time.sleep(delay)
                retries_taken += 1
                continue

            if self._config.debug:
                logger.debug(
                    "Response: %d headers=%s body=%s",
                    response.status_code,
                    dict(response.headers),
                    response.text[:500] if response.text else "",
                )

            if _should_retry_status(response.status_code) and retries_taken < max_retries:
                delay = _calculate_retry_delay(retries_taken, response)
                if self._config.debug:
                    logger.debug(
                        "HTTP %d, retrying in %.2fs (attempt %d/%d)",
                        response.status_code,
                        delay,
                        retries_taken + 1,
                        max_retries,
                    )
                time.sleep(delay)
                retries_taken += 1
                continue

            if response.status_code >= 400:
                raise APIStatusError.from_response(response)

            return response

    # -- convenience HTTP verb methods -----------------------------------------

    def _get(
        self,
        path: str,
        *,
        params: dict[str, Any] | None = None,
        timeout: float | None = None,
    ) -> dict[str, Any]:
        """Send a GET request and return the parsed JSON body."""
        response = self._request("GET", path, params=params, timeout=timeout)
        data: dict[str, Any] = cast("dict[str, Any]", response.json())
        return data

    def _post(
        self,
        path: str,
        *,
        json: dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        timeout: float | None = None,
    ) -> dict[str, Any] | None:
        """Send a POST request and return the parsed JSON body."""
        response = self._request("POST", path, json_body=json, params=params, timeout=timeout)
        if response.status_code == 204 or not response.text:
            return None
        data: dict[str, Any] = cast("dict[str, Any]", response.json())
        return data

    def _put(
        self,
        path: str,
        *,
        json: dict[str, Any] | None = None,
        timeout: float | None = None,
    ) -> dict[str, Any] | None:
        """Send a PUT request and return the parsed JSON body."""
        response = self._request("PUT", path, json_body=json, timeout=timeout)
        if response.status_code == 204 or not response.text:
            return None
        data: dict[str, Any] = cast("dict[str, Any]", response.json())
        return data

    def _patch(
        self,
        path: str,
        *,
        json: dict[str, Any] | None = None,
        timeout: float | None = None,
    ) -> dict[str, Any] | None:
        """Send a PATCH request and return the parsed JSON body."""
        response = self._request("PATCH", path, json_body=json, timeout=timeout)
        if response.status_code == 204 or not response.text:
            return None
        data: dict[str, Any] = cast("dict[str, Any]", response.json())
        return data

    def _delete(
        self,
        path: str,
        *,
        params: dict[str, Any] | None = None,
        timeout: float | None = None,
    ) -> dict[str, Any] | None:
        """Send a DELETE request and return the parsed JSON body (if any)."""
        response = self._request("DELETE", path, params=params, timeout=timeout)
        if response.status_code == 204 or not response.text:
            return None
        data: dict[str, Any] = cast("dict[str, Any]", response.json())
        return data

    # -- paginated GET ---------------------------------------------------------

    def _get_paginated(
        self,
        path: str,
        *,
        params: dict[str, Any] | None = None,
        model: type[T],
        timeout: float | None = None,
        bind_ctx: dict[str, Any] | None = None,
    ) -> CursorPage[T]:
        """Send a GET request and return a ``CursorPage[T]``.

        Handles both response envelope shapes:
        1. ``{"data": [...], "pagination": {"has_more": bool, "next_cursor": str}}``
        2. ``{"data": [...], "cursor": str | null}``

        ``bind_ctx`` is forwarded to every model in the page (and to subsequent
        pages fetched via ``next_page``) so that bound models keep their context.
        """
        from socialapi._pagination import CursorPage as _CursorPage

        body = self._get(path, params=params, timeout=timeout)

        raw_items: list[Any] = body.get("data", [])
        items = [model.model_validate(item) for item in raw_items]

        # Detect envelope shape
        next_cursor: str | None
        pagination_raw: Any = body.get("pagination")
        if isinstance(pagination_raw, dict):
            pagination_dict = cast("dict[str, Any]", pagination_raw)
            has_more = bool(pagination_dict.get("has_more", False))
            cursor_val: Any = pagination_dict.get("next_cursor")
            next_cursor = str(cursor_val) if cursor_val is not None else None
        else:
            cursor_val2: Any = body.get("cursor")
            next_cursor = str(cursor_val2) if cursor_val2 is not None else None
            has_more = next_cursor is not None

        return _CursorPage(
            data=items,
            has_more=has_more,
            next_cursor=next_cursor,
            client=self,
            path=path,
            params=params or {},
            model=model,
            bind_ctx=bind_ctx,
        )

    # -- lifecycle -------------------------------------------------------------

    def close(self) -> None:
        """Close the underlying HTTP transport."""
        self._client.close()


# ---------------------------------------------------------------------------
# Async client
# ---------------------------------------------------------------------------


class BaseAsyncClient:
    """Shared HTTP logic for the asynchronous client.

    Wraps ``httpx.AsyncClient``, injects auth headers, handles retries,
    and maps error responses to SDK exceptions.
    """

    _config: ClientConfig
    _client: httpx.AsyncClient

    def __init__(self, config: ClientConfig, *, http_client: httpx.AsyncClient | None = None) -> None:
        self._config = config
        if http_client is not None:
            self._client = http_client
        else:
            self._client = httpx.AsyncClient(
                timeout=httpx.Timeout(config.timeout),
            )

    # -- public helpers --------------------------------------------------------

    @property
    def base_url(self) -> str:
        return self._config.base_url

    @property
    def api_key(self) -> str:
        return self._config.api_key

    # -- header construction ---------------------------------------------------

    def _build_headers(self) -> dict[str, str]:
        return {
            "Authorization": f"Bearer {self._config.api_key}",
            "User-Agent": f"{USER_AGENT_PREFIX}/{__version__}",
            "Accept": "application/json",
        }

    # -- core request execution ------------------------------------------------

    async def _request(
        self,
        method: str,
        path: str,
        *,
        params: dict[str, Any] | None = None,
        json_body: dict[str, Any] | None = None,
        timeout: float | None = None,
    ) -> httpx.Response:
        """Build, send and retry an HTTP request.  Returns the raw response."""
        url = f"{self._config.base_url}{path}"
        query = _build_query_params(params)
        headers = self._build_headers()

        request = self._client.build_request(
            method,
            url,
            params=query,
            json=json_body,
            headers=headers,
            timeout=httpx.Timeout(timeout) if timeout is not None else None,
        )

        if self._config.debug:
            logger.debug(
                "Request: %s %s headers=%s params=%s body=%s",
                method,
                url,
                headers,
                query,
                json_body,
            )

        retries_taken = 0
        max_retries = self._config.max_retries

        while True:
            response: httpx.Response | None = None
            try:
                response = await self._client.send(request)
            except httpx.TimeoutException as exc:
                if retries_taken >= max_retries:
                    raise APITimeoutError(
                        f"Request timed out: {exc}",
                        request=request,
                    ) from exc
                delay = _calculate_retry_delay(retries_taken, None)
                if self._config.debug:
                    logger.debug("Timeout, retrying in %.2fs (attempt %d/%d)", delay, retries_taken + 1, max_retries)
                await asyncio.sleep(delay)
                retries_taken += 1
                continue
            except httpx.ConnectError as exc:
                if retries_taken >= max_retries:
                    raise APIConnectionError(
                        f"Connection error: {exc}",
                        request=request,
                    ) from exc
                delay = _calculate_retry_delay(retries_taken, None)
                if self._config.debug:
                    logger.debug(
                        "Connection error, retrying in %.2fs (attempt %d/%d)", delay, retries_taken + 1, max_retries
                    )
                await asyncio.sleep(delay)
                retries_taken += 1
                continue

            if self._config.debug:
                logger.debug(
                    "Response: %d headers=%s body=%s",
                    response.status_code,
                    dict(response.headers),
                    response.text[:500] if response.text else "",
                )

            if _should_retry_status(response.status_code) and retries_taken < max_retries:
                delay = _calculate_retry_delay(retries_taken, response)
                if self._config.debug:
                    logger.debug(
                        "HTTP %d, retrying in %.2fs (attempt %d/%d)",
                        response.status_code,
                        delay,
                        retries_taken + 1,
                        max_retries,
                    )
                await asyncio.sleep(delay)
                retries_taken += 1
                continue

            if response.status_code >= 400:
                raise APIStatusError.from_response(response)

            return response

    # -- convenience HTTP verb methods -----------------------------------------

    async def _get(
        self,
        path: str,
        *,
        params: dict[str, Any] | None = None,
        timeout: float | None = None,
    ) -> dict[str, Any]:
        """Send a GET request and return the parsed JSON body."""
        response = await self._request("GET", path, params=params, timeout=timeout)
        data: dict[str, Any] = cast("dict[str, Any]", response.json())
        return data

    async def _post(
        self,
        path: str,
        *,
        json: dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        timeout: float | None = None,
    ) -> dict[str, Any] | None:
        """Send a POST request and return the parsed JSON body."""
        response = await self._request("POST", path, json_body=json, params=params, timeout=timeout)
        if response.status_code == 204 or not response.text:
            return None
        data: dict[str, Any] = cast("dict[str, Any]", response.json())
        return data

    async def _put(
        self,
        path: str,
        *,
        json: dict[str, Any] | None = None,
        timeout: float | None = None,
    ) -> dict[str, Any] | None:
        """Send a PUT request and return the parsed JSON body."""
        response = await self._request("PUT", path, json_body=json, timeout=timeout)
        if response.status_code == 204 or not response.text:
            return None
        data: dict[str, Any] = cast("dict[str, Any]", response.json())
        return data

    async def _patch(
        self,
        path: str,
        *,
        json: dict[str, Any] | None = None,
        timeout: float | None = None,
    ) -> dict[str, Any] | None:
        """Send a PATCH request and return the parsed JSON body."""
        response = await self._request("PATCH", path, json_body=json, timeout=timeout)
        if response.status_code == 204 or not response.text:
            return None
        data: dict[str, Any] = cast("dict[str, Any]", response.json())
        return data

    async def _delete(
        self,
        path: str,
        *,
        params: dict[str, Any] | None = None,
        timeout: float | None = None,
    ) -> dict[str, Any] | None:
        """Send a DELETE request and return the parsed JSON body (if any)."""
        response = await self._request("DELETE", path, params=params, timeout=timeout)
        if response.status_code == 204 or not response.text:
            return None
        data: dict[str, Any] = cast("dict[str, Any]", response.json())
        return data

    # -- paginated GET ---------------------------------------------------------

    async def _get_paginated(
        self,
        path: str,
        *,
        params: dict[str, Any] | None = None,
        model: type[T],
        timeout: float | None = None,
        bind_ctx: dict[str, Any] | None = None,
    ) -> AsyncCursorPage[T]:
        """Send a GET request and return an ``AsyncCursorPage[T]``.

        Handles both response envelope shapes:
        1. ``{"data": [...], "pagination": {"has_more": bool, "next_cursor": str}}``
        2. ``{"data": [...], "cursor": str | null}``

        ``bind_ctx`` is forwarded to every model in the page (and to subsequent
        pages fetched via ``next_page``) so that bound models keep their context.
        """
        from socialapi._pagination import AsyncCursorPage as _AsyncCursorPage

        body = await self._get(path, params=params, timeout=timeout)

        raw_items: list[Any] = body.get("data", [])
        items = [model.model_validate(item) for item in raw_items]

        # Detect envelope shape
        next_cursor: str | None
        pagination_raw: Any = body.get("pagination")
        if isinstance(pagination_raw, dict):
            pagination_dict = cast("dict[str, Any]", pagination_raw)
            has_more = bool(pagination_dict.get("has_more", False))
            cursor_val: Any = pagination_dict.get("next_cursor")
            next_cursor = str(cursor_val) if cursor_val is not None else None
        else:
            cursor_val2: Any = body.get("cursor")
            next_cursor = str(cursor_val2) if cursor_val2 is not None else None
            has_more = next_cursor is not None

        return _AsyncCursorPage(
            data=items,
            has_more=has_more,
            next_cursor=next_cursor,
            client=self,
            path=path,
            params=params or {},
            model=model,
            bind_ctx=bind_ctx,
        )

    # -- lifecycle -------------------------------------------------------------

    async def close(self) -> None:
        """Close the underlying HTTP transport."""
        await self._client.aclose()
