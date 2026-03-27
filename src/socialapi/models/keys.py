from __future__ import annotations

from pydantic import BaseModel, ConfigDict


class APIKey(BaseModel):
    """A registered API key (never includes the raw secret)."""

    model_config = ConfigDict(populate_by_name=True)

    id: str
    name: str
    preview: str
    is_active: bool
    last_used_at: str | None = None
    created_at: str


class CreateKeyRequest(BaseModel):
    """Request body for ``POST /v1/keys``."""

    model_config = ConfigDict(populate_by_name=True)

    name: str


class CreateKeyResponse(BaseModel):
    """Response returned once when a new key is created (includes raw key)."""

    model_config = ConfigDict(populate_by_name=True)

    id: str
    name: str
    raw_key: str
    message: str
