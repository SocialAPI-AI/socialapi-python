from __future__ import annotations

import hashlib
import hmac

from socialapi.webhooks import verify_signature


# Known values derived from Go's SignPayload: "sha256=" + hex(HMAC-SHA256(secret, payload))
def _make_signature(secret: str, payload: bytes) -> str:
    mac = hmac.new(secret.encode(), payload, hashlib.sha256)
    return "sha256=" + mac.hexdigest()


class TestVerifySignature:
    """Tests for the verify_signature helper."""

    def test_valid_signature_returns_true(self) -> None:
        secret = "whsec_test_secret_abc123"
        payload = b'{"event":"comment.received","data":{}}'
        sig = _make_signature(secret, payload)
        assert verify_signature(secret=secret, payload=payload, signature=sig) is True

    def test_tampered_payload_returns_false(self) -> None:
        secret = "whsec_test_secret_abc123"
        payload = b'{"event":"comment.received","data":{}}'
        sig = _make_signature(secret, payload)
        tampered = b'{"event":"dm.received","data":{}}'
        assert verify_signature(secret=secret, payload=tampered, signature=sig) is False

    def test_wrong_secret_returns_false(self) -> None:
        secret = "whsec_correct_secret"
        wrong_secret = "whsec_wrong_secret"
        payload = b'{"event":"post.published","data":{}}'
        sig = _make_signature(secret, payload)
        assert verify_signature(secret=wrong_secret, payload=payload, signature=sig) is False

    def test_tampered_signature_returns_false(self) -> None:
        secret = "whsec_test_secret"
        payload = b'{"event":"review.received","data":{}}'
        sig = _make_signature(secret, payload)
        # Flip last character
        tampered_sig = sig[:-1] + ("0" if sig[-1] != "0" else "1")
        assert verify_signature(secret=secret, payload=payload, signature=tampered_sig) is False

    def test_sha256_prefix_accepted(self) -> None:
        secret = "whsec_abc"
        payload = b"hello world"
        sig = _make_signature(secret, payload)
        assert sig.startswith("sha256=")
        assert verify_signature(secret=secret, payload=payload, signature=sig) is True

    def test_empty_payload(self) -> None:
        secret = "whsec_empty_test"
        payload = b""
        sig = _make_signature(secret, payload)
        assert verify_signature(secret=secret, payload=payload, signature=sig) is True

    def test_unicode_in_payload(self) -> None:
        secret = "whsec_unicode"
        payload = '{"text":"Hello 世界"}'.encode()
        sig = _make_signature(secret, payload)
        assert verify_signature(secret=secret, payload=payload, signature=sig) is True


class TestVerifySignatureExported:
    """Verify that verify_signature is reachable from the top-level package."""

    def test_importable_from_top_level(self) -> None:
        from socialapi import verify_signature as vs

        assert callable(vs)

    def test_top_level_import_works(self) -> None:
        from socialapi import verify_signature as vs

        secret = "whsec_top"
        payload = b"test"
        sig = _make_signature(secret, payload)
        assert vs(secret=secret, payload=payload, signature=sig) is True
