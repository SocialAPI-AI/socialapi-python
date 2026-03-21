"""Shared base logic for sync and async clients."""

from __future__ import annotations

import time
from typing import TYPE_CHECKING, Any, TypeVar, overload

import httpx
from pydantic import BaseModel

from socialapi._exceptions import raise_for_status
from socialapi._retry import RetryHandler
from socialapi._version import __version__

if TYPE_CHECKING:
    from socialapi._config import ClientConfig
    from socialapi._types import Headers, QueryParams

T = TypeVar("T", bound=BaseModel)


class SyncAPIClient:
    """Synchronous HTTP client for the SocialAPI.

    Provides ``_get``, ``_post``, ``_patch``, ``_delete`` convenience
    methods that handle retries, error raising, and optional Pydantic
    response parsing.

    Args:
        config: Client configuration (api_key, base_url, timeout, max_retries).
        http_client: Optional pre-configured ``httpx.Client`` for advanced use.
    """

    config: ClientConfig

    def __init__(
        self,
        config: ClientConfig,
        *,
        http_client: httpx.Client | None = None,
    ) -> None:
        self.config = config
        self._retry = RetryHandler(config.max_retries)
        self._own_client = http_client is None
        self._http_client = http_client or httpx.Client(timeout=config.timeout)

    # ------------------------------------------------------------------
    # Header / URL helpers
    # ------------------------------------------------------------------

    def _build_headers(self, *, has_files: bool = False) -> Headers:
        """Build default request headers.

        Args:
            has_files: When ``True``, omit ``Content-Type`` so that httpx
                sets the correct multipart boundary automatically.

        Returns:
            A dictionary of HTTP headers.
        """
        headers: Headers = {
            "Authorization": f"Bearer {self.config.api_key}",
            "User-Agent": f"socialapi-python/{__version__}",
        }
        if not has_files:
            headers["Content-Type"] = "application/json"
        return headers

    def _build_url(self, path: str) -> str:
        """Construct the full URL for an API path.

        Args:
            path: The API path (e.g. ``/v1/accounts``).

        Returns:
            The complete URL.
        """
        base = self.config.base_url.rstrip("/")
        path = path.lstrip("/")
        return f"{base}/{path}"

    # ------------------------------------------------------------------
    # Core request method
    # ------------------------------------------------------------------

    def _request(
        self,
        method: str,
        path: str,
        *,
        params: QueryParams | None = None,
        json_data: dict[str, Any] | None = None,
        files: Any | None = None,
    ) -> httpx.Response:
        """Send an HTTP request with automatic retries and error handling.

        Args:
            method: HTTP method (``GET``, ``POST``, ``PATCH``, ``DELETE``).
            path: API path (e.g. ``/v1/accounts``).
            params: Optional query parameters. ``None`` values are stripped.
            json_data: Optional JSON body payload.
            files: Optional files for multipart uploads.

        Returns:
            The ``httpx.Response`` on success.

        Raises:
            SocialAPIError: Or a subclass, on non-2xx responses that are
                not retryable or after all retries are exhausted.
        """
        url = self._build_url(path)
        headers = self._build_headers(has_files=files is not None)
        clean_params = _strip_none(params) if params else None

        last_exc: Exception | None = None
        response: httpx.Response | None = None

        for attempt in range(self._retry.max_retries + 1):
            try:
                response = self._http_client.request(
                    method,
                    url,
                    headers=headers,
                    params=clean_params,
                    json=json_data,
                    files=files,
                )
            except (httpx.TimeoutException, httpx.NetworkError) as exc:
                last_exc = exc
                if self._retry.should_retry(None, attempt, is_network_error=True):
                    delay = self._retry.calculate_delay(attempt)
                    time.sleep(delay)
                    continue
                raise

            if response.is_success:
                return response

            if self._retry.should_retry(response, attempt):
                delay = self._retry.calculate_delay(attempt, response)
                time.sleep(delay)
                continue

            raise_for_status(response)

        # Exhausted retries -- raise last error.
        if last_exc is not None:
            raise last_exc
        if response is not None:
            raise_for_status(response)

        # Should be unreachable, but satisfies the type checker.
        raise RuntimeError("Unexpected state in retry loop")  # pragma: no cover

    # ------------------------------------------------------------------
    # Convenience methods
    # ------------------------------------------------------------------

    @overload
    def _get(
        self,
        path: str,
        *,
        params: QueryParams | None = ...,
        response_model: type[T],
    ) -> T: ...

    @overload
    def _get(
        self,
        path: str,
        *,
        params: QueryParams | None = ...,
        response_model: None = ...,
    ) -> Any: ...

    def _get(
        self,
        path: str,
        *,
        params: QueryParams | None = None,
        response_model: type[T] | None = None,
    ) -> T | Any:
        """Send a GET request.

        Args:
            path: API path.
            params: Optional query parameters.
            response_model: Optional Pydantic model class to parse the response into.

        Returns:
            A Pydantic model instance if ``response_model`` is provided,
            otherwise the parsed JSON response.
        """
        response = self._request("GET", path, params=params)
        return _parse_response(response, response_model)

    @overload
    def _post(
        self,
        path: str,
        *,
        json_data: dict[str, Any] | None = ...,
        files: Any | None = ...,
        response_model: type[T],
    ) -> T: ...

    @overload
    def _post(
        self,
        path: str,
        *,
        json_data: dict[str, Any] | None = ...,
        files: Any | None = ...,
        response_model: None = ...,
    ) -> Any: ...

    def _post(
        self,
        path: str,
        *,
        json_data: dict[str, Any] | None = None,
        files: Any | None = None,
        response_model: type[T] | None = None,
    ) -> T | Any:
        """Send a POST request.

        Args:
            path: API path.
            json_data: Optional JSON body.
            files: Optional files for multipart uploads.
            response_model: Optional Pydantic model class to parse the response into.

        Returns:
            A Pydantic model instance if ``response_model`` is provided,
            otherwise the parsed JSON response.
        """
        response = self._request("POST", path, json_data=json_data, files=files)
        return _parse_response(response, response_model)

    @overload
    def _patch(
        self,
        path: str,
        *,
        json_data: dict[str, Any] | None = ...,
        response_model: type[T],
    ) -> T: ...

    @overload
    def _patch(
        self,
        path: str,
        *,
        json_data: dict[str, Any] | None = ...,
        response_model: None = ...,
    ) -> Any: ...

    def _patch(
        self,
        path: str,
        *,
        json_data: dict[str, Any] | None = None,
        response_model: type[T] | None = None,
    ) -> T | Any:
        """Send a PATCH request.

        Args:
            path: API path.
            json_data: Optional JSON body.
            response_model: Optional Pydantic model class to parse the response into.

        Returns:
            A Pydantic model instance if ``response_model`` is provided,
            otherwise the parsed JSON response.
        """
        response = self._request("PATCH", path, json_data=json_data)
        return _parse_response(response, response_model)

    @overload
    def _delete(
        self,
        path: str,
        *,
        response_model: type[T],
    ) -> T: ...

    @overload
    def _delete(
        self,
        path: str,
        *,
        response_model: None = ...,
    ) -> Any: ...

    def _delete(
        self,
        path: str,
        *,
        response_model: type[T] | None = None,
    ) -> T | Any:
        """Send a DELETE request.

        Args:
            path: API path.
            response_model: Optional Pydantic model class to parse the response into.

        Returns:
            A Pydantic model instance if ``response_model`` is provided,
            otherwise the parsed JSON response (or ``None`` for 204).
        """
        response = self._request("DELETE", path)
        return _parse_response(response, response_model)

    # ------------------------------------------------------------------
    # Lifecycle
    # ------------------------------------------------------------------

    def close(self) -> None:
        """Close the underlying HTTP client and release resources."""
        if self._own_client:
            self._http_client.close()

    def __enter__(self) -> SyncAPIClient:
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: Any,
    ) -> None:
        self.close()


