from __future__ import annotations

from typing import TYPE_CHECKING, Any

from pydantic import BaseModel, ConfigDict

from socialapi._bound import _Bound

if TYPE_CHECKING:
    from socialapi.models.usage import AccountLimits


# ---------------------------------------------------------------------------
# Shared data
# ---------------------------------------------------------------------------


class _AccountBase(_Bound):
    """Fields shared by Account / AsyncAccount."""

    id: str
    platform: str
    name: str
    username: str
    brand_id: str | None = None
    bio: str | None = None
    profile_picture_url: str | None = None
    reconnect_reason: str | None = None
    status: str | None = None
    metadata: dict[str, Any] | None = None


class Account(_AccountBase):
    """A connected social media account (sync)."""

    def disconnect(self, *, timeout: float | None = None) -> None:
        """Disconnect this account.

        Raises:
            UnboundModelError: If this model was not built by a client.
            NotFoundError: If the account no longer exists.
        """
        client = self._client_or_raise_sync()
        client._delete(f"/v1/accounts/{self.id}", timeout=timeout)

    def get_creator_info(self, *, timeout: float | None = None) -> CreatorInfo:
        """Fetch platform-specific creator settings (TikTok only)."""
        client = self._client_or_raise_sync()
        data = client._get(f"/v1/accounts/{self.id}/creator-info", timeout=timeout)
        return CreatorInfo.model_validate(data)

    def list_pages(self, *, timeout: float | None = None) -> list[Page]:
        """List pages associated with this connected account."""
        client = self._client_or_raise_sync()
        data = client._get(f"/v1/accounts/{self.id}/pages", timeout=timeout)
        raw_items: list[Any] = data.get("data", [])
        items = [Page.model_validate(item) for item in raw_items]
        for item in items:
            item._bind(client, {"account_id": self.id})
        return items

    def get_limits(self, *, timeout: float | None = None) -> AccountLimits:
        """Get platform-specific quota limits for this account."""
        from socialapi.models.usage import AccountLimits

        client = self._client_or_raise_sync()
        data = client._get(f"/v1/accounts/{self.id}/limits", timeout=timeout)
        if "limits" in data:
            return AccountLimits.model_validate(data)
        return AccountLimits(limits=data)

    def export(
        self,
        *,
        include_transcript: bool | None = None,
        include_vision: bool | None = None,
        timeout: float | None = None,
    ) -> dict[str, Any]:
        """Enqueue an analytics export job for this account."""
        client = self._client_or_raise_sync()
        body: dict[str, Any] = {}
        if include_transcript is not None:
            body["include_transcript"] = include_transcript
        if include_vision is not None:
            body["include_vision"] = include_vision
        data = client._post(f"/v1/accounts/{self.id}/export", json=body or None, timeout=timeout)
        if data is None:
            return {}
        return data


class AsyncAccount(_AccountBase):
    """A connected social media account (async)."""

    async def disconnect(self, *, timeout: float | None = None) -> None:
        client = self._client_or_raise_async()
        await client._delete(f"/v1/accounts/{self.id}", timeout=timeout)

    async def get_creator_info(self, *, timeout: float | None = None) -> CreatorInfo:
        client = self._client_or_raise_async()
        data = await client._get(f"/v1/accounts/{self.id}/creator-info", timeout=timeout)
        return CreatorInfo.model_validate(data)

    async def list_pages(self, *, timeout: float | None = None) -> list[AsyncPage]:
        client = self._client_or_raise_async()
        data = await client._get(f"/v1/accounts/{self.id}/pages", timeout=timeout)
        raw_items: list[Any] = data.get("data", [])
        items = [AsyncPage.model_validate(item) for item in raw_items]
        for item in items:
            item._bind(client, {"account_id": self.id})
        return items

    async def get_limits(self, *, timeout: float | None = None) -> AccountLimits:
        from socialapi.models.usage import AccountLimits

        client = self._client_or_raise_async()
        data = await client._get(f"/v1/accounts/{self.id}/limits", timeout=timeout)
        if "limits" in data:
            return AccountLimits.model_validate(data)
        return AccountLimits(limits=data)

    async def export(
        self,
        *,
        include_transcript: bool | None = None,
        include_vision: bool | None = None,
        timeout: float | None = None,
    ) -> dict[str, Any]:
        client = self._client_or_raise_async()
        body: dict[str, Any] = {}
        if include_transcript is not None:
            body["include_transcript"] = include_transcript
        if include_vision is not None:
            body["include_vision"] = include_vision
        data = await client._post(f"/v1/accounts/{self.id}/export", json=body or None, timeout=timeout)
        return data or {}


