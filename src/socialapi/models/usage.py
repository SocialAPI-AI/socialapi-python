"""Usage models."""

from __future__ import annotations

from pydantic import BaseModel


class UsageResponse(BaseModel):
    """Current usage and limits for the authenticated user."""

    accounts_used: int
    accounts_limit: int
    posts_used: int
    posts_limit: int
    interactions_used: int
    interactions_limit: int
    period_start: str
    period_end: str
