from __future__ import annotations

from typing import TYPE_CHECKING, Any

from socialapi.models.webhooks import (
    AsyncWebhook,
    CreateWebhookResponse,
    DeliveryDetail,
    DeliveryListItem,
    TestDeliveryResponse,
    Webhook,
    WebhookDetail,
    WebhookEventInfo,
)

if TYPE_CHECKING:
    from socialapi._base_client import BaseAsyncClient, BaseSyncClient
    from socialapi._pagination import AsyncCursorPage, CursorPage


class Webhooks:
    """Manage webhook endpoints (sync)."""

    _client: BaseSyncClient

    def __init__(self, client: BaseSyncClient) -> None:
        self._client = client

    def list(self, *, timeout: float | None = None) -> list[Webhook]:
        """List all webhook endpoints.

        Args:
            timeout: Override the client-level timeout for this request.

        Returns:
            A list of registered webhook endpoints.

        Raises:
            AuthenticationError: If the API key is invalid.
        """
        data = self._client._get("/v1/webhooks", timeout=timeout)
        raw_items: list[Any] = data.get("data", [])
        items = [Webhook.model_validate(item) for item in raw_items]
        for item in items:
            item._bind(self._client)
        return items

    def get(self, webhook_id: str, *, timeout: float | None = None) -> WebhookDetail:
        """Get a single webhook endpoint with delivery stats.

        Args:
            webhook_id: The webhook endpoint ID.
            timeout: Override the client-level timeout for this request.

        Returns:
            The webhook detail including stats.

        Raises:
            NotFoundError: If the webhook does not exist.
            AuthenticationError: If the API key is invalid.
        """
        data = self._client._get(f"/v1/webhooks/{webhook_id}", timeout=timeout)
        return WebhookDetail.model_validate(data)

    def list_events(self, *, timeout: float | None = None) -> list[WebhookEventInfo]:
        """List available webhook event types.

        Args:
            timeout: Override the client-level timeout for this request.

        Returns:
            The catalog of subscribable webhook event types.

        Raises:
            AuthenticationError: If the API key is invalid.
        """
        data = self._client._get("/v1/webhooks/events", timeout=timeout)
        raw_items: list[Any] = data.get("data", [])
        return [WebhookEventInfo.model_validate(item) for item in raw_items]

    def list_deliveries(
        self,
        webhook_id: str,
        *,
        status: str | None = None,
        event_type: str | None = None,
        cursor: str | None = None,
        limit: int | None = None,
        timeout: float | None = None,
    ) -> CursorPage[DeliveryListItem]:
        """List deliveries for a webhook endpoint.

        Args:
            webhook_id: The webhook endpoint ID.
            status: Filter by delivery status (e.g. ``delivered``, ``failed``).
            event_type: Filter by event type.
            cursor: Pagination cursor from a previous response.
            limit: Maximum number of results per page (default 50).
            timeout: Override the client-level timeout for this request.

        Returns:
            A cursor-paginated list of delivery records.

        Raises:
            NotFoundError: If the webhook does not exist.
            AuthenticationError: If the API key is invalid.
        """
        params: dict[str, Any] = {}
        if status is not None:
            params["status"] = status
        if event_type is not None:
            params["event_type"] = event_type
        if cursor is not None:
            params["cursor"] = cursor
        if limit is not None:
            params["limit"] = limit
        return self._client._get_paginated(
            f"/v1/webhooks/{webhook_id}/deliveries",
            params=params,
            model=DeliveryListItem,
            timeout=timeout,
        )

    def get_delivery(
        self,
        webhook_id: str,
        delivery_id: str,
        *,
        timeout: float | None = None,
    ) -> DeliveryDetail:
        """Get a single webhook delivery record.

        Args:
            webhook_id: The webhook endpoint ID.
            delivery_id: The delivery ID.
            timeout: Override the client-level timeout for this request.

        Returns:
            The full delivery record including attempts and payload.

        Raises:
            NotFoundError: If the webhook or delivery does not exist.
            AuthenticationError: If the API key is invalid.
        """
        data = self._client._get(f"/v1/webhooks/{webhook_id}/deliveries/{delivery_id}", timeout=timeout)
        return DeliveryDetail.model_validate(data)

    def retry_delivery(
        self,
        webhook_id: str,
        delivery_id: str,
        *,
        timeout: float | None = None,
    ) -> DeliveryDetail:
        """Retry a failed webhook delivery.

        Args:
            webhook_id: The webhook endpoint ID.
            delivery_id: The delivery ID to retry.
            timeout: Override the client-level timeout for this request.

        Returns:
            The updated delivery record.

        Raises:
            NotFoundError: If the webhook or delivery does not exist.
            AuthenticationError: If the API key is invalid.
        """
        data = self._client._post(
            f"/v1/webhooks/{webhook_id}/deliveries/{delivery_id}/retry",
            timeout=timeout,
        )
        return DeliveryDetail.model_validate(data)

    def test(
        self,
        webhook_id: str,
        *,
        event_type: str,
        payload: Any,
        timeout: float | None = None,
    ) -> TestDeliveryResponse:
        """Send a test delivery to a webhook endpoint.

        Args:
            webhook_id: The webhook endpoint ID.
            event_type: The event type to simulate.
            payload: The event payload to send (will be JSON-serialized).
            timeout: Override the client-level timeout for this request.

        Returns:
            The test delivery result including response status and body.

        Raises:
            NotFoundError: If the webhook does not exist.
            BadRequestError: If the event_type or payload is invalid.
            AuthenticationError: If the API key is invalid.
        """
        body: dict[str, Any] = {"event_type": event_type, "payload": payload}
        data = self._client._post(f"/v1/webhooks/{webhook_id}/test", json=body, timeout=timeout)
        return TestDeliveryResponse.model_validate(data)

    def create(
        self,
        *,
        url: str,
        events: list[str],
        timeout: float | None = None,
    ) -> CreateWebhookResponse:
        """Create a new webhook endpoint.

        Args:
            url: The HTTPS endpoint URL to deliver events to.
            events: The list of event types to subscribe to.
            timeout: Override the client-level timeout for this request.

        Returns:
            The created webhook including the one-time secret.

        Raises:
            BadRequestError: If the URL is invalid or events are unrecognised.
            AuthenticationError: If the API key is invalid.
        """
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
        """Update a webhook endpoint.

        Args:
            webhook_id: The webhook endpoint ID.
            url: New delivery URL (must be HTTPS).
            events: Replacement list of event types.
            is_active: Enable or disable delivery.
            timeout: Override the client-level timeout for this request.

        Returns:
            The updated webhook endpoint.

        Raises:
            NotFoundError: If the webhook does not exist.
            BadRequestError: If no fields are provided or values are invalid.
            AuthenticationError: If the API key is invalid.
        """
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
        """Delete a webhook endpoint.

        Args:
            webhook_id: The webhook endpoint ID.
            timeout: Override the client-level timeout for this request.

        Raises:
            NotFoundError: If the webhook does not exist.
            AuthenticationError: If the API key is invalid.
        """
        self._client._delete(f"/v1/webhooks/{webhook_id}", timeout=timeout)


