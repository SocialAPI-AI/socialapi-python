from __future__ import annotations

from pydantic import BaseModel, ConfigDict


class Webhook(BaseModel):
    """A registered webhook endpoint."""

    model_config = ConfigDict(populate_by_name=True)

    id: str
    url: str
    events: list[str]
    is_active: bool = True
    created_at: str


class CreateWebhookRequest(BaseModel):
    """Request body for ``POST /v1/webhooks``."""

    model_config = ConfigDict(populate_by_name=True)

    url: str
    events: list[str]


class CreateWebhookResponse(BaseModel):
    """Response when a webhook is created (includes secret, shown once)."""

    model_config = ConfigDict(populate_by_name=True)

    id: str
    url: str
    events: list[str]
    secret: str
    message: str


class UpdateWebhookRequest(BaseModel):
    """Request body for ``PATCH /v1/webhooks/:id``."""

    model_config = ConfigDict(populate_by_name=True)

    url: str | None = None
    events: list[str] | None = None
    is_active: bool | None = None
