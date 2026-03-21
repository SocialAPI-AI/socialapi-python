"""Tests for reviews resource."""

from __future__ import annotations

import httpx
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


ACCOUNT_ID = "acc_123"

REVIEW_DATA = {
    "id": "rev_001",
    "platform": "google",
    "type": "review",
    "author": {"id": "user_1", "name": "Bob", "avatar_url": ""},
    "content": {"text": "Great service!", "media": []},
    "metadata": {"rating": 5},
    "created_at": "2025-01-10T08:00:00Z",
    "account_id": ACCOUNT_ID,
    "platform_id": "goog_rev_001",
}


def test_reviews_list(httpx_mock, client: SocialAPI) -> None:
    httpx_mock.add_response(
        url=httpx.URL(
            "https://api.social-api.ai/v1/accounts/acc_123/reviews",
            params={"limit": "50"},
        ),
        json={"data": [REVIEW_DATA], "count": 1},
    )
    result = client.reviews.list(ACCOUNT_ID)
    assert result.count == 1
    assert len(result.data) == 1
    assert result.data[0].id == "rev_001"
    assert result.data[0].type == "review"


async def test_async_reviews_list(httpx_mock, async_client: AsyncSocialAPI) -> None:
    httpx_mock.add_response(
        url=httpx.URL(
            "https://api.social-api.ai/v1/accounts/acc_123/reviews",
            params={"limit": "50"},
        ),
        json={"data": [REVIEW_DATA], "count": 1},
    )
    result = await async_client.reviews.list(ACCOUNT_ID)
    assert result.count == 1
    assert result.data[0].id == "rev_001"
