from __future__ import annotations

from datetime import datetime  # noqa: TC003

from pydantic import BaseModel, ConfigDict

from socialapi._bound import _Bound


class _MediaItemBase(_Bound):
    """Shared fields for MediaItem / AsyncMediaItem."""

    id: str
    filename: str
    content_type: str
    size_bytes: int
    status: str
    url: str
    created_at: datetime


class MediaItem(_MediaItemBase):
    """An uploaded media file (sync)."""

    def delete(self, *, timeout: float | None = None) -> None:
        client = self._client_or_raise_sync()
        client._delete(f"/v1/media/{self.id}", timeout=timeout)

    def verify(self, *, timeout: float | None = None) -> None:
        client = self._client_or_raise_sync()
        client._post(f"/v1/media/{self.id}/verify", timeout=timeout)


class AsyncMediaItem(_MediaItemBase):
    """An uploaded media file (async)."""

    async def delete(self, *, timeout: float | None = None) -> None:
        client = self._client_or_raise_async()
        await client._delete(f"/v1/media/{self.id}", timeout=timeout)

    async def verify(self, *, timeout: float | None = None) -> None:
        client = self._client_or_raise_async()
        await client._post(f"/v1/media/{self.id}/verify", timeout=timeout)


class StorageUsage(BaseModel):
    """Storage usage for the authenticated user."""

    model_config = ConfigDict(populate_by_name=True)

    used_bytes: int
    limit_bytes: int
    count: int
