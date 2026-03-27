from __future__ import annotations

from pydantic import BaseModel, ConfigDict


class CommentCapabilities(BaseModel):
    """Describes supported actions for a comment on this platform."""

    model_config = ConfigDict(populate_by_name=True)

    can_reply: bool = False
    can_delete: bool = False
    can_hide: bool = False
    can_like: bool = False
    can_private_reply: bool = False


class InboxComment(BaseModel):
    """A comment in the unified inbox with platform capabilities."""

    model_config = ConfigDict(populate_by_name=True)

    id: str
    inbox_post_id: str
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
    is_hidden: bool = False
    is_liked: bool = False
    parent_id: str | None = None
    created_at: str
    capabilities: CommentCapabilities


class CommentedPost(BaseModel):
    """A post that has received comments, shown in the inbox."""

    model_config = ConfigDict(populate_by_name=True)

    id: str
    user_id: str
    account_id: str
    platform: str
    platform_id: str
    content: str | None = None
    thumbnail: str | None = None
    permalink: str | None = None
    comment_count: int = 0
    like_count: int = 0
    created_at: str
    updated_at: str


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
