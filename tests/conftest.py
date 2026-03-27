from __future__ import annotations

import pytest

from socialapi import AsyncSocialAPI, SocialAPI

BASE_URL = "https://api.test.local"
TEST_API_KEY = "sapi_key_test_000000000000000000"


@pytest.fixture
def client() -> SocialAPI:
    """Sync client configured for testing with httpx_mock interception."""
    return SocialAPI(api_key=TEST_API_KEY, base_url=BASE_URL, max_retries=0)


@pytest.fixture
def async_client() -> AsyncSocialAPI:
    """Async client configured for testing with httpx_mock interception."""
    return AsyncSocialAPI(api_key=TEST_API_KEY, base_url=BASE_URL, max_retries=0)
