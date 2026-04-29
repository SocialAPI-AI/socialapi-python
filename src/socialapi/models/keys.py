from __future__ import annotations

from datetime import datetime  # noqa: TC003

from pydantic import BaseModel, ConfigDict

from socialapi._bound import _Bound


class _APIKeyBase(_Bound):
    """Shared fields for APIKey / AsyncAPIKey."""

    id: str
    name: str
    preview: str
    is_active: bool
    last_used_at: datetime | None = None
    created_at: datetime


class APIKey(_APIKeyBase):
    """A registered API key (sync). Never includes the raw secret."""

    def revoke(self, *, timeout: float | None = None) -> None:
        client = self._client_or_raise_sync()
        client._delete(f"/v1/keys/{self.id}", timeout=timeout)


class AsyncAPIKey(_APIKeyBase):
    """A registered API key (async). Never includes the raw secret."""

    async def revoke(self, *, timeout: float | None = None) -> None:
        client = self._client_or_raise_async()
        await client._delete(f"/v1/keys/{self.id}", timeout=timeout)


class CreateKeyRequest(BaseModel):
    """Request body for ``POST /v1/keys``."""

    model_config = ConfigDict(populate_by_name=True)

    name: str


class CreateKeyResponse(BaseModel):
    """Response returned once when a new key is created (includes raw key)."""

    model_config = ConfigDict(populate_by_name=True)

    id: str
    name: str
    raw_key: str
    message: str
