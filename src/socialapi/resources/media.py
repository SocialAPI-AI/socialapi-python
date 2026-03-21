"""Media resource."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from socialapi.models.media import MediaListResponse, MediaUploadInfo, MediaUploadResponse, StorageUsageResponse
from socialapi.models.shared import SuccessResponse

if TYPE_CHECKING:
    from socialapi._async_client import AsyncSocialAPI
    from socialapi._client import SocialAPI


class Media:
    """Synchronous media resource.

    Provides methods for uploading, verifying, listing, and deleting media.
    """

    def __init__(self, client: SocialAPI) -> None:
        self._client = client

    def upload_url(self, media_type: str, filename: str) -> MediaUploadInfo:
        """Get a pre-signed upload URL for direct media upload.

        Args:
            media_type: The MIME type of the media (e.g. ``"image/png"``).
            filename: The original filename of the media.

        Returns:
            A MediaUploadInfo with the pre-signed upload URL and media ID.

        Raises:
            ValidationError: If the media type is unsupported.
        """
        return self._client._get(
            "/v1/media/upload-url",
            params={"media_type": media_type, "filename": filename},
            response_model=MediaUploadInfo,
        )

    def upload(self, file: Any) -> MediaUploadResponse:
        """Upload media directly via multipart form data.

        Args:
            file: The file to upload. Can be a file-like object, bytes, or a tuple
                of ``(filename, file_object)`` or ``(filename, file_object, content_type)``.

        Returns:
            A MediaUploadResponse with the uploaded media ID.

        Raises:
            StorageQuotaError: If the storage quota is exceeded.
        """
        return self._client._post(
            "/v1/media/upload",
            files={"file": file},
            response_model=MediaUploadResponse,
        )

    def verify(self, media_id: str) -> SuccessResponse:
        """Verify that an uploaded media file is ready for use.

        Args:
            media_id: The media ID to verify.

        Returns:
            A SuccessResponse indicating verification status.

        Raises:
            NotFoundError: If the media is not found.
        """
        return self._client._post(f"/v1/media/{media_id}/verify", response_model=SuccessResponse)

    def list(self, *, limit: int = 50, cursor: str | None = None) -> MediaListResponse:
        """List uploaded media files.

        Args:
            limit: Maximum results per page (1--100). Defaults to 50.
            cursor: Opaque cursor from a previous response for pagination.

        Returns:
            A MediaListResponse containing the media items.
        """
        params: dict[str, Any] = {"limit": limit}
        if cursor is not None:
            params["cursor"] = cursor
        return self._client._get("/v1/media", params=params, response_model=MediaListResponse)

    def delete(self, media_id: str) -> None:
        """Delete an uploaded media file.

        Args:
            media_id: The media ID to delete.

        Raises:
            NotFoundError: If the media is not found.
        """
        self._client._delete(f"/v1/media/{media_id}")

    def storage(self) -> StorageUsageResponse:
        """Get current storage usage and limits.

        Returns:
            A StorageUsageResponse with used and limit bytes.
        """
        return self._client._get("/v1/media/storage", response_model=StorageUsageResponse)


class AsyncMedia:
    """Asynchronous media resource.

    Provides methods for uploading, verifying, listing, and deleting media.
    """

    def __init__(self, client: AsyncSocialAPI) -> None:
        self._client = client

    async def upload_url(self, media_type: str, filename: str) -> MediaUploadInfo:
        """Get a pre-signed upload URL for direct media upload.

        Args:
            media_type: The MIME type of the media (e.g. ``"image/png"``).
            filename: The original filename of the media.

        Returns:
            A MediaUploadInfo with the pre-signed upload URL and media ID.

        Raises:
            ValidationError: If the media type is unsupported.
        """
        return await self._client._get(
            "/v1/media/upload-url",
            params={"media_type": media_type, "filename": filename},
            response_model=MediaUploadInfo,
        )

    async def upload(self, file: Any) -> MediaUploadResponse:
        """Upload media directly via multipart form data.

        Args:
            file: The file to upload. Can be a file-like object, bytes, or a tuple
                of ``(filename, file_object)`` or ``(filename, file_object, content_type)``.

        Returns:
            A MediaUploadResponse with the uploaded media ID.

        Raises:
            StorageQuotaError: If the storage quota is exceeded.
        """
        return await self._client._post(
            "/v1/media/upload",
            files={"file": file},
            response_model=MediaUploadResponse,
        )

    async def verify(self, media_id: str) -> SuccessResponse:
        """Verify that an uploaded media file is ready for use.

        Args:
            media_id: The media ID to verify.

        Returns:
            A SuccessResponse indicating verification status.

        Raises:
            NotFoundError: If the media is not found.
        """
        return await self._client._post(f"/v1/media/{media_id}/verify", response_model=SuccessResponse)

    async def list(self, *, limit: int = 50, cursor: str | None = None) -> MediaListResponse:
        """List uploaded media files.

        Args:
            limit: Maximum results per page (1--100). Defaults to 50.
            cursor: Opaque cursor from a previous response for pagination.

        Returns:
            A MediaListResponse containing the media items.
        """
        params: dict[str, Any] = {"limit": limit}
        if cursor is not None:
            params["cursor"] = cursor
        return await self._client._get("/v1/media", params=params, response_model=MediaListResponse)

    async def delete(self, media_id: str) -> None:
        """Delete an uploaded media file.

        Args:
            media_id: The media ID to delete.

        Raises:
            NotFoundError: If the media is not found.
        """
        await self._client._delete(f"/v1/media/{media_id}")

    async def storage(self) -> StorageUsageResponse:
        """Get current storage usage and limits.

        Returns:
            A StorageUsageResponse with used and limit bytes.
        """
        return await self._client._get("/v1/media/storage", response_model=StorageUsageResponse)
