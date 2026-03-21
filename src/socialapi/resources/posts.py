"""Posts resource (publishing)."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from socialapi.models.posts import ScheduledPost, ScheduledPostsListResponse
from socialapi.models.shared import SuccessResponse

if TYPE_CHECKING:
    from socialapi._async_client import AsyncSocialAPI
    from socialapi._client import SocialAPI


class Posts:
    """Synchronous posts resource.

    Provides methods for creating, updating, deleting, and retrying posts.
    """

    def __init__(self, client: SocialAPI) -> None:
        self._client = client

    def list(
        self,
        from_: str,
        to: str,
        *,
        status: str | None = None,
        limit: int = 100,
        cursor: str | None = None,
    ) -> ScheduledPostsListResponse:
        """List scheduled and published posts.

        Args:
            from_: Start date filter (RFC 3339 timestamp).
            to: End date filter (RFC 3339 timestamp).
            status: Filter by post status (e.g. ``"scheduled"``, ``"published"``).
            limit: Maximum results per page (1--100). Defaults to 100.
            cursor: Opaque cursor from a previous response for pagination.

        Returns:
            A ScheduledPostsListResponse containing the posts.

        Raises:
            AuthenticationError: If the API key is invalid.
        """
        params: dict[str, Any] = {"from": from_, "to": to, "limit": limit}
        if status is not None:
            params["status"] = status
        if cursor is not None:
            params["cursor"] = cursor
        return self._client._get("/v1/posts", params=params, response_model=ScheduledPostsListResponse)

    def create(
        self,
        account_ids: list[str],
        text: str,
        *,
        media_ids: list[str] | None = None,
        platform_options: dict[str, Any] | None = None,
        scheduled_at: str | None = None,
    ) -> ScheduledPost:
        """Create a new post.

        Args:
            account_ids: List of account IDs to publish to.
            text: The post text content.
            media_ids: Optional list of media IDs to attach.
            platform_options: Optional platform-specific options.
            scheduled_at: Optional scheduled publish time (RFC 3339).

        Returns:
            The created ScheduledPost.

        Raises:
            ValidationError: If required fields are missing or invalid.
            RateLimitError: If the monthly post limit is exceeded.
        """
        body: dict[str, Any] = {"account_ids": account_ids, "text": text}
        if media_ids is not None:
            body["media_ids"] = media_ids
        if platform_options is not None:
            body["platform_options"] = platform_options
        if scheduled_at is not None:
            body["scheduled_at"] = scheduled_at
        return self._client._post("/v1/posts", json_data=body, response_model=ScheduledPost)

    def update(
        self,
        post_id: str,
        *,
        text: str,
        media_ids: list[str] | None = None,
        platform_options: dict[str, Any] | None = None,
        scheduled_at: str | None = None,
        account_ids: list[str] | None = None,
    ) -> SuccessResponse:
        """Update a scheduled post.

        Args:
            post_id: The ID of the post to update.
            text: The updated post text.
            media_ids: Optional updated list of media IDs.
            platform_options: Optional updated platform-specific options.
            scheduled_at: Optional updated scheduled time (RFC 3339).
            account_ids: Optional updated list of account IDs.

        Returns:
            A SuccessResponse indicating the update was applied.

        Raises:
            NotFoundError: If the post is not found.
            ValidationError: If the update payload is invalid.
        """
        body: dict[str, Any] = {"text": text}
        if media_ids is not None:
            body["media_ids"] = media_ids
        if platform_options is not None:
            body["platform_options"] = platform_options
        if scheduled_at is not None:
            body["scheduled_at"] = scheduled_at
        if account_ids is not None:
            body["account_ids"] = account_ids
        return self._client._patch(f"/v1/posts/{post_id}", json_data=body, response_model=SuccessResponse)

    def delete(self, post_id: str) -> SuccessResponse:
        """Delete a scheduled post.

        Args:
            post_id: The ID of the post to delete.

        Returns:
            A SuccessResponse indicating the post was deleted.

        Raises:
            NotFoundError: If the post is not found.
        """
        return self._client._delete(f"/v1/posts/{post_id}", response_model=SuccessResponse)

    def retry(self, post_id: str) -> SuccessResponse:
        """Retry a failed post.

        Args:
            post_id: The ID of the post to retry.

        Returns:
            A SuccessResponse indicating the retry was queued.

        Raises:
            NotFoundError: If the post is not found.
        """
        return self._client._post(f"/v1/posts/{post_id}/retry", response_model=SuccessResponse)


class AsyncPosts:
    """Asynchronous posts resource.

    Provides methods for creating, updating, deleting, and retrying posts.
    """

    def __init__(self, client: AsyncSocialAPI) -> None:
        self._client = client

    async def list(
        self,
        from_: str,
        to: str,
        *,
        status: str | None = None,
        limit: int = 100,
        cursor: str | None = None,
    ) -> ScheduledPostsListResponse:
        """List scheduled and published posts.

        Args:
            from_: Start date filter (RFC 3339 timestamp).
            to: End date filter (RFC 3339 timestamp).
            status: Filter by post status (e.g. ``"scheduled"``, ``"published"``).
            limit: Maximum results per page (1--100). Defaults to 100.
            cursor: Opaque cursor from a previous response for pagination.

        Returns:
            A ScheduledPostsListResponse containing the posts.

        Raises:
            AuthenticationError: If the API key is invalid.
        """
        params: dict[str, Any] = {"from": from_, "to": to, "limit": limit}
        if status is not None:
            params["status"] = status
        if cursor is not None:
            params["cursor"] = cursor
        return await self._client._get("/v1/posts", params=params, response_model=ScheduledPostsListResponse)

    async def create(
        self,
        account_ids: list[str],
        text: str,
        *,
        media_ids: list[str] | None = None,
        platform_options: dict[str, Any] | None = None,
        scheduled_at: str | None = None,
    ) -> ScheduledPost:
        """Create a new post.

        Args:
            account_ids: List of account IDs to publish to.
            text: The post text content.
            media_ids: Optional list of media IDs to attach.
            platform_options: Optional platform-specific options.
            scheduled_at: Optional scheduled publish time (RFC 3339).

        Returns:
            The created ScheduledPost.

        Raises:
            ValidationError: If required fields are missing or invalid.
            RateLimitError: If the monthly post limit is exceeded.
        """
        body: dict[str, Any] = {"account_ids": account_ids, "text": text}
        if media_ids is not None:
            body["media_ids"] = media_ids
        if platform_options is not None:
            body["platform_options"] = platform_options
        if scheduled_at is not None:
            body["scheduled_at"] = scheduled_at
        return await self._client._post("/v1/posts", json_data=body, response_model=ScheduledPost)

    async def update(
        self,
        post_id: str,
        *,
        text: str,
        media_ids: list[str] | None = None,
        platform_options: dict[str, Any] | None = None,
        scheduled_at: str | None = None,
        account_ids: list[str] | None = None,
    ) -> SuccessResponse:
        """Update a scheduled post.

        Args:
            post_id: The ID of the post to update.
            text: The updated post text.
            media_ids: Optional updated list of media IDs.
            platform_options: Optional updated platform-specific options.
            scheduled_at: Optional updated scheduled time (RFC 3339).
            account_ids: Optional updated list of account IDs.

        Returns:
            A SuccessResponse indicating the update was applied.

        Raises:
            NotFoundError: If the post is not found.
            ValidationError: If the update payload is invalid.
        """
        body: dict[str, Any] = {"text": text}
        if media_ids is not None:
            body["media_ids"] = media_ids
        if platform_options is not None:
            body["platform_options"] = platform_options
        if scheduled_at is not None:
            body["scheduled_at"] = scheduled_at
        if account_ids is not None:
            body["account_ids"] = account_ids
        return await self._client._patch(f"/v1/posts/{post_id}", json_data=body, response_model=SuccessResponse)

    async def delete(self, post_id: str) -> SuccessResponse:
        """Delete a scheduled post.

        Args:
            post_id: The ID of the post to delete.

        Returns:
            A SuccessResponse indicating the post was deleted.

        Raises:
            NotFoundError: If the post is not found.
        """
        return await self._client._delete(f"/v1/posts/{post_id}", response_model=SuccessResponse)

    async def retry(self, post_id: str) -> SuccessResponse:
        """Retry a failed post.

        Args:
            post_id: The ID of the post to retry.

        Returns:
            A SuccessResponse indicating the retry was queued.

        Raises:
            NotFoundError: If the post is not found.
        """
        return await self._client._post(f"/v1/posts/{post_id}/retry", response_model=SuccessResponse)
