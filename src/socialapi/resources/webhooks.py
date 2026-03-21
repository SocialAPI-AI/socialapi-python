"""Webhooks resource."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from socialapi.models.shared import OKResponse
from socialapi.models.webhooks import CreateWebhookResponse, WebhookEndpoint, WebhooksListResponse

if TYPE_CHECKING:
    from socialapi._async_client import AsyncSocialAPI
    from socialapi._client import SocialAPI


class Webhooks:
    """Synchronous webhooks resource.

    Provides methods for listing, creating, updating, and deleting webhook endpoints.
    """

    def __init__(self, client: SocialAPI) -> None:
        self._client = client

    def list(self) -> WebhooksListResponse:
        """List all webhook endpoints.

        Returns:
            A WebhooksListResponse containing the webhook endpoints.

        Raises:
            AuthenticationError: If the API key is invalid.
        """
        return self._client._get("/v1/webhooks", response_model=WebhooksListResponse)

    def create(self, url: str, events: list[str]) -> CreateWebhookResponse:
        """Create a new webhook endpoint.

        Args:
            url: The URL to receive webhook events.
            events: List of event types to subscribe to.

        Returns:
            A CreateWebhookResponse with the endpoint details and signing secret.

        Raises:
            ValidationError: If the URL or events are invalid.
        """
        return self._client._post(
            "/v1/webhooks",
            json_data={"url": url, "events": events},
            response_model=CreateWebhookResponse,
        )

    def update(
        self,
        webhook_id: str,
        *,
        url: str | None = None,
        events: list[str] | None = None,
        is_active: bool | None = None,
    ) -> WebhookEndpoint:
        """Update a webhook endpoint.

        Args:
            webhook_id: The ID of the webhook endpoint to update.
            url: Optional new URL for the endpoint.
            events: Optional new list of event types.
            is_active: Optional flag to enable or disable the endpoint.

        Returns:
            The updated WebhookEndpoint.

        Raises:
            NotFoundError: If the webhook endpoint is not found.
            ValidationError: If the update payload is invalid.
        """
        body: dict[str, Any] = {}
        if url is not None:
            body["url"] = url
        if events is not None:
            body["events"] = events
        if is_active is not None:
            body["is_active"] = is_active
        return self._client._patch(f"/v1/webhooks/{webhook_id}", json_data=body, response_model=WebhookEndpoint)

    def delete(self, webhook_id: str) -> OKResponse:
        """Delete a webhook endpoint.

        Args:
            webhook_id: The ID of the webhook endpoint to delete.

        Returns:
            An OKResponse indicating the endpoint was deleted.

        Raises:
            NotFoundError: If the webhook endpoint is not found.
        """
        return self._client._delete(f"/v1/webhooks/{webhook_id}", response_model=OKResponse)


class AsyncWebhooks:
    """Asynchronous webhooks resource.

    Provides methods for listing, creating, updating, and deleting webhook endpoints.
    """

    def __init__(self, client: AsyncSocialAPI) -> None:
        self._client = client

    async def list(self) -> WebhooksListResponse:
        """List all webhook endpoints.

        Returns:
            A WebhooksListResponse containing the webhook endpoints.

        Raises:
            AuthenticationError: If the API key is invalid.
        """
        return await self._client._get("/v1/webhooks", response_model=WebhooksListResponse)

    async def create(self, url: str, events: list[str]) -> CreateWebhookResponse:
        """Create a new webhook endpoint.

        Args:
            url: The URL to receive webhook events.
            events: List of event types to subscribe to.

        Returns:
            A CreateWebhookResponse with the endpoint details and signing secret.

        Raises:
            ValidationError: If the URL or events are invalid.
        """
        return await self._client._post(
            "/v1/webhooks",
            json_data={"url": url, "events": events},
            response_model=CreateWebhookResponse,
        )

    async def update(
        self,
        webhook_id: str,
        *,
        url: str | None = None,
        events: list[str] | None = None,
        is_active: bool | None = None,
    ) -> WebhookEndpoint:
        """Update a webhook endpoint.

        Args:
            webhook_id: The ID of the webhook endpoint to update.
            url: Optional new URL for the endpoint.
            events: Optional new list of event types.
            is_active: Optional flag to enable or disable the endpoint.

        Returns:
            The updated WebhookEndpoint.

        Raises:
            NotFoundError: If the webhook endpoint is not found.
            ValidationError: If the update payload is invalid.
        """
        body: dict[str, Any] = {}
        if url is not None:
            body["url"] = url
        if events is not None:
            body["events"] = events
        if is_active is not None:
            body["is_active"] = is_active
        return await self._client._patch(f"/v1/webhooks/{webhook_id}", json_data=body, response_model=WebhookEndpoint)

    async def delete(self, webhook_id: str) -> OKResponse:
        """Delete a webhook endpoint.

        Args:
            webhook_id: The ID of the webhook endpoint to delete.

        Returns:
            An OKResponse indicating the endpoint was deleted.

        Raises:
            NotFoundError: If the webhook endpoint is not found.
        """
        return await self._client._delete(f"/v1/webhooks/{webhook_id}", response_model=OKResponse)
