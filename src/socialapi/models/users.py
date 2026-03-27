from __future__ import annotations

from pydantic import BaseModel, ConfigDict


class User(BaseModel):
    """The authenticated user's profile from ``GET /v1/users/me``."""

    model_config = ConfigDict(populate_by_name=True)

    id: str
    email: str
    plan: str
    onboarding: bool = True
    avatar_url: str | None = None
    beta_tester: bool = False
    allowed_platforms: list[str] | None = None


class UpdateUserRequest(BaseModel):
    """Request body for ``PATCH /v1/users/me``."""

    model_config = ConfigDict(populate_by_name=True)

    onboarding: bool | None = None
    use_case: str | None = None
    referral: str | None = None
