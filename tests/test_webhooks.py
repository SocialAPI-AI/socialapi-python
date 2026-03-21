"""Tests for webhooks resource."""

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


WEBHOOK_DATA = {
    "id": "wh_001",
    "url": "https://example.com/webhook",
    "events": ["interaction.created", "post.published"],
    "is_active": True,
    "created_at": "2025-01-01T00:00:00Z",
}


def test_webhooks_list(httpx_mock, client: SocialAPI) -> None:
    httpx_mock.add_response(
        url="https://api.social-api.ai/v1/webhooks",
        json={"data": [WEBHOOK_DATA], "count": 1},
    )
    result = client.webhooks.list()
    assert result.count == 1
    assert len(result.data) == 1
    assert result.data[0].id == "wh_001"
    assert result.data[0].url == "https://example.com/webhook"
    assert result.data[0].is_active is True
    assert "interaction.created" in result.data[0].events


def test_webhooks_create(httpx_mock, client: SocialAPI) -> None:
    httpx_mock.add_response(
        url="https://api.social-api.ai/v1/webhooks",
        method="POST",
        json={
            "id": "wh_002",
            "url": "https://example.com/new-webhook",
            "events": ["interaction.created"],
            "secret": "whsec_abc123def456",
            "message": "Webhook endpoint created.",
        },
    )
    result = client.webhooks.create(
        "https://example.com/new-webhook",
        ["interaction.created"],
    )
    assert result.id == "wh_002"
    assert result.secret == "whsec_abc123def456"
    assert result.url == "https://example.com/new-webhook"


def test_webhooks_update(httpx_mock, client: SocialAPI) -> None:
    updated = {**WEBHOOK_DATA, "url": "https://example.com/updated-webhook"}
    httpx_mock.add_response(
        url="https://api.social-api.ai/v1/webhooks/wh_001",
        method="PATCH",
        json=updated,
    )
    result = client.webhooks.update("wh_001", url="https://example.com/updated-webhook")
    assert result.url == "https://example.com/updated-webhook"
    assert result.id == "wh_001"


def test_webhooks_delete(httpx_mock, client: SocialAPI) -> None:
    httpx_mock.add_response(
        url="https://api.social-api.ai/v1/webhooks/wh_001",
        method="DELETE",
        json={"ok": True},
    )
    result = client.webhooks.delete("wh_001")
    assert result.ok is True


async def test_async_webhooks_list(httpx_mock, async_client: AsyncSocialAPI) -> None:
    httpx_mock.add_response(
        url="https://api.social-api.ai/v1/webhooks",
        json={"data": [WEBHOOK_DATA], "count": 1},
    )
    result = await async_client.webhooks.list()
    assert result.count == 1
    assert result.data[0].id == "wh_001"


async def test_async_webhooks_create(httpx_mock, async_client: AsyncSocialAPI) -> None:
    httpx_mock.add_response(
        url="https://api.social-api.ai/v1/webhooks",
        method="POST",
        json={
            "id": "wh_002",
            "url": "https://example.com/new-webhook",
            "events": ["interaction.created"],
            "secret": "whsec_abc123def456",
            "message": "Webhook endpoint created.",
        },
    )
    result = await async_client.webhooks.create(
        "https://example.com/new-webhook",
        ["interaction.created"],
    )
    assert result.id == "wh_002"
    assert result.secret == "whsec_abc123def456"


async def test_async_webhooks_update(httpx_mock, async_client: AsyncSocialAPI) -> None:
    updated = {**WEBHOOK_DATA, "is_active": False}
    httpx_mock.add_response(
        url="https://api.social-api.ai/v1/webhooks/wh_001",
        method="PATCH",
        json=updated,
    )
    result = await async_client.webhooks.update("wh_001", is_active=False)
    assert result.is_active is False


async def test_async_webhooks_delete(httpx_mock, async_client: AsyncSocialAPI) -> None:
    httpx_mock.add_response(
        url="https://api.social-api.ai/v1/webhooks/wh_001",
        method="DELETE",
        json={"ok": True},
    )
    result = await async_client.webhooks.delete("wh_001")
    assert result.ok is True
