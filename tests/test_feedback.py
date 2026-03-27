from __future__ import annotations

from .conftest import BASE_URL


def test_send_feedback(httpx_mock, client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/feedback",
        status_code=204,
    )
    client.feedback.send(type="bug", message="The comment reply endpoint returns 500 intermittently")

    import json

    request = httpx_mock.get_requests()[0]
    body = json.loads(request.content)
    assert body["type"] == "bug"
    assert "comment reply" in body["message"]


async def test_send_feedback_async(httpx_mock, async_client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/feedback",
        status_code=204,
    )
    await async_client.feedback.send(type="feature_request", message="Please add YouTube support")
