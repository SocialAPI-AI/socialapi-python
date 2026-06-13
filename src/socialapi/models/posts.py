from __future__ import annotations

from datetime import datetime
from typing import Any

from pydantic import BaseModel, ConfigDict

from socialapi._bound import _Bound


class PostTargetError(BaseModel):
    """Structured error info for a failed platform target."""

    model_config = ConfigDict(populate_by_name=True)

    code: str | None = None
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
    page_id: str | None = None
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
    metadata: dict[str, Any] | None = None


# ---------------------------------------------------------------------------
# Delete response models
# ---------------------------------------------------------------------------


class TargetDeleteOutcome(BaseModel):
    """Per-platform result of a delete operation."""

    model_config = ConfigDict(populate_by_name=True)

    platform: str
    account_id: str | None = None
    outcome: str
    message: str | None = None


class DeletePostResponse(BaseModel):
    """Response from ``DELETE /v1/posts/:pid``."""

    model_config = ConfigDict(populate_by_name=True)

    success: bool
    deleted: bool
    results: list[TargetDeleteOutcome]


# ---------------------------------------------------------------------------
# Post
# ---------------------------------------------------------------------------


class _PostBase(_Bound):
    """Shared fields for Post / AsyncPost."""

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


class Post(_PostBase):
    """A post in the unified publishing system (sync)."""

    def update(
        self,
        *,
        text: str | None = None,
        title: str | None = None,
        media_ids: list[str] | None = None,
        visibility: str | None = None,
        first_comment: str | None = None,
        scheduled_at: datetime | str | None = None,
        hidden: bool | None = None,
        targets: list[dict[str, Any]] | None = None,
        timeout: float | None = None,
    ) -> Post:
        """Update the post.

        Args:
            text: New text content.
            title: New title.
            media_ids: New media IDs.
            visibility: New visibility.
            first_comment: New first comment.
            scheduled_at: New schedule time.
            hidden: Archive/unarchive the post.
            targets: New target configuration.
            timeout: Per-request timeout in seconds.

        Returns:
            Updated Post instance.

        Raises:
            UnboundModelError: If the model is not bound to a client.
        """
        client = self._client_or_raise_sync()
        body: dict[str, Any] = {}
        if text is not None:
            body["text"] = text
        if title is not None:
            body["title"] = title
        if media_ids is not None:
            body["media_ids"] = media_ids
        if visibility is not None:
            body["visibility"] = visibility
        if first_comment is not None:
            body["first_comment"] = first_comment
        if scheduled_at is not None:
            body["scheduled_at"] = scheduled_at.isoformat() if isinstance(scheduled_at, datetime) else scheduled_at
        if hidden is not None:
            body["hidden"] = hidden
        if targets is not None:
            body["targets"] = targets
        data = client._patch(f"/v1/posts/{self.id}", json=body, timeout=timeout)
        if isinstance(data, dict):
            updated = Post.model_validate(data)
            updated._bind(client)
            return updated
        return self

    def delete(self, *, timeout: float | None = None) -> DeletePostResponse:
        """Delete this post.

        Args:
            timeout: Per-request timeout in seconds.

        Returns:
            DeletePostResponse with per-platform results.

        Raises:
            UnboundModelError: If the model is not bound to a client.
        """
        client = self._client_or_raise_sync()
        data = client._delete(f"/v1/posts/{self.id}", timeout=timeout)
        return DeletePostResponse.model_validate(data)

    def retry(self, *, timeout: float | None = None) -> None:
        """Retry a failed post.

        Args:
            timeout: Per-request timeout in seconds.

        Raises:
            UnboundModelError: If the model is not bound to a client.
        """
        client = self._client_or_raise_sync()
        client._post(f"/v1/posts/{self.id}/retry", timeout=timeout)

    def unpublish(self, *, account_id: str | None = None, timeout: float | None = None) -> None:
        """Unpublish this post.

        Args:
            account_id: Optional account to unpublish from (otherwise all).
            timeout: Per-request timeout in seconds.

        Raises:
            UnboundModelError: If the model is not bound to a client.
        """
        client = self._client_or_raise_sync()
        body: dict[str, Any] = {}
        if account_id is not None:
            body["account_id"] = account_id
        client._post(f"/v1/posts/{self.id}/unpublish", json=body or None, timeout=timeout)

    def get_metrics(self, *, timeout: float | None = None) -> PostMetrics:
        """Fetch live metrics for this post.

        Args:
            timeout: Per-request timeout in seconds.

        Returns:
            PostMetrics with per-platform engagement data.

        Raises:
            UnboundModelError: If the model is not bound to a client.
        """
        client = self._client_or_raise_sync()
        data = client._get(f"/v1/posts/{self.id}/metrics", timeout=timeout)
        raw: dict[str, Any] = data.get("data", data)
        return PostMetrics.model_validate(raw)


