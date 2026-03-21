"""Interaction models."""

from typing import Any

from pydantic import BaseModel, Field


class Media(BaseModel):
    """A media attachment."""

    url: str
    type: str


class Author(BaseModel):
    """Author of an interaction."""

    id: str
    name: str
    avatar_url: str = ""


class Content(BaseModel):
    """Content of an interaction."""

    text: str = ""
    media: list[Media] = Field(default_factory=lambda: [])


class Interaction(BaseModel):
    """A social media interaction (comment, review, DM, or mention)."""

    id: str
    platform: str
    type: str
    author: Author
    content: Content
    metadata: dict[str, Any] = Field(default_factory=dict)
    created_at: str
    account_id: str
    platform_id: str


class InteractionsListResponse(BaseModel):
    """Response for listing interactions."""

    data: list[Interaction]
    count: int


class ReplyResponse(BaseModel):
    """Response after replying to an interaction."""

    id: str
    created_at: str


class DMThreadResponse(BaseModel):
    """Response for getting a DM thread."""

    thread_id: str
