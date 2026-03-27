from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, Any

from socialapi.models.posts import Post, ValidationResult
from socialapi.models.publishing import ImportPostsResponse, MediaUploadURL, PlatformConstraints

if TYPE_CHECKING:
    from socialapi._base_client import BaseAsyncClient, BaseSyncClient


class Publishing:
    """Create, update, and validate posts for publishing (sync)."""

    _client: BaseSyncClient

    def __init__(self, client: BaseSyncClient) -> None:
        self._client = client

    def create(
        self,
        *,
        text: str,
        title: str | None = None,
        media_ids: list[str] | None = None,
        visibility: str | None = None,
        first_comment: str | None = None,
        scheduled_at: datetime | str | None = None,
        publish_now: bool = False,
        skip_duplicate_check: bool = False,
        targets: list[dict[str, Any]] | None = None,
        timeout: float | None = None,
    ) -> Post:
        """Create a new post.

        Args:
            text: Post body content.
            title: Optional post title (used by LinkedIn, Google).
            media_ids: Previously uploaded media file IDs to attach.
            visibility: Who can see the post (``"public"``, ``"private"``, ``"connections_only"``).
            first_comment: Auto-posted as first comment after publishing.
            scheduled_at: Datetime or ISO 8601 string for scheduled publication.
            publish_now: Immediately publish if targets are provided.
            skip_duplicate_check: Bypass duplicate content detection.
            targets: Per-platform target configurations.
            timeout: Override the client-level timeout for this request.

        Returns:
            The created post.

        Raises:
            BadRequestError: If the post content is invalid.
            AuthenticationError: If the API key is invalid.
        """
        body: dict[str, Any] = {"text": text}
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
        if publish_now:
            body["publish_now"] = True
        if skip_duplicate_check:
            body["skip_duplicate_check"] = True
        if targets is not None:
            body["targets"] = targets
        data = self._client._post("/v1/posts", json=body, timeout=timeout)
        return Post.model_validate(data)

    def update(
        self,
        post_id: str,
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
        """Update a draft, scheduled, or failed post.

        Args:
            post_id: The post ID to update.
            text: New post body content.
            title: New post title.
            media_ids: New media file IDs.
            visibility: New visibility setting.
            first_comment: New first comment text.
            scheduled_at: New scheduled publication time (datetime or ISO 8601 string).
            hidden: Archive or unarchive the post.
            targets: Updated per-platform target configurations.
            timeout: Override the client-level timeout for this request.

        Returns:
            The updated post.

        Raises:
            NotFoundError: If the post does not exist.
            BadRequestError: If the update content is invalid.
            AuthenticationError: If the API key is invalid.
        """
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
        data = self._client._patch(f"/v1/posts/{post_id}", json=body, timeout=timeout)
        return Post.model_validate(data)

    def get_constraints(
        self,
        *,
        platform: str | None = None,
        timeout: float | None = None,
    ) -> dict[str, PlatformConstraints]:
        """Get platform-specific content constraints.

        Args:
            platform: Optional platform to filter constraints.
            timeout: Override the client-level timeout for this request.

        Returns:
            A dict mapping platform names to their content constraints.

        Raises:
            AuthenticationError: If the API key is invalid.
        """
        params: dict[str, Any] = {}
        if platform is not None:
            params["platform"] = platform
        data = self._client._get("/v1/posts/validate", params=params or None, timeout=timeout)
        raw: dict[str, Any] = data.get("data", data)
        return {k: PlatformConstraints.model_validate({**v, "platform": k}) for k, v in raw.items()}

    def validate(
        self,
        *,
        text: str,
        platforms: list[str] | None = None,
        account_ids: list[str] | None = None,
        media_ids: list[str] | None = None,
        scheduled_at: datetime | str | None = None,
        targets: list[dict[str, Any]] | None = None,
        timeout: float | None = None,
    ) -> ValidationResult:
        """Validate post content against platform constraints.

        Args:
            text: Post content to validate.
            platforms: Platform names to validate against.
            account_ids: Account IDs (resolved to platforms automatically).
            media_ids: Media file IDs to validate.
            scheduled_at: Schedule time to validate (datetime or ISO 8601 string).
            targets: Per-target overrides to validate.
            timeout: Override the client-level timeout for this request.

        Returns:
            Validation result with errors and warnings.

        Raises:
            BadRequestError: If validation parameters are invalid.
            AuthenticationError: If the API key is invalid.
        """
        body: dict[str, Any] = {"text": text}
        if platforms is not None:
            body["platforms"] = platforms
        if account_ids is not None:
            body["account_ids"] = account_ids
        if media_ids is not None:
            body["media_ids"] = media_ids
        if scheduled_at is not None:
            body["scheduled_at"] = scheduled_at.isoformat() if isinstance(scheduled_at, datetime) else scheduled_at
        if targets is not None:
            body["targets"] = targets
        data = self._client._post("/v1/posts/validate", json=body, timeout=timeout)
        return ValidationResult.model_validate(data)

    def get_upload_url(
        self,
        *,
        media_type: str,
        filename: str,
        timeout: float | None = None,
    ) -> MediaUploadURL:
        """Get a presigned URL for media upload.

        Args:
            media_type: MIME type of the file (e.g. ``"image/jpeg"``).
            filename: Original filename.
            timeout: Override the client-level timeout for this request.

        Returns:
            Upload URL and metadata.

        Raises:
            AuthenticationError: If the API key is invalid.
            StorageQuotaExceededError: If storage quota is exceeded.
        """
        params: dict[str, Any] = {
            "content_type": media_type,
            "filename": filename,
        }
        data = self._client._get("/v1/media/upload-url", params=params, timeout=timeout)
        return MediaUploadURL.model_validate(data)

    def verify_upload(
        self,
        media_id: str,
        *,
        timeout: float | None = None,
    ) -> None:
        """Verify a media upload completed successfully.

        Args:
            media_id: The media ID from the upload URL response.
            timeout: Override the client-level timeout for this request.

        Raises:
            NotFoundError: If the media does not exist.
            AuthenticationError: If the API key is invalid.
        """
        self._client._post(f"/v1/media/{media_id}/verify", timeout=timeout)

    def import_posts(
        self,
        *,
        file: Any,
        dry_run: bool = False,
        timeout: float | None = None,
    ) -> ImportPostsResponse:
        """Import posts from a CSV file.

        Args:
            file: CSV file content.
            dry_run: Validate only, do not create posts.
            timeout: Override the client-level timeout for this request.

        Returns:
            Import results with created posts and any errors.

        Raises:
            BadRequestError: If the CSV is invalid.
            AuthenticationError: If the API key is invalid.
        """
        params: dict[str, Any] = {}
        if dry_run:
            params["dry_run"] = "true"
        data = self._client._post("/v1/posts/import", json={"file": "csv"}, params=params or None, timeout=timeout)
        return ImportPostsResponse.model_validate(data)


class AsyncPublishing:
    """Create, update, and validate posts for publishing (async)."""

    _client: BaseAsyncClient

    def __init__(self, client: BaseAsyncClient) -> None:
        self._client = client

    async def create(
        self,
        *,
        text: str,
        title: str | None = None,
        media_ids: list[str] | None = None,
        visibility: str | None = None,
        first_comment: str | None = None,
        scheduled_at: datetime | str | None = None,
        publish_now: bool = False,
        skip_duplicate_check: bool = False,
        targets: list[dict[str, Any]] | None = None,
        timeout: float | None = None,
    ) -> Post:
        """Create a new post.

        Args:
            text: Post body content.
            title: Optional post title (used by LinkedIn, Google).
            media_ids: Previously uploaded media file IDs to attach.
            visibility: Who can see the post (``"public"``, ``"private"``, ``"connections_only"``).
            first_comment: Auto-posted as first comment after publishing.
            scheduled_at: Datetime or ISO 8601 string for scheduled publication.
            publish_now: Immediately publish if targets are provided.
            skip_duplicate_check: Bypass duplicate content detection.
            targets: Per-platform target configurations.
            timeout: Override the client-level timeout for this request.

        Returns:
            The created post.

        Raises:
            BadRequestError: If the post content is invalid.
            AuthenticationError: If the API key is invalid.
        """
        body: dict[str, Any] = {"text": text}
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
        if publish_now:
            body["publish_now"] = True
        if skip_duplicate_check:
            body["skip_duplicate_check"] = True
        if targets is not None:
            body["targets"] = targets
        data = await self._client._post("/v1/posts", json=body, timeout=timeout)
        return Post.model_validate(data)

    async def update(
        self,
        post_id: str,
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
        """Update a draft, scheduled, or failed post.

        Args:
            post_id: The post ID to update.
            text: New post body content.
            title: New post title.
            media_ids: New media file IDs.
            visibility: New visibility setting.
            first_comment: New first comment text.
            scheduled_at: New scheduled publication time (datetime or ISO 8601 string).
            hidden: Archive or unarchive the post.
            targets: Updated per-platform target configurations.
            timeout: Override the client-level timeout for this request.

        Returns:
            The updated post.

        Raises:
            NotFoundError: If the post does not exist.
            BadRequestError: If the update content is invalid.
            AuthenticationError: If the API key is invalid.
        """
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
        data = await self._client._patch(f"/v1/posts/{post_id}", json=body, timeout=timeout)
        return Post.model_validate(data)

    async def get_constraints(
        self,
        *,
        platform: str | None = None,
        timeout: float | None = None,
    ) -> dict[str, PlatformConstraints]:
        """Get platform-specific content constraints.

        Args:
            platform: Optional platform to filter constraints.
            timeout: Override the client-level timeout for this request.

        Returns:
            A dict mapping platform names to their content constraints.

        Raises:
            AuthenticationError: If the API key is invalid.
        """
        params: dict[str, Any] = {}
        if platform is not None:
            params["platform"] = platform
        data = await self._client._get("/v1/posts/validate", params=params or None, timeout=timeout)
        raw: dict[str, Any] = data.get("data", data)
        return {k: PlatformConstraints.model_validate({**v, "platform": k}) for k, v in raw.items()}

    async def validate(
        self,
        *,
        text: str,
        platforms: list[str] | None = None,
        account_ids: list[str] | None = None,
        media_ids: list[str] | None = None,
        scheduled_at: datetime | str | None = None,
        targets: list[dict[str, Any]] | None = None,
        timeout: float | None = None,
    ) -> ValidationResult:
        """Validate post content against platform constraints.

        Args:
            text: Post content to validate.
            platforms: Platform names to validate against.
            account_ids: Account IDs (resolved to platforms automatically).
            media_ids: Media file IDs to validate.
            scheduled_at: Schedule time to validate (datetime or ISO 8601 string).
            targets: Per-target overrides to validate.
            timeout: Override the client-level timeout for this request.

        Returns:
            Validation result with errors and warnings.

        Raises:
            BadRequestError: If validation parameters are invalid.
            AuthenticationError: If the API key is invalid.
        """
        body: dict[str, Any] = {"text": text}
        if platforms is not None:
            body["platforms"] = platforms
        if account_ids is not None:
            body["account_ids"] = account_ids
        if media_ids is not None:
            body["media_ids"] = media_ids
        if scheduled_at is not None:
            body["scheduled_at"] = scheduled_at.isoformat() if isinstance(scheduled_at, datetime) else scheduled_at
        if targets is not None:
            body["targets"] = targets
        data = await self._client._post("/v1/posts/validate", json=body, timeout=timeout)
        return ValidationResult.model_validate(data)

    async def get_upload_url(
        self,
        *,
        media_type: str,
        filename: str,
        timeout: float | None = None,
    ) -> MediaUploadURL:
        """Get a presigned URL for media upload.

        Args:
            media_type: MIME type of the file (e.g. ``"image/jpeg"``).
            filename: Original filename.
            timeout: Override the client-level timeout for this request.

        Returns:
            Upload URL and metadata.

        Raises:
            AuthenticationError: If the API key is invalid.
            StorageQuotaExceededError: If storage quota is exceeded.
        """
        params: dict[str, Any] = {
            "content_type": media_type,
            "filename": filename,
        }
        data = await self._client._get("/v1/media/upload-url", params=params, timeout=timeout)
        return MediaUploadURL.model_validate(data)

    async def verify_upload(
        self,
        media_id: str,
        *,
        timeout: float | None = None,
    ) -> None:
        """Verify a media upload completed successfully.

        Args:
            media_id: The media ID from the upload URL response.
            timeout: Override the client-level timeout for this request.

        Raises:
            NotFoundError: If the media does not exist.
            AuthenticationError: If the API key is invalid.
        """
        await self._client._post(f"/v1/media/{media_id}/verify", timeout=timeout)

    async def import_posts(
        self,
        *,
        file: Any,
        dry_run: bool = False,
        timeout: float | None = None,
    ) -> ImportPostsResponse:
        """Import posts from a CSV file.

        Args:
            file: CSV file content.
            dry_run: Validate only, do not create posts.
            timeout: Override the client-level timeout for this request.

        Returns:
            Import results with created posts and any errors.

        Raises:
            BadRequestError: If the CSV is invalid.
            AuthenticationError: If the API key is invalid.
        """
        params: dict[str, Any] = {}
        if dry_run:
            params["dry_run"] = "true"
        data = await self._client._post(
            "/v1/posts/import", json={"file": "csv"}, params=params or None, timeout=timeout
        )
        return ImportPostsResponse.model_validate(data)
