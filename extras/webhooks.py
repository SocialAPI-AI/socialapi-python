"""Webhook signature verification. Hand-written: copied in by scripts/generate.sh."""

from __future__ import annotations

import hashlib
import hmac
import time
from collections.abc import Mapping

DEFAULT_TOLERANCE_SECONDS = 300


def verify_webhook(
    secret: str,
    body: bytes,
    headers: Mapping[str, str],
    tolerance_seconds: int = DEFAULT_TOLERANCE_SECONDS,
    now: float | None = None,
) -> bool:
    """Return True when a delivery's X-SocialAPI-Signature-V2 matches and its timestamp is recent.

    Pass the raw request body, before any JSON decoding. Header lookup is case-insensitive.
    """
    lower = {k.lower(): v for k, v in headers.items()}
    ts = lower.get("x-socialapi-timestamp", "")
    sig = lower.get("x-socialapi-signature-v2", "")
    try:
        age = abs((time.time() if now is None else now) - int(ts))
    except ValueError:
        return False
    if age > tolerance_seconds:
        return False
    expected = "sha256=" + hmac.new(secret.encode(), ts.encode() + b"." + body, hashlib.sha256).hexdigest()
    return hmac.compare_digest(expected, sig)
