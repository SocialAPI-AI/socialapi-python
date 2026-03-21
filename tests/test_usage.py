"""Tests for usage resource."""

from __future__ import annotations

import pytest

from socialapi import AsyncSocialAPI, SocialAPI


@pytest.fixture
def api_key() -> str:
    return "sapi_key_test_0123456789abcdef"


@pytest.fixture
def client(api_key: str) -> SocialAPI:
    return SocialAPI(api_key=api_key, base_url="https://api.social-api.ai")


@pytest.fixture
def async_client(api_key: str) -> AsyncSocialAPI:
    return AsyncSocialAPI(api_key=api_key, base_url="https://api.social-api.ai")


USAGE_DATA = {
    "accounts_used": 3,
    "accounts_limit": 10,
    "posts_used": 42,
    "posts_limit": 100,
    "interactions_used": 150,
    "interactions_limit": 500,
    "period_start": "2025-01-01T00:00:00Z",
    "period_end": "2025-02-01T00:00:00Z",
}


def test_usage_get(httpx_mock, client: SocialAPI) -> None:
    httpx_mock.add_response(
        url="https://api.social-api.ai/v1/usage",
        json=USAGE_DATA,
    )
    result = client.usage.get()
    assert result.accounts_used == 3
    assert result.accounts_limit == 10
    assert result.posts_used == 42
    assert result.interactions_used == 150
    assert result.period_start == "2025-01-01T00:00:00Z"
    assert result.period_end == "2025-02-01T00:00:00Z"


async def test_async_usage_get(httpx_mock, async_client: AsyncSocialAPI) -> None:
    httpx_mock.add_response(
        url="https://api.social-api.ai/v1/usage",
        json=USAGE_DATA,
    )
    result = await async_client.usage.get()
    assert result.accounts_used == 3
    assert result.posts_limit == 100
