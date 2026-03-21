"""Tests for webhook signature verification."""

from __future__ import annotations

import hashlib
import hmac

from socialapi.webhooks import verify_signature

SECRET = "whsec_test_secret_123"
PAYLOAD = b'{"event": "comment.created", "data": {}}'


def _compute_signature(payload: bytes, secret: str) -> str:
    return hmac.new(secret.encode("utf-8"), payload, hashlib.sha256).hexdigest()


def test_valid_signature() -> None:
    sig = _compute_signature(PAYLOAD, SECRET)
    assert verify_signature(PAYLOAD, sig, SECRET) is True


def test_invalid_signature() -> None:
    assert verify_signature(PAYLOAD, "deadbeef" * 8, SECRET) is False


def test_signature_with_sha256_prefix() -> None:
    sig = "sha256=" + _compute_signature(PAYLOAD, SECRET)
    assert verify_signature(PAYLOAD, sig, SECRET) is True


def test_signature_without_prefix() -> None:
    sig = _compute_signature(PAYLOAD, SECRET)
    # No prefix -- should still work
    assert verify_signature(PAYLOAD, sig, SECRET) is True
