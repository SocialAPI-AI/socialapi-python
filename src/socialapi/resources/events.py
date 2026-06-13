from __future__ import annotations

from typing import TYPE_CHECKING, Any, cast

from socialapi.models.events import Event, EventList, EventsSummary

if TYPE_CHECKING:
    from socialapi._base_client import BaseAsyncClient, BaseSyncClient


class Events:
    """Access the unified developer event log (sync).

    The event log covers post lifecycle, inbox activity, account changes,
    and webhook deliveries. Retention window varies by plan tier.
    """

    _client: BaseSyncClient

    def __init__(self, client: BaseSyncClient) -> None:
        self._client = client

    def list(
        self,
        *,
        category: str | None = None,
        status: str | None = None,
        platform: str | None = None,
        account_id: str | None = None,
        resource_id: str | None = None,
        action: str | None = None,
        since: str | None = None,
        until: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        timeout: float | None = None,
    ) -> EventList:
        """List events from the unified developer event log.

        The query parameters ``since`` and ``until`` are sent as ``from`` and
        ``to`` on the wire, matching the Go handler's expected parameter names.

        Args:
            category: Filter by event category (e.g. ``post``, ``webhook``,
                ``inbox``).
            status: Filter by status (``ok`` or ``failed``).
            platform: Filter by platform (e.g. ``instagram``).
            account_id: Filter by connected account ID.
            resource_id: Filter by resource ID (post, conversation, etc.).
            action: Filter by action (e.g. ``post.published``).
            since: Lower time bound (RFC3339 string). Sent as ``from`` param.
            until: Upper time bound (RFC3339 string). Sent as ``to`` param.
            limit: Page size (default 50 server-side).
            cursor: Pagination cursor from a previous response.
            timeout: Override the client-level timeout for this request.

        Returns:
            An ``EventList`` containing events, retention_days, and pagination
            state.

        Raises:
            AuthenticationError: If the API key is invalid.
        """
        params: dict[str, Any] = {}
        if category is not None:
            params["category"] = category
        if status is not None:
            params["status"] = status
        if platform is not None:
            params["platform"] = platform
        if account_id is not None:
            params["account_id"] = account_id
        if resource_id is not None:
            params["resource_id"] = resource_id
        if action is not None:
            params["action"] = action
        if since is not None:
            params["from"] = since
        if until is not None:
            params["to"] = until
        if limit is not None:
            params["limit"] = limit
        if cursor is not None:
            params["cursor"] = cursor

        body = self._client._get("/v1/events", params=params, timeout=timeout)
        return _parse_event_list(body)

    def get_summary(
        self,
        *,
        since: str | None = None,
        until: str | None = None,
        timeout: float | None = None,
    ) -> EventsSummary:
        """Get aggregated event counts for a time window.

        Args:
            since: Lower time bound (RFC3339 string). Sent as ``from`` param.
            until: Upper time bound (RFC3339 string). Sent as ``to`` param.
            timeout: Override the client-level timeout for this request.

        Returns:
            Aggregated event counts including totals, failure counts,
            by-category breakdown, inbox breakdown, and retention window.

        Raises:
            AuthenticationError: If the API key is invalid.
        """
        params: dict[str, Any] = {}
        if since is not None:
            params["from"] = since
        if until is not None:
            params["to"] = until

        data = self._client._get("/v1/events/summary", params=params, timeout=timeout)
        return EventsSummary.model_validate(data)


class AsyncEvents:
    """Access the unified developer event log (async).

    The event log covers post lifecycle, inbox activity, account changes,
    and webhook deliveries. Retention window varies by plan tier.
    """

    _client: BaseAsyncClient

    def __init__(self, client: BaseAsyncClient) -> None:
        self._client = client

    async def list(
        self,
        *,
        category: str | None = None,
        status: str | None = None,
        platform: str | None = None,
        account_id: str | None = None,
        resource_id: str | None = None,
        action: str | None = None,
        since: str | None = None,
        until: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        timeout: float | None = None,
    ) -> EventList:
        """List events from the unified developer event log.

        The query parameters ``since`` and ``until`` are sent as ``from`` and
        ``to`` on the wire, matching the Go handler's expected parameter names.

        Args:
            category: Filter by event category (e.g. ``post``, ``webhook``,
                ``inbox``).
            status: Filter by status (``ok`` or ``failed``).
            platform: Filter by platform (e.g. ``instagram``).
            account_id: Filter by connected account ID.
            resource_id: Filter by resource ID (post, conversation, etc.).
            action: Filter by action (e.g. ``post.published``).
            since: Lower time bound (RFC3339 string). Sent as ``from`` param.
            until: Upper time bound (RFC3339 string). Sent as ``to`` param.
            limit: Page size (default 50 server-side).
            cursor: Pagination cursor from a previous response.
            timeout: Override the client-level timeout for this request.

        Returns:
            An ``EventList`` containing events, retention_days, and pagination
            state.

        Raises:
            AuthenticationError: If the API key is invalid.
        """
        params: dict[str, Any] = {}
        if category is not None:
            params["category"] = category
        if status is not None:
            params["status"] = status
        if platform is not None:
            params["platform"] = platform
        if account_id is not None:
            params["account_id"] = account_id
        if resource_id is not None:
            params["resource_id"] = resource_id
        if action is not None:
            params["action"] = action
        if since is not None:
            params["from"] = since
        if until is not None:
            params["to"] = until
        if limit is not None:
            params["limit"] = limit
        if cursor is not None:
            params["cursor"] = cursor

        body = await self._client._get("/v1/events", params=params, timeout=timeout)
        return _parse_event_list(body)

    async def get_summary(
        self,
        *,
        since: str | None = None,
        until: str | None = None,
        timeout: float | None = None,
    ) -> EventsSummary:
        """Get aggregated event counts for a time window.

        Args:
            since: Lower time bound (RFC3339 string). Sent as ``from`` param.
            until: Upper time bound (RFC3339 string). Sent as ``to`` param.
            timeout: Override the client-level timeout for this request.

        Returns:
            Aggregated event counts including totals, failure counts,
            by-category breakdown, inbox breakdown, and retention window.

        Raises:
            AuthenticationError: If the API key is invalid.
        """
        params: dict[str, Any] = {}
        if since is not None:
            params["from"] = since
        if until is not None:
            params["to"] = until

        data = await self._client._get("/v1/events/summary", params=params, timeout=timeout)
        return EventsSummary.model_validate(data)


def _parse_event_list(body: dict[str, Any]) -> EventList:
    """Parse the ``EventsListResponse`` envelope into an ``EventList``.

    The events list endpoint returns ``{"events": [...], "pagination": {...},
    "retention_days": N}`` rather than the standard ``{"data": [...]}``
    shape, so this helper handles the non-standard envelope.
    """
    raw_items: list[Any] = body.get("events", [])
    items = [Event.model_validate(item) for item in raw_items]

    pagination_raw: Any = body.get("pagination")
    next_cursor: str | None
    if isinstance(pagination_raw, dict):
        pagination_dict = cast("dict[str, Any]", pagination_raw)
        has_more = bool(pagination_dict.get("has_more", False))
        cursor_val: Any = pagination_dict.get("next_cursor")
        next_cursor = str(cursor_val) if cursor_val is not None else None
    else:
        has_more = False
        next_cursor = None

    retention_days_raw: Any = body.get("retention_days", 0)
    retention_days: int = int(retention_days_raw)

    return EventList(
        data=items,
        retention_days=retention_days,
        has_more=has_more,
        next_cursor=next_cursor,
    )
