from __future__ import annotations

import os
from typing import TYPE_CHECKING

from socialapi._base_client import BaseAsyncClient, BaseSyncClient
from socialapi._config import ClientConfig
from socialapi._constants import (
    API_KEY_ENV_VAR,
    BASE_URL_ENV_VAR,
    DEFAULT_BASE_URL,
    DEFAULT_MAX_RETRIES,
    DEFAULT_TIMEOUT,
)
from socialapi._exceptions import SocialAPIError

if TYPE_CHECKING:
    from types import TracebackType

    import httpx

    from socialapi.resources.accounts import Accounts, AsyncAccounts
    from socialapi.resources.brands import AsyncBrands, Brands
    from socialapi.resources.comments import AsyncComments, Comments
    from socialapi.resources.conversations import AsyncConversations, Conversations
    from socialapi.resources.events import AsyncEvents, Events
    from socialapi.resources.feedback import AsyncFeedback, Feedback
    from socialapi.resources.invites import AsyncInvites, Invites
    from socialapi.resources.keys import AsyncKeys, Keys
    from socialapi.resources.media import AsyncMedia, Media
    from socialapi.resources.mentions import AsyncMentions, Mentions
    from socialapi.resources.posts import AsyncPosts, Posts
    from socialapi.resources.publishing import AsyncPublishing, Publishing
    from socialapi.resources.reviews import AsyncReviews, Reviews
    from socialapi.resources.usage import AsyncUsage, Usage
    from socialapi.resources.users import AsyncUsers, Users
    from socialapi.resources.webhooks import AsyncWebhooks, Webhooks


def _resolve_api_key(api_key: str | None) -> str:
    """Resolve the API key from the argument or environment variable.

    Raises:
        SocialAPIError: If no API key can be found.
    """
    if api_key is not None:
        return api_key
    env_key = os.environ.get(API_KEY_ENV_VAR)
    if env_key:
        return env_key
    msg = f"No API key provided. Pass api_key to the constructor or set the {API_KEY_ENV_VAR} environment variable."
    raise SocialAPIError(msg)


def _resolve_base_url(base_url: str | None) -> str:
    """Resolve the base URL from the argument or environment variable."""
    if base_url is not None:
        return base_url.rstrip("/")
    env_url = os.environ.get(BASE_URL_ENV_VAR)
    if env_url:
        return env_url.rstrip("/")
    return DEFAULT_BASE_URL