# ---------------------------------------------------------------------------
# Page (sub-resource of Account)
# ---------------------------------------------------------------------------


class _PageBase(_Bound):
    """Fields for a page (e.g. Facebook Page) attached to an account.

    The OpenAPI spec marks the response as a free-form object; the SDK
    validates the commonly-returned fields and tolerates extras.
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id: str | None = None
    name: str | None = None
    platform_id: str | None = None
    is_default: bool | None = None
    is_active: bool | None = None


class Page(_PageBase):
    """A page (sync)."""

    def update(
        self,
        *,
        is_default: bool | None = None,
        is_active: bool | None = None,
        timeout: float | None = None,
    ) -> Page:
        client = self._client_or_raise_sync()
        account_id = self._ctx_value("account_id")
        page_id = self.id or self._ctx_value("page_id")
        body: dict[str, Any] = {}
        if is_default is not None:
            body["is_default"] = is_default
        if is_active is not None:
            body["is_active"] = is_active
        data = client._patch(
            f"/v1/accounts/{account_id}/pages/{page_id}",
            json=body,
            timeout=timeout,
        )
        if isinstance(data, dict):
            updated = Page.model_validate(data)
            updated._bind(client, {"account_id": account_id, "page_id": page_id})
            return updated
        return self


class AsyncPage(_PageBase):
    """A page (async)."""

    async def update(
        self,
        *,
        is_default: bool | None = None,
        is_active: bool | None = None,
        timeout: float | None = None,
    ) -> AsyncPage:
        client = self._client_or_raise_async()
        account_id = self._ctx_value("account_id")
        page_id = self.id or self._ctx_value("page_id")
        body: dict[str, Any] = {}
        if is_default is not None:
            body["is_default"] = is_default
        if is_active is not None:
            body["is_active"] = is_active
        data = await client._patch(
            f"/v1/accounts/{account_id}/pages/{page_id}",
            json=body,
            timeout=timeout,
        )
        if isinstance(data, dict):
            updated = AsyncPage.model_validate(data)
            updated._bind(client, {"account_id": account_id, "page_id": page_id})
            return updated
        return self


# ---------------------------------------------------------------------------
# Pure data response models
# ---------------------------------------------------------------------------


class InteractionSettings(BaseModel):
    """Per-platform interaction toggles (TikTok creator info)."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    comment_disabled: bool | None = None
    duet_disabled: bool | None = None
    stitch_disabled: bool | None = None


class CreatorInfo(BaseModel):
    """Response of ``GET /v1/accounts/:id/creator-info``."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    platform: str | None = None
    nickname: str | None = None
    avatar_url: str | None = None
    can_post: bool | None = None
    max_video_duration_sec: int | None = None
    privacy_level_options: list[str] | None = None
    interaction_settings: InteractionSettings | None = None


class ConnectAccountRequest(BaseModel):
    """Request body for ``POST /v1/accounts/connect``."""

    model_config = ConfigDict(populate_by_name=True)

    platform: str
    brand_id: str | None = None
    metadata: dict[str, Any] | None = None


class ConnectAccountResponse(BaseModel):
    """Response when a direct-auth account is connected (HTTP 201)."""

    model_config = ConfigDict(populate_by_name=True)

    account_id: str
    platform: str
    username: str


class ConnectOAuthResponse(BaseModel):
    """Response when an OAuth2 flow is initiated (HTTP 202)."""

    model_config = ConfigDict(populate_by_name=True)

    auth_url: str
    state: str
    message: str


class OAuthExchangeRequest(BaseModel):
    """Request body for ``POST /v1/oauth/exchange``."""

    model_config = ConfigDict(populate_by_name=True)

    platform: str
    code: str
    metadata: dict[str, Any] | None = None


class OAuthExchangeResponse(BaseModel):
    """Response after a successful OAuth code exchange.

    Returns the list of connected accounts (some platforms return multiple,
    e.g. Facebook pages).
    """

    model_config = ConfigDict(populate_by_name=True)

    accounts: list[ConnectAccountResponse] | None = None
