"""Reviews resource."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from socialapi.models.interactions import InteractionsListResponse

if TYPE_CHECKING:
    from socialapi._async_client import AsyncSocialAPI
    from socialapi._client import SocialAPI


class Reviews:
    """Synchronous reviews resource.

    Provides methods for listing reviews on connected accounts.
    """

    def __init__(self, client: SocialAPI) -> None:
        self._client = client

    def list(
        self,
        account_id: str,
        *,
        limit: int = 50,
        cursor: str | None = None,
        since: str | None = None,
    ) -> InteractionsListResponse:
        """List reviews for a connected account.

        Args:
            account_id: The connected account ID.
            limit: Maximum results per page (1--100). Defaults to 50.
            cursor: Opaque cursor from a previous response for pagination.
            since: Only return items created after this timestamp (RFC 3339).

        Returns:
            An InteractionsListResponse containing the reviews and count.

        Raises:
            NotFoundError: If the account is not found.
            NotSupportedError: If the platform does not support reviews.
        """
        params: dict[str, Any] = {"limit": limit}
        if cursor is not None:
            params["cursor"] = cursor
        if since is not None:
            params["since"] = since
        return self._client._get(
            f"/v1/accounts/{account_id}/reviews",
            params=params,
            response_model=InteractionsListResponse,
        )


class AsyncReviews:
    """Asynchronous reviews resource.

    Provides methods for listing reviews on connected accounts.
    """

    def __init__(self, client: AsyncSocialAPI) -> None:
        self._client = client

    async def list(
        self,
        account_id: str,
        *,
        limit: int = 50,
        cursor: str | None = None,
        since: str | None = None,
    ) -> InteractionsListResponse:
        """List reviews for a connected account.

        Args:
            account_id: The connected account ID.
            limit: Maximum results per page (1--100). Defaults to 50.
            cursor: Opaque cursor from a previous response for pagination.
            since: Only return items created after this timestamp (RFC 3339).

        Returns:
            An InteractionsListResponse containing the reviews and count.

        Raises:
            NotFoundError: If the account is not found.
            NotSupportedError: If the platform does not support reviews.
        """
        params: dict[str, Any] = {"limit": limit}
        if cursor is not None:
            params["cursor"] = cursor
        if since is not None:
            params["since"] = since
        return await self._client._get(
            f"/v1/accounts/{account_id}/reviews",
            params=params,
            response_model=InteractionsListResponse,
        )
