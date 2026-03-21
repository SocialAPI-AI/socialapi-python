"""Webhook models."""

from __future__ import annotations

from pydantic import BaseModel


class WebhookEndpoint(BaseModel):
    """A configured webhook endpoint."""

    id: str
    url: str
    events: list[str]
    is_active: bool
    created_at: str


class WebhooksListResponse(BaseModel):
    """Response for listing webhook endpoints."""

    data: list[WebhookEndpoint]
    count: int


class CreateWebhookResponse(BaseModel):
    """Response after creating a new webhook endpoint."""

    id: str
    url: str
    events: list[str]
    secret: str
    message: str
