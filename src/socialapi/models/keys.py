"""API key models."""

from __future__ import annotations

from pydantic import BaseModel


class KeyListItem(BaseModel):
    """An API key summary (without the raw key)."""

    id: str
    name: str
    preview: str
    is_active: bool
    last_used_at: str | None = None
    created_at: str


class KeysListResponse(BaseModel):
    """Response for listing API keys."""

    data: list[KeyListItem]
    count: int


class CreateKeyResponse(BaseModel):
    """Response after creating a new API key."""

    id: str
    name: str
    raw_key: str
    message: str
