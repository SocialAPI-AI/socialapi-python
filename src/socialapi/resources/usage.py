"""Usage resource."""

from __future__ import annotations

from typing import TYPE_CHECKING

from socialapi.models.usage import UsageResponse

if TYPE_CHECKING:
    from socialapi._async_client import AsyncSocialAPI
    from socialapi._client import SocialAPI


class Usage:
    """Synchronous usage resource.

    Provides methods for retrieving usage statistics.
    """

    def __init__(self, client: SocialAPI) -> None:
        self._client = client

    def get(self) -> UsageResponse:
        """Get current usage and limits for the authenticated user.

        Returns:
            A UsageResponse with account, post, and interaction usage counts.

        Raises:
            AuthenticationError: If the API key is invalid.
        """
        return self._client._get("/v1/usage", response_model=UsageResponse)


class AsyncUsage:
    """Asynchronous usage resource.

    Provides methods for retrieving usage statistics.
    """

    def __init__(self, client: AsyncSocialAPI) -> None:
        self._client = client

    async def get(self) -> UsageResponse:
        """Get current usage and limits for the authenticated user.

        Returns:
            A UsageResponse with account, post, and interaction usage counts.

        Raises:
            AuthenticationError: If the API key is invalid.
        """
        return await self._client._get("/v1/usage", response_model=UsageResponse)
