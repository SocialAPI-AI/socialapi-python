"""Tests for retry logic."""

from __future__ import annotations

import httpx

from socialapi._retry import RetryHandler


def _make_response(
    status_code: int,
    *,
    json_body: dict | None = None,
    headers: dict[str, str] | None = None,
) -> httpx.Response:
    """Build a fake httpx.Response."""
    import json as _json

    content = _json.dumps(json_body or {}).encode()
    resp_headers = {"content-type": "application/json"}
    if headers:
        resp_headers.update(headers)
    return httpx.Response(
        status_code=status_code,
        content=content,
        headers=resp_headers,
        request=httpx.Request("GET", "https://api.social-api.ai/v1/test"),
    )


class TestShouldRetry:
    def test_returns_true_for_500(self) -> None:
        handler = RetryHandler(max_retries=3)
        resp = _make_response(500, json_body={"error": "internal", "code": "internal_error"})
        assert handler.should_retry(resp, attempt=0) is True

    def test_returns_true_for_429_platform_rate_limit(self) -> None:
        handler = RetryHandler(max_retries=3)
        resp = _make_response(429, json_body={"error": "slow down", "code": "platform_rate_limit"})
        assert handler.should_retry(resp, attempt=0) is True

    def test_returns_false_for_429_plan_limit(self) -> None:
        handler = RetryHandler(max_retries=3)
        resp = _make_response(429, json_body={"error": "limit exceeded", "code": "rate_limit_exceeded"})
        assert handler.should_retry(resp, attempt=0) is False

    def test_returns_false_for_400(self) -> None:
        handler = RetryHandler(max_retries=3)
        resp = _make_response(400, json_body={"error": "bad request", "code": "bad_request"})
        assert handler.should_retry(resp, attempt=0) is False

    def test_returns_false_when_attempt_ge_max_retries(self) -> None:
        handler = RetryHandler(max_retries=3)
        resp = _make_response(500, json_body={"error": "internal", "code": "internal_error"})
        assert handler.should_retry(resp, attempt=3) is False

    def test_returns_true_for_network_errors(self) -> None:
        handler = RetryHandler(max_retries=3)
        assert handler.should_retry(None, attempt=0, is_network_error=True) is True

    def test_returns_false_for_network_error_when_exhausted(self) -> None:
        handler = RetryHandler(max_retries=3)
        assert handler.should_retry(None, attempt=3, is_network_error=True) is False


class TestCalculateDelay:
    def test_returns_value_within_expected_range(self) -> None:
        handler = RetryHandler(max_retries=3)
        # attempt 0: base = min(1.0 * 2^0, 8.0) = 1.0, jitter in [0, 1.0]
        for _ in range(20):
            delay = handler.calculate_delay(0)
            assert 0.0 <= delay <= 1.0

    def test_respects_retry_after_header(self) -> None:
        handler = RetryHandler(max_retries=3)
        resp = _make_response(429, headers={"Retry-After": "5"})
        delay = handler.calculate_delay(0, resp)
        assert delay == 5.0

    def test_attempt_2_within_range(self) -> None:
        handler = RetryHandler(max_retries=3)
        # attempt 2: base = min(1.0 * 2^2, 8.0) = 4.0, jitter in [0, 4.0]
        for _ in range(20):
            delay = handler.calculate_delay(2)
            assert 0.0 <= delay <= 4.0

    def test_delay_capped_at_max(self) -> None:
        handler = RetryHandler(max_retries=10)
        # attempt 10: base = min(1.0 * 2^10, 8.0) = 8.0, jitter in [0, 8.0]
        for _ in range(20):
            delay = handler.calculate_delay(10)
            assert 0.0 <= delay <= 8.0
