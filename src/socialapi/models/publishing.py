from __future__ import annotations

from typing import Any

from pydantic import BaseModel, ConfigDict


class TargetRequest(BaseModel):
    """Per-platform target with optional overrides for a post."""

    model_config = ConfigDict(populate_by_name=True)

    account_id: str
    text: str | None = None
    title: str | None = None
    media_ids: list[str] | None = None
    first_comment: str | None = None
    visibility: str | None = None
    scheduled_at: str | None = None
    platform_data: dict[str, Any] | None = None


class CreatePostRequest(BaseModel):
    """Request body for ``POST /v1/posts``."""

    model_config = ConfigDict(populate_by_name=True)

    text: str
    title: str | None = None
    media_ids: list[str] | None = None
    visibility: str | None = None
    first_comment: str | None = None
    scheduled_at: str | None = None
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
    scheduled_at: str | None = None
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
    scheduled_at: str | None = None
    targets: list[TargetRequest] | None = None


class PlatformConstraints(BaseModel):
    """Platform-specific content constraints from ``GET /v1/posts/validate``."""

    model_config = ConfigDict(populate_by_name=True)

    platform: str
    max_text_length: int | None = None
    max_title_length: int | None = None
    max_images: int | None = None
    max_videos: int | None = None
    max_media: int | None = None
    supported_media_types: list[str] | None = None
    supports_scheduling: bool | None = None
    min_schedule_ahead_minutes: int | None = None


class MediaUploadURL(BaseModel):
    """Presigned upload URL from ``GET /v1/media/upload-url``."""

    model_config = ConfigDict(populate_by_name=True)

    media_id: str
    upload_url: str
    expires_at: str


class MediaUploadResponse(BaseModel):
    """Response from ``POST /v1/media/upload`` (server-side upload)."""

    model_config = ConfigDict(populate_by_name=True)

    media_id: str
