from __future__ import annotations

from typing import TYPE_CHECKING, Any

from socialapi.models.accounts import (
    Account,
    ConnectAccountResponse,
    ConnectOAuthResponse,
    OAuthExchangeResponse,
)

if TYPE_CHECKING:
    from socialapi._base_client import BaseAsyncClient, BaseSyncClient
    from socialapi._pagination import AsyncCursorPage, CursorPage


class Accounts:
    """Manage connected social media accounts (sync)."""

    _client: BaseSyncClient

    def __init__(self, client: BaseSyncClient) -> None:
        self._client = client

    def list(
        self,
        *,
        brand_id: str | None = None,
        timeout: float | None = None,
    ) -> CursorPage[Account]:
        """List all connected social media accounts.

        Args:
            brand_id: Optional brand ID to filter accounts by.
            timeout: Override the client-level timeout for this request.

        Returns:
            A paginated list of connected accounts.

        Raises:
            AuthenticationError: If the API key is invalid.
        """
        params: dict[str, Any] = {}
        if brand_id is not None:
            params["brand_id"] = brand_id
        return self._client._get_paginated(
            "/v1/accounts",
            params=params,
            model=Account,
            timeout=timeout,
        )

    def connect(
        self,
        *,
        platform: str,
        brand_id: str | None = None,
        metadata: dict[str, Any] | None = None,
        timeout: float | None = None,
    ) -> ConnectAccountResponse | ConnectOAuthResponse:
        """Initiate a new account connection.

        For OAuth2 platforms (instagram, facebook, etc.) this returns a
        ``ConnectOAuthResponse`` with an ``auth_url`` to redirect the user.
        For direct-auth platforms it returns a ``ConnectAccountResponse``
        with the new account details.

        Args:
            platform: Social platform identifier (e.g. ``"instagram"``).
            brand_id: Optional brand to attach the account to.
            metadata: Platform-specific connection data (e.g. ``redirect_uri``).
            timeout: Override the client-level timeout for this request.

        Returns:
            A direct connection response or an OAuth redirect response.

        Raises:
            BadRequestError: If the platform is unsupported or metadata is missing.
            AuthenticationError: If the API key is invalid.
        """
        body: dict[str, Any] = {"platform": platform}
        if brand_id is not None:
            body["brand_id"] = brand_id
        if metadata is not None:
            body["metadata"] = metadata
        data = self._client._post("/v1/accounts/connect", json=body, timeout=timeout)
        # OAuth flow returns auth_url; direct returns account_id
        if isinstance(data, dict) and "auth_url" in data:
            return ConnectOAuthResponse.model_validate(data)
        return ConnectAccountResponse.model_validate(data)

    def exchange_oauth(
        self,
        *,
        platform: str,
        code: str,
        metadata: dict[str, Any],
        timeout: float | None = None,
    ) -> OAuthExchangeResponse:
        """Exchange an OAuth authorization code for account credentials.

        Args:
            platform: Social platform identifier.
            code: Authorization code from the platform callback.
            metadata: Must include ``redirect_uri`` and ``state``.
            timeout: Override the client-level timeout for this request.

        Returns:
            The exchange result with connected account details.

        Raises:
            BadRequestError: If the code or metadata is invalid.
            AuthenticationError: If the API key is invalid.
        """
        body: dict[str, Any] = {
            "platform": platform,
            "code": code,
            "metadata": metadata,
        }
        data = self._client._post("/v1/oauth/exchange", json=body, timeout=timeout)
        # Single account: flat response; multiple: wrapped in data/count
        if isinstance(data, dict) and "data" in data:
            accounts = [ConnectAccountResponse.model_validate(a) for a in data["data"]]
            return OAuthExchangeResponse(accounts=accounts)
        # Single account response (backward compat)
        account = ConnectAccountResponse.model_validate(data)
        return OAuthExchangeResponse(accounts=[account])

    def disconnect(
        self,
        account_id: str,
        *,
        timeout: float | None = None,
    ) -> None:
        """Disconnect (delete) a connected account.

        Args:
            account_id: The account ID to disconnect.
            timeout: Override the client-level timeout for this request.

        Raises:
            NotFoundError: If the account does not exist.
            AuthenticationError: If the API key is invalid.
        """
        self._client._delete(f"/v1/accounts/{account_id}", timeout=timeout)


