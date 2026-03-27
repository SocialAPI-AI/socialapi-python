from __future__ import annotations

import pytest

from socialapi import AsyncSocialAPI, SocialAPI
from socialapi._constants import DEFAULT_BASE_URL
from socialapi._exceptions import SocialAPIError
from socialapi._version import __version__

from .conftest import BASE_URL, TEST_API_KEY


def test_client_init_with_api_key() -> None:
    c = SocialAPI(api_key=TEST_API_KEY)
    assert c._client.api_key == TEST_API_KEY
    c.close()


def test_client_init_from_env_var(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("SOCIALAPI_API_KEY", "sapi_key_env_var_test")
    c = SocialAPI()
    assert c._client.api_key == "sapi_key_env_var_test"
    c.close()


def test_client_init_missing_key_raises(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("SOCIALAPI_API_KEY", raising=False)
    with pytest.raises(SocialAPIError, match="No API key provided"):
        SocialAPI()


def test_client_default_base_url() -> None:
    c = SocialAPI(api_key=TEST_API_KEY)
    assert c._client.base_url == DEFAULT_BASE_URL
    c.close()


def test_client_custom_base_url() -> None:
    c = SocialAPI(api_key=TEST_API_KEY, base_url="https://custom.local/")
    assert c._client.base_url == "https://custom.local"
    c.close()


def test_client_context_manager() -> None:
    with SocialAPI(api_key=TEST_API_KEY) as c:
        assert c._client.api_key == TEST_API_KEY


async def test_async_client_context_manager() -> None:
    async with AsyncSocialAPI(api_key=TEST_API_KEY) as c:
        assert c._client.api_key == TEST_API_KEY


def test_client_has_all_resources() -> None:
    c = SocialAPI(api_key=TEST_API_KEY)
    resource_names = [
        "accounts",
        "comments",
        "conversations",
        "feedback",
        "keys",
        "mentions",
        "posts",
        "publishing",
        "reviews",
        "usage",
        "users",
        "webhooks",
    ]
    for name in resource_names:
        assert hasattr(c, name), f"Client missing resource: {name}"
    c.close()


def test_client_user_agent_header() -> None:
    c = SocialAPI(api_key=TEST_API_KEY)
    headers = c._client._build_headers()
    assert headers["User-Agent"] == f"socialapi-python/{__version__}"
    c.close()


def test_client_close(httpx_mock) -> None:
    c = SocialAPI(api_key=TEST_API_KEY, base_url=BASE_URL)
    c.close()
    # After close, calling close again should not error
    c.close()


def test_client_debug_logging(httpx_mock) -> None:
    """Debug mode should log request and response details."""
    import logging

    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/users/me",
        json={"id": "usr_1", "email": "a@b.com", "plan": "free"},
    )
    c = SocialAPI(api_key=TEST_API_KEY, base_url=BASE_URL, max_retries=0, debug=True)
    logger = logging.getLogger("socialapi")
    logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    try:
        user = c.users.get_me()
        assert user.id == "usr_1"
    finally:
        logger.removeHandler(handler)
    c.close()


async def test_async_client_debug_logging(httpx_mock) -> None:
    """Async debug mode should log request and response details."""
    import logging

    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/users/me",
        json={"id": "usr_1", "email": "a@b.com", "plan": "free"},
    )
    c = AsyncSocialAPI(api_key=TEST_API_KEY, base_url=BASE_URL, max_retries=0, debug=True)
    logger = logging.getLogger("socialapi")
    logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    try:
        user = await c.users.get_me()
        assert user.id == "usr_1"
    finally:
        logger.removeHandler(handler)
    await c.close()


def test_client_with_options() -> None:
    """with_options returns a new client with overridden settings."""
    c = SocialAPI(api_key=TEST_API_KEY, base_url=BASE_URL, timeout=10.0, max_retries=0)
    c2 = c.with_options(timeout=30.0, max_retries=5)
    assert c2._client._config.timeout == 30.0
    assert c2._client._config.max_retries == 5
    # Original unchanged
    assert c._client._config.timeout == 10.0
    assert c._client._config.max_retries == 0
    c.close()
    c2.close()


async def test_async_client_with_options() -> None:
    """Async with_options returns a new client with overridden settings."""
    c = AsyncSocialAPI(api_key=TEST_API_KEY, base_url=BASE_URL, timeout=10.0, max_retries=0)
    c2 = c.with_options(timeout=20.0, max_retries=3)
    assert c2._client._config.timeout == 20.0
    assert c2._client._config.max_retries == 3
    await c.close()
    await c2.close()


def test_client_base_url_from_env(monkeypatch: pytest.MonkeyPatch) -> None:
    """Base URL can be set via env var."""
    monkeypatch.setenv("SOCIALAPI_BASE_URL", "https://custom-env.local/api/")
    c = SocialAPI(api_key=TEST_API_KEY)
    assert c._client.base_url == "https://custom-env.local/api"
    c.close()


