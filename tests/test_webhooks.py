from __future__ import annotations

from .conftest import BASE_URL

WEBHOOK_JSON = {
    "id": "wh_001",
    "url": "https://myapp.example.com/webhook",
    "events": ["comment.received", "dm.received"],
    "is_active": True,
    "created_at": "2026-03-15T10:00:00Z",
}


def test_list_webhooks(httpx_mock, client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/webhooks",
        json={"data": [WEBHOOK_JSON]},
    )
    webhooks = client.webhooks.list()
    assert len(webhooks) == 1
    assert webhooks[0].id == "wh_001"
    assert webhooks[0].url == "https://myapp.example.com/webhook"
    assert "comment.received" in webhooks[0].events


def test_create_webhook(httpx_mock, client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/webhooks",
        json={
            "id": "wh_002",
            "url": "https://myapp.example.com/hooks/social",
            "events": ["review.received"],
            "secret": "whsec_random_secret_abc",
            "message": "Webhook created. Save the secret -- it is shown once.",
        },
    )
    result = client.webhooks.create(url="https://myapp.example.com/hooks/social", events=["review.received"])
    assert result.id == "wh_002"
    assert result.secret == "whsec_random_secret_abc"

    import json

    request = httpx_mock.get_requests()[0]
    body = json.loads(request.content)
    assert body["url"] == "https://myapp.example.com/hooks/social"
    assert body["events"] == ["review.received"]


def test_update_webhook(httpx_mock, client) -> None:
    updated = {**WEBHOOK_JSON, "is_active": False}
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/webhooks/wh_001",
        json=updated,
    )
    wh = client.webhooks.update("wh_001", is_active=False)
    assert wh.is_active is False


def test_delete_webhook(httpx_mock, client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/webhooks/wh_001",
        status_code=204,
    )
    client.webhooks.delete("wh_001")


def test_update_webhook_with_all_options(httpx_mock, client) -> None:
    updated = {**WEBHOOK_JSON, "url": "https://new.example.com/hook", "events": ["dm.received"], "is_active": True}
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/webhooks/wh_001",
        json=updated,
    )
    wh = client.webhooks.update("wh_001", url="https://new.example.com/hook", events=["dm.received"], is_active=True)
    assert wh.url == "https://new.example.com/hook"

    import json

    body = json.loads(httpx_mock.get_requests()[0].content)
    assert body["url"] == "https://new.example.com/hook"
    assert body["events"] == ["dm.received"]
    assert body["is_active"] is True


async def test_list_webhooks_async(httpx_mock, async_client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/webhooks",
        json={"data": [WEBHOOK_JSON]},
    )
    webhooks = await async_client.webhooks.list()
    assert len(webhooks) == 1
    assert webhooks[0].id == "wh_001"


async def test_create_webhook_async(httpx_mock, async_client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/webhooks",
        json={
            "id": "wh_async_001",
            "url": "https://app.example.com/hook",
            "events": ["comment.received"],
            "secret": "whsec_async_secret",
            "message": "Webhook created. Save the secret -- it is shown once.",
        },
    )
    result = await async_client.webhooks.create(url="https://app.example.com/hook", events=["comment.received"])
    assert result.id == "wh_async_001"
    assert result.secret == "whsec_async_secret"


async def test_update_webhook_async(httpx_mock, async_client) -> None:
    updated = {**WEBHOOK_JSON, "is_active": False}
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/webhooks/wh_001",
        json=updated,
    )
    wh = await async_client.webhooks.update(
        "wh_001", is_active=False, url="https://new.example.com", events=["dm.received"]
    )
    assert wh.is_active is False


async def test_delete_webhook_async(httpx_mock, async_client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/webhooks/wh_001",
        status_code=204,
    )
    await async_client.webhooks.delete("wh_001")
