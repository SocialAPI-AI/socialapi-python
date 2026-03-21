"""Tests for exception hierarchy and error parsing."""

from __future__ import annotations

import httpx
import pytest

from socialapi._exceptions import (
    AuthenticationError,
    ConflictError,
    InternalError,
    NotFoundError,
    NotSupportedError,
    PlanLimitError,
    PlatformRateLimitError,
    RateLimitError,
    SocialAPIError,
    StorageQuotaError,
    ValidationError,
    raise_for_status,
)


def _make_response(
    status_code: int,
    *,
    json_body: dict | None = None,
    text: str = "",
) -> httpx.Response:
    """Build a fake httpx.Response."""
    if json_body is not None:
        import json as _json

        content = _json.dumps(json_body).encode()
        headers = {"content-type": "application/json"}
    else:
        content = text.encode()
        headers = {"content-type": "text/plain"}

    return httpx.Response(
        status_code=status_code,
        content=content,
        headers=headers,
        request=httpx.Request("GET", "https://api.social-api.ai/v1/test"),
    )


# -- error code mapping tests --


@pytest.mark.parametrize(
    ("code", "status", "exc_class"),
    [
        ("unauthorized", 401, AuthenticationError),
        ("invalid_token", 401, AuthenticationError),
        ("invalid_credentials", 401, AuthenticationError),
        ("not_found", 404, NotFoundError),
        ("account_not_found", 404, NotFoundError),
        ("bad_request", 400, ValidationError),
        ("unsupported_platform", 400, ValidationError),
        ("missing_metadata", 400, ValidationError),
        ("account_already_linked", 409, ConflictError),
        ("storage_quota_exceeded", 413, StorageQuotaError),
        ("rate_limit_exceeded", 429, PlanLimitError),
        ("platform_rate_limit", 429, PlatformRateLimitError),
        ("not_supported", 501, NotSupportedError),
        ("not_implemented", 501, NotSupportedError),
        ("internal_error", 500, InternalError),
    ],
)
def test_raise_for_status_error_code_mapping(code: str, status: int, exc_class: type[SocialAPIError]) -> None:
    resp = _make_response(status, json_body={"error": "test error", "code": code})
    with pytest.raises(exc_class) as exc_info:
        raise_for_status(resp)
    assert exc_info.value.code == code
    assert exc_info.value.status_code == status


def test_raise_for_status_unknown_code_falls_back_to_status() -> None:
    resp = _make_response(404, json_body={"error": "oops", "code": "weird_code"})
    with pytest.raises(NotFoundError) as exc_info:
        raise_for_status(resp)
    assert exc_info.value.code == "weird_code"


def test_raise_for_status_unknown_status_code_falls_back_to_base() -> None:
    resp = _make_response(418, json_body={"error": "teapot", "code": "im_a_teapot"})
    with pytest.raises(SocialAPIError) as exc_info:
        raise_for_status(resp)
    assert exc_info.value.status_code == 418


def test_raise_for_status_non_json_body() -> None:
    resp = _make_response(500, text="Internal Server Error")
    with pytest.raises(InternalError) as exc_info:
        raise_for_status(resp)
    assert exc_info.value.message == "Internal Server Error"
    assert exc_info.value.code == "unknown"


def test_exception_attributes() -> None:
    resp = _make_response(401, json_body={"error": "invalid API key", "code": "unauthorized"})
    with pytest.raises(AuthenticationError) as exc_info:
        raise_for_status(resp)
    exc = exc_info.value
    assert exc.message == "invalid API key"
    assert exc.code == "unauthorized"
    assert exc.status_code == 401
    assert exc.response is resp


def test_plan_limit_is_subclass_of_rate_limit() -> None:
    assert issubclass(PlanLimitError, RateLimitError)


def test_platform_rate_limit_is_subclass_of_rate_limit() -> None:
    assert issubclass(PlatformRateLimitError, RateLimitError)


def test_raise_for_status_success_noop() -> None:
    resp = _make_response(200, json_body={"ok": True})
    # Should not raise
    raise_for_status(resp)
