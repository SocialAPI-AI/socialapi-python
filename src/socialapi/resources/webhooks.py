from __future__ import annotations

from typing import TYPE_CHECKING, Any

from socialapi.models.webhooks import AsyncWebhook, CreateWebhookResponse, Webhook

if TYPE_CHECKING:
    from socialapi._base_client import BaseAsyncClient, BaseSyncClient


class Webhooks:
    """Manage webhook endpoints (sync)."""

    _client: BaseSyncClient

    def __init__(self, client: BaseSyncClient) -> None:
        self._client = client

    def list(self, *, timeout: float | None = None) -> list[Webhook]:
        data = self._client._get("/v1/webhooks", timeout=timeout)
        raw_items: list[Any] = data.get("data", [])
        items = [Webhook.model_validate(item) for item in raw_items]
        for item in items:
            item._bind(self._client)
        return items

    def create(
        self,
        *,
        url: str,
        events: list[str],
        timeout: float | None = None,
    ) -> CreateWebhookResponse:
        body: dict[str, Any] = {"url": url, "events": events}
        data = self._client._post("/v1/webhooks", json=body, timeout=timeout)
        return CreateWebhookResponse.model_validate(data)

    def update(
        self,
        webhook_id: str,
        *,
        url: str | None = None,
        events: list[str] | None = None,
        is_active: bool | None = None,
        timeout: float | None = None,
    ) -> Webhook:
        body: dict[str, Any] = {}
        if url is not None:
            body["url"] = url
        if events is not None:
            body["events"] = events
        if is_active is not None:
            body["is_active"] = is_active
        data = self._client._patch(f"/v1/webhooks/{webhook_id}", json=body, timeout=timeout)
        webhook = Webhook.model_validate(data)
        webhook._bind(self._client)
        return webhook

    def delete(self, webhook_id: str, *, timeout: float | None = None) -> None:
        self._client._delete(f"/v1/webhooks/{webhook_id}", timeout=timeout)


class AsyncWebhooks:
    """Manage webhook endpoints (async)."""

    _client: BaseAsyncClient

    def __init__(self, client: BaseAsyncClient) -> None:
        self._client = client

    async def list(self, *, timeout: float | None = None) -> list[AsyncWebhook]:
        data = await self._client._get("/v1/webhooks", timeout=timeout)
        raw_items: list[Any] = data.get("data", [])
        items = [AsyncWebhook.model_validate(item) for item in raw_items]
        for item in items:
            item._bind(self._client)
        return items

    async def create(
        self,
        *,
        url: str,
        events: list[str],
        timeout: float | None = None,
    ) -> CreateWebhookResponse:
        body: dict[str, Any] = {"url": url, "events": events}
        data = await self._client._post("/v1/webhooks", json=body, timeout=timeout)
        return CreateWebhookResponse.model_validate(data)

    async def update(
        self,
        webhook_id: str,
        *,
        url: str | None = None,
        events: list[str] | None = None,
        is_active: bool | None = None,
        timeout: float | None = None,
    ) -> AsyncWebhook:
        body: dict[str, Any] = {}
        if url is not None:
            body["url"] = url
        if events is not None:
            body["events"] = events
        if is_active is not None:
            body["is_active"] = is_active
        data = await self._client._patch(f"/v1/webhooks/{webhook_id}", json=body, timeout=timeout)
        webhook = AsyncWebhook.model_validate(data)
        webhook._bind(self._client)
        return webhook

    async def delete(self, webhook_id: str, *, timeout: float | None = None) -> None:
        await self._client._delete(f"/v1/webhooks/{webhook_id}", timeout=timeout)
