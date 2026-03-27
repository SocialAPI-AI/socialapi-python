from __future__ import annotations

from datetime import datetime  # noqa: TC003

from pydantic import BaseModel, ConfigDict


class Invite(BaseModel):
    """An invite created for a brand (full response with token)."""

    model_config = ConfigDict(populate_by_name=True)

    id: str
    platform: str
    token: str
    url: str
    expires_at: datetime


class InviteListItem(BaseModel):
    """An invite as returned by the list endpoint."""

    model_config = ConfigDict(populate_by_name=True)

    id: str
    platform: str
    token: str
    url: str
    is_active: bool
    expires_at: datetime
    created_at: datetime


class CreateInviteRequest(BaseModel):
    """Request body for ``POST /v1/invites``."""

    model_config = ConfigDict(populate_by_name=True)

    brand_id: str
    platform: str
    expires_in_days: int