class AsyncWebhooks:
    """Manage webhook endpoints (async)."""

    _client: BaseAsyncClient

    def __init__(self, client: BaseAsyncClient) -> None:
        self._client = client

    async def list(self, *, timeout: float | None = None) -> list[AsyncWebhook]:
        """List all webhook endpoints.

        Args:
            timeout: Override the client-level timeout for this request.

        Returns:
            A list of registered webhook endpoints.

        Raises:
            AuthenticationError: If the API key is invalid.
        """
        data = await self._client._get("/v1/webhooks", timeout=timeout)
        raw_items: list[Any] = data.get("data", [])
        items = [AsyncWebhook.model_validate(item) for item in raw_items]
        for item in items:
            item._bind(self._client)
        return items

    async def get(self, webhook_id: str, *, timeout: float | None = None) -> WebhookDetail:
        """Get a single webhook endpoint with delivery stats.

        Args:
            webhook_id: The webhook endpoint ID.
            timeout: Override the client-level timeout for this request.

        Returns:
            The webhook detail including stats.

        Raises:
            NotFoundError: If the webhook does not exist.
            AuthenticationError: If the API key is invalid.
        """
        data = await self._client._get(f"/v1/webhooks/{webhook_id}", timeout=timeout)
        return WebhookDetail.model_validate(data)

    async def list_events(self, *, timeout: float | None = None) -> list[WebhookEventInfo]:
        """List available webhook event types.

        Args:
            timeout: Override the client-level timeout for this request.

        Returns:
            The catalog of subscribable webhook event types.

        Raises:
            AuthenticationError: If the API key is invalid.
        """
        data = await self._client._get("/v1/webhooks/events", timeout=timeout)
        raw_items: list[Any] = data.get("data", [])
        return [WebhookEventInfo.model_validate(item) for item in raw_items]

    async def list_deliveries(
        self,
        webhook_id: str,
        *,
        status: str | None = None,
        event_type: str | None = None,
        cursor: str | None = None,
        limit: int | None = None,
        timeout: float | None = None,
    ) -> AsyncCursorPage[DeliveryListItem]:
        """List deliveries for a webhook endpoint.

        Args:
            webhook_id: The webhook endpoint ID.
            status: Filter by delivery status (e.g. ``delivered``, ``failed``).
            event_type: Filter by event type.
            cursor: Pagination cursor from a previous response.
            limit: Maximum number of results per page (default 50).
            timeout: Override the client-level timeout for this request.

        Returns:
            A cursor-paginated list of delivery records.

        Raises:
            NotFoundError: If the webhook does not exist.
            AuthenticationError: If the API key is invalid.
        """
        params: dict[str, Any] = {}
        if status is not None:
            params["status"] = status
        if event_type is not None:
            params["event_type"] = event_type
        if cursor is not None:
            params["cursor"] = cursor
        if limit is not None:
            params["limit"] = limit
        return await self._client._get_paginated(
            f"/v1/webhooks/{webhook_id}/deliveries",
            params=params,
            model=DeliveryListItem,
            timeout=timeout,
        )

    async def get_delivery(
        self,
        webhook_id: str,
        delivery_id: str,
        *,
        timeout: float | None = None,
    ) -> DeliveryDetail:
        """Get a single webhook delivery record.

        Args:
            webhook_id: The webhook endpoint ID.
            delivery_id: The delivery ID.
            timeout: Override the client-level timeout for this request.

        Returns:
            The full delivery record including attempts and payload.

        Raises:
            NotFoundError: If the webhook or delivery does not exist.
            AuthenticationError: If the API key is invalid.
        """
        data = await self._client._get(f"/v1/webhooks/{webhook_id}/deliveries/{delivery_id}", timeout=timeout)
        return DeliveryDetail.model_validate(data)

    async def retry_delivery(
        self,
        webhook_id: str,
        delivery_id: str,
        *,
        timeout: float | None = None,
    ) -> DeliveryDetail:
        """Retry a failed webhook delivery.

        Args:
            webhook_id: The webhook endpoint ID.
            delivery_id: The delivery ID to retry.
            timeout: Override the client-level timeout for this request.

        Returns:
            The updated delivery record.

        Raises:
            NotFoundError: If the webhook or delivery does not exist.
            AuthenticationError: If the API key is invalid.
        """
        data = await self._client._post(
            f"/v1/webhooks/{webhook_id}/deliveries/{delivery_id}/retry",
            timeout=timeout,
        )
        return DeliveryDetail.model_validate(data)

    async def test(
        self,
        webhook_id: str,
        *,
        event_type: str,
        payload: Any,
        timeout: float | None = None,
    ) -> TestDeliveryResponse:
        """Send a test delivery to a webhook endpoint.

        Args:
            webhook_id: The webhook endpoint ID.
            event_type: The event type to simulate.
            payload: The event payload to send (will be JSON-serialized).
            timeout: Override the client-level timeout for this request.

        Returns:
            The test delivery result including response status and body.

        Raises:
            NotFoundError: If the webhook does not exist.
            BadRequestError: If the event_type or payload is invalid.
            AuthenticationError: If the API key is invalid.
        """
        body: dict[str, Any] = {"event_type": event_type, "payload": payload}
        data = await self._client._post(f"/v1/webhooks/{webhook_id}/test", json=body, timeout=timeout)
        return TestDeliveryResponse.model_validate(data)

    async def create(
        self,
        *,
        url: str,
        events: list[str],
        timeout: float | None = None,
    ) -> CreateWebhookResponse:
        """Create a new webhook endpoint.

        Args:
            url: The HTTPS endpoint URL to deliver events to.
            events: The list of event types to subscribe to.
            timeout: Override the client-level timeout for this request.

        Returns:
            The created webhook including the one-time secret.

        Raises:
            BadRequestError: If the URL is invalid or events are unrecognised.
            AuthenticationError: If the API key is invalid.
        """
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
        """Update a webhook endpoint.

        Args:
            webhook_id: The webhook endpoint ID.
            url: New delivery URL (must be HTTPS).
            events: Replacement list of event types.
            is_active: Enable or disable delivery.
            timeout: Override the client-level timeout for this request.

        Returns:
            The updated webhook endpoint.

        Raises:
            NotFoundError: If the webhook does not exist.
            BadRequestError: If no fields are provided or values are invalid.
            AuthenticationError: If the API key is invalid.
        """
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
        """Delete a webhook endpoint.

        Args:
            webhook_id: The webhook endpoint ID.
            timeout: Override the client-level timeout for this request.

        Raises:
            NotFoundError: If the webhook does not exist.
            AuthenticationError: If the API key is invalid.
        """
        await self._client._delete(f"/v1/webhooks/{webhook_id}", timeout=timeout)
