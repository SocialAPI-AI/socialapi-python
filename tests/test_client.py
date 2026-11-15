"""Release gate for the generated client: base URL, bearer auth, decoding,
error mapping, and tolerance of values the spec does not list yet."""

import httpx2 as httpx

from socialapi import AuthenticatedClient
from socialapi.api.posts import get_posts_pid

POST = (
    b'{"id":"p_1","status":"published","queue_id":null,"field_from_the_future":1,'
    b'"targets":[{"platform":"platform_from_the_future"}]}'
)
ERROR = b'{"error":{"code":"post.not_found","message":"Post not found"},"request_id":"req_1"}'


def client(status: int, body: bytes) -> AuthenticatedClient:
    def handler(request: httpx.Request) -> httpx.Response:
        assert request.headers["Authorization"] == "Bearer sapi_key_test"
        assert request.url.path == "/v1/posts/p_1"
        return httpx.Response(status, content=body, headers={"Content-Type": "application/json"})

    return AuthenticatedClient(
        base_url="https://api.test.local/v1",
        token="sapi_key_test",
        httpx_args={"transport": httpx.MockTransport(handler)},
    )


def test_forward_compatible_decode() -> None:
    # An unlisted platform, an unknown field, and a null must all decode.
    resp = get_posts_pid.sync_detailed("p_1", client=client(200, POST))
    assert resp.status_code == 200
    assert resp.parsed.id == "p_1"
    assert str(resp.parsed.targets[0].platform) == "platform_from_the_future"


def test_error_response() -> None:
    resp = get_posts_pid.sync_detailed("p_1", client=client(404, ERROR))
    assert resp.status_code == 404
    assert resp.parsed.error.code == "post.not_found"
