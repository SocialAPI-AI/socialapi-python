from __future__ import annotations

from typing import TYPE_CHECKING, Any

from socialapi.models.media import AsyncMediaItem, MediaItem, StorageUsage
from socialapi.models.publishing import MediaUploadResponse, MediaUploadURL

if TYPE_CHECKING:
    from socialapi._base_client import BaseAsyncClient, BaseSyncClient
    from socialapi._pagination import AsyncCursorPage, CursorPage


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
    ) -> CursorPage[MediaItem]:
        """List uploaded media files, returning a paginated result set.

        Args:
            limit: Maximum number of items to return (server default 50, max 100).
            cursor: Pagination cursor from a previous response.
            timeout: Optional per-request timeout in seconds.

        Returns:
            A ``CursorPage[MediaItem]`` containing the current page of media items.

        Raises:
            AuthenticationError: If the API key is invalid.
        """
        params: dict[str, Any] = {}
        if limit is not None:
            params["limit"] = limit
        if cursor is not None:
            params["cursor"] = cursor
        return self._client._get_paginated("/v1/media", params=params, model=MediaItem, timeout=timeout)

    def get_upload_url(
        self,
        *,
        media_type: str,
        filename: str,
        timeout: float | None = None,
    ) -> MediaUploadURL:
        """Get a presigned upload URL for client-side media upload.

        Args:
            media_type: MIME type of the file (e.g. ``image/jpeg``).
            filename: Name of the file to upload.
            timeout: Optional per-request timeout in seconds.

        Returns:
            A ``MediaUploadURL`` containing the presigned URL and media ID.

        Raises:
            AuthenticationError: If the API key is invalid.
        """
        params: dict[str, Any] = {"media_type": media_type, "filename": filename}
        data = self._client._get("/v1/media/upload-url", params=params, timeout=timeout)
        return MediaUploadURL.model_validate(data)

    def upload(
        self,
        *,
        content: bytes,
        filename: str,
        content_type: str | None = None,
        timeout: float | None = None,
    ) -> MediaUploadResponse:
        """Upload a media file via server-side multipart upload.

        Sends the file as ``multipart/form-data`` with the field name ``file``.
        The server stores the file and returns a ``media_id`` that can be used
        in post targets.

        Args:
            content: Raw bytes of the file to upload.
            filename: Filename to use in the multipart part (e.g. ``photo.jpg``).
            content_type: Optional MIME type override (e.g. ``image/jpeg``).
                If omitted, httpx infers it from the filename.
            timeout: Optional per-request timeout in seconds.

        Returns:
            A ``MediaUploadResponse`` with ``media_id``.

        Raises:
            AuthenticationError: If the API key is invalid.
            StorageQuotaExceededError: If the storage quota is exceeded.
        """
        file_tuple: tuple[str, bytes] | tuple[str, bytes, str] = (
            (filename, content, content_type) if content_type is not None else (filename, content)
        )
        files: dict[str, Any] = {"file": file_tuple}
        data = self._client._post_multipart("/v1/media/upload", files=files, timeout=timeout)
        return MediaUploadResponse.model_validate(data)

    def verify(self, media_id: str, *, timeout: float | None = None) -> None:
        """Confirm that a media file has been uploaded successfully.

        Args:
            media_id: ID of the media item to verify.
            timeout: Optional per-request timeout in seconds.

        Raises:
            AuthenticationError: If the API key is invalid.
            NotFoundError: If the media item does not exist.
        """
        self._client._post(f"/v1/media/{media_id}/verify", timeout=timeout)

    def delete(self, media_id: str, *, timeout: float | None = None) -> None:
        """Delete a media file.

        Args:
            media_id: ID of the media item to delete.
            timeout: Optional per-request timeout in seconds.

        Raises:
            AuthenticationError: If the API key is invalid.
            NotFoundError: If the media item does not exist.
        """
        self._client._delete(f"/v1/media/{media_id}", timeout=timeout)

    def get_storage_usage(self, *, timeout: float | None = None) -> StorageUsage:
        """Get storage usage statistics for the authenticated user.

        Args:
            timeout: Optional per-request timeout in seconds.

        Returns:
            A ``StorageUsage`` instance with bytes used, limit, and file count.

        Raises:
            AuthenticationError: If the API key is invalid.
        """
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
    ) -> AsyncCursorPage[AsyncMediaItem]:
        """List uploaded media files, returning a paginated result set.

        Args:
            limit: Maximum number of items to return (server default 50, max 100).
            cursor: Pagination cursor from a previous response.
            timeout: Optional per-request timeout in seconds.

        Returns:
            An ``AsyncCursorPage[AsyncMediaItem]`` containing the current page.

        Raises:
            AuthenticationError: If the API key is invalid.
        """
        params: dict[str, Any] = {}
        if limit is not None:
            params["limit"] = limit
        if cursor is not None:
            params["cursor"] = cursor
        return await self._client._get_paginated("/v1/media", params=params, model=AsyncMediaItem, timeout=timeout)

    async def get_upload_url(
        self,
        *,
        media_type: str,
        filename: str,
        timeout: float | None = None,
    ) -> MediaUploadURL:
        """Get a presigned upload URL for client-side media upload.

        Args:
            media_type: MIME type of the file (e.g. ``image/jpeg``).
            filename: Name of the file to upload.
            timeout: Optional per-request timeout in seconds.

        Returns:
            A ``MediaUploadURL`` containing the presigned URL and media ID.

        Raises:
            AuthenticationError: If the API key is invalid.
        """
        params: dict[str, Any] = {"media_type": media_type, "filename": filename}
        data = await self._client._get("/v1/media/upload-url", params=params, timeout=timeout)
        return MediaUploadURL.model_validate(data)

    async def upload(
        self,
        *,
        content: bytes,
        filename: str,
        content_type: str | None = None,
        timeout: float | None = None,
    ) -> MediaUploadResponse:
        """Upload a media file via server-side multipart upload.

        Sends the file as ``multipart/form-data`` with the field name ``file``.
        The server stores the file and returns a ``media_id`` that can be used
        in post targets.

        Args:
            content: Raw bytes of the file to upload.
            filename: Filename to use in the multipart part (e.g. ``photo.jpg``).
            content_type: Optional MIME type override (e.g. ``image/jpeg``).
                If omitted, httpx infers it from the filename.
            timeout: Optional per-request timeout in seconds.

        Returns:
            A ``MediaUploadResponse`` with ``media_id``.

        Raises:
            AuthenticationError: If the API key is invalid.
            StorageQuotaExceededError: If the storage quota is exceeded.
        """
        file_tuple: tuple[str, bytes] | tuple[str, bytes, str] = (
            (filename, content, content_type) if content_type is not None else (filename, content)
        )
        files: dict[str, Any] = {"file": file_tuple}
        data = await self._client._post_multipart("/v1/media/upload", files=files, timeout=timeout)
        return MediaUploadResponse.model_validate(data)

    async def verify(self, media_id: str, *, timeout: float | None = None) -> None:
        """Confirm that a media file has been uploaded successfully.

        Args:
            media_id: ID of the media item to verify.
            timeout: Optional per-request timeout in seconds.

        Raises:
            AuthenticationError: If the API key is invalid.
            NotFoundError: If the media item does not exist.
        """
        await self._client._post(f"/v1/media/{media_id}/verify", timeout=timeout)

    async def delete(self, media_id: str, *, timeout: float | None = None) -> None:
        """Delete a media file.

        Args:
            media_id: ID of the media item to delete.
            timeout: Optional per-request timeout in seconds.

        Raises:
            AuthenticationError: If the API key is invalid.
            NotFoundError: If the media item does not exist.
        """
        await self._client._delete(f"/v1/media/{media_id}", timeout=timeout)

    async def get_storage_usage(self, *, timeout: float | None = None) -> StorageUsage:
        """Get storage usage statistics for the authenticated user.

        Args:
            timeout: Optional per-request timeout in seconds.

        Returns:
            A ``StorageUsage`` instance with bytes used, limit, and file count.

        Raises:
            AuthenticationError: If the API key is invalid.
        """
        data = await self._client._get("/v1/media/storage", timeout=timeout)
        return StorageUsage.model_validate(data)
