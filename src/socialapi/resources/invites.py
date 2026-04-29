from __future__ import annotations

from typing import TYPE_CHECKING, Any

from socialapi.models.invites import AsyncInvite, AsyncInviteListItem, Invite, InviteListItem

if TYPE_CHECKING:
    from socialapi._base_client import BaseAsyncClient, BaseSyncClient


class Invites:
    """Manage brand invites (sync)."""

    _client: BaseSyncClient

    def __init__(self, client: BaseSyncClient) -> None:
        self._client = client

    def create(
        self,
        *,
        brand_id: str,
        platform: str,
        expires_in_days: int = 7,
        timeout: float | None = None,
    ) -> Invite:
        body: dict[str, Any] = {
            "brand_id": brand_id,
            "platform": platform,
            "expires_in_days": expires_in_days,
        }
        data = self._client._post("/v1/invites", json=body, timeout=timeout)
        invite = Invite.model_validate(data)
        invite._bind(self._client, {"brand_id": brand_id})
        return invite

    def list(self, brand_id: str, *, timeout: float | None = None) -> list[InviteListItem]:
        data = self._client._get("/v1/invites", params={"brand_id": brand_id}, timeout=timeout)
        raw_items: list[Any] = data.get("data", [])
        items = [InviteListItem.model_validate(item) for item in raw_items]
        for item in items:
            item._bind(self._client, {"brand_id": brand_id})
        return items

    def revoke(self, invite_id: str, *, timeout: float | None = None) -> None:
        self._client._delete(f"/v1/invites/{invite_id}", timeout=timeout)


class AsyncInvites:
    """Manage brand invites (async)."""

    _client: BaseAsyncClient

    def __init__(self, client: BaseAsyncClient) -> None:
        self._client = client

    async def create(
        self,
        *,
        brand_id: str,
        platform: str,
        expires_in_days: int = 7,
        timeout: float | None = None,
    ) -> AsyncInvite:
        body: dict[str, Any] = {
            "brand_id": brand_id,
            "platform": platform,
            "expires_in_days": expires_in_days,
        }
        data = await self._client._post("/v1/invites", json=body, timeout=timeout)
        invite = AsyncInvite.model_validate(data)
        invite._bind(self._client, {"brand_id": brand_id})
        return invite

    async def list(self, brand_id: str, *, timeout: float | None = None) -> list[AsyncInviteListItem]:
        data = await self._client._get("/v1/invites", params={"brand_id": brand_id}, timeout=timeout)
        raw_items: list[Any] = data.get("data", [])
        items = [AsyncInviteListItem.model_validate(item) for item in raw_items]
        for item in items:
            item._bind(self._client, {"brand_id": brand_id})
        return items

    async def revoke(self, invite_id: str, *, timeout: float | None = None) -> None:
        await self._client._delete(f"/v1/invites/{invite_id}", timeout=timeout)
