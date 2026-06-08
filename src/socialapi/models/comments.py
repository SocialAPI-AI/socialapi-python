from __future__ import annotations

from datetime import datetime  # noqa: TC003
from typing import TYPE_CHECKING, Any

from pydantic import BaseModel, ConfigDict

from socialapi._bound import _Bound

if TYPE_CHECKING:
    from socialapi._pagination import AsyncCursorPage, CursorPage


class CommentCapabilities(BaseModel):
    """Describes supported actions for a comment on this platform."""

    model_config = ConfigDict(populate_by_name=True)

    can_reply: bool = False
    can_delete: bool = False
    can_hide: bool = False
    can_like: bool = False
    can_private_reply: bool = False


# ---------------------------------------------------------------------------
# Inbox comment
# ---------------------------------------------------------------------------


class _InboxCommentBase(_Bound):
    """Shared fields for InboxComment / AsyncInboxComment.

    Matches ProxyCommentRow (CommentWithCapabilities wire shape).
    No ``id`` field: the platform comment identifier is ``platform_id``.
    ``inbox_post_id`` may be absent from the wire (ProxyCommentRow does not
    include it); it is seeded into ``_ctx`` by the resource layer and read
    via ``_resolve_inbox_post_id()`` in action methods.
    """

    inbox_post_id: str | None = None
    platform_id: str
    platform: str
    text: str
    author_id: str
    author_name: str | None = None
    author_username: str | None = None
    author_picture: str | None = None
    is_owner: bool = False
    like_count: int = 0
    reply_count: int = 0
    has_replies: bool = False
    is_hidden: bool = False
    moderation_status: str | None = None
    parent_id: str | None = None
    created_at: datetime
    capabilities: CommentCapabilities


