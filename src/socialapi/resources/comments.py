from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, Any

from socialapi.models.comments import (
    CommentedPost,
    InboxComment,
    ReplyToCommentResponse,
)

if TYPE_CHECKING:
    from socialapi._base_client import BaseAsyncClient, BaseSyncClient
    from socialapi._pagination import AsyncCursorPage, CursorPage


class Comments:
    """Manage inbox comments across platforms (sync)."""

    _client: BaseSyncClient

    def __init__(self, client: BaseSyncClient) -> None:
        self._client = client

    def list_posts(
        self,
        *,
        account_id: str | None = None,
        platform: str | None = None,
        since: datetime | str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        timeout: float | None = None,
    ) -> CursorPage[CommentedPost]:
        """List posts that have received comments.

        Args:
            account_id: Filter by connected account.
            platform: Filter by platform.
            since: Only posts commented after this datetime or ISO 8601 string.
            limit: Maximum number of results per page.
            cursor: Pagination cursor from a previous response.
            timeout: Override the client-level timeout for this request.

        Returns:
            A paginated list of commented posts.

        Raises:
            AuthenticationError: If the API key is invalid.
            BadRequestError: If query parameters are invalid.
        """
        params: dict[str, Any] = {}
        if account_id is not None:
            params["account_id"] = account_id
        if platform is not None:
            params["platform"] = platform
        if since is not None:
            params["since"] = since.isoformat() if isinstance(since, datetime) else since
        if limit is not None:
            params["limit"] = limit
        if cursor is not None:
            params["cursor"] = cursor
        return self._client._get_paginated(
            "/v1/inbox/comments",
            params=params,
            model=CommentedPost,
            timeout=timeout,
        )

    def list(
        self,
        inbox_post_id: str,
        *,
        account_id: str,
        limit: int | None = None,
        cursor: str | None = None,
        timeout: float | None = None,
    ) -> CursorPage[InboxComment]:
        """List comments on a specific post.

        Args:
            inbox_post_id: The inbox post ID.
            account_id: The connected account ID that owns this post.
            limit: Maximum number of results per page.
            cursor: Pagination cursor from a previous response.
            timeout: Override the client-level timeout for this request.

        Returns:
            A paginated list of comments.

        Raises:
            NotFoundError: If the post does not exist.
            AuthenticationError: If the API key is invalid.
        """
        params: dict[str, Any] = {"account_id": account_id}
        if limit is not None:
            params["limit"] = limit
        if cursor is not None:
            params["cursor"] = cursor
        return self._client._get_paginated(
            f"/v1/inbox/comments/{inbox_post_id}",
            params=params,
            model=InboxComment,
            timeout=timeout,
        )

    def reply(
        self,
        post_id: str,
        *,
        account_id: str,
        text: str,
        comment_id: str | None = None,
        timeout: float | None = None,
    ) -> ReplyToCommentResponse:
        """Reply to a comment or post.

        Args:
            post_id: The inbox post ID.
            account_id: The connected account ID.
            text: Reply text content.
            comment_id: Optional parent comment ID for threaded replies.
            timeout: Override the client-level timeout for this request.

        Returns:
            The reply result with the new comment ID.

        Raises:
            NotFoundError: If the post does not exist.
            AuthenticationError: If the API key is invalid.
        """
        body: dict[str, Any] = {"account_id": account_id, "text": text}
        if comment_id is not None:
            body["comment_id"] = comment_id
        data = self._client._post(f"/v1/inbox/comments/{post_id}", json=body, timeout=timeout)
        return ReplyToCommentResponse.model_validate(data)

    def delete(
        self,
        post_id: str,
        comment_id: str,
        *,
        account_id: str,
        timeout: float | None = None,
    ) -> None:
        """Delete a comment.

        Args:
            post_id: The inbox post ID.
            comment_id: The comment ID to delete.
            account_id: The connected account ID.
            timeout: Override the client-level timeout for this request.

        Raises:
            NotFoundError: If the comment does not exist.
            AuthenticationError: If the API key is invalid.
        """
        self._client._delete(
            f"/v1/inbox/comments/{post_id}/{comment_id}",
            params={"account_id": account_id},
            timeout=timeout,
        )

    def hide(
        self,
        post_id: str,
        comment_id: str,
        *,
        account_id: str,
        timeout: float | None = None,
    ) -> None:
        """Hide a comment from public view.

        Args:
            post_id: The inbox post ID.
            comment_id: The comment ID to hide.
            account_id: The connected account ID.
            timeout: Override the client-level timeout for this request.

        Raises:
            NotFoundError: If the comment does not exist.
            NotSupportedError: If the platform does not support hiding.
        """
        self._client._post(
            f"/v1/inbox/comments/{post_id}/{comment_id}/hide",
            json={"account_id": account_id},
            timeout=timeout,
        )

    def unhide(
        self,
        post_id: str,
        comment_id: str,
        *,
        account_id: str,
        timeout: float | None = None,
    ) -> None:
        """Unhide a previously hidden comment.

        Args:
            post_id: The inbox post ID.
            comment_id: The comment ID to unhide.
            account_id: The connected account ID.
            timeout: Override the client-level timeout for this request.

        Raises:
            NotFoundError: If the comment does not exist.
            NotSupportedError: If the platform does not support hiding.
        """
        self._client._delete(
            f"/v1/inbox/comments/{post_id}/{comment_id}/hide",
            params={"account_id": account_id},
            timeout=timeout,
        )

    def like(
        self,
        post_id: str,
        comment_id: str,
        *,
        account_id: str,
        timeout: float | None = None,
    ) -> None:
        """Like a comment.

        Args:
            post_id: The inbox post ID.
            comment_id: The comment ID to like.
            account_id: The connected account ID.
            timeout: Override the client-level timeout for this request.

        Raises:
            NotFoundError: If the comment does not exist.
            NotSupportedError: If the platform does not support liking.
        """
        self._client._post(
            f"/v1/inbox/comments/{post_id}/{comment_id}/like",
            json={"account_id": account_id},
            timeout=timeout,
        )

    def unlike(
        self,
        post_id: str,
        comment_id: str,
        *,
        account_id: str,
        timeout: float | None = None,
    ) -> None:
        """Remove a like from a comment.

        Args:
            post_id: The inbox post ID.
            comment_id: The comment ID to unlike.
            account_id: The connected account ID.
            timeout: Override the client-level timeout for this request.

        Raises:
            NotFoundError: If the comment does not exist.
            NotSupportedError: If the platform does not support liking.
        """
        self._client._delete(
            f"/v1/inbox/comments/{post_id}/{comment_id}/like",
            params={"account_id": account_id},
            timeout=timeout,
        )

    def private_reply(
        self,
        post_id: str,
        comment_id: str,
        *,
        account_id: str,
        text: str,
        timeout: float | None = None,
    ) -> None:
        """Send a private reply to a comment author.

        Args:
            post_id: The inbox post ID.
            comment_id: The comment ID to privately reply to.
            account_id: The connected account ID.
            text: Private message text.
            timeout: Override the client-level timeout for this request.

        Raises:
            NotFoundError: If the comment does not exist.
            NotSupportedError: If the platform does not support private replies.
        """
        self._client._post(
            f"/v1/inbox/comments/{post_id}/{comment_id}/private-reply",
            json={"account_id": account_id, "text": text},
            timeout=timeout,
        )


