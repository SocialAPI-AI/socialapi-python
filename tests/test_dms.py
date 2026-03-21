"""Tests for DMs resource."""

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
THREAD_ID = "thread_456"

INTERACTION_DATA = {
    "id": "int_001",
    "platform": "instagram",
    "type": "dm",
    "author": {"id": "user_1", "name": "Alice", "avatar_url": "https://example.com/avatar.png"},
    "content": {"text": "Hello!", "media": []},
    "metadata": {},
    "created_at": "2025-01-15T10:30:00Z",
    "account_id": ACCOUNT_ID,
    "platform_id": "ig_dm_001",
}


def test_dms_list(httpx_mock, client: SocialAPI) -> None:
    httpx_mock.add_response(
        url=httpx.URL(
            "https://api.social-api.ai/v1/accounts/acc_123/dms",
            params={"limit": "50"},
        ),
        json={"data": [INTERACTION_DATA], "count": 1},
    )
    result = client.dms.list(ACCOUNT_ID)
    assert result.count == 1
    assert len(result.data) == 1
    assert result.data[0].id == "int_001"
    assert result.data[0].type == "dm"


def test_dms_send(httpx_mock, client: SocialAPI) -> None:
    httpx_mock.add_response(
        url="https://api.social-api.ai/v1/accounts/acc_123/dms/thread_456/send",
        method="POST",
        json={"id": "reply_789", "created_at": "2025-01-15T11:00:00Z"},
    )
    result = client.dms.send(ACCOUNT_ID, THREAD_ID, "Hi there!")
    assert result.id == "reply_789"
    assert result.created_at == "2025-01-15T11:00:00Z"


def test_dms_thread(httpx_mock, client: SocialAPI) -> None:
    httpx_mock.add_response(
        url=httpx.URL(
            "https://api.social-api.ai/v1/accounts/acc_123/dms/thread",
            params={"user_id": "user_42"},
        ),
        json={"thread_id": "thread_new_001"},
    )
    result = client.dms.thread(ACCOUNT_ID, "user_42")
    assert result.thread_id == "thread_new_001"


async def test_async_dms_list(httpx_mock, async_client: AsyncSocialAPI) -> None:
    httpx_mock.add_response(
        url=httpx.URL(
            "https://api.social-api.ai/v1/accounts/acc_123/dms",
            params={"limit": "50"},
        ),
        json={"data": [INTERACTION_DATA], "count": 1},
    )
    result = await async_client.dms.list(ACCOUNT_ID)
    assert result.count == 1
    assert result.data[0].id == "int_001"


async def test_async_dms_send(httpx_mock, async_client: AsyncSocialAPI) -> None:
    httpx_mock.add_response(
        url="https://api.social-api.ai/v1/accounts/acc_123/dms/thread_456/send",
        method="POST",
        json={"id": "reply_789", "created_at": "2025-01-15T11:00:00Z"},
    )
    result = await async_client.dms.send(ACCOUNT_ID, THREAD_ID, "Hi there!")
    assert result.id == "reply_789"


async def test_async_dms_thread(httpx_mock, async_client: AsyncSocialAPI) -> None:
    httpx_mock.add_response(
        url=httpx.URL(
            "https://api.social-api.ai/v1/accounts/acc_123/dms/thread",
            params={"user_id": "user_42"},
        ),
        json={"thread_id": "thread_new_001"},
    )
    result = await async_client.dms.thread(ACCOUNT_ID, "user_42")
    assert result.thread_id == "thread_new_001"
