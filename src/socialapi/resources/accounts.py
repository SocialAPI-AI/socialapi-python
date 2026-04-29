from __future__ import annotations

from typing import TYPE_CHECKING, Any

from socialapi.models.accounts import (
    Account,
    AsyncAccount,
    AsyncPage,
    ConnectAccountResponse,
    ConnectOAuthResponse,
    CreatorInfo,
    OAuthExchangeResponse,
    Page,
)
from socialapi.models.exports import AsyncExport, Export
from socialapi.models.usage import AccountLimits

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
        """List all connected social media accounts."""
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
        """Initiate a new account connection."""
        body: dict[str, Any] = {"platform": platform}
        if brand_id is not None:
            body["brand_id"] = brand_id
        if metadata is not None:
            body["metadata"] = metadata
        data = self._client._post("/v1/accounts/connect", json=body, timeout=timeout)
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
        """Exchange an OAuth authorization code for account credentials."""
        body: dict[str, Any] = {"platform": platform, "code": code, "metadata": metadata}
        data = self._client._post("/v1/oauth/exchange", json=body, timeout=timeout)
        if isinstance(data, dict) and "data" in data:
            accounts = [ConnectAccountResponse.model_validate(a) for a in data["data"]]
            return OAuthExchangeResponse(accounts=accounts)
        account = ConnectAccountResponse.model_validate(data)
        return OAuthExchangeResponse(accounts=[account])

    def disconnect(self, account_id: str, *, timeout: float | None = None) -> None:
        """Disconnect a connected account."""
        self._client._delete(f"/v1/accounts/{account_id}", timeout=timeout)

    def get_creator_info(self, account_id: str, *, timeout: float | None = None) -> CreatorInfo:
        """Get platform-specific creator settings (TikTok only)."""
        data = self._client._get(f"/v1/accounts/{account_id}/creator-info", timeout=timeout)
        return CreatorInfo.model_validate(data)

    def list_pages(self, account_id: str, *, timeout: float | None = None) -> list[Page]:
        """List pages associated with this connected account."""
        data = self._client._get(f"/v1/accounts/{account_id}/pages", timeout=timeout)
        raw_items: list[Any] = data.get("data", [])
        items = [Page.model_validate(item) for item in raw_items]
        for item in items:
            item._bind(self._client, {"account_id": account_id})
        return items

    def update_page(
        self,
        account_id: str,
        page_id: str,
        *,
        is_default: bool | None = None,
        is_active: bool | None = None,
        timeout: float | None = None,
    ) -> Page:
        """Update a page's is_default or is_active status."""
        body: dict[str, Any] = {}
        if is_default is not None:
            body["is_default"] = is_default
        if is_active is not None:
            body["is_active"] = is_active
        data = self._client._patch(
            f"/v1/accounts/{account_id}/pages/{page_id}",
            json=body,
            timeout=timeout,
        )
        page = Page.model_validate(data or {})
        page._bind(self._client, {"account_id": account_id, "page_id": page_id})
        return page

    def export(
        self,
        account_id: str,
        *,
        include_transcript: bool | None = None,
        include_vision: bool | None = None,
        timeout: float | None = None,
    ) -> Export:
        """Enqueue an analytics export job for an account."""
        body: dict[str, Any] = {}
        if include_transcript is not None:
            body["include_transcript"] = include_transcript
        if include_vision is not None:
            body["include_vision"] = include_vision
        data = self._client._post(
            f"/v1/accounts/{account_id}/export",
            json=body or None,
            timeout=timeout,
        )
        export = Export.model_validate(data or {})
        if export.id is not None:
            export._bind(self._client, {"export_id": export.id, "account_id": account_id})
        else:
            export._bind(self._client, {"account_id": account_id})
        return export

    def get_limits(self, account_id: str, *, timeout: float | None = None) -> AccountLimits:
        """Get platform-specific quota limits for a connected account."""
        data = self._client._get(f"/v1/accounts/{account_id}/limits", timeout=timeout)
        if "limits" in data:
            return AccountLimits.model_validate(data)
        return AccountLimits(limits=data)


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
    ) -> AsyncCursorPage[AsyncAccount]:
        params: dict[str, Any] = {}
        if brand_id is not None:
            params["brand_id"] = brand_id
        return await self._client._get_paginated(
            "/v1/accounts",
            params=params,
            model=AsyncAccount,
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
        body: dict[str, Any] = {"platform": platform, "code": code, "metadata": metadata}
        data = await self._client._post("/v1/oauth/exchange", json=body, timeout=timeout)
        if isinstance(data, dict) and "data" in data:
            accounts = [ConnectAccountResponse.model_validate(a) for a in data["data"]]
            return OAuthExchangeResponse(accounts=accounts)
        account = ConnectAccountResponse.model_validate(data)
        return OAuthExchangeResponse(accounts=[account])

    async def disconnect(self, account_id: str, *, timeout: float | None = None) -> None:
        await self._client._delete(f"/v1/accounts/{account_id}", timeout=timeout)

    async def get_creator_info(self, account_id: str, *, timeout: float | None = None) -> CreatorInfo:
        data = await self._client._get(f"/v1/accounts/{account_id}/creator-info", timeout=timeout)
        return CreatorInfo.model_validate(data)

    async def list_pages(self, account_id: str, *, timeout: float | None = None) -> list[AsyncPage]:
        data = await self._client._get(f"/v1/accounts/{account_id}/pages", timeout=timeout)
        raw_items: list[Any] = data.get("data", [])
        items = [AsyncPage.model_validate(item) for item in raw_items]
        for item in items:
            item._bind(self._client, {"account_id": account_id})
        return items

    async def update_page(
        self,
        account_id: str,
        page_id: str,
        *,
        is_default: bool | None = None,
        is_active: bool | None = None,
        timeout: float | None = None,
    ) -> AsyncPage:
        body: dict[str, Any] = {}
        if is_default is not None:
            body["is_default"] = is_default
        if is_active is not None:
            body["is_active"] = is_active
        data = await self._client._patch(
            f"/v1/accounts/{account_id}/pages/{page_id}",
            json=body,
            timeout=timeout,
        )
        page = AsyncPage.model_validate(data or {})
        page._bind(self._client, {"account_id": account_id, "page_id": page_id})
        return page

    async def export(
        self,
        account_id: str,
        *,
        include_transcript: bool | None = None,
        include_vision: bool | None = None,
        timeout: float | None = None,
    ) -> AsyncExport:
        body: dict[str, Any] = {}
        if include_transcript is not None:
            body["include_transcript"] = include_transcript
        if include_vision is not None:
            body["include_vision"] = include_vision
        data = await self._client._post(
            f"/v1/accounts/{account_id}/export",
            json=body or None,
            timeout=timeout,
        )
        export = AsyncExport.model_validate(data or {})
        if export.id is not None:
            export._bind(self._client, {"export_id": export.id, "account_id": account_id})
        else:
            export._bind(self._client, {"account_id": account_id})
        return export

    async def get_limits(self, account_id: str, *, timeout: float | None = None) -> AccountLimits:
        data = await self._client._get(f"/v1/accounts/{account_id}/limits", timeout=timeout)
        if "limits" in data:
            return AccountLimits.model_validate(data)
        return AccountLimits(limits=data)
