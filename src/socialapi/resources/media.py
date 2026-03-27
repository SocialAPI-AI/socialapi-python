from __future__ import annotations

from typing import TYPE_CHECKING, Any

from socialapi.models.media import MediaItem, StorageUsage
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
        """List uploaded media files.

        Args:
            limit: Maximum number of results (max 100).
            cursor: Pagination cursor from a previous response.
            timeout: Override the client-level timeout for this request.

        Returns:
            A list of media items.

        Raises:
            AuthenticationError: If the API key is invalid.
        """
        params: dict[str, Any] = {}
        if limit is not None:
            params["limit"] = limit
        if cursor is not None:
            params["cursor"] = cursor
        data = self._client._get("/v1/media", params=params, timeout=timeout)
        raw_items: list[Any] = data.get("data", [])
        return [MediaItem.model_validate(item) for item in raw_items]

    def get_upload_url(
        self,
        *,
        media_type: str,
        filename: str,
        timeout: float | None = None,
    ) -> MediaUploadURL:
        """Get a presigned URL for client-side media upload.

        Args:
            media_type: MIME type of the file (e.g. ``"image/jpeg"``).
            filename: Original filename.
            timeout: Override the client-level timeout for this request.

        Returns:
            Upload URL and metadata.

        Raises:
            BadRequestError: If media_type or filename is missing.
            StorageQuotaExceededError: If storage quota is exceeded.
            AuthenticationError: If the API key is invalid.
        """
        params: dict[str, Any] = {
            "media_type": media_type,
            "filename": filename,
        }
        data = self._client._get("/v1/media/upload-url", params=params, timeout=timeout)
        return MediaUploadURL.model_validate(data)

    def upload(
        self,
        file: Any,
        *,
        timeout: float | None = None,
    ) -> MediaUploadResponse:
        """Upload a media file through the API server.

        Note: This method sends a multipart/form-data request. The ``file``
        parameter should be a file-like object or bytes.

        Args:
            file: The file to upload.
            timeout: Override the client-level timeout for this request.

        Returns:
            The upload result with the media ID.

        Raises:
            BadRequestError: If the file is missing or exceeds 50 MB.
            StorageQuotaExceededError: If storage quota is exceeded.
            AuthenticationError: If the API key is invalid.
        """
        data = self._client._post("/v1/media/upload", json={"file": "multipart"}, timeout=timeout)
        return MediaUploadResponse.model_validate(data)

    def verify(
        self,
        media_id: str,
        *,
        timeout: float | None = None,
    ) -> None:
        """Verify that a presigned-URL upload completed successfully.

        Args:
            media_id: The media ID from the upload URL response.
            timeout: Override the client-level timeout for this request.

        Raises:
            NotFoundError: If the media does not exist.
            AuthenticationError: If the API key is invalid.
        """
        self._client._post(f"/v1/media/{media_id}/verify", timeout=timeout)

    def delete(
        self,
        media_id: str,
        *,
        timeout: float | None = None,
    ) -> None:
        """Delete a media file from storage.

        Args:
            media_id: The media ID.
            timeout: Override the client-level timeout for this request.

        Raises:
            NotFoundError: If the media does not exist.
            AuthenticationError: If the API key is invalid.
        """
        self._client._delete(f"/v1/media/{media_id}", timeout=timeout)

    def get_storage_usage(
        self,
        *,
        timeout: float | None = None,
    ) -> StorageUsage:
        """Get storage usage for the current user.

        Args:
            timeout: Override the client-level timeout for this request.

        Returns:
            Storage usage statistics.

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
    ) -> list[MediaItem]:
        """List uploaded media files.

        Args:
            limit: Maximum number of results (max 100).
            cursor: Pagination cursor from a previous response.
            timeout: Override the client-level timeout for this request.

        Returns:
            A list of media items.

        Raises:
            AuthenticationError: If the API key is invalid.
        """
        params: dict[str, Any] = {}
        if limit is not None:
            params["limit"] = limit
        if cursor is not None:
            params["cursor"] = cursor
        data = await self._client._get("/v1/media", params=params, timeout=timeout)
        raw_items: list[Any] = data.get("data", [])
        return [MediaItem.model_validate(item) for item in raw_items]

    async def get_upload_url(
        self,
        *,
        media_type: str,
        filename: str,
        timeout: float | None = None,
    ) -> MediaUploadURL:
        """Get a presigned URL for client-side media upload.

        Args:
            media_type: MIME type of the file (e.g. ``"image/jpeg"``).
            filename: Original filename.
            timeout: Override the client-level timeout for this request.

        Returns:
            Upload URL and metadata.

        Raises:
            BadRequestError: If media_type or filename is missing.
            StorageQuotaExceededError: If storage quota is exceeded.
            AuthenticationError: If the API key is invalid.
        """
        params: dict[str, Any] = {
            "media_type": media_type,
            "filename": filename,
        }
        data = await self._client._get("/v1/media/upload-url", params=params, timeout=timeout)
        return MediaUploadURL.model_validate(data)

    async def upload(
        self,
        file: Any,
        *,
        timeout: float | None = None,
    ) -> MediaUploadResponse:
        """Upload a media file through the API server.

        Note: This method sends a multipart/form-data request. The ``file``
        parameter should be a file-like object or bytes.

        Args:
            file: The file to upload.
            timeout: Override the client-level timeout for this request.

        Returns:
            The upload result with the media ID.

        Raises:
            BadRequestError: If the file is missing or exceeds 50 MB.
            StorageQuotaExceededError: If storage quota is exceeded.
            AuthenticationError: If the API key is invalid.
        """
        data = await self._client._post("/v1/media/upload", json={"file": "multipart"}, timeout=timeout)
        return MediaUploadResponse.model_validate(data)

    async def verify(
        self,
        media_id: str,
        *,
        timeout: float | None = None,
    ) -> None:
        """Verify that a presigned-URL upload completed successfully.

        Args:
            media_id: The media ID from the upload URL response.
            timeout: Override the client-level timeout for this request.

        Raises:
            NotFoundError: If the media does not exist.
            AuthenticationError: If the API key is invalid.
        """
        await self._client._post(f"/v1/media/{media_id}/verify", timeout=timeout)

    async def delete(
        self,
        media_id: str,
        *,
        timeout: float | None = None,
    ) -> None:
        """Delete a media file from storage.

        Args:
            media_id: The media ID.
            timeout: Override the client-level timeout for this request.

        Raises:
            NotFoundError: If the media does not exist.
            AuthenticationError: If the API key is invalid.
        """
        await self._client._delete(f"/v1/media/{media_id}", timeout=timeout)

    async def get_storage_usage(
        self,
        *,
        timeout: float | None = None,
    ) -> StorageUsage:
        """Get storage usage for the current user.

        Args:
            timeout: Override the client-level timeout for this request.

        Returns:
            Storage usage statistics.

        Raises:
            AuthenticationError: If the API key is invalid.
        """
        data = await self._client._get("/v1/media/storage", timeout=timeout)
        return StorageUsage.model_validate(data)
