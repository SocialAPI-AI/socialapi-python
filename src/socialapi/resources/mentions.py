from __future__ import annotations

from typing import TYPE_CHECKING, Any

from socialapi.models.mentions import Mention

if TYPE_CHECKING:
    from socialapi._base_client import BaseAsyncClient, BaseSyncClient
    from socialapi._pagination import AsyncCursorPage, CursorPage


class Mentions:
    """Access mentions of connected accounts (sync)."""

    _client: BaseSyncClient

    def __init__(self, client: BaseSyncClient) -> None:
        self._client = client

    def list(
        self,
        account_id: str,
        *,
        since: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        timeout: float | None = None,
    ) -> CursorPage[Mention]:
        """List mentions for a connected account.

        Args:
            account_id: The connected account ID.
            since: Only return mentions after this ISO 8601 datetime.
            limit: Maximum number of results.
            cursor: Pagination cursor from a previous response.
            timeout: Override the client-level timeout for this request.

        Returns:
            A paginated list of mentions.

        Raises:
            NotFoundError: If the account does not exist.
            NotSupportedError: If the platform does not support mentions.
            AuthenticationError: If the API key is invalid.
        """
        params: dict[str, Any] = {}
        if since is not None:
            params["since"] = since
        if limit is not None:
            params["limit"] = limit
        if cursor is not None:
            params["cursor"] = cursor
        return self._client._get_paginated(
            f"/v1/accounts/{account_id}/mentions",
            params=params,
            model=Mention,
            timeout=timeout,
        )


class AsyncMentions:
    """Access mentions of connected accounts (async)."""

    _client: BaseAsyncClient

    def __init__(self, client: BaseAsyncClient) -> None:
        self._client = client

    async def list(
        self,
        account_id: str,
        *,
        since: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        timeout: float | None = None,
    ) -> AsyncCursorPage[Mention]:
        """List mentions for a connected account.

        Args:
            account_id: The connected account ID.
            since: Only return mentions after this ISO 8601 datetime.
            limit: Maximum number of results.
            cursor: Pagination cursor from a previous response.
            timeout: Override the client-level timeout for this request.

        Returns:
            A paginated list of mentions.

        Raises:
            NotFoundError: If the account does not exist.
            NotSupportedError: If the platform does not support mentions.
            AuthenticationError: If the API key is invalid.
        """
        params: dict[str, Any] = {}
        if since is not None:
            params["since"] = since
        if limit is not None:
            params["limit"] = limit
        if cursor is not None:
            params["cursor"] = cursor
        return await self._client._get_paginated(
            f"/v1/accounts/{account_id}/mentions",
            params=params,
            model=Mention,
            timeout=timeout,
        )