class SocialAPI:
    """Synchronous SocialAPI client.

    Usage::

        from socialapi import SocialAPI

        client = SocialAPI(api_key="sapi_key_...")
        accounts = client.accounts.list()

    The client can be used as a context manager::

        with SocialAPI(api_key="sapi_key_...") as client:
            accounts = client.accounts.list()
    """

    _client: BaseSyncClient

    # Resource namespaces (set in __init__)
    accounts: Accounts
    brands: Brands
    comments: Comments
    conversations: Conversations
    events: Events
    feedback: Feedback
    invites: Invites
    keys: Keys
    media: Media
    mentions: Mentions
    posts: Posts
    publishing: Publishing
    reviews: Reviews
    usage: Usage
    users: Users
    webhooks: Webhooks

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | None = None,
        timeout: float = DEFAULT_TIMEOUT,
        max_retries: int = DEFAULT_MAX_RETRIES,
        debug: bool = False,
        http_client: httpx.Client | None = None,
    ) -> None:
        """Create a new synchronous SocialAPI client.

        Args:
            api_key: Bearer token for authentication. Falls back to the
                ``SOCIALAPI_API_KEY`` environment variable if not provided.
            base_url: API root URL. Falls back to ``SOCIALAPI_BASE_URL`` env var.
            timeout: Request timeout in seconds.
            max_retries: Maximum automatic retries for transient failures.
            debug: Enable debug logging of requests and responses.
            http_client: Optional pre-configured ``httpx.Client`` instance.

        Raises:
            SocialAPIError: If no API key is found.
        """
        resolved_key = _resolve_api_key(api_key)
        resolved_url = _resolve_base_url(base_url)

        config = ClientConfig(
            api_key=resolved_key,
            base_url=resolved_url,
            timeout=timeout,
            max_retries=max_retries,
            debug=debug,
        )
        self._client = BaseSyncClient(config, http_client=http_client)

        # Lazy import to avoid circular imports at module level
        from socialapi.resources.accounts import Accounts as _Accounts
        from socialapi.resources.brands import Brands as _Brands
        from socialapi.resources.comments import Comments as _Comments
        from socialapi.resources.conversations import Conversations as _Conversations
        from socialapi.resources.events import Events as _Events
        from socialapi.resources.feedback import Feedback as _Feedback
        from socialapi.resources.invites import Invites as _Invites
        from socialapi.resources.keys import Keys as _Keys
        from socialapi.resources.media import Media as _Media
        from socialapi.resources.mentions import Mentions as _Mentions
        from socialapi.resources.posts import Posts as _Posts
        from socialapi.resources.publishing import Publishing as _Publishing
        from socialapi.resources.reviews import Reviews as _Reviews
        from socialapi.resources.usage import Usage as _Usage
        from socialapi.resources.users import Users as _Users
        from socialapi.resources.webhooks import Webhooks as _Webhooks

        self.accounts = _Accounts(self._client)
        self.brands = _Brands(self._client)
        self.comments = _Comments(self._client)
        self.conversations = _Conversations(self._client)
        self.events = _Events(self._client)
        self.feedback = _Feedback(self._client)
        self.invites = _Invites(self._client)
        self.keys = _Keys(self._client)
        self.media = _Media(self._client)
        self.mentions = _Mentions(self._client)
        self.posts = _Posts(self._client)
        self.publishing = _Publishing(self._client)
        self.reviews = _Reviews(self._client)
        self.usage = _Usage(self._client)
        self.users = _Users(self._client)
        self.webhooks = _Webhooks(self._client)

    def with_options(
        self,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> SocialAPI:
        """Return a new client with overridden options.

        The returned client shares no state with the original except the
        underlying ``httpx.Client`` transport.

        Args:
            timeout: Override request timeout in seconds.
            max_retries: Override maximum retries.

        Returns:
            A new ``SocialAPI`` instance with the specified overrides.
        """
        return SocialAPI(
            api_key=self._client._config.api_key,
            base_url=self._client._config.base_url,
            timeout=timeout if timeout is not None else self._client._config.timeout,
            max_retries=max_retries if max_retries is not None else self._client._config.max_retries,
            debug=self._client._config.debug,
        )

    def close(self) -> None:
        """Release the underlying HTTP transport resources."""
        self._client.close()

    def __enter__(self) -> SocialAPI:
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        self.close()


class AsyncSocialAPI:
    """Asynchronous SocialAPI client.

    Usage::

        from socialapi import AsyncSocialAPI

        client = AsyncSocialAPI(api_key="sapi_key_...")
        accounts = await client.accounts.list()

    The client can be used as an async context manager::

        async with AsyncSocialAPI(api_key="sapi_key_...") as client:
            accounts = await client.accounts.list()
    """

    _client: BaseAsyncClient

    # Resource namespaces (set in __init__)
    accounts: AsyncAccounts
    brands: AsyncBrands
    comments: AsyncComments
    conversations: AsyncConversations
    events: AsyncEvents
    feedback: AsyncFeedback
    invites: AsyncInvites
    keys: AsyncKeys
    media: AsyncMedia
    mentions: AsyncMentions
    posts: AsyncPosts
    publishing: AsyncPublishing
    reviews: AsyncReviews
    usage: AsyncUsage
    users: AsyncUsers
    webhooks: AsyncWebhooks

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | None = None,
        timeout: float = DEFAULT_TIMEOUT,
        max_retries: int = DEFAULT_MAX_RETRIES,
        debug: bool = False,
        http_client: httpx.AsyncClient | None = None,
    ) -> None:
        """Create a new asynchronous SocialAPI client.

        Args:
            api_key: Bearer token for authentication. Falls back to the
                ``SOCIALAPI_API_KEY`` environment variable if not provided.
            base_url: API root URL. Falls back to ``SOCIALAPI_BASE_URL`` env var.
            timeout: Request timeout in seconds.
            max_retries: Maximum automatic retries for transient failures.
            debug: Enable debug logging of requests and responses.
            http_client: Optional pre-configured ``httpx.AsyncClient`` instance.

        Raises:
            SocialAPIError: If no API key is found.
        """
        resolved_key = _resolve_api_key(api_key)
        resolved_url = _resolve_base_url(base_url)

        config = ClientConfig(
            api_key=resolved_key,
            base_url=resolved_url,
            timeout=timeout,
            max_retries=max_retries,
            debug=debug,
        )
        self._client = BaseAsyncClient(config, http_client=http_client)

        # Lazy import to avoid circular imports at module level
        from socialapi.resources.accounts import AsyncAccounts as _AsyncAccounts
        from socialapi.resources.brands import AsyncBrands as _AsyncBrands
        from socialapi.resources.comments import AsyncComments as _AsyncComments
        from socialapi.resources.conversations import AsyncConversations as _AsyncConversations
        from socialapi.resources.events import AsyncEvents as _AsyncEvents
        from socialapi.resources.feedback import AsyncFeedback as _AsyncFeedback
        from socialapi.resources.invites import AsyncInvites as _AsyncInvites
        from socialapi.resources.keys import AsyncKeys as _AsyncKeys
        from socialapi.resources.media import AsyncMedia as _AsyncMedia
        from socialapi.resources.mentions import AsyncMentions as _AsyncMentions
        from socialapi.resources.posts import AsyncPosts as _AsyncPosts
        from socialapi.resources.publishing import AsyncPublishing as _AsyncPublishing
        from socialapi.resources.reviews import AsyncReviews as _AsyncReviews
        from socialapi.resources.usage import AsyncUsage as _AsyncUsage
        from socialapi.resources.users import AsyncUsers as _AsyncUsers
        from socialapi.resources.webhooks import AsyncWebhooks as _AsyncWebhooks

        self.accounts = _AsyncAccounts(self._client)
        self.brands = _AsyncBrands(self._client)
        self.comments = _AsyncComments(self._client)
        self.conversations = _AsyncConversations(self._client)
        self.events = _AsyncEvents(self._client)
        self.feedback = _AsyncFeedback(self._client)
        self.invites = _AsyncInvites(self._client)
        self.keys = _AsyncKeys(self._client)
        self.media = _AsyncMedia(self._client)
        self.mentions = _AsyncMentions(self._client)
        self.posts = _AsyncPosts(self._client)
        self.publishing = _AsyncPublishing(self._client)
        self.reviews = _AsyncReviews(self._client)
        self.usage = _AsyncUsage(self._client)
        self.users = _AsyncUsers(self._client)
        self.webhooks = _AsyncWebhooks(self._client)

    def with_options(
        self,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> AsyncSocialAPI:
        """Return a new client with overridden options.

        The returned client shares no state with the original except the
        underlying ``httpx.AsyncClient`` transport.

        Args:
            timeout: Override request timeout in seconds.
            max_retries: Override maximum retries.

        Returns:
            A new ``AsyncSocialAPI`` instance with the specified overrides.
        """
        return AsyncSocialAPI(
            api_key=self._client._config.api_key,
            base_url=self._client._config.base_url,
            timeout=timeout if timeout is not None else self._client._config.timeout,
            max_retries=max_retries if max_retries is not None else self._client._config.max_retries,
            debug=self._client._config.debug,
        )

    async def close(self) -> None:
        """Release the underlying HTTP transport resources."""
        await self._client.close()

    async def __aenter__(self) -> AsyncSocialAPI:
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        await self.close()
