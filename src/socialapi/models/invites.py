from __future__ import annotations

from datetime import datetime  # noqa: TC003

from pydantic import BaseModel, ConfigDict

from socialapi._bound import _Bound


class _InviteBase(_Bound):
    """Shared fields for Invite / AsyncInvite (full create response)."""

    id: str
    platform: str
    token: str
    url: str
    expires_at: datetime


class Invite(_InviteBase):
    """An invite created for a brand (sync, full response with token)."""

    def revoke(self, *, timeout: float | None = None) -> None:
        client = self._client_or_raise_sync()
        client._delete(f"/v1/invites/{self.id}", timeout=timeout)


class AsyncInvite(_InviteBase):
    """An invite created for a brand (async, full response with token)."""

    async def revoke(self, *, timeout: float | None = None) -> None:
        client = self._client_or_raise_async()
        await client._delete(f"/v1/invites/{self.id}", timeout=timeout)


class _InviteListItemBase(_Bound):
    """Shared fields for InviteListItem / AsyncInviteListItem (list response)."""

    id: str
    platform: str
    token: str
    url: str
    is_active: bool
    expires_at: datetime
    created_at: datetime


class InviteListItem(_InviteListItemBase):
    """An invite as returned by the list endpoint (sync)."""

    def revoke(self, *, timeout: float | None = None) -> None:
        client = self._client_or_raise_sync()
        client._delete(f"/v1/invites/{self.id}", timeout=timeout)


class AsyncInviteListItem(_InviteListItemBase):
    """An invite as returned by the list endpoint (async)."""

    async def revoke(self, *, timeout: float | None = None) -> None:
        client = self._client_or_raise_async()
        await client._delete(f"/v1/invites/{self.id}", timeout=timeout)


class CreateInviteRequest(BaseModel):
    """Request body for ``POST /v1/invites``."""

    model_config = ConfigDict(populate_by_name=True)

    brand_id: str
    platform: str
    expires_in_days: int
