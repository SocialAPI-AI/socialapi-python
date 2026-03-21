"""Shared test fixtures."""

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
