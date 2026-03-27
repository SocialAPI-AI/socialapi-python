from __future__ import annotations

from datetime import datetime  # noqa: TC003
from typing import TYPE_CHECKING, Any

from socialapi.models.events import EventsListResponse

if TYPE_CHECKING:
    from socialapi._base_client import BaseAsyncClient, BaseSyncClient


class Events:
    """Access developer events / audit log (sync)."""

    _client: BaseSyncClient

    def __init__(self, client: BaseSyncClient) -> None:
        self._client = client

    def list(
        self,
        *,
        category: str | None = None,
        action: str | None = None,
        status: str | None = None,
        platform: str | None = None,
        account_id: str | None = None,
        resource_id: str | None = None,
        from_date: datetime | None = None,
        to_date: datetime | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        timeout: float | None = None,
    ) -> EventsListResponse:
        """List developer events with optional filtering.

        Args:
            category: Filter by event category (e.g. ``"post"``, ``"account"``).
            action: Filter by action (e.g. ``"publish"``, ``"connect"``).
            status: Filter by outcome (e.g. ``"success"``, ``"error"``).
            platform: Filter by platform.
            account_id: Filter by account ID.
            resource_id: Filter by resource ID.
            from_date: Events after this time.
            to_date: Events before this time.
            limit: Maximum number of results.
            cursor: Pagination cursor from a previous response.
            timeout: Override the client-level timeout for this request.

        Returns:
            Events list with pagination and retention info.

        Raises:
            BadRequestError: If from/to format is invalid.
            AuthenticationError: If the API key is invalid.
        """
        params: dict[str, Any] = {}
        if category is not None:
            params["category"] = category
        if action is not None:
            params["action"] = action
        if status is not None:
            params["status"] = status
        if platform is not None:
            params["platform"] = platform
        if account_id is not None:
            params["account_id"] = account_id
        if resource_id is not None:
            params["resource_id"] = resource_id
        if from_date is not None:
            params["from"] = from_date.isoformat()
        if to_date is not None:
            params["to"] = to_date.isoformat()
        if limit is not None:
            params["limit"] = limit
        if cursor is not None:
            params["cursor"] = cursor
        data = self._client._get("/v1/events", params=params, timeout=timeout)
        return EventsListResponse.model_validate(data)


class AsyncEvents:
    """Access developer events / audit log (async)."""

    _client: BaseAsyncClient

    def __init__(self, client: BaseAsyncClient) -> None:
        self._client = client

    async def list(
        self,
        *,
        category: str | None = None,
        action: str | None = None,
        status: str | None = None,
        platform: str | None = None,
        account_id: str | None = None,
        resource_id: str | None = None,
        from_date: datetime | None = None,
        to_date: datetime | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        timeout: float | None = None,
    ) -> EventsListResponse:
        """List developer events with optional filtering.

        Args:
            category: Filter by event category (e.g. ``"post"``, ``"account"``).
            action: Filter by action (e.g. ``"publish"``, ``"connect"``).
            status: Filter by outcome (e.g. ``"success"``, ``"error"``).
            platform: Filter by platform.
            account_id: Filter by account ID.
            resource_id: Filter by resource ID.
            from_date: Events after this time.
            to_date: Events before this time.
            limit: Maximum number of results.
            cursor: Pagination cursor from a previous response.
            timeout: Override the client-level timeout for this request.

        Returns:
            Events list with pagination and retention info.

        Raises:
            BadRequestError: If from/to format is invalid.
            AuthenticationError: If the API key is invalid.
        """
        params: dict[str, Any] = {}
        if category is not None:
            params["category"] = category
        if action is not None:
            params["action"] = action
        if status is not None:
            params["status"] = status
        if platform is not None:
            params["platform"] = platform
        if account_id is not None:
            params["account_id"] = account_id
        if resource_id is not None:
            params["resource_id"] = resource_id
        if from_date is not None:
            params["from"] = from_date.isoformat()
        if to_date is not None:
            params["to"] = to_date.isoformat()
        if limit is not None:
            params["limit"] = limit
        if cursor is not None:
            params["cursor"] = cursor
        data = await self._client._get("/v1/events", params=params, timeout=timeout)
        return EventsListResponse.model_validate(data)
