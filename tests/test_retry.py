from __future__ import annotations

from unittest.mock import patch

import pytest

from socialapi import SocialAPI
from socialapi._exceptions import (
    AuthenticationError,
    BadRequestError,
    InternalServerError,
    NotFoundError,
)

from .conftest import BASE_URL, TEST_API_KEY


def test_retry_on_500(httpx_mock) -> None:
    """500 responses should be retried, then succeed."""
    httpx_mock.add_response(status_code=500, json={"error": "server error"})
    httpx_mock.add_response(status_code=200, json={"id": "usr_1", "email": "a@b.com", "plan": "free"})

    client = SocialAPI(api_key=TEST_API_KEY, base_url=BASE_URL, max_retries=2)
    with patch("socialapi._base_client.time.sleep"):
        user = client.users.get_me()
    assert user.id == "usr_1"
    client.close()


def test_retry_on_429_with_retry_after(httpx_mock) -> None:
    """429 with Retry-After header should be respected."""
    httpx_mock.add_response(
        status_code=429,
        json={"error": "rate limited", "code": "rate_limit_exceeded"},
        headers={"retry-after": "1"},
    )
    httpx_mock.add_response(status_code=200, json={"id": "usr_1", "email": "a@b.com", "plan": "free"})

    client = SocialAPI(api_key=TEST_API_KEY, base_url=BASE_URL, max_retries=2)
    with patch("socialapi._base_client.time.sleep") as mock_sleep:
        user = client.users.get_me()
    assert user.id == "usr_1"
    # Verify that the sleep was called with the retry-after value (1.0 second)
    mock_sleep.assert_called_once()
    assert mock_sleep.call_args[0][0] == 1.0
    client.close()


def test_no_retry_on_400(httpx_mock) -> None:
    """400 should NOT be retried."""
    httpx_mock.add_response(status_code=400, json={"error": "bad request", "code": "bad_request"})

    client = SocialAPI(api_key=TEST_API_KEY, base_url=BASE_URL, max_retries=2)
    with pytest.raises(BadRequestError):
        client.users.get_me()
    client.close()


def test_no_retry_on_401(httpx_mock) -> None:
    """401 should NOT be retried."""
    httpx_mock.add_response(status_code=401, json={"error": "unauthorized", "code": "unauthorized"})

    client = SocialAPI(api_key=TEST_API_KEY, base_url=BASE_URL, max_retries=2)
    with pytest.raises(AuthenticationError):
        client.users.get_me()
    client.close()


def test_no_retry_on_404(httpx_mock) -> None:
    """404 should NOT be retried."""
    httpx_mock.add_response(status_code=404, json={"error": "not found", "code": "not_found"})

    client = SocialAPI(api_key=TEST_API_KEY, base_url=BASE_URL, max_retries=2)
    with pytest.raises(NotFoundError):
        client.users.get_me()
    client.close()


def test_max_retries_exhausted(httpx_mock) -> None:
    """After max retries, the error should be raised."""
    httpx_mock.add_response(status_code=500, json={"error": "server error"})
    httpx_mock.add_response(status_code=500, json={"error": "server error"})
    httpx_mock.add_response(status_code=500, json={"error": "server error"})

    client = SocialAPI(api_key=TEST_API_KEY, base_url=BASE_URL, max_retries=2)
    with patch("socialapi._base_client.time.sleep"), pytest.raises(InternalServerError):
        client.users.get_me()
    client.close()


def test_exponential_backoff_jitter(httpx_mock) -> None:
    """Backoff delay should use exponential backoff with jitter."""
    httpx_mock.add_response(status_code=500, json={"error": "server error"})
    httpx_mock.add_response(status_code=200, json={"id": "usr_1", "email": "a@b.com", "plan": "free"})

    client = SocialAPI(api_key=TEST_API_KEY, base_url=BASE_URL, max_retries=2)
    with (
        patch("socialapi._base_client.time.sleep") as mock_sleep,
        patch("socialapi._base_client.random.random", return_value=0.5),
    ):
        client.users.get_me()
    mock_sleep.assert_called_once()
    # With retries_taken=0: min(8.0, 0.5 * 2^0) = 0.5, then * 0.5 (random) = 0.25
    assert mock_sleep.call_args[0][0] == pytest.approx(0.25)
    client.close()


