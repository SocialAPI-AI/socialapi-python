from __future__ import annotations

from datetime import datetime  # noqa: TC003
from typing import Any

from pydantic import BaseModel, ConfigDict

from socialapi._bound import _Bound


class _WebhookBase(_Bound):
    """Shared fields for Webhook / AsyncWebhook."""

    id: str
    url: str
    events: list[str]
    is_active: bool = True
    created_at: datetime


class Webhook(_WebhookBase):
    """A registered webhook endpoint (sync)."""

    def update(
        self,
        *,
        url: str | None = None,
        events: list[str] | None = None,
        is_active: bool | None = None,
        timeout: float | None = None,
    ) -> Webhook:
        client = self._client_or_raise_sync()
        body: dict[str, Any] = {}
        if url is not None:
            body["url"] = url
        if events is not None:
            body["events"] = events
        if is_active is not None:
            body["is_active"] = is_active
        data = client._patch(f"/v1/webhooks/{self.id}", json=body, timeout=timeout)
        if isinstance(data, dict):
            updated = Webhook.model_validate(data)
            updated._bind(client)
            return updated
        return self

    def delete(self, *, timeout: float | None = None) -> None:
        client = self._client_or_raise_sync()
        client._delete(f"/v1/webhooks/{self.id}", timeout=timeout)


class AsyncWebhook(_WebhookBase):
    """A registered webhook endpoint (async)."""

    async def update(
        self,
        *,
        url: str | None = None,
        events: list[str] | None = None,
        is_active: bool | None = None,
        timeout: float | None = None,
    ) -> AsyncWebhook:
        client = self._client_or_raise_async()
        body: dict[str, Any] = {}
        if url is not None:
            body["url"] = url
        if events is not None:
            body["events"] = events
        if is_active is not None:
            body["is_active"] = is_active
        data = await client._patch(f"/v1/webhooks/{self.id}", json=body, timeout=timeout)
        if isinstance(data, dict):
            updated = AsyncWebhook.model_validate(data)
            updated._bind(client)
            return updated
        return self

    async def delete(self, *, timeout: float | None = None) -> None:
        client = self._client_or_raise_async()
        await client._delete(f"/v1/webhooks/{self.id}", timeout=timeout)


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
