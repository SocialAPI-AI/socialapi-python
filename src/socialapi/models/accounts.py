"""Account models."""

from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field


class Account(BaseModel):
    """A connected social media account."""

    id: str
    platform: str
    name: str
    username: str
    metadata: dict[str, Any] = Field(default_factory=dict)


class AccountsListResponse(BaseModel):
    """Response for listing connected accounts."""

    data: list[Account]
    count: int


class ConnectResponse(BaseModel):
    """Response for connecting an account.

    For direct auth (201), account_id/platform/username are populated.
    For OAuth2 (202), auth_url/state/message are populated.
    """

    account_id: str | None = None
    platform: str | None = None
    username: str | None = None
    auth_url: str | None = None
    state: str | None = None
    message: str | None = None


class OAuthExchangeResponse(BaseModel):
    """Response for exchanging an OAuth code.

    For single-account platforms, account_id/platform/username are populated.
    For multi-account platforms (e.g. Facebook Pages), data/count are populated.
    """

    account_id: str | None = None
    platform: str | None = None
    username: str | None = None
    data: list[Account] | None = None
    count: int | None = None
