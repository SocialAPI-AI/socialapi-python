"""Webhook signature verification helper.

Usage::

    from socialapi.webhooks import verify_signature

    is_valid = verify_signature(
        secret="whsec_...",
        payload=request.body,
        signature=request.headers["X-SocialAPI-Signature"],
    )
"""

from __future__ import annotations

import hashlib
import hmac


def verify_signature(*, secret: str, payload: bytes, signature: str) -> bool:
    """Verify a webhook payload signature using HMAC-SHA256.

    The SocialAPI server signs every delivery with
    ``X-SocialAPI-Signature: sha256=<hex_digest>`` where the digest is
    ``HMAC-SHA256(secret, payload)``.  This helper performs a constant-time
    comparison so it is safe to use in request handlers.

    Args:
        secret: The endpoint secret returned when the webhook was created
            (``whsec_...``).
        payload: The raw request body bytes exactly as received.
        signature: The value of the ``X-SocialAPI-Signature`` header,
            e.g. ``sha256=abc123...``.

    Returns:
        ``True`` if the signature matches, ``False`` otherwise.
    """
    mac = hmac.new(secret.encode(), payload, hashlib.sha256)
    expected = "sha256=" + mac.hexdigest()
    return hmac.compare_digest(expected, signature)
