"""Post models."""

from typing import Any

from pydantic import BaseModel, Field


class PostResult(BaseModel):
    """Result of publishing a post to a single account."""

    account_id: str
    platform: str
    status: str
    platform_post_id: str = ""
    permalink: str = ""
    error: str | None = None


class ScheduledPost(BaseModel):
    """A scheduled or published post."""

    id: str
    user_id: str
    account_ids: list[str]
    text: str
    media_ids: list[str] = Field(default_factory=list)
    platform_options: dict[str, Any] = Field(default_factory=dict)
    status: str
    scheduled_at: str | None = None
    error_message: str | None = None
    retry_count: int = 0
    created_at: str
    updated_at: str
    results: list[PostResult] = Field(default_factory=lambda: [])


class ScheduledPostsListResponse(BaseModel):
    """Response for listing scheduled posts."""

    data: list[ScheduledPost]
    cursor: str | None = None


class PlatformPost(BaseModel):
    """A post retrieved from a connected platform."""

    id: str
    platform: str
    caption: str
    media_type: str | None = None
    media_url: str | None = None
    permalink: str
    timestamp: str
    like_count: int
    comments_count: int
    account_id: str


class PlatformPostsListResponse(BaseModel):
    """Response for listing platform posts."""

    data: list[PlatformPost]
    count: int
