from __future__ import annotations

from pydantic import BaseModel, ConfigDict


class Review(BaseModel):
    """A review from a platform (proxied in real-time, not stored)."""

    model_config = ConfigDict(populate_by_name=True)

    id: str
    platform: str
    account_id: str
    rating: int
    text: str | None = None
    author: str
    created_at: str


class ReplyToReviewRequest(BaseModel):
    """Request body for ``POST /v1/inbox/reviews/:id/reply``."""

    model_config = ConfigDict(populate_by_name=True)

    account_id: str
    text: str


class ReplyToReviewResponse(BaseModel):
    """Response after replying to a review."""

    model_config = ConfigDict(populate_by_name=True)

    success: bool
    reply_id: str


class UpdateReviewReplyRequest(BaseModel):
    """Request body for ``PUT /v1/inbox/reviews/:id/reply``."""

    model_config = ConfigDict(populate_by_name=True)

    account_id: str
    text: str
