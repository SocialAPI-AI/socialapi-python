"""Tests for keys resource."""

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


KEY_ITEM = {
    "id": "key_001",
    "name": "Production Key",
    "preview": "sapi_key_...abcd",
    "is_active": True,
    "last_used_at": "2025-01-14T09:30:00Z",
    "created_at": "2025-01-01T00:00:00Z",
}


def test_keys_list(httpx_mock, client: SocialAPI) -> None:
    httpx_mock.add_response(
        url="https://api.social-api.ai/v1/keys",
        json={"data": [KEY_ITEM], "count": 1},
    )
    result = client.keys.list()
    assert result.count == 1
    assert len(result.data) == 1
    assert result.data[0].id == "key_001"
    assert result.data[0].name == "Production Key"
    assert result.data[0].is_active is True


def test_keys_create(httpx_mock, client: SocialAPI) -> None:
    httpx_mock.add_response(
        url="https://api.social-api.ai/v1/keys",
        method="POST",
        json={
            "id": "key_002",
            "name": "Staging Key",
            "raw_key": "sapi_key_live_9876543210fedcba",
            "message": "Store this key securely. It will not be shown again.",
        },
    )
    result = client.keys.create("Staging Key")
    assert result.id == "key_002"
    assert result.name == "Staging Key"
    assert result.raw_key == "sapi_key_live_9876543210fedcba"
    assert "Store" in result.message


def test_keys_revoke(httpx_mock, client: SocialAPI) -> None:
    httpx_mock.add_response(
        url="https://api.social-api.ai/v1/keys/key_001",
        method="DELETE",
        json={"ok": True},
    )
    result = client.keys.revoke("key_001")
    assert result.ok is True


async def test_async_keys_list(httpx_mock, async_client: AsyncSocialAPI) -> None:
    httpx_mock.add_response(
        url="https://api.social-api.ai/v1/keys",
        json={"data": [KEY_ITEM], "count": 1},
    )
    result = await async_client.keys.list()
    assert result.count == 1
    assert result.data[0].id == "key_001"


async def test_async_keys_create(httpx_mock, async_client: AsyncSocialAPI) -> None:
    httpx_mock.add_response(
        url="https://api.social-api.ai/v1/keys",
        method="POST",
        json={
            "id": "key_002",
            "name": "Staging Key",
            "raw_key": "sapi_key_live_9876543210fedcba",
            "message": "Store this key securely.",
        },
    )
    result = await async_client.keys.create("Staging Key")
    assert result.id == "key_002"


async def test_async_keys_revoke(httpx_mock, async_client: AsyncSocialAPI) -> None:
    httpx_mock.add_response(
        url="https://api.social-api.ai/v1/keys/key_001",
        method="DELETE",
        json={"ok": True},
    )
    result = await async_client.keys.revoke("key_001")
    assert result.ok is True
