from __future__ import annotations

import httpx

from socialapi._exceptions import (
    APIStatusError,
    AuthenticationError,
    BadRequestError,
    ConflictError,
    InternalServerError,
    NotFoundError,
    NotSupportedError,
    RateLimitError,
    StorageQuotaExceededError,
)


def _make_response(status_code: int, json_body: dict | None = None) -> httpx.Response:
    """Build a fake httpx.Response for testing error mapping."""
    if json_body is not None:
        import json as _json

        content = _json.dumps(json_body).encode()
        headers = {"content-type": "application/json"}
    else:
        content = b""
        headers = {}
    return httpx.Response(
        status_code=status_code,
        content=content,
        headers=headers,
        request=httpx.Request("GET", "https://api.test.local/v1/test"),
    )


def test_from_response_400_bad_request() -> None:
    resp = _make_response(400, {"error": "missing field", "code": "missing_metadata"})
    exc = APIStatusError.from_response(resp)
    assert isinstance(exc, BadRequestError)
    assert exc.status_code == 400
    assert exc.message == "missing field"
    assert exc.code == "missing_metadata"


def test_from_response_401_auth_error() -> None:
    resp = _make_response(401, {"error": "invalid api key", "code": "unauthorized"})
    exc = APIStatusError.from_response(resp)
    assert isinstance(exc, AuthenticationError)
    assert exc.status_code == 401
    assert exc.code == "unauthorized"


def test_from_response_404_not_found() -> None:
    resp = _make_response(404, {"error": "account not found", "code": "account_not_found"})
    exc = APIStatusError.from_response(resp)
    assert isinstance(exc, NotFoundError)
    assert exc.status_code == 404


def test_from_response_409_conflict() -> None:
    resp = _make_response(409, {"error": "already linked", "code": "account_already_linked"})
    exc = APIStatusError.from_response(resp)
    assert isinstance(exc, ConflictError)
    assert exc.status_code == 409


def test_from_response_413_storage_quota() -> None:
    resp = _make_response(413, {"error": "storage quota exceeded", "code": "storage_quota_exceeded"})
    exc = APIStatusError.from_response(resp)
    assert isinstance(exc, StorageQuotaExceededError)
    assert exc.status_code == 413


def test_from_response_429_rate_limit() -> None:
    resp = _make_response(429, {"error": "rate limited", "code": "rate_limit_exceeded"})
    exc = APIStatusError.from_response(resp)
    assert isinstance(exc, RateLimitError)
    assert exc.status_code == 429


def test_from_response_500_internal_error() -> None:
    resp = _make_response(500, {"error": "unexpected failure"})
    exc = APIStatusError.from_response(resp)
    assert isinstance(exc, InternalServerError)
    assert exc.status_code == 500


def test_from_response_501_not_implemented() -> None:
    resp = _make_response(501, {"error": "not supported", "code": "not_supported"})
    exc = APIStatusError.from_response(resp)
    assert isinstance(exc, NotSupportedError)
    assert exc.status_code == 501


def test_from_response_unknown_status() -> None:
    resp = _make_response(418, {"error": "I'm a teapot"})
    exc = APIStatusError.from_response(resp)
    assert type(exc) is APIStatusError
    assert exc.status_code == 418


def test_exception_attributes() -> None:
    resp = _make_response(400, {"error": "bad request", "code": "invalid_params"})
    exc = APIStatusError.from_response(resp)
    assert exc.message == "bad request"
    assert exc.code == "invalid_params"
    assert exc.status_code == 400
    assert exc.body == {"error": "bad request", "code": "invalid_params"}
    assert exc.response is resp


def test_exception_repr() -> None:
    resp = _make_response(404, {"error": "not found", "code": "not_found"})
    exc = APIStatusError.from_response(resp)
    r = repr(exc)
    assert "NotFoundError" in r
    assert "404" in r


def test_exception_without_json_body() -> None:
    resp = _make_response(500, None)
    exc = APIStatusError.from_response(resp)
    assert isinstance(exc, InternalServerError)
    assert exc.body is None
    assert exc.code is None
