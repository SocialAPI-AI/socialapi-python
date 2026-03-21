"""Media models."""

from __future__ import annotations

from pydantic import BaseModel


class MediaItem(BaseModel):
    """An uploaded media item."""

    id: str
    filename: str
    content_type: str
    size_bytes: int
    status: str
    url: str
    created_at: str


class MediaListResponse(BaseModel):
    """Response for listing media items."""

    data: list[MediaItem]
    count: int
    cursor: str | None = None


class MediaUploadInfo(BaseModel):
    """Pre-signed upload URL information."""

    media_id: str
    upload_url: str
    expires_at: str


class MediaUploadResponse(BaseModel):
    """Response after uploading media directly."""

    media_id: str


class StorageUsageResponse(BaseModel):
    """Current storage usage and limits."""

    used_bytes: int
    limit_bytes: int
    count: int
