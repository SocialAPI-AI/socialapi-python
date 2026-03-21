"""Tests for mentions resource."""

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

MENTION_DATA = {
    "id": "men_001",
    "platform": "instagram",
    "type": "mention",
    "author": {"id": "user_5", "name": "Charlie", "avatar_url": ""},
    "content": {"text": "@myaccount check this out", "media": []},
    "metadata": {},
    "created_at": "2025-01-12T14:00:00Z",
    "account_id": ACCOUNT_ID,
    "platform_id": "ig_men_001",
}


def test_mentions_list(httpx_mock, client: SocialAPI) -> None:
    httpx_mock.add_response(
        url=httpx.URL(
            "https://api.social-api.ai/v1/accounts/acc_123/mentions",
            params={"limit": "50"},
        ),
        json={"data": [MENTION_DATA], "count": 1},
    )
    result = client.mentions.list(ACCOUNT_ID)
    assert result.count == 1
    assert len(result.data) == 1
    assert result.data[0].id == "men_001"
    assert result.data[0].type == "mention"


async def test_async_mentions_list(httpx_mock, async_client: AsyncSocialAPI) -> None:
    httpx_mock.add_response(
        url=httpx.URL(
            "https://api.social-api.ai/v1/accounts/acc_123/mentions",
            params={"limit": "50"},
        ),
        json={"data": [MENTION_DATA], "count": 1},
    )
    result = await async_client.mentions.list(ACCOUNT_ID)
    assert result.count == 1
    assert result.data[0].id == "men_001"
