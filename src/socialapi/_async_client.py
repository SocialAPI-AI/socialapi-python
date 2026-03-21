"""Asynchronous SocialAPI client."""

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any

from socialapi._base_client import AsyncAPIClient
from socialapi._config import ClientConfig
from socialapi._constants import DEFAULT_BASE_URL, DEFAULT_MAX_RETRIES, DEFAULT_TIMEOUT
from socialapi.resources.accounts import AsyncAccounts
from socialapi.resources.comments import AsyncComments
from socialapi.resources.dms import AsyncDMs
from socialapi.resources.feedback import AsyncFeedback
from socialapi.resources.interactions import AsyncInteractions
from socialapi.resources.keys import AsyncKeys
from socialapi.resources.media import AsyncMedia
from socialapi.resources.mentions import AsyncMentions
from socialapi.resources.oauth import AsyncOAuth
from socialapi.resources.posts import AsyncPosts
from socialapi.resources.reviews import AsyncReviews
from socialapi.resources.usage import AsyncUsage
from socialapi.resources.users import AsyncUsers
from socialapi.resources.webhooks import AsyncWebhooks

if TYPE_CHECKING:
    import httpx


class AsyncSocialAPI(AsyncAPIClient):
    """Asynchronous client for the SocialAPI.

    Usage::

        client = AsyncSocialAPI(api_key="sapi_key_...")
        accounts = await client.accounts.list()

    Or as an async context manager::

        async with AsyncSocialAPI(api_key="sapi_key_...") as client:
            accounts = await client.accounts.list()

    Args:
        api_key: API key for authentication. Falls back to the
            ``SOCIALAPI_API_KEY`` environment variable if not provided.
        base_url: Override the default API base URL.
        timeout: Request timeout in seconds.
        max_retries: Maximum number of retries for failed requests.
        http_client: Optional custom httpx.AsyncClient instance.
    """

    accounts: AsyncAccounts
    posts: AsyncPosts
    comments: AsyncComments
    interactions: AsyncInteractions
    dms: AsyncDMs
    reviews: AsyncReviews
    mentions: AsyncMentions
    media: AsyncMedia
    usage: AsyncUsage
    keys: AsyncKeys
    users: AsyncUsers
    webhooks: AsyncWebhooks
    oauth: AsyncOAuth
    feedback: AsyncFeedback

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str = DEFAULT_BASE_URL,
        timeout: float = DEFAULT_TIMEOUT,
        max_retries: int = DEFAULT_MAX_RETRIES,
        http_client: httpx.AsyncClient | None = None,
    ) -> None:
        resolved_key = api_key or os.environ.get("SOCIALAPI_API_KEY", "")
        if not resolved_key:
            msg = (
                "The api_key parameter or SOCIALAPI_API_KEY environment variable must be set. "
                "You can generate a key at https://app.social-api.ai/keys"
            )
            raise ValueError(msg)

        config = ClientConfig(
            api_key=resolved_key,
            base_url=base_url,
            timeout=timeout,
            max_retries=max_retries,
        )
        super().__init__(config, http_client=http_client)

        # Initialize resource namespaces.
        self.accounts = AsyncAccounts(self)
        self.posts = AsyncPosts(self)
        self.comments = AsyncComments(self)
        self.interactions = AsyncInteractions(self)
        self.dms = AsyncDMs(self)
        self.reviews = AsyncReviews(self)
        self.mentions = AsyncMentions(self)
        self.media = AsyncMedia(self)
        self.usage = AsyncUsage(self)
        self.keys = AsyncKeys(self)
        self.users = AsyncUsers(self)
        self.webhooks = AsyncWebhooks(self)
        self.oauth = AsyncOAuth(self)
        self.feedback = AsyncFeedback(self)

    async def __aenter__(self) -> AsyncSocialAPI:
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: Any,
    ) -> None:
        await self.close()