class InboxComment(_InboxCommentBase):
    """A comment in the unified inbox (sync)."""

    def _resolve_inbox_post_id(self) -> str:
        """Return inbox_post_id from field or context."""
        if self.inbox_post_id:
            return self.inbox_post_id
        return self._ctx_value("inbox_post_id")

    def reply(
        self,
        *,
        text: str,
        timeout: float | None = None,
    ) -> ReplyToCommentResponse:
        """Reply to this comment.

        Args:
            text: The reply text.
            timeout: Optional request timeout in seconds.

        Returns:
            A ReplyToCommentResponse with the new comment ID.

        Raises:
            UnboundModelError: If this model was not built by a client.
            MissingContextError: If account_id is missing from context.
        """
        client = self._client_or_raise_sync()
        account_id = self._ctx_value("account_id")
        body: dict[str, Any] = {"account_id": account_id, "text": text, "comment_id": self.platform_id}
        inbox_post_id = self._resolve_inbox_post_id()
        data = client._post(f"/v1/inbox/comments/{inbox_post_id}", json=body, timeout=timeout)
        return ReplyToCommentResponse.model_validate(data)

    def delete(self, *, timeout: float | None = None) -> None:
        """Delete this comment.

        Args:
            timeout: Optional request timeout in seconds.

        Raises:
            UnboundModelError: If this model was not built by a client.
            MissingContextError: If account_id is missing from context.
        """
        client = self._client_or_raise_sync()
        account_id = self._ctx_value("account_id")
        inbox_post_id = self._resolve_inbox_post_id()
        client._delete(
            f"/v1/inbox/comments/{inbox_post_id}/{self.platform_id}",
            params={"account_id": account_id},
            timeout=timeout,
        )

    def hide(self, *, timeout: float | None = None) -> None:
        """Hide this comment.

        Args:
            timeout: Optional request timeout in seconds.

        Raises:
            UnboundModelError: If this model was not built by a client.
            MissingContextError: If account_id is missing from context.
        """
        client = self._client_or_raise_sync()
        account_id = self._ctx_value("account_id")
        inbox_post_id = self._resolve_inbox_post_id()
        client._post(
            f"/v1/inbox/comments/{inbox_post_id}/{self.platform_id}/hide",
            json={"account_id": account_id},
            timeout=timeout,
        )

    def unhide(self, *, timeout: float | None = None) -> None:
        """Unhide this comment.

        Args:
            timeout: Optional request timeout in seconds.

        Raises:
            UnboundModelError: If this model was not built by a client.
            MissingContextError: If account_id is missing from context.
        """
        client = self._client_or_raise_sync()
        account_id = self._ctx_value("account_id")
        inbox_post_id = self._resolve_inbox_post_id()
        client._delete(
            f"/v1/inbox/comments/{inbox_post_id}/{self.platform_id}/hide",
            params={"account_id": account_id},
            timeout=timeout,
        )

    def like(self, *, timeout: float | None = None) -> None:
        """Like this comment.

        Args:
            timeout: Optional request timeout in seconds.

        Raises:
            UnboundModelError: If this model was not built by a client.
            MissingContextError: If account_id is missing from context.
        """
        client = self._client_or_raise_sync()
        account_id = self._ctx_value("account_id")
        inbox_post_id = self._resolve_inbox_post_id()
        client._post(
            f"/v1/inbox/comments/{inbox_post_id}/{self.platform_id}/like",
            json={"account_id": account_id},
            timeout=timeout,
        )

    def unlike(self, *, timeout: float | None = None) -> None:
        """Unlike this comment.

        Args:
            timeout: Optional request timeout in seconds.

        Raises:
            UnboundModelError: If this model was not built by a client.
            MissingContextError: If account_id is missing from context.
        """
        client = self._client_or_raise_sync()
        account_id = self._ctx_value("account_id")
        inbox_post_id = self._resolve_inbox_post_id()
        client._delete(
            f"/v1/inbox/comments/{inbox_post_id}/{self.platform_id}/like",
            params={"account_id": account_id},
            timeout=timeout,
        )

    def private_reply(self, *, text: str, timeout: float | None = None) -> None:
        """Send a private reply to this comment.

        Args:
            text: The private reply text.
            timeout: Optional request timeout in seconds.

        Raises:
            UnboundModelError: If this model was not built by a client.
            MissingContextError: If account_id is missing from context.
        """
        client = self._client_or_raise_sync()
        account_id = self._ctx_value("account_id")
        inbox_post_id = self._resolve_inbox_post_id()
        client._post(
            f"/v1/inbox/comments/{inbox_post_id}/{self.platform_id}/private-reply",
            json={"account_id": account_id, "text": text},
            timeout=timeout,
        )

    def list_replies(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        timeout: float | None = None,
    ) -> CursorPage[InboxComment]:
        """List replies to this comment.

        Args:
            limit: Maximum number of replies to return.
            cursor: Pagination cursor.
            timeout: Optional request timeout in seconds.

        Returns:
            A CursorPage of InboxComment replies.

        Raises:
            UnboundModelError: If this model was not built by a client.
            MissingContextError: If account_id is missing from context.
        """
        client = self._client_or_raise_sync()
        account_id = self._ctx_value("account_id")
        inbox_post_id = self._resolve_inbox_post_id()
        params: dict[str, Any] = {"account_id": account_id}
        if limit is not None:
            params["limit"] = limit
        if cursor is not None:
            params["cursor"] = cursor
        return client._get_paginated(
            f"/v1/inbox/comments/{inbox_post_id}/{self.platform_id}/replies",
            params=params,
            model=InboxComment,
            timeout=timeout,
            bind_ctx={"account_id": account_id, "inbox_post_id": inbox_post_id},
        )


