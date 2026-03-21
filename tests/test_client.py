"""Tests for client initialization."""

from __future__ import annotations

import pytest

from socialapi import AsyncSocialAPI, SocialAPI
from socialapi.resources.accounts import Accounts, AsyncAccounts
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


def test_creates_with_explicit_api_key() -> None:
    client = SocialAPI(api_key="sapi_key_test_abc123")
    assert client.config.api_key == "sapi_key_test_abc123"
    client.close()


def test_creates_from_env_var(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("SOCIALAPI_API_KEY", "sapi_key_from_env")
    client = SocialAPI()
    assert client.config.api_key == "sapi_key_from_env"
    client.close()


def test_raises_without_api_key(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("SOCIALAPI_API_KEY", raising=False)
    with pytest.raises(ValueError, match="api_key"):
        SocialAPI()


def test_context_manager() -> None:
    with SocialAPI(api_key="sapi_key_test_ctx") as client:
        assert isinstance(client, SocialAPI)


def test_resource_namespaces_initialized() -> None:
    client = SocialAPI(api_key="sapi_key_test_ns")
    assert isinstance(client.accounts, Accounts)
    assert isinstance(client.posts, Posts)
    assert isinstance(client.comments, Comments)
    assert isinstance(client.interactions, Interactions)
    assert isinstance(client.dms, DMs)
    assert isinstance(client.reviews, Reviews)
    assert isinstance(client.mentions, Mentions)
    assert isinstance(client.media, Media)
    assert isinstance(client.usage, Usage)
    assert isinstance(client.keys, Keys)
    assert isinstance(client.users, Users)
    assert isinstance(client.webhooks, Webhooks)
    assert isinstance(client.oauth, OAuth)
    assert isinstance(client.feedback, Feedback)
    client.close()


def test_custom_base_url() -> None:
    client = SocialAPI(api_key="sapi_key_test_url", base_url="https://custom.example.com")
    assert client.config.base_url == "https://custom.example.com"
    client.close()


def test_async_creates_correctly() -> None:
    client = AsyncSocialAPI(api_key="sapi_key_test_async")
    assert client.config.api_key == "sapi_key_test_async"
    assert isinstance(client.accounts, AsyncAccounts)


async def test_async_context_manager() -> None:
    async with AsyncSocialAPI(api_key="sapi_key_test_async_ctx") as client:
        assert isinstance(client, AsyncSocialAPI)


def test_async_raises_without_api_key(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("SOCIALAPI_API_KEY", raising=False)
    with pytest.raises(ValueError, match="api_key"):
        AsyncSocialAPI()