def test_build_query_params_edge_cases() -> None:
    """Test _build_query_params with booleans, lists, and None values."""
    from socialapi._base_client import _build_query_params

    # Empty/None
    assert _build_query_params(None) == {}
    assert _build_query_params({}) == {}

    # Booleans
    result = _build_query_params({"hidden": True, "active": False})
    assert result == {"hidden": "true", "active": "false"}

    # Lists
    result = _build_query_params({"account_ids": ["a1", "a2", "a3"]})
    assert result == {"account_ids": "a1,a2,a3"}

    # None values dropped
    result = _build_query_params({"key": "val", "empty": None})
    assert result == {"key": "val"}

    # Mixed types
    result = _build_query_params({"limit": 10, "flag": True, "ids": ["x", "y"]})
    assert result == {"limit": "10", "flag": "true", "ids": "x,y"}


def test_calculate_retry_delay_non_numeric_header() -> None:
    """Non-numeric Retry-After header should fall through to backoff."""
    import httpx

    from socialapi._base_client import _calculate_retry_delay

    response = httpx.Response(
        status_code=429,
        headers={"retry-after": "not-a-number"},
        request=httpx.Request("GET", "https://test.local/v1/test"),
    )
    delay = _calculate_retry_delay(0, response)
    # Should use backoff, not retry-after
    assert delay >= 0
    assert delay <= 0.5  # max for retries_taken=0 is 0.5


def test_sync_client_custom_http_client() -> None:
    """Sync client should accept a custom httpx.Client."""
    import httpx

    custom = httpx.Client(timeout=httpx.Timeout(99.0))
    c = SocialAPI(api_key=TEST_API_KEY, base_url=BASE_URL, http_client=custom)
    assert c._client._client is custom
    c.close()


async def test_async_client_custom_http_client() -> None:
    """Async client should accept a custom httpx.AsyncClient."""
    import httpx

    custom = httpx.AsyncClient(timeout=httpx.Timeout(99.0))
    c = AsyncSocialAPI(api_key=TEST_API_KEY, base_url=BASE_URL, http_client=custom)
    assert c._client._client is custom
    await c.close()


async def test_async_client_properties() -> None:
    """Async client base_url and api_key properties should work."""
    c = AsyncSocialAPI(api_key=TEST_API_KEY, base_url=BASE_URL)
    assert c._client.base_url == BASE_URL
    assert c._client.api_key == TEST_API_KEY
    await c.close()


async def test_async_put_204_response(httpx_mock) -> None:
    """Async PUT returning 204 should return None."""
    c = AsyncSocialAPI(api_key=TEST_API_KEY, base_url=BASE_URL, max_retries=0)
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/test/put",
        status_code=204,
        method="PUT",
    )
    result = await c._client._put("/v1/test/put", json={"data": "value"})
    assert result is None
    await c.close()


async def test_async_patch_204_response(httpx_mock) -> None:
    """Async PATCH returning 204 should return None."""
    c = AsyncSocialAPI(api_key=TEST_API_KEY, base_url=BASE_URL, max_retries=0)
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/test/patch",
        status_code=204,
        method="PATCH",
    )
    result = await c._client._patch("/v1/test/patch", json={"data": "value"})
    assert result is None
    await c.close()


async def test_async_delete_json_response(httpx_mock) -> None:
    """Async DELETE returning JSON should parse the body."""
    c = AsyncSocialAPI(api_key=TEST_API_KEY, base_url=BASE_URL, max_retries=0)
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/test/del",
        json={"deleted": True},
        method="DELETE",
    )
    result = await c._client._delete("/v1/test/del")
    assert result == {"deleted": True}
    await c.close()


def test_sync_put_204_response(httpx_mock) -> None:
    """Sync PUT returning 204 should return None."""
    c = SocialAPI(api_key=TEST_API_KEY, base_url=BASE_URL, max_retries=0)
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/test/put",
        status_code=204,
        method="PUT",
    )
    result = c._client._put("/v1/test/put", json={"data": "value"})
    assert result is None
    c.close()


def test_sync_patch_204_response(httpx_mock) -> None:
    """Sync PATCH returning 204 should return None."""
    c = SocialAPI(api_key=TEST_API_KEY, base_url=BASE_URL, max_retries=0)
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/test/patch",
        status_code=204,
        method="PATCH",
    )
    result = c._client._patch("/v1/test/patch", json={"data": "value"})
    assert result is None
    c.close()


def test_sync_delete_json_response(httpx_mock) -> None:
    """Sync DELETE returning JSON should parse the body."""
    c = SocialAPI(api_key=TEST_API_KEY, base_url=BASE_URL, max_retries=0)
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/test/del",
        json={"deleted": True},
        method="DELETE",
    )
    result = c._client._delete("/v1/test/del")
    assert result == {"deleted": True}
    c.close()