class AsyncComments:
    """Manage inbox comments across platforms (async)."""

    _client: BaseAsyncClient

    def __init__(self, client: BaseAsyncClient) -> None:
        self._client = client

    async def list_posts(
        self,
        *,
        account_id: str | None = None,
        platform: str | None = None,
        since: datetime | str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        timeout: float | None = None,
    ) -> AsyncCursorPage[CommentedPost]:
        """List posts that have received comments.

        Args:
            account_id: Filter by connected account.
            platform: Filter by platform.
            since: Only posts commented after this datetime or ISO 8601 string.
            limit: Maximum number of results per page.
            cursor: Pagination cursor from a previous response.
            timeout: Override the client-level timeout for this request.

        Returns:
            A paginated list of commented posts.

        Raises:
            AuthenticationError: If the API key is invalid.
            BadRequestError: If query parameters are invalid.
        """
        params: dict[str, Any] = {}
        if account_id is not None:
            params["account_id"] = account_id
        if platform is not None:
            params["platform"] = platform
        if since is not None:
            params["since"] = since.isoformat() if isinstance(since, datetime) else since
        if limit is not None:
            params["limit"] = limit
        if cursor is not None:
            params["cursor"] = cursor
        return await self._client._get_paginated(
            "/v1/inbox/comments",
            params=params,
            model=CommentedPost,
            timeout=timeout,
        )

    async def list(
        self,
        inbox_post_id: str,
        *,
        account_id: str,
        limit: int | None = None,
        cursor: str | None = None,
        timeout: float | None = None,
    ) -> AsyncCursorPage[InboxComment]:
        """List comments on a specific post.

        Args:
            inbox_post_id: The inbox post ID.
            account_id: The connected account ID that owns this post.
            limit: Maximum number of results per page.
            cursor: Pagination cursor from a previous response.
            timeout: Override the client-level timeout for this request.

        Returns:
            A paginated list of comments.

        Raises:
            NotFoundError: If the post does not exist.
            AuthenticationError: If the API key is invalid.
        """
        params: dict[str, Any] = {"account_id": account_id}
        if limit is not None:
            params["limit"] = limit
        if cursor is not None:
            params["cursor"] = cursor
        return await self._client._get_paginated(
            f"/v1/inbox/comments/{inbox_post_id}",
            params=params,
            model=InboxComment,
            timeout=timeout,
        )

    async def reply(
        self,
        post_id: str,
        *,
        account_id: str,
        text: str,
        comment_id: str | None = None,
        timeout: float | None = None,
    ) -> ReplyToCommentResponse:
        """Reply to a comment or post.

        Args:
            post_id: The inbox post ID.
            account_id: The connected account ID.
            text: Reply text content.
            comment_id: Optional parent comment ID for threaded replies.
            timeout: Override the client-level timeout for this request.

        Returns:
            The reply result with the new comment ID.

        Raises:
            NotFoundError: If the post does not exist.
            AuthenticationError: If the API key is invalid.
        """
        body: dict[str, Any] = {"account_id": account_id, "text": text}
        if comment_id is not None:
            body["comment_id"] = comment_id
        data = await self._client._post(f"/v1/inbox/comments/{post_id}", json=body, timeout=timeout)
        return ReplyToCommentResponse.model_validate(data)

    async def delete(
        self,
        post_id: str,
        comment_id: str,
        *,
        account_id: str,
        timeout: float | None = None,
    ) -> None:
        """Delete a comment.

        Args:
            post_id: The inbox post ID.
            comment_id: The comment ID to delete.
            account_id: The connected account ID.
            timeout: Override the client-level timeout for this request.

        Raises:
            NotFoundError: If the comment does not exist.
            AuthenticationError: If the API key is invalid.
        """
        await self._client._delete(
            f"/v1/inbox/comments/{post_id}/{comment_id}",
            params={"account_id": account_id},
            timeout=timeout,
        )

    async def hide(
        self,
        post_id: str,
        comment_id: str,
        *,
        account_id: str,
        timeout: float | None = None,
    ) -> None:
        """Hide a comment from public view.

        Args:
            post_id: The inbox post ID.
            comment_id: The comment ID to hide.
            account_id: The connected account ID.
            timeout: Override the client-level timeout for this request.

        Raises:
            NotFoundError: If the comment does not exist.
            NotSupportedError: If the platform does not support hiding.
        """
        await self._client._post(
            f"/v1/inbox/comments/{post_id}/{comment_id}/hide",
            json={"account_id": account_id},
            timeout=timeout,
        )

    async def unhide(
        self,
        post_id: str,
        comment_id: str,
        *,
        account_id: str,
        timeout: float | None = None,
    ) -> None:
        """Unhide a previously hidden comment.

        Args:
            post_id: The inbox post ID.
            comment_id: The comment ID to unhide.
            account_id: The connected account ID.
            timeout: Override the client-level timeout for this request.

        Raises:
            NotFoundError: If the comment does not exist.
            NotSupportedError: If the platform does not support hiding.
        """
        await self._client._delete(
            f"/v1/inbox/comments/{post_id}/{comment_id}/hide",
            params={"account_id": account_id},
            timeout=timeout,
        )

    async def like(
        self,
        post_id: str,
        comment_id: str,
        *,
        account_id: str,
        timeout: float | None = None,
    ) -> None:
        """Like a comment.

        Args:
            post_id: The inbox post ID.
            comment_id: The comment ID to like.
            account_id: The connected account ID.
            timeout: Override the client-level timeout for this request.

        Raises:
            NotFoundError: If the comment does not exist.
            NotSupportedError: If the platform does not support liking.
        """
        await self._client._post(
            f"/v1/inbox/comments/{post_id}/{comment_id}/like",
            json={"account_id": account_id},
            timeout=timeout,
        )

    async def unlike(
        self,
        post_id: str,
        comment_id: str,
        *,
        account_id: str,
        timeout: float | None = None,
    ) -> None:
        """Remove a like from a comment.

        Args:
            post_id: The inbox post ID.
            comment_id: The comment ID to unlike.
            account_id: The connected account ID.
            timeout: Override the client-level timeout for this request.

        Raises:
            NotFoundError: If the comment does not exist.
            NotSupportedError: If the platform does not support liking.
        """
        await self._client._delete(
            f"/v1/inbox/comments/{post_id}/{comment_id}/like",
            params={"account_id": account_id},
            timeout=timeout,
        )

    async def private_reply(
        self,
        post_id: str,
        comment_id: str,
        *,
        account_id: str,
        text: str,
        timeout: float | None = None,
    ) -> None:
        """Send a private reply to a comment author.

        Args:
            post_id: The inbox post ID.
            comment_id: The comment ID to privately reply to.
            account_id: The connected account ID.
            text: Private message text.
            timeout: Override the client-level timeout for this request.

        Raises:
            NotFoundError: If the comment does not exist.
            NotSupportedError: If the platform does not support private replies.
        """
        await self._client._post(
            f"/v1/inbox/comments/{post_id}/{comment_id}/private-reply",
            json={"account_id": account_id, "text": text},
            timeout=timeout,
        )
