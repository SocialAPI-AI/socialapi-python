"""User models."""

from __future__ import annotations

from pydantic import BaseModel


class User(BaseModel):
    """The authenticated user."""

    id: str
    email: str
    plan: str
    onboarding: bool
    avatar_url: str | None = None
    beta_tester: bool = False
