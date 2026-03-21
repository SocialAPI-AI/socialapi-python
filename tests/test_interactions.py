"""Tests for interactions resource."""

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


ACCOUNT_ID = "acc_123"
INTERACTION_ID = "int_456"


def test_interactions_reply(httpx_mock, client: SocialAPI) -> None:
    httpx_mock.add_response(
        url="https://api.social-api.ai/v1/accounts/acc_123/interactions/int_456/reply",
        method="POST",
        json={"id": "reply_001", "created_at": "2025-01-15T12:00:00Z"},
    )
    result = client.interactions.reply(ACCOUNT_ID, INTERACTION_ID, "Thanks for the feedback!")
    assert result.id == "reply_001"
    assert result.created_at == "2025-01-15T12:00:00Z"


async def test_async_interactions_reply(httpx_mock, async_client: AsyncSocialAPI) -> None:
    httpx_mock.add_response(
        url="https://api.social-api.ai/v1/accounts/acc_123/interactions/int_456/reply",
        method="POST",
        json={"id": "reply_001", "created_at": "2025-01-15T12:00:00Z"},
    )
    result = await async_client.interactions.reply(ACCOUNT_ID, INTERACTION_ID, "Thanks!")
    assert result.id == "reply_001"