class AsyncAccounts:
    """Manage connected social media accounts (async)."""

    _client: BaseAsyncClient

    def __init__(self, client: BaseAsyncClient) -> None:
        self._client = client

    async def list(
        self,
        *,
        brand_id: str | None = None,
        timeout: float | None = None,
    ) -> AsyncCursorPage[Account]:
        """List all connected social media accounts.

        Args:
            brand_id: Optional brand ID to filter accounts by.
            timeout: Override the client-level timeout for this request.

        Returns:
            A paginated list of connected accounts.

        Raises:
            AuthenticationError: If the API key is invalid.
        """
        params: dict[str, Any] = {}
        if brand_id is not None:
            params["brand_id"] = brand_id
        return await self._client._get_paginated(
            "/v1/accounts",
            params=params,
            model=Account,
            timeout=timeout,
        )

    async def connect(
        self,
        *,
        platform: str,
        brand_id: str | None = None,
        metadata: dict[str, Any] | None = None,
        timeout: float | None = None,
    ) -> ConnectAccountResponse | ConnectOAuthResponse:
        """Initiate a new account connection.

        For OAuth2 platforms (instagram, facebook, etc.) this returns a
        ``ConnectOAuthResponse`` with an ``auth_url`` to redirect the user.
        For direct-auth platforms it returns a ``ConnectAccountResponse``
        with the new account details.

        Args:
            platform: Social platform identifier (e.g. ``"instagram"``).
            brand_id: Optional brand to attach the account to.
            metadata: Platform-specific connection data (e.g. ``redirect_uri``).
            timeout: Override the client-level timeout for this request.

        Returns:
            A direct connection response or an OAuth redirect response.

        Raises:
            BadRequestError: If the platform is unsupported or metadata is missing.
            AuthenticationError: If the API key is invalid.
        """
        body: dict[str, Any] = {"platform": platform}
        if brand_id is not None:
            body["brand_id"] = brand_id
        if metadata is not None:
            body["metadata"] = metadata
        data = await self._client._post("/v1/accounts/connect", json=body, timeout=timeout)
        if isinstance(data, dict) and "auth_url" in data:
            return ConnectOAuthResponse.model_validate(data)
        return ConnectAccountResponse.model_validate(data)

    async def exchange_oauth(
        self,
        *,
        platform: str,
        code: str,
        metadata: dict[str, Any],
        timeout: float | None = None,
    ) -> OAuthExchangeResponse:
        """Exchange an OAuth authorization code for account credentials.

        Args:
            platform: Social platform identifier.
            code: Authorization code from the platform callback.
            metadata: Must include ``redirect_uri`` and ``state``.
            timeout: Override the client-level timeout for this request.

        Returns:
            The exchange result with connected account details.

        Raises:
            BadRequestError: If the code or metadata is invalid.
            AuthenticationError: If the API key is invalid.
        """
        body: dict[str, Any] = {
            "platform": platform,
            "code": code,
            "metadata": metadata,
        }
        data = await self._client._post("/v1/oauth/exchange", json=body, timeout=timeout)
        if isinstance(data, dict) and "data" in data:
            accounts = [ConnectAccountResponse.model_validate(a) for a in data["data"]]
            return OAuthExchangeResponse(accounts=accounts)
        account = ConnectAccountResponse.model_validate(data)
        return OAuthExchangeResponse(accounts=[account])

    async def disconnect(
        self,
        account_id: str,
        *,
        timeout: float | None = None,
    ) -> None:
        """Disconnect (delete) a connected account.

        Args:
            account_id: The account ID to disconnect.
            timeout: Override the client-level timeout for this request.

        Raises:
            NotFoundError: If the account does not exist.
            AuthenticationError: If the API key is invalid.
        """
        await self._client._delete(f"/v1/accounts/{account_id}", timeout=timeout)
