from __future__ import annotations

from typing import TYPE_CHECKING, Any

from socialapi.models.webhooks import CreateWebhookResponse, Webhook

if TYPE_CHECKING:
    from socialapi._base_client import BaseAsyncClient, BaseSyncClient


class Webhooks:
    """Manage webhook endpoints (sync)."""

    _client: BaseSyncClient

    def __init__(self, client: BaseSyncClient) -> None:
        self._client = client

    def list(
        self,
        *,
        timeout: float | None = None,
    ) -> list[Webhook]:
        """List all registered webhook endpoints.

        Args:
            timeout: Override the client-level timeout for this request.

        Returns:
            A list of webhook endpoints.

        Raises:
            AuthenticationError: If the API key is invalid.
        """
        data = self._client._get("/v1/webhooks", timeout=timeout)
        raw_items: list[Any] = data.get("data", [])
        return [Webhook.model_validate(item) for item in raw_items]

    def create(
        self,
        *,
        url: str,
        events: list[str],
        timeout: float | None = None,
    ) -> CreateWebhookResponse:
        """Create a new webhook endpoint.

        Args:
            url: HTTPS URL to receive webhook POST requests.
            events: Event types to subscribe to.
            timeout: Override the client-level timeout for this request.

        Returns:
            The new webhook including the signing secret (shown once).

        Raises:
            BadRequestError: If the URL or events are invalid.
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
            webhook_id: The webhook ID to update.
            url: New delivery URL.
            events: New event subscriptions (replaces existing).
            is_active: Enable or disable the endpoint.
            timeout: Override the client-level timeout for this request.

        Returns:
            The updated webhook.

        Raises:
            NotFoundError: If the webhook does not exist.
            BadRequestError: If the update parameters are invalid.
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
        return Webhook.model_validate(data)

    def delete(
        self,
        webhook_id: str,
        *,
        timeout: float | None = None,
    ) -> None:
        """Delete a webhook endpoint.

        Args:
            webhook_id: The webhook ID to delete.
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

    async def list(
        self,
        *,
        timeout: float | None = None,
    ) -> list[Webhook]:
        """List all registered webhook endpoints.

        Args:
            timeout: Override the client-level timeout for this request.

        Returns:
            A list of webhook endpoints.

        Raises:
            AuthenticationError: If the API key is invalid.
        """
        data = await self._client._get("/v1/webhooks", timeout=timeout)
        raw_items: list[Any] = data.get("data", [])
        return [Webhook.model_validate(item) for item in raw_items]

    async def create(
        self,
        *,
        url: str,
        events: list[str],
        timeout: float | None = None,
    ) -> CreateWebhookResponse:
        """Create a new webhook endpoint.

        Args:
            url: HTTPS URL to receive webhook POST requests.
            events: Event types to subscribe to.
            timeout: Override the client-level timeout for this request.

        Returns:
            The new webhook including the signing secret (shown once).

        Raises:
            BadRequestError: If the URL or events are invalid.
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
    ) -> Webhook:
        """Update a webhook endpoint.

        Args:
            webhook_id: The webhook ID to update.
            url: New delivery URL.
            events: New event subscriptions (replaces existing).
            is_active: Enable or disable the endpoint.
            timeout: Override the client-level timeout for this request.

        Returns:
            The updated webhook.

        Raises:
            NotFoundError: If the webhook does not exist.
            BadRequestError: If the update parameters are invalid.
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
        return Webhook.model_validate(data)

    async def delete(
        self,
        webhook_id: str,
        *,
        timeout: float | None = None,
    ) -> None:
        """Delete a webhook endpoint.

        Args:
            webhook_id: The webhook ID to delete.
            timeout: Override the client-level timeout for this request.

        Raises:
            NotFoundError: If the webhook does not exist.
            AuthenticationError: If the API key is invalid.
        """
        await self._client._delete(f"/v1/webhooks/{webhook_id}", timeout=timeout)