def test_retry_after_header_respected(httpx_mock) -> None:
    """Retry-After header value should be used as the delay, capped at 60s."""
    httpx_mock.add_response(
        status_code=429,
        json={"error": "rate limited"},
        headers={"retry-after": "5"},
    )
    httpx_mock.add_response(status_code=200, json={"id": "usr_1", "email": "a@b.com", "plan": "free"})

    client = SocialAPI(api_key=TEST_API_KEY, base_url=BASE_URL, max_retries=2)
    with patch("socialapi._base_client.time.sleep") as mock_sleep:
        client.users.get_me()
    mock_sleep.assert_called_once_with(5.0)
    client.close()


async def test_async_retry_on_500(httpx_mock) -> None:
    """Async: 500 responses should be retried, then succeed."""
    from socialapi import AsyncSocialAPI

    httpx_mock.add_response(status_code=500, json={"error": "server error"})
    httpx_mock.add_response(status_code=200, json={"id": "usr_1", "email": "a@b.com", "plan": "free"})

    client = AsyncSocialAPI(api_key=TEST_API_KEY, base_url=BASE_URL, max_retries=2)
    with patch("socialapi._base_client.asyncio.sleep", return_value=None) as mock_sleep:
        user = await client.users.get_me()
    assert user.id == "usr_1"
    mock_sleep.assert_called_once()
    await client.close()


async def test_async_retry_exhausted(httpx_mock) -> None:
    """Async: After max retries, the error should be raised."""
    from socialapi import AsyncSocialAPI

    httpx_mock.add_response(status_code=500, json={"error": "server error"})
    httpx_mock.add_response(status_code=500, json={"error": "server error"})
    httpx_mock.add_response(status_code=500, json={"error": "server error"})

    client = AsyncSocialAPI(api_key=TEST_API_KEY, base_url=BASE_URL, max_retries=2)
    with patch("socialapi._base_client.asyncio.sleep", return_value=None), pytest.raises(InternalServerError):
        await client.users.get_me()
    await client.close()


async def test_async_retry_on_429_with_retry_after(httpx_mock) -> None:
    """Async: 429 with Retry-After should be respected."""
    from socialapi import AsyncSocialAPI

    httpx_mock.add_response(
        status_code=429,
        json={"error": "rate limited"},
        headers={"retry-after": "2"},
    )
    httpx_mock.add_response(status_code=200, json={"id": "usr_1", "email": "a@b.com", "plan": "free"})

    client = AsyncSocialAPI(api_key=TEST_API_KEY, base_url=BASE_URL, max_retries=2)
    with patch("socialapi._base_client.asyncio.sleep", return_value=None) as mock_sleep:
        user = await client.users.get_me()
    assert user.id == "usr_1"
    mock_sleep.assert_called_once_with(2.0)
    await client.close()


async def test_async_retry_debug_logging_on_status(httpx_mock) -> None:
    """Async: Debug mode should log retry information."""
    import logging

    from socialapi import AsyncSocialAPI

    httpx_mock.add_response(status_code=500, json={"error": "server error"})
    httpx_mock.add_response(status_code=200, json={"id": "usr_1", "email": "a@b.com", "plan": "free"})

    client = AsyncSocialAPI(api_key=TEST_API_KEY, base_url=BASE_URL, max_retries=2, debug=True)
    logger = logging.getLogger("socialapi")
    logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler()
    logger.addHandler(handler)
    try:
        with patch("socialapi._base_client.asyncio.sleep", return_value=None):
            user = await client.users.get_me()
        assert user.id == "usr_1"
    finally:
        logger.removeHandler(handler)
    await client.close()


def test_sync_timeout_exception(httpx_mock) -> None:
    """Sync: Timeout exceptions should be retried, then raise APITimeoutError."""
    import httpx as _httpx

    from socialapi._exceptions import APITimeoutError

    httpx_mock.add_exception(_httpx.ReadTimeout("read timed out"))
    httpx_mock.add_exception(_httpx.ReadTimeout("read timed out"))

    client = SocialAPI(api_key=TEST_API_KEY, base_url=BASE_URL, max_retries=1)
    with patch("socialapi._base_client.time.sleep"), pytest.raises(APITimeoutError):
        client.users.get_me()
    client.close()


