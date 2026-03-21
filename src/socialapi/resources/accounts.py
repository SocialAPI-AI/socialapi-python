"""Accounts resource."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from socialapi.models.accounts import AccountsListResponse, ConnectResponse
from socialapi.models.posts import PlatformPostsListResponse

if TYPE_CHECKING:
    from socialapi._async_client import AsyncSocialAPI
    from socialapi._client import SocialAPI


class Accounts:
    """Synchronous accounts resource.

    Provides methods for listing, connecting, and disconnecting social accounts,
    as well as retrieving account posts and rate limits.
    """

    def __init__(self, client: SocialAPI) -> None:
        self._client = client

    def list(self) -> AccountsListResponse:
        """List all connected accounts.

        Returns:
            An AccountsListResponse containing the list of connected accounts.

        Raises:
            AuthenticationError: If the API key is invalid.
        """
        return self._client._get("/v1/accounts", response_model=AccountsListResponse)

    def connect(self, platform: str, metadata: dict[str, Any]) -> ConnectResponse:
        """Connect a new social media account.

        Args:
            platform: The social media platform (e.g. ``"instagram"``, ``"facebook"``).
            metadata: Platform-specific metadata required for authentication.

        Returns:
            A ConnectResponse with the new account details or an OAuth URL.

        Raises:
            ValidationError: If the platform is unsupported or metadata is missing.
            ConflictError: If the account is already linked.
        """
        return self._client._post(
            "/v1/accounts/connect",
            json_data={"platform": platform, "metadata": metadata},
            response_model=ConnectResponse,
        )

    def disconnect(self, account_id: str) -> None:
        """Disconnect a social media account.

        Args:
            account_id: The ID of the account to disconnect.

        Raises:
            NotFoundError: If the account is not found.
        """
        self._client._delete(f"/v1/accounts/{account_id}")

    def posts(
        self,
        account_id: str,
        *,
        limit: int = 50,
        cursor: str | None = None,
        since: str | None = None,
    ) -> PlatformPostsListResponse:
        """List posts for a connected account.

        Args:
            account_id: The connected account ID.
            limit: Maximum results per page (1--100). Defaults to 50.
            cursor: Opaque cursor from a previous response for pagination.
            since: Only return items created after this timestamp (RFC 3339).

        Returns:
            A PlatformPostsListResponse containing the posts and count.

        Raises:
            NotFoundError: If the account is not found.
            NotSupportedError: If the platform does not support listing posts.
        """
        params = {"limit": limit, "cursor": cursor, "since": since}
        params = {k: v for k, v in params.items() if v is not None}
        return self._client._get(
            f"/v1/accounts/{account_id}/posts",
            params=params,
            response_model=PlatformPostsListResponse,
        )

    def limits(self, account_id: str) -> dict[str, int]:
        """Get rate limits for a connected account.

        Args:
            account_id: The connected account ID.

        Returns:
            A dict mapping limit names to their current values.

        Raises:
            NotFoundError: If the account is not found.
        """
        return self._client._get(f"/v1/accounts/{account_id}/limits")


class AsyncAccounts:
    """Asynchronous accounts resource.

    Provides methods for listing, connecting, and disconnecting social accounts,
    as well as retrieving account posts and rate limits.
    """

    def __init__(self, client: AsyncSocialAPI) -> None:
        self._client = client

    async def list(self) -> AccountsListResponse:
        """List all connected accounts.

        Returns:
            An AccountsListResponse containing the list of connected accounts.

        Raises:
            AuthenticationError: If the API key is invalid.
        """
        return await self._client._get("/v1/accounts", response_model=AccountsListResponse)

    async def connect(self, platform: str, metadata: dict[str, Any]) -> ConnectResponse:
        """Connect a new social media account.

        Args:
            platform: The social media platform (e.g. ``"instagram"``, ``"facebook"``).
            metadata: Platform-specific metadata required for authentication.

        Returns:
            A ConnectResponse with the new account details or an OAuth URL.

        Raises:
            ValidationError: If the platform is unsupported or metadata is missing.
            ConflictError: If the account is already linked.
        """
        return await self._client._post(
            "/v1/accounts/connect",
            json_data={"platform": platform, "metadata": metadata},
            response_model=ConnectResponse,
        )

    async def disconnect(self, account_id: str) -> None:
        """Disconnect a social media account.

        Args:
            account_id: The ID of the account to disconnect.

        Raises:
            NotFoundError: If the account is not found.
        """
        await self._client._delete(f"/v1/accounts/{account_id}")

    async def posts(
        self,
        account_id: str,
        *,
        limit: int = 50,
        cursor: str | None = None,
        since: str | None = None,
    ) -> PlatformPostsListResponse:
        """List posts for a connected account.

        Args:
            account_id: The connected account ID.
            limit: Maximum results per page (1--100). Defaults to 50.
            cursor: Opaque cursor from a previous response for pagination.
            since: Only return items created after this timestamp (RFC 3339).

        Returns:
            A PlatformPostsListResponse containing the posts and count.

        Raises:
            NotFoundError: If the account is not found.
            NotSupportedError: If the platform does not support listing posts.
        """
        params = {"limit": limit, "cursor": cursor, "since": since}
        params = {k: v for k, v in params.items() if v is not None}
        return await self._client._get(
            f"/v1/accounts/{account_id}/posts",
            params=params,
            response_model=PlatformPostsListResponse,
        )

    async def limits(self, account_id: str) -> dict[str, int]:
        """Get rate limits for a connected account.

        Args:
            account_id: The connected account ID.

        Returns:
            A dict mapping limit names to their current values.

        Raises:
            NotFoundError: If the account is not found.
        """
        return await self._client._get(f"/v1/accounts/{account_id}/limits")
