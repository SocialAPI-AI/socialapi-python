"""Tests for users resource."""

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


USER_DATA = {
    "id": "usr_001",
    "email": "alice@example.com",
    "plan": "pro",
    "onboarding": True,
    "avatar_url": "https://example.com/avatar.png",
    "beta_tester": False,
}


def test_users_me(httpx_mock, client: SocialAPI) -> None:
    httpx_mock.add_response(
        url="https://api.social-api.ai/v1/users/me",
        json=USER_DATA,
    )
    result = client.users.me()
    assert result.id == "usr_001"
    assert result.email == "alice@example.com"
    assert result.plan == "pro"
    assert result.onboarding is True
    assert result.avatar_url == "https://example.com/avatar.png"
    assert result.beta_tester is False


def test_users_update(httpx_mock, client: SocialAPI) -> None:
    updated = {**USER_DATA, "onboarding": False}
    httpx_mock.add_response(
        url="https://api.social-api.ai/v1/users/me",
        method="PATCH",
        json=updated,
    )
    result = client.users.update(onboarding=False)
    assert result.onboarding is False
    assert result.id == "usr_001"


def test_users_delete(httpx_mock, client: SocialAPI) -> None:
    httpx_mock.add_response(
        url="https://api.social-api.ai/v1/users/me",
        method="DELETE",
        json={"ok": True},
    )
    result = client.users.delete()
    assert result.ok is True


async def test_async_users_me(httpx_mock, async_client: AsyncSocialAPI) -> None:
    httpx_mock.add_response(
        url="https://api.social-api.ai/v1/users/me",
        json=USER_DATA,
    )
    result = await async_client.users.me()
    assert result.id == "usr_001"
    assert result.email == "alice@example.com"


async def test_async_users_update(httpx_mock, async_client: AsyncSocialAPI) -> None:
    updated = {**USER_DATA, "onboarding": False}
    httpx_mock.add_response(
        url="https://api.social-api.ai/v1/users/me",
        method="PATCH",
        json=updated,
    )
    result = await async_client.users.update(onboarding=False)
    assert result.onboarding is False


async def test_async_users_delete(httpx_mock, async_client: AsyncSocialAPI) -> None:
    httpx_mock.add_response(
        url="https://api.social-api.ai/v1/users/me",
        method="DELETE",
        json={"ok": True},
    )
    result = await async_client.users.delete()
    assert result.ok is True