class AsyncPost(_PostBase):
    """A post in the unified publishing system (async)."""

    async def update(
        self,
        *,
        text: str | None = None,
        title: str | None = None,
        media_ids: list[str] | None = None,
        visibility: str | None = None,
        first_comment: str | None = None,
        scheduled_at: datetime | str | None = None,
        hidden: bool | None = None,
        targets: list[dict[str, Any]] | None = None,
        timeout: float | None = None,
    ) -> AsyncPost:
        """Update the post.

        Args:
            text: New text content.
            title: New title.
            media_ids: New media IDs.
            visibility: New visibility.
            first_comment: New first comment.
            scheduled_at: New schedule time.
            hidden: Archive/unarchive the post.
            targets: New target configuration.
            timeout: Per-request timeout in seconds.

        Returns:
            Updated AsyncPost instance.

        Raises:
            UnboundModelError: If the model is not bound to a client.
        """
        client = self._client_or_raise_async()
        body: dict[str, Any] = {}
        if text is not None:
            body["text"] = text
        if title is not None:
            body["title"] = title
        if media_ids is not None:
            body["media_ids"] = media_ids
        if visibility is not None:
            body["visibility"] = visibility
        if first_comment is not None:
            body["first_comment"] = first_comment
        if scheduled_at is not None:
            body["scheduled_at"] = scheduled_at.isoformat() if isinstance(scheduled_at, datetime) else scheduled_at
        if hidden is not None:
            body["hidden"] = hidden
        if targets is not None:
            body["targets"] = targets
        data = await client._patch(f"/v1/posts/{self.id}", json=body, timeout=timeout)
        if isinstance(data, dict):
            updated = AsyncPost.model_validate(data)
            updated._bind(client)
            return updated
        return self

    async def delete(self, *, timeout: float | None = None) -> DeletePostResponse:
        """Delete this post.

        Args:
            timeout: Per-request timeout in seconds.

        Returns:
            DeletePostResponse with per-platform results.

        Raises:
            UnboundModelError: If the model is not bound to a client.
        """
        client = self._client_or_raise_async()
        data = await client._delete(f"/v1/posts/{self.id}", timeout=timeout)
        return DeletePostResponse.model_validate(data)

    async def retry(self, *, timeout: float | None = None) -> None:
        """Retry a failed post.

        Args:
            timeout: Per-request timeout in seconds.

        Raises:
            UnboundModelError: If the model is not bound to a client.
        """
        client = self._client_or_raise_async()
        await client._post(f"/v1/posts/{self.id}/retry", timeout=timeout)

    async def unpublish(self, *, account_id: str | None = None, timeout: float | None = None) -> None:
        """Unpublish this post.

        Args:
            account_id: Optional account to unpublish from (otherwise all).
            timeout: Per-request timeout in seconds.

        Raises:
            UnboundModelError: If the model is not bound to a client.
        """
        client = self._client_or_raise_async()
        body: dict[str, Any] = {}
        if account_id is not None:
            body["account_id"] = account_id
        await client._post(f"/v1/posts/{self.id}/unpublish", json=body or None, timeout=timeout)

    async def get_metrics(self, *, timeout: float | None = None) -> PostMetrics:
        """Fetch live metrics for this post.

        Args:
            timeout: Per-request timeout in seconds.

        Returns:
            PostMetrics with per-platform engagement data.

        Raises:
            UnboundModelError: If the model is not bound to a client.
        """
        client = self._client_or_raise_async()
        data = await client._get(f"/v1/posts/{self.id}/metrics", timeout=timeout)
        raw: dict[str, Any] = data.get("data", data)
        return PostMetrics.model_validate(raw)


# ---------------------------------------------------------------------------
# Pure data
# ---------------------------------------------------------------------------


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
