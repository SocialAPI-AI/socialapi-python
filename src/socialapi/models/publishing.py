from __future__ import annotations

from datetime import datetime  # noqa: TC003
from typing import Any

from pydantic import BaseModel, ConfigDict


class TargetRequest(BaseModel):
    """Per-platform target with optional overrides for a post."""

    model_config = ConfigDict(populate_by_name=True)

    account_id: str
    page_id: str | None = None
    text: str | None = None
    title: str | None = None
    media_ids: list[str] | None = None
    first_comment: str | None = None
    visibility: str | None = None
    scheduled_at: datetime | None = None
    platform_data: dict[str, Any] | None = None


class CreatePostRequest(BaseModel):
    """Request body for ``POST /v1/posts``."""

    model_config = ConfigDict(populate_by_name=True)

    text: str
    title: str | None = None
    media_ids: list[str] | None = None
    visibility: str | None = None
    first_comment: str | None = None
    scheduled_at: datetime | None = None
    publish_now: bool | None = None
    skip_duplicate_check: bool | None = None
    targets: list[TargetRequest] | None = None


class UpdatePostRequest(BaseModel):
    """Request body for ``PATCH /v1/posts/:pid``."""

    model_config = ConfigDict(populate_by_name=True)

    text: str | None = None
    title: str | None = None
    media_ids: list[str] | None = None
    visibility: str | None = None
    first_comment: str | None = None
    scheduled_at: datetime | None = None
    hidden: bool | None = None
    targets: list[TargetRequest] | None = None


class UnpublishRequest(BaseModel):
    """Request body for ``POST /v1/posts/:pid/unpublish``."""

    model_config = ConfigDict(populate_by_name=True)

    account_id: str | None = None


class ValidatePostRequest(BaseModel):
    """Request body for ``POST /v1/posts/validate``."""

    model_config = ConfigDict(populate_by_name=True)

    text: str
    platforms: list[str] | None = None
    account_ids: list[str] | None = None
    media_ids: list[str] | None = None
    scheduled_at: datetime | None = None
    targets: list[TargetRequest] | None = None


# ---------------------------------------------------------------------------
# Nested constraint sub-models (wire shape from PlatformConstraints in Go)
# ---------------------------------------------------------------------------


class ConstraintsText(BaseModel):
    """Text constraints for a platform."""

    model_config = ConfigDict(populate_by_name=True)

    max_length: int = 0
    max_hashtags: int = 0
    max_mentions: int = 0
    counting_mode: str = "chars"


class ConstraintsMedia(BaseModel):
    """Media constraints for a platform."""

    model_config = ConfigDict(populate_by_name=True)

    max_image_size_bytes: int = 0
    max_video_size_bytes: int = 0
    max_video_duration_sec: int = 0
    min_video_duration_sec: int = 0
    max_video_fps: int = 0
    supported_image_types: list[str] | None = None
    supported_video_types: list[str] | None = None


class ConstraintsCarousel(BaseModel):
    """Carousel constraints for a platform."""

    model_config = ConfigDict(populate_by_name=True)

    supported: bool = False
    min_items: int = 0
    max_items: int = 0
    allow_video: bool = False
    images_only: bool = False
    photos_only: bool = False


class PlatformConstraints(BaseModel):
    """Platform-specific content constraints from ``GET /v1/posts/validate``.

    The wire shape is nested: ``text``, ``media``, and ``carousel`` sub-objects
    matching the Go ``service.PlatformConstraints`` struct.
    """

    model_config = ConfigDict(populate_by_name=True)

    text: ConstraintsText = ConstraintsText()
    media: ConstraintsMedia = ConstraintsMedia()
    carousel: ConstraintsCarousel = ConstraintsCarousel()


class MediaUploadURL(BaseModel):
    """Presigned upload URL from ``GET /v1/media/upload-url``."""

    model_config = ConfigDict(populate_by_name=True)

    media_id: str
    upload_url: str
    expires_at: datetime


class MediaUploadResponse(BaseModel):
    """Response from ``POST /v1/media/upload`` (server-side upload)."""

    model_config = ConfigDict(populate_by_name=True)

    media_id: str


class ImportRowError(BaseModel):
    """Per-row error detail from CSV import."""

    model_config = ConfigDict(populate_by_name=True)

    row: int
    message: str


class ImportPostsResponse(BaseModel):
    """Response from ``POST /v1/posts/import``."""

    model_config = ConfigDict(populate_by_name=True)

    total_rows: int
    created: int
    failed: int
    errors: list[ImportRowError] | None = None
    posts: list[Any] | None = None