def test_sync_timeout_retry_then_success(httpx_mock) -> None:
    """Sync: Timeout on first try, success on retry."""
    import httpx as _httpx

    httpx_mock.add_exception(_httpx.ReadTimeout("read timed out"))
    httpx_mock.add_response(status_code=200, json={"id": "usr_1", "email": "a@b.com", "plan": "free"})

    client = SocialAPI(api_key=TEST_API_KEY, base_url=BASE_URL, max_retries=1)
    with patch("socialapi._base_client.time.sleep"):
        user = client.users.get_me()
    assert user.id == "usr_1"
    client.close()


def test_sync_connect_error(httpx_mock) -> None:
    """Sync: Connection errors should be retried, then raise APIConnectionError."""
    import httpx as _httpx

    from socialapi._exceptions import APIConnectionError

    httpx_mock.add_exception(_httpx.ConnectError("connection refused"))
    httpx_mock.add_exception(_httpx.ConnectError("connection refused"))

    client = SocialAPI(api_key=TEST_API_KEY, base_url=BASE_URL, max_retries=1)
    with patch("socialapi._base_client.time.sleep"), pytest.raises(APIConnectionError):
        client.users.get_me()
    client.close()


def test_sync_connect_error_retry_then_success(httpx_mock) -> None:
    """Sync: Connection error on first try, success on retry."""
    import httpx as _httpx

    httpx_mock.add_exception(_httpx.ConnectError("connection refused"))
    httpx_mock.add_response(status_code=200, json={"id": "usr_1", "email": "a@b.com", "plan": "free"})

    client = SocialAPI(api_key=TEST_API_KEY, base_url=BASE_URL, max_retries=1)
    with patch("socialapi._base_client.time.sleep"):
        user = client.users.get_me()
    assert user.id == "usr_1"
    client.close()


def test_sync_timeout_with_debug(httpx_mock) -> None:
    """Sync: Timeout retry with debug logging enabled."""
    import logging

    import httpx as _httpx

    httpx_mock.add_exception(_httpx.ReadTimeout("timed out"))
    httpx_mock.add_response(status_code=200, json={"id": "usr_1", "email": "a@b.com", "plan": "free"})

    client = SocialAPI(api_key=TEST_API_KEY, base_url=BASE_URL, max_retries=1, debug=True)
    logger = logging.getLogger("socialapi")
    logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler()
    logger.addHandler(handler)
    try:
        with patch("socialapi._base_client.time.sleep"):
            user = client.users.get_me()
        assert user.id == "usr_1"
    finally:
        logger.removeHandler(handler)
    client.close()


def test_sync_connect_error_with_debug(httpx_mock) -> None:
    """Sync: Connection error retry with debug logging enabled."""
    import logging

    import httpx as _httpx

    httpx_mock.add_exception(_httpx.ConnectError("refused"))
    httpx_mock.add_response(status_code=200, json={"id": "usr_1", "email": "a@b.com", "plan": "free"})

    client = SocialAPI(api_key=TEST_API_KEY, base_url=BASE_URL, max_retries=1, debug=True)
    logger = logging.getLogger("socialapi")
    logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler()
    logger.addHandler(handler)
    try:
        with patch("socialapi._base_client.time.sleep"):
            user = client.users.get_me()
        assert user.id == "usr_1"
    finally:
        logger.removeHandler(handler)
    client.close()


def test_sync_retry_status_with_debug(httpx_mock) -> None:
    """Sync: Retryable status code with debug logging enabled."""
    import logging

    httpx_mock.add_response(status_code=500, json={"error": "server error"})
    httpx_mock.add_response(status_code=200, json={"id": "usr_1", "email": "a@b.com", "plan": "free"})

    client = SocialAPI(api_key=TEST_API_KEY, base_url=BASE_URL, max_retries=1, debug=True)
    logger = logging.getLogger("socialapi")
    logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler()
    logger.addHandler(handler)
    try:
        with patch("socialapi._base_client.time.sleep"):
            user = client.users.get_me()
        assert user.id == "usr_1"
    finally:
        logger.removeHandler(handler)
    client.close()