class AsyncInboxComment(_InboxCommentBase):
    """A comment in the unified inbox (async)."""

    def _resolve_inbox_post_id(self) -> str:
        """Return inbox_post_id from field or context."""
        if self.inbox_post_id:
            return self.inbox_post_id
        return self._ctx_value("inbox_post_id")

    async def reply(
        self,
        *,
        text: str,
        timeout: float | None = None,
    ) -> ReplyToCommentResponse:
        """Reply to this comment.

        Args:
            text: The reply text.
            timeout: Optional request timeout in seconds.

        Returns:
            A ReplyToCommentResponse with the new comment ID.

        Raises:
            UnboundModelError: If this model was not built by a client.
            MissingContextError: If account_id is missing from context.
        """
        client = self._client_or_raise_async()
        account_id = self._ctx_value("account_id")
        inbox_post_id = self._resolve_inbox_post_id()
        body: dict[str, Any] = {"account_id": account_id, "text": text, "comment_id": self.platform_id}
        data = await client._post(f"/v1/inbox/comments/{inbox_post_id}", json=body, timeout=timeout)
        return ReplyToCommentResponse.model_validate(data)

    async def delete(self, *, timeout: float | None = None) -> None:
        """Delete this comment.

        Args:
            timeout: Optional request timeout in seconds.

        Raises:
            UnboundModelError: If this model was not built by a client.
            MissingContextError: If account_id is missing from context.
        """
        client = self._client_or_raise_async()
        account_id = self._ctx_value("account_id")
        inbox_post_id = self._resolve_inbox_post_id()
        await client._delete(
            f"/v1/inbox/comments/{inbox_post_id}/{self.platform_id}",
            params={"account_id": account_id},
            timeout=timeout,
        )

    async def hide(self, *, timeout: float | None = None) -> None:
        """Hide this comment.

        Args:
            timeout: Optional request timeout in seconds.

        Raises:
            UnboundModelError: If this model was not built by a client.
            MissingContextError: If account_id is missing from context.
        """
        client = self._client_or_raise_async()
        account_id = self._ctx_value("account_id")
        inbox_post_id = self._resolve_inbox_post_id()
        await client._post(
            f"/v1/inbox/comments/{inbox_post_id}/{self.platform_id}/hide",
            json={"account_id": account_id},
            timeout=timeout,
        )

    async def unhide(self, *, timeout: float | None = None) -> None:
        """Unhide this comment.

        Args:
            timeout: Optional request timeout in seconds.

        Raises:
            UnboundModelError: If this model was not built by a client.
            MissingContextError: If account_id is missing from context.
        """
        client = self._client_or_raise_async()
        account_id = self._ctx_value("account_id")
        inbox_post_id = self._resolve_inbox_post_id()
        await client._delete(
            f"/v1/inbox/comments/{inbox_post_id}/{self.platform_id}/hide",
            params={"account_id": account_id},
            timeout=timeout,
        )

    async def like(self, *, timeout: float | None = None) -> None:
        """Like this comment.

        Args:
            timeout: Optional request timeout in seconds.

        Raises:
            UnboundModelError: If this model was not built by a client.
            MissingContextError: If account_id is missing from context.
        """
        client = self._client_or_raise_async()
        account_id = self._ctx_value("account_id")
        inbox_post_id = self._resolve_inbox_post_id()
        await client._post(
            f"/v1/inbox/comments/{inbox_post_id}/{self.platform_id}/like",
            json={"account_id": account_id},
            timeout=timeout,
        )

    async def unlike(self, *, timeout: float | None = None) -> None:
        """Unlike this comment.

        Args:
            timeout: Optional request timeout in seconds.

        Raises:
            UnboundModelError: If this model was not built by a client.
            MissingContextError: If account_id is missing from context.
        """
        client = self._client_or_raise_async()
        account_id = self._ctx_value("account_id")
        inbox_post_id = self._resolve_inbox_post_id()
        await client._delete(
            f"/v1/inbox/comments/{inbox_post_id}/{self.platform_id}/like",
            params={"account_id": account_id},
            timeout=timeout,
        )

    async def private_reply(self, *, text: str, timeout: float | None = None) -> None:
        """Send a private reply to this comment.

        Args:
            text: The private reply text.
            timeout: Optional request timeout in seconds.

        Raises:
            UnboundModelError: If this model was not built by a client.
            MissingContextError: If account_id is missing from context.
        """
        client = self._client_or_raise_async()
        account_id = self._ctx_value("account_id")
        inbox_post_id = self._resolve_inbox_post_id()
        await client._post(
            f"/v1/inbox/comments/{inbox_post_id}/{self.platform_id}/private-reply",
            json={"account_id": account_id, "text": text},
            timeout=timeout,
        )

    async def list_replies(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        timeout: float | None = None,
    ) -> AsyncCursorPage[AsyncInboxComment]:
        """List replies to this comment.

        Args:
            limit: Maximum number of replies to return.
            cursor: Pagination cursor.
            timeout: Optional request timeout in seconds.

        Returns:
            An AsyncCursorPage of AsyncInboxComment replies.

        Raises:
            UnboundModelError: If this model was not built by a client.
            MissingContextError: If account_id is missing from context.
        """
        client = self._client_or_raise_async()
        account_id = self._ctx_value("account_id")
        inbox_post_id = self._resolve_inbox_post_id()
        params: dict[str, Any] = {"account_id": account_id}
        if limit is not None:
            params["limit"] = limit
        if cursor is not None:
            params["cursor"] = cursor
        return await client._get_paginated(
            f"/v1/inbox/comments/{inbox_post_id}/{self.platform_id}/replies",
            params=params,
            model=AsyncInboxComment,
            timeout=timeout,
            bind_ctx={"account_id": account_id, "inbox_post_id": inbox_post_id},
        )