class AsyncAPIClient:
    """Asynchronous HTTP client for the SocialAPI.

    Provides ``_get``, ``_post``, ``_patch``, ``_delete`` convenience
    methods that handle retries, error raising, and optional Pydantic
    response parsing.

    Args:
        config: Client configuration (api_key, base_url, timeout, max_retries).
        http_client: Optional pre-configured ``httpx.AsyncClient``.
    """

    config: ClientConfig

    def __init__(
        self,
        config: ClientConfig,
        *,
        http_client: httpx.AsyncClient | None = None,
    ) -> None:
        self.config = config
        self._retry = RetryHandler(config.max_retries)
        self._own_client = http_client is None
        self._http_client = http_client or httpx.AsyncClient(timeout=config.timeout)

    # ------------------------------------------------------------------
    # Header / URL helpers
    # ------------------------------------------------------------------

    def _build_headers(self, *, has_files: bool = False) -> Headers:
        """Build default request headers.

        Args:
            has_files: When ``True``, omit ``Content-Type`` so that httpx
                sets the correct multipart boundary automatically.

        Returns:
            A dictionary of HTTP headers.
        """
        headers: Headers = {
            "Authorization": f"Bearer {self.config.api_key}",
            "User-Agent": f"socialapi-python/{__version__}",
        }
        if not has_files:
            headers["Content-Type"] = "application/json"
        return headers

    def _build_url(self, path: str) -> str:
        """Construct the full URL for an API path.

        Args:
            path: The API path (e.g. ``/v1/accounts``).

        Returns:
            The complete URL.
        """
        base = self.config.base_url.rstrip("/")
        path = path.lstrip("/")
        return f"{base}/{path}"

    # ------------------------------------------------------------------
    # Core request method
    # ------------------------------------------------------------------

    async def _request(
        self,
        method: str,
        path: str,
        *,
        params: QueryParams | None = None,
        json_data: dict[str, Any] | None = None,
        files: Any | None = None,
    ) -> httpx.Response:
        """Send an HTTP request with automatic retries and error handling.

        Args:
            method: HTTP method (``GET``, ``POST``, ``PATCH``, ``DELETE``).
            path: API path (e.g. ``/v1/accounts``).
            params: Optional query parameters. ``None`` values are stripped.
            json_data: Optional JSON body payload.
            files: Optional files for multipart uploads.

        Returns:
            The ``httpx.Response`` on success.

        Raises:
            SocialAPIError: Or a subclass, on non-2xx responses that are
                not retryable or after all retries are exhausted.
        """
        import asyncio

        url = self._build_url(path)
        headers = self._build_headers(has_files=files is not None)
        clean_params = _strip_none(params) if params else None

        last_exc: Exception | None = None
        response: httpx.Response | None = None

        for attempt in range(self._retry.max_retries + 1):
            try:
                response = await self._http_client.request(
                    method,
                    url,
                    headers=headers,
                    params=clean_params,
                    json=json_data,
                    files=files,
                )
            except (httpx.TimeoutException, httpx.NetworkError) as exc:
                last_exc = exc
                if self._retry.should_retry(None, attempt, is_network_error=True):
                    delay = self._retry.calculate_delay(attempt)
                    await asyncio.sleep(delay)
                    continue
                raise

            if response.is_success:
                return response

            if self._retry.should_retry(response, attempt):
                delay = self._retry.calculate_delay(attempt, response)
                await asyncio.sleep(delay)
                continue

            raise_for_status(response)

        # Exhausted retries -- raise last error.
        if last_exc is not None:
            raise last_exc
        if response is not None:
            raise_for_status(response)

        # Should be unreachable, but satisfies the type checker.
        raise RuntimeError("Unexpected state in retry loop")  # pragma: no cover

    # ------------------------------------------------------------------
    # Convenience methods
    # ------------------------------------------------------------------

    @overload
    async def _get(
        self,
        path: str,
        *,
        params: QueryParams | None = ...,
        response_model: type[T],
    ) -> T: ...

    @overload
    async def _get(
        self,
        path: str,
        *,
        params: QueryParams | None = ...,
        response_model: None = ...,
    ) -> Any: ...

    async def _get(
        self,
        path: str,
        *,
        params: QueryParams | None = None,
        response_model: type[T] | None = None,
    ) -> T | Any:
        """Send a GET request.

        Args:
            path: API path.
            params: Optional query parameters.
            response_model: Optional Pydantic model class to parse the response into.

        Returns:
            A Pydantic model instance if ``response_model`` is provided,
            otherwise the parsed JSON response.
        """
        response = await self._request("GET", path, params=params)
        return _parse_response(response, response_model)

    @overload
    async def _post(
        self,
        path: str,
        *,
        json_data: dict[str, Any] | None = ...,
        files: Any | None = ...,
        response_model: type[T],
    ) -> T: ...

    @overload
    async def _post(
        self,
        path: str,
        *,
        json_data: dict[str, Any] | None = ...,
        files: Any | None = ...,
        response_model: None = ...,
    ) -> Any: ...

    async def _post(
        self,
        path: str,
        *,
        json_data: dict[str, Any] | None = None,
        files: Any | None = None,
        response_model: type[T] | None = None,
    ) -> T | Any:
        """Send a POST request.

        Args:
            path: API path.
            json_data: Optional JSON body.
            files: Optional files for multipart uploads.
            response_model: Optional Pydantic model class to parse the response into.

        Returns:
            A Pydantic model instance if ``response_model`` is provided,
            otherwise the parsed JSON response.
        """
        response = await self._request("POST", path, json_data=json_data, files=files)
        return _parse_response(response, response_model)

    @overload
    async def _patch(
        self,
        path: str,
        *,
        json_data: dict[str, Any] | None = ...,
        response_model: type[T],
    ) -> T: ...

    @overload
    async def _patch(
        self,
        path: str,
        *,
        json_data: dict[str, Any] | None = ...,
        response_model: None = ...,
    ) -> Any: ...

    async def _patch(
        self,
        path: str,
        *,
        json_data: dict[str, Any] | None = None,
        response_model: type[T] | None = None,
    ) -> T | Any:
        """Send a PATCH request.

        Args:
            path: API path.
            json_data: Optional JSON body.
            response_model: Optional Pydantic model class to parse the response into.

        Returns:
            A Pydantic model instance if ``response_model`` is provided,
            otherwise the parsed JSON response.
        """
        response = await self._request("PATCH", path, json_data=json_data)
        return _parse_response(response, response_model)

    @overload
    async def _delete(
        self,
        path: str,
        *,
        response_model: type[T],
    ) -> T: ...

    @overload
    async def _delete(
        self,
        path: str,
        *,
        response_model: None = ...,
    ) -> Any: ...

    async def _delete(
        self,
        path: str,
        *,
        response_model: type[T] | None = None,
    ) -> T | Any:
        """Send a DELETE request.

        Args:
            path: API path.
            response_model: Optional Pydantic model class to parse the response into.

        Returns:
            A Pydantic model instance if ``response_model`` is provided,
            otherwise the parsed JSON response (or ``None`` for 204).
        """
        response = await self._request("DELETE", path)
        return _parse_response(response, response_model)

    # ------------------------------------------------------------------
    # Lifecycle
    # ------------------------------------------------------------------

    async def close(self) -> None:
        """Close the underlying HTTP client and release resources."""
        if self._own_client:
            await self._http_client.aclose()

    async def __aenter__(self) -> AsyncAPIClient:
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: Any,
    ) -> None:
        await self.close()


# ---------------------------------------------------------------------------
# Utilities
# ---------------------------------------------------------------------------


def _strip_none(params: QueryParams) -> dict[str, str | int]:
    """Remove keys with ``None`` values from query parameters.

    Args:
        params: The raw query parameter dict.

    Returns:
        A cleaned dict with only non-``None`` values.
    """
    return {k: v for k, v in params.items() if v is not None}


def _parse_response(response: httpx.Response, model: type[T] | None) -> T | Any:
    """Parse an httpx response, optionally into a Pydantic model.

    Args:
        response: The httpx response.
        model: Optional Pydantic model class.

    Returns:
        A model instance if ``model`` is provided, otherwise the parsed
        JSON body, or ``None`` for 204 No Content responses.
    """
    if response.status_code == 204:
        return None

    data = response.json()

    if model is not None:
        return model.model_validate(data)

    return data
