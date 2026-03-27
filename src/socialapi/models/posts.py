from __future__ import annotations

from datetime import datetime  # noqa: TC003
from typing import Any

from pydantic import BaseModel, ConfigDict


class PostTargetError(BaseModel):
    """Structured error info for a failed platform target."""

    model_config = ConfigDict(populate_by_name=True)

    message: str
    category: str
    caused_by: str


class PostTargetMetrics(BaseModel):
    """Engagement metrics for a published platform target."""

    model_config = ConfigDict(populate_by_name=True)

    likes: int = 0
    comments: int = 0
    shares: int = 0
    saves: int = 0
    extra: dict[str, Any] | None = None


class PostTarget(BaseModel):
    """Per-platform delivery result nested in a Post."""

    model_config = ConfigDict(populate_by_name=True)

    account_id: str | None = None
    platform: str
    status: str
    text: str | None = None
    title: str | None = None
    first_comment: str | None = None
    visibility: str | None = None
    scheduled_at: datetime | None = None
    platform_post_id: str | None = None
    permalink: str | None = None
    published_at: datetime | None = None
    metrics: PostTargetMetrics | None = None
    metrics_synced_at: datetime | None = None
    error: PostTargetError | None = None


class Post(BaseModel):
    """A post in the unified publishing system."""

    model_config = ConfigDict(populate_by_name=True)

    id: str
    text: str | None = None
    title: str | None = None
    status: str
    visibility: str | None = None
    media_ids: list[str] | None = None
    scheduled_at: datetime | None = None
    published_at: datetime | None = None
    hidden: bool = False
    retry_count: int = 0
    created_at: datetime
    updated_at: datetime
    targets: list[PostTarget] | None = None


class PostMetrics(BaseModel):
    """Aggregated metrics response for ``GET /v1/posts/:id/metrics``."""

    model_config = ConfigDict(populate_by_name=True)

    post_id: str
    targets: list[PostTarget]


class ValidationIssue(BaseModel):
    """A single error or warning from content validation."""

    model_config = ConfigDict(populate_by_name=True)

    platform: str
    field: str
    message: str
    target: str | None = None


class ValidationResult(BaseModel):
    """Result of ``POST /v1/posts/validate``."""

    model_config = ConfigDict(populate_by_name=True)

    valid: bool
    errors: list[ValidationIssue]
    warnings: list[ValidationIssue]