# ---------------------------------------------------------------------------
# Commented post (parent of comments)
# ---------------------------------------------------------------------------


class _CommentedPostBase(_Bound):
    """Shared fields for CommentedPost / AsyncCommentedPost.

    Matches InboxPostRow wire shape.
    """

    id: str
    user_id: str
    account_id: str
    page_id: str | None = None
    platform: str
    platform_id: str
    content: str | None = None
    thumbnail: str | None = None
    permalink: str | None = None
    comment_count: int = 0
    like_count: int = 0
    published_at: datetime | None = None
    created_at: datetime
    updated_at: datetime


class CommentedPost(_CommentedPostBase):
    """A post that has received comments (sync)."""

    def list_comments(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        timeout: float | None = None,
    ) -> CursorPage[InboxComment]:
        """List comments on this post.

        Args:
            limit: Maximum number of comments to return.
            cursor: Pagination cursor.
            timeout: Optional request timeout in seconds.

        Returns:
            A CursorPage of InboxComment objects.

        Raises:
            UnboundModelError: If this model was not built by a client.
        """
        client = self._client_or_raise_sync()
        params: dict[str, Any] = {"account_id": self.account_id}
        if limit is not None:
            params["limit"] = limit
        if cursor is not None:
            params["cursor"] = cursor
        return client._get_paginated(
            f"/v1/inbox/comments/{self.id}",
            params=params,
            model=InboxComment,
            timeout=timeout,
            bind_ctx={"account_id": self.account_id, "inbox_post_id": self.id},
        )

    def reply(self, *, text: str, timeout: float | None = None) -> ReplyToCommentResponse:
        """Post a top-level comment on this post.

        Args:
            text: The comment text.
            timeout: Optional request timeout in seconds.

        Returns:
            A ReplyToCommentResponse with the new comment ID.

        Raises:
            UnboundModelError: If this model was not built by a client.
        """
        client = self._client_or_raise_sync()
        body: dict[str, Any] = {"account_id": self.account_id, "text": text}
        data = client._post(f"/v1/inbox/comments/{self.id}", json=body, timeout=timeout)
        return ReplyToCommentResponse.model_validate(data)


class AsyncCommentedPost(_CommentedPostBase):
    """A post that has received comments (async)."""

    async def list_comments(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        timeout: float | None = None,
    ) -> AsyncCursorPage[AsyncInboxComment]:
        """List comments on this post.

        Args:
            limit: Maximum number of comments to return.
            cursor: Pagination cursor.
            timeout: Optional request timeout in seconds.

        Returns:
            An AsyncCursorPage of AsyncInboxComment objects.

        Raises:
            UnboundModelError: If this model was not built by a client.
        """
        client = self._client_or_raise_async()
        params: dict[str, Any] = {"account_id": self.account_id}
        if limit is not None:
            params["limit"] = limit
        if cursor is not None:
            params["cursor"] = cursor
        return await client._get_paginated(
            f"/v1/inbox/comments/{self.id}",
            params=params,
            model=AsyncInboxComment,
            timeout=timeout,
            bind_ctx={"account_id": self.account_id, "inbox_post_id": self.id},
        )

    async def reply(self, *, text: str, timeout: float | None = None) -> ReplyToCommentResponse:
        """Post a top-level comment on this post.

        Args:
            text: The comment text.
            timeout: Optional request timeout in seconds.

        Returns:
            A ReplyToCommentResponse with the new comment ID.

        Raises:
            UnboundModelError: If this model was not built by a client.
        """
        client = self._client_or_raise_async()
        body: dict[str, Any] = {"account_id": self.account_id, "text": text}
        data = await client._post(f"/v1/inbox/comments/{self.id}", json=body, timeout=timeout)
        return ReplyToCommentResponse.model_validate(data)


# ---------------------------------------------------------------------------
# Pure data request/response models
# ---------------------------------------------------------------------------


class ReplyToCommentRequest(BaseModel):
    """Request body for ``POST /v1/inbox/comments/:postId``."""

    model_config = ConfigDict(populate_by_name=True)

    account_id: str
    text: str
    comment_id: str | None = None


class ReplyToCommentResponse(BaseModel):
    """Response after replying to a comment."""

    model_config = ConfigDict(populate_by_name=True)

    success: bool
    comment_id: str


class PrivateReplyRequest(BaseModel):
    """Request body for ``POST .../private-reply``."""

    model_config = ConfigDict(populate_by_name=True)

    account_id: str
    text: str
