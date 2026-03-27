from __future__ import annotations

from typing import Any

from pydantic import BaseModel, ConfigDict


class Account(BaseModel):
    """A connected social media account."""

    model_config = ConfigDict(populate_by_name=True)

    id: str
    platform: str
    name: str
    username: str
    brand_id: str
    metadata: dict[str, Any] | None = None


class ConnectAccountRequest(BaseModel):
    """Request body for ``POST /v1/accounts/connect``."""

    model_config = ConfigDict(populate_by_name=True)

    platform: str
    brand_id: str | None = None
    metadata: dict[str, Any] | None = None


class ConnectAccountResponse(BaseModel):
    """Response when a direct-auth account is connected (HTTP 201)."""

    model_config = ConfigDict(populate_by_name=True)

    account_id: str
    platform: str
    username: str


class ConnectOAuthResponse(BaseModel):
    """Response when an OAuth2 flow is initiated (HTTP 202)."""

    model_config = ConfigDict(populate_by_name=True)

    auth_url: str
    state: str
    message: str


class OAuthExchangeRequest(BaseModel):
    """Request body for ``POST /v1/oauth/exchange``."""

    model_config = ConfigDict(populate_by_name=True)

    platform: str
    code: str
    metadata: dict[str, Any] | None = None


class OAuthExchangeResponse(BaseModel):
    """Response after a successful OAuth code exchange.

    Returns the list of connected accounts (some platforms return multiple,
    e.g. Facebook pages).
    """

    model_config = ConfigDict(populate_by_name=True)

    accounts: list[ConnectAccountResponse] | None = None