async def test_async_timeout_exception(httpx_mock) -> None:
    """Async: Timeout exceptions should be retried, then raise APITimeoutError."""
    import httpx as _httpx

    from socialapi import AsyncSocialAPI
    from socialapi._exceptions import APITimeoutError

    httpx_mock.add_exception(_httpx.ReadTimeout("read timed out"))
    httpx_mock.add_exception(_httpx.ReadTimeout("read timed out"))

    client = AsyncSocialAPI(api_key=TEST_API_KEY, base_url=BASE_URL, max_retries=1)
    with patch("socialapi._base_client.asyncio.sleep", return_value=None), pytest.raises(APITimeoutError):
        await client.users.get_me()
    await client.close()


async def test_async_timeout_retry_then_success(httpx_mock) -> None:
    """Async: Timeout on first try, success on retry."""
    import httpx as _httpx

    from socialapi import AsyncSocialAPI

    httpx_mock.add_exception(_httpx.ReadTimeout("read timed out"))
    httpx_mock.add_response(status_code=200, json={"id": "usr_1", "email": "a@b.com", "plan": "free"})

    client = AsyncSocialAPI(api_key=TEST_API_KEY, base_url=BASE_URL, max_retries=1)
    with patch("socialapi._base_client.asyncio.sleep", return_value=None):
        user = await client.users.get_me()
    assert user.id == "usr_1"
    await client.close()


async def test_async_connect_error(httpx_mock) -> None:
    """Async: Connection errors should be retried, then raise APIConnectionError."""
    import httpx as _httpx

    from socialapi import AsyncSocialAPI
    from socialapi._exceptions import APIConnectionError

    httpx_mock.add_exception(_httpx.ConnectError("connection refused"))
    httpx_mock.add_exception(_httpx.ConnectError("connection refused"))

    client = AsyncSocialAPI(api_key=TEST_API_KEY, base_url=BASE_URL, max_retries=1)
    with patch("socialapi._base_client.asyncio.sleep", return_value=None), pytest.raises(APIConnectionError):
        await client.users.get_me()
    await client.close()


async def test_async_connect_error_retry_then_success(httpx_mock) -> None:
    """Async: Connect error on first try, success on retry."""
    import httpx as _httpx

    from socialapi import AsyncSocialAPI

    httpx_mock.add_exception(_httpx.ConnectError("connection refused"))
    httpx_mock.add_response(status_code=200, json={"id": "usr_1", "email": "a@b.com", "plan": "free"})

    client = AsyncSocialAPI(api_key=TEST_API_KEY, base_url=BASE_URL, max_retries=1)
    with patch("socialapi._base_client.asyncio.sleep", return_value=None):
        user = await client.users.get_me()
    assert user.id == "usr_1"
    await client.close()


async def test_async_timeout_with_debug(httpx_mock) -> None:
    """Async: Timeout retry with debug logging enabled."""
    import logging

    import httpx as _httpx

    from socialapi import AsyncSocialAPI

    httpx_mock.add_exception(_httpx.ReadTimeout("timed out"))
    httpx_mock.add_response(status_code=200, json={"id": "usr_1", "email": "a@b.com", "plan": "free"})

    client = AsyncSocialAPI(api_key=TEST_API_KEY, base_url=BASE_URL, max_retries=1, debug=True)
    logger = logging.getLogger("socialapi")
    logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler()
    logger.addHandler(handler)
    try:
        with patch("socialapi._base_client.asyncio.sleep", return_value=None):
            user = await client.users.get_me()
        assert user.id == "usr_1"
    finally:
        logger.removeHandler(handler)
    await client.close()


async def test_async_connect_error_with_debug(httpx_mock) -> None:
    """Async: Connect error retry with debug logging enabled."""
    import logging

    import httpx as _httpx

    from socialapi import AsyncSocialAPI

    httpx_mock.add_exception(_httpx.ConnectError("refused"))
    httpx_mock.add_response(status_code=200, json={"id": "usr_1", "email": "a@b.com", "plan": "free"})

    client = AsyncSocialAPI(api_key=TEST_API_KEY, base_url=BASE_URL, max_retries=1, debug=True)
    logger = logging.getLogger("socialapi")
    logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler()
    logger.addHandler(handler)
    try:
        with patch("socialapi._base_client.asyncio.sleep", return_value=None):
            user = await client.users.get_me()
        assert user.id == "usr_1"
    finally:
        logger.removeHandler(handler)
    await client.close()
