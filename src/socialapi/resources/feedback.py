from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from socialapi._base_client import BaseAsyncClient, BaseSyncClient


class Feedback:
    """Submit feedback to SocialAPI (sync)."""

    _client: BaseSyncClient

    def __init__(self, client: BaseSyncClient) -> None:
        self._client = client

    def send(
        self,
        *,
        type: str,
        message: str,
        timeout: float | None = None,
    ) -> None:
        """Send feedback to the SocialAPI team.

        Args:
            type: Feedback type (``"bug"``, ``"feature_request"``, or ``"general"``).
            message: Feedback message content.
            timeout: Override the client-level timeout for this request.

        Raises:
            BadRequestError: If type or message is invalid.
            AuthenticationError: If the API key is invalid.
        """
        body: dict[str, Any] = {"type": type, "message": message}
        self._client._post("/v1/feedback", json=body, timeout=timeout)


class AsyncFeedback:
    """Submit feedback to SocialAPI (async)."""

    _client: BaseAsyncClient

    def __init__(self, client: BaseAsyncClient) -> None:
        self._client = client

    async def send(
        self,
        *,
        type: str,
        message: str,
        timeout: float | None = None,
    ) -> None:
        """Send feedback to the SocialAPI team.

        Args:
            type: Feedback type (``"bug"``, ``"feature_request"``, or ``"general"``).
            message: Feedback message content.
            timeout: Override the client-level timeout for this request.

        Raises:
            BadRequestError: If type or message is invalid.
            AuthenticationError: If the API key is invalid.
        """
        body: dict[str, Any] = {"type": type, "message": message}
        await self._client._post("/v1/feedback", json=body, timeout=timeout)
