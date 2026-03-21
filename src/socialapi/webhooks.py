"""Webhook signature verification utility.

This module provides a standalone function for verifying inbound webhook
signatures. It does not require a client instance.

Example::

    from socialapi.webhooks import verify_signature

    is_valid = verify_signature(
        payload=raw_body,
        signature=request.headers["X-SocialAPI-Signature"],
        secret="whsec_...",
    )
"""

from __future__ import annotations

import hashlib
import hmac


def verify_signature(payload: bytes, signature: str, secret: str) -> bool:
    """Verify an inbound webhook signature using HMAC-SHA256.

    Computes ``HMAC-SHA256(secret, payload)`` and compares the hex digest
    against the provided signature using constant-time comparison to
    prevent timing attacks.

    The signature may optionally be prefixed with ``sha256=``.

    Args:
        payload: The raw request body bytes.
        signature: The value of the ``X-SocialAPI-Signature`` header.
        secret: The webhook endpoint signing secret (e.g. ``whsec_...``).

    Returns:
        ``True`` if the signature is valid, ``False`` otherwise.
    """
    expected = hmac.new(
        secret.encode("utf-8"),
        payload,
        hashlib.sha256,
    ).hexdigest()

    # Strip optional "sha256=" prefix.
    actual = signature.removeprefix("sha256=")

    return hmac.compare_digest(expected, actual)
