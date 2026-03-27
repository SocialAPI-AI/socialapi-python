from __future__ import annotations

from datetime import datetime  # noqa: TC003

from pydantic import BaseModel, ConfigDict


class UsageResponse(BaseModel):
    """Current billing period usage from ``GET /v1/usage``."""

    model_config = ConfigDict(populate_by_name=True)

    brands_used: int
    brands_limit: int
    posts_used: int
    posts_limit: int
    interactions_used: int
    interactions_limit: int
    period_start: datetime
    period_end: datetime


class AccountLimits(BaseModel):
    """Platform-specific quota limits for a connected account.

    The ``limits`` dict maps platform-defined keys (e.g. ``posts_remaining``)
    to their remaining counts. Platforms without usage limits return an empty dict.
    """

    model_config = ConfigDict(populate_by_name=True)

    limits: dict[str, int] = {}
