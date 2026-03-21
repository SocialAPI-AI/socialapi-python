"""OAuth resource."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from socialapi.models.accounts import OAuthExchangeResponse

if TYPE_CHECKING:
    from socialapi._async_client import AsyncSocialAPI
    from socialapi._client import SocialAPI


class OAuth:
    """Synchronous OAuth resource.

    Provides methods for exchanging OAuth authorization codes.
    """

    def __init__(self, client: SocialAPI) -> None:
        self._client = client

    def exchange(self, platform: str, code: str, metadata: dict[str, Any]) -> OAuthExchangeResponse:
        """Exchange an OAuth authorization code for account access.

        Args:
            platform: The social media platform (e.g. ``"instagram"``, ``"facebook"``).
            code: The OAuth authorization code received from the platform.
            metadata: Platform-specific metadata (e.g. redirect URI).

        Returns:
            An OAuthExchangeResponse with the connected account details.

        Raises:
            ValidationError: If the platform, code, or metadata is invalid.
            AuthenticationError: If the OAuth code is expired or invalid.
        """
        return self._client._post(
            "/v1/oauth/exchange",
            json_data={"platform": platform, "code": code, "metadata": metadata},
            response_model=OAuthExchangeResponse,
        )


class AsyncOAuth:
    """Asynchronous OAuth resource.

    Provides methods for exchanging OAuth authorization codes.
    """

    def __init__(self, client: AsyncSocialAPI) -> None:
        self._client = client

    async def exchange(self, platform: str, code: str, metadata: dict[str, Any]) -> OAuthExchangeResponse:
        """Exchange an OAuth authorization code for account access.

        Args:
            platform: The social media platform (e.g. ``"instagram"``, ``"facebook"``).
            code: The OAuth authorization code received from the platform.
            metadata: Platform-specific metadata (e.g. redirect URI).

        Returns:
            An OAuthExchangeResponse with the connected account details.

        Raises:
            ValidationError: If the platform, code, or metadata is invalid.
            AuthenticationError: If the OAuth code is expired or invalid.
        """
        return await self._client._post(
            "/v1/oauth/exchange",
            json_data={"platform": platform, "code": code, "metadata": metadata},
            response_model=OAuthExchangeResponse,
        )
