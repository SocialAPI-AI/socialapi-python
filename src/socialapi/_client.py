"""Synchronous SocialAPI client."""

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any

from socialapi._base_client import SyncAPIClient
from socialapi._config import ClientConfig
from socialapi._constants import DEFAULT_BASE_URL, DEFAULT_MAX_RETRIES, DEFAULT_TIMEOUT
from socialapi.resources.accounts import Accounts
from socialapi.resources.comments import Comments
from socialapi.resources.dms import DMs
from socialapi.resources.feedback import Feedback
from socialapi.resources.interactions import Interactions
from socialapi.resources.keys import Keys
from socialapi.resources.media import Media
from socialapi.resources.mentions import Mentions
from socialapi.resources.oauth import OAuth
from socialapi.resources.posts import Posts
from socialapi.resources.reviews import Reviews
from socialapi.resources.usage import Usage
from socialapi.resources.users import Users
from socialapi.resources.webhooks import Webhooks

if TYPE_CHECKING:
    import httpx


class SocialAPI(SyncAPIClient):
    """Synchronous client for the SocialAPI.

    Usage::

        client = SocialAPI(api_key="sapi_key_...")
        accounts = client.accounts.list()

    Or as a context manager::

        with SocialAPI(api_key="sapi_key_...") as client:
            accounts = client.accounts.list()

    Args:
        api_key: API key for authentication. Falls back to the
            ``SOCIALAPI_API_KEY`` environment variable if not provided.
        base_url: Override the default API base URL.
        timeout: Request timeout in seconds.
        max_retries: Maximum number of retries for failed requests.
        http_client: Optional custom httpx.Client instance.
    """

    accounts: Accounts
    posts: Posts
    comments: Comments
    interactions: Interactions
    dms: DMs
    reviews: Reviews
    mentions: Mentions
    media: Media
    usage: Usage
    keys: Keys
    users: Users
    webhooks: Webhooks
    oauth: OAuth
    feedback: Feedback

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str = DEFAULT_BASE_URL,
        timeout: float = DEFAULT_TIMEOUT,
        max_retries: int = DEFAULT_MAX_RETRIES,
        http_client: httpx.Client | None = None,
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
        self.accounts = Accounts(self)
        self.posts = Posts(self)
        self.comments = Comments(self)
        self.interactions = Interactions(self)
        self.dms = DMs(self)
        self.reviews = Reviews(self)
        self.mentions = Mentions(self)
        self.media = Media(self)
        self.usage = Usage(self)
        self.keys = Keys(self)
        self.users = Users(self)
        self.webhooks = Webhooks(self)
        self.oauth = OAuth(self)
        self.feedback = Feedback(self)

    def __enter__(self) -> SocialAPI:
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: Any,
    ) -> None:
        self.close()
