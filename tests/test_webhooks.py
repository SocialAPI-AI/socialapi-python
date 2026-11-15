from socialapi.webhooks import verify_webhook

# Reference vector shared by every SDK: HMAC-SHA256("whsec_test", "1700000000." + body).
SECRET = "whsec_test"
BODY = b'{"event":"comment.received"}'
HEADERS = {
    "X-SocialAPI-Timestamp": "1700000000",
    "X-SocialAPI-Signature-V2": "sha256=a1c084394bcdc1743e02d34447378108cde7b6ac0c963bd211e97ba76bb3f3bf",
}
NOW = 1700000000


def test_valid() -> None:
    assert verify_webhook(SECRET, BODY, HEADERS, now=NOW + 60)
    assert verify_webhook(SECRET, BODY, {k.lower(): v for k, v in HEADERS.items()}, now=NOW)


def test_rejected() -> None:
    assert not verify_webhook("wrong", BODY, HEADERS, now=NOW)
    assert not verify_webhook(SECRET, b"{}", HEADERS, now=NOW)
    assert not verify_webhook(SECRET, BODY, HEADERS, now=NOW + 360)
    assert not verify_webhook(SECRET, BODY, {"X-SocialAPI-Signature-V2": HEADERS["X-SocialAPI-Signature-V2"]}, now=NOW)
