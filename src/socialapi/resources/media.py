from __future__ import annotations

from typing import TYPE_CHECKING, Any

from socialapi.models.media import AsyncMediaItem, MediaItem, StorageUsage
from socialapi.models.publishing import MediaUploadResponse, MediaUploadURL

if TYPE_CHECKING:
    from socialapi._base_client import BaseAsyncClient, BaseSyncClient


class Media:
    """Manage media files (sync)."""

    _client: BaseSyncClient

    def __init__(self, client: BaseSyncClient) -> None:
        self._client = client

    def list(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        timeout: float | None = None,
    ) -> list[MediaItem]:
        params: dict[str, Any] = {}
        if limit is not None:
            params["limit"] = limit
        if cursor is not None:
            params["cursor"] = cursor
        data = self._client._get("/v1/media", params=params, timeout=timeout)
        raw_items: list[Any] = data.get("data", [])
        items = [MediaItem.model_validate(item) for item in raw_items]
        for item in items:
            item._bind(self._client)
        return items

    def get_upload_url(
        self,
        *,
        media_type: str,
        filename: str,
        timeout: float | None = None,
    ) -> MediaUploadURL:
        params: dict[str, Any] = {"media_type": media_type, "filename": filename}
        data = self._client._get("/v1/media/upload-url", params=params, timeout=timeout)
        return MediaUploadURL.model_validate(data)

    def upload(self, file: Any, *, timeout: float | None = None) -> MediaUploadResponse:
        data = self._client._post("/v1/media/upload", json={"file": "multipart"}, timeout=timeout)
        return MediaUploadResponse.model_validate(data)

    def verify(self, media_id: str, *, timeout: float | None = None) -> None:
        self._client._post(f"/v1/media/{media_id}/verify", timeout=timeout)

    def delete(self, media_id: str, *, timeout: float | None = None) -> None:
        self._client._delete(f"/v1/media/{media_id}", timeout=timeout)

    def get_storage_usage(self, *, timeout: float | None = None) -> StorageUsage:
        data = self._client._get("/v1/media/storage", timeout=timeout)
        return StorageUsage.model_validate(data)


class AsyncMedia:
    """Manage media files (async)."""

    _client: BaseAsyncClient

    def __init__(self, client: BaseAsyncClient) -> None:
        self._client = client

    async def list(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        timeout: float | None = None,
    ) -> list[AsyncMediaItem]:
        params: dict[str, Any] = {}
        if limit is not None:
            params["limit"] = limit
        if cursor is not None:
            params["cursor"] = cursor
        data = await self._client._get("/v1/media", params=params, timeout=timeout)
        raw_items: list[Any] = data.get("data", [])
        items = [AsyncMediaItem.model_validate(item) for item in raw_items]
        for item in items:
            item._bind(self._client)
        return items

    async def get_upload_url(
        self,
        *,
        media_type: str,
        filename: str,
        timeout: float | None = None,
    ) -> MediaUploadURL:
        params: dict[str, Any] = {"media_type": media_type, "filename": filename}
        data = await self._client._get("/v1/media/upload-url", params=params, timeout=timeout)
        return MediaUploadURL.model_validate(data)

    async def upload(self, file: Any, *, timeout: float | None = None) -> MediaUploadResponse:
        data = await self._client._post("/v1/media/upload", json={"file": "multipart"}, timeout=timeout)
        return MediaUploadResponse.model_validate(data)

    async def verify(self, media_id: str, *, timeout: float | None = None) -> None:
        await self._client._post(f"/v1/media/{media_id}/verify", timeout=timeout)

    async def delete(self, media_id: str, *, timeout: float | None = None) -> None:
        await self._client._delete(f"/v1/media/{media_id}", timeout=timeout)

    async def get_storage_usage(self, *, timeout: float | None = None) -> StorageUsage:
        data = await self._client._get("/v1/media/storage", timeout=timeout)
        return StorageUsage.model_validate(data)
