"""Tests for accounts resource."""

from __future__ import annotations

import pytest

from socialapi import AsyncSocialAPI, AuthenticationError, SocialAPI
from socialapi.models.accounts import AccountsListResponse, ConnectResponse
from socialapi.models.posts import PlatformPostsListResponse

BASE = "https://api.social-api.ai"

ACCOUNT_DATA = {
    "id": "acc_123",
    "platform": "instagram",
    "name": "Test Account",
    "username": "testuser",
    "metadata": {},
}


def test_accounts_list(httpx_mock, client: SocialAPI) -> None:
    httpx_mock.add_response(
        url=f"{BASE}/v1/accounts",
        json={"data": [ACCOUNT_DATA], "count": 1},
    )
    result = client.accounts.list()
    assert isinstance(result, AccountsListResponse)
    assert len(result.data) == 1
    assert result.data[0].id == "acc_123"
    assert result.count == 1


def test_accounts_connect(httpx_mock, client: SocialAPI) -> None:
    httpx_mock.add_response(
        url=f"{BASE}/v1/accounts/connect",
        json={
            "account_id": "acc_new",
            "platform": "facebook",
            "username": "fbuser",
        },
    )
    result = client.accounts.connect("facebook", {"access_token": "tok_abc"})
    assert isinstance(result, ConnectResponse)
    assert result.account_id == "acc_new"
    assert result.platform == "facebook"


def test_accounts_disconnect(httpx_mock, client: SocialAPI) -> None:
    httpx_mock.add_response(
        url=f"{BASE}/v1/accounts/acc_123",
        status_code=204,
    )
    result = client.accounts.disconnect("acc_123")
    assert result is None


def test_accounts_posts(httpx_mock, client: SocialAPI) -> None:
    httpx_mock.add_response(
        url=f"{BASE}/v1/accounts/acc_123/posts?limit=50",
        json={
            "data": [
                {
                    "id": "post_1",
                    "platform": "instagram",
                    "caption": "Hello",
                    "permalink": "https://instagram.com/p/123",
                    "timestamp": "2025-01-01T00:00:00Z",
                    "like_count": 10,
                    "comments_count": 2,
                    "account_id": "acc_123",
                }
            ],
            "count": 1,
        },
    )
    result = client.accounts.posts("acc_123")
    assert isinstance(result, PlatformPostsListResponse)
    assert len(result.data) == 1
    assert result.data[0].id == "post_1"


def test_accounts_limits(httpx_mock, client: SocialAPI) -> None:
    httpx_mock.add_response(
        url=f"{BASE}/v1/accounts/acc_123/limits",
        json={"posts": 100, "interactions": 500},
    )
    result = client.accounts.limits("acc_123")
    assert result == {"posts": 100, "interactions": 500}


def test_accounts_list_unauthorized(httpx_mock, client: SocialAPI) -> None:
    httpx_mock.add_response(
        url=f"{BASE}/v1/accounts",
        status_code=401,
        json={"error": "invalid API key", "code": "unauthorized"},
    )
    with pytest.raises(AuthenticationError) as exc_info:
        client.accounts.list()
    assert exc_info.value.code == "unauthorized"


# -- Async tests --


async def test_async_accounts_list(httpx_mock, async_client: AsyncSocialAPI) -> None:
    httpx_mock.add_response(
        url=f"{BASE}/v1/accounts",
        json={"data": [ACCOUNT_DATA], "count": 1},
    )
    result = await async_client.accounts.list()
    assert isinstance(result, AccountsListResponse)
    assert len(result.data) == 1


async def test_async_accounts_disconnect(httpx_mock, async_client: AsyncSocialAPI) -> None:
    httpx_mock.add_response(
        url=f"{BASE}/v1/accounts/acc_123",
        status_code=204,
    )
    result = await async_client.accounts.disconnect("acc_123")
    assert result is None
