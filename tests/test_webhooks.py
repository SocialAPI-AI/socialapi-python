from __future__ import annotations

import json

from .conftest import BASE_URL

WEBHOOK_JSON = {
    "id": "wh_001",
    "url": "https://myapp.example.com/webhook",
    "events": ["comment.received", "dm.received"],
    "is_active": True,
    "created_at": "2026-03-15T10:00:00Z",
}

WEBHOOK_DETAIL_JSON = {
    **WEBHOOK_JSON,
    "secret_hint": "whsec_abc...xyz",
    "stats": {
        "last_24h": {"delivered": 42, "failed": 3},
        "last_7d": {"delivered": 210, "failed": 17},
    },
}

DELIVERY_LIST_ITEM_JSON = {
    "id": "del_001",
    "event_type": "comment.received",
    "status": "delivered",
    "response_status_code": 200,
    "response_duration_ms": 123,
    "attempt_count": 1,
    "description": "Test delivery",
    "created_at": "2026-03-15T10:00:00Z",
}

DELIVERY_ATTEMPT_JSON = {
    "attempt_number": 1,
    "status_code": 200,
    "response_body": '{"ok":true}',
    "duration_ms": 123,
    "error_message": "",
    "created_at": "2026-03-15T10:00:00Z",
}

DELIVERY_DETAIL_JSON = {
    "id": "del_001",
    "endpoint_id": "wh_001",
    "event_type": "comment.received",
    "status": "delivered",
    "response_status_code": 200,
    "response_duration_ms": 123,
    "attempt_count": 1,
    "description": "Test delivery",
    "payload": {"event": "comment.received", "data": {}},
    "attempts": [DELIVERY_ATTEMPT_JSON],
    "created_at": "2026-03-15T10:00:00Z",
}

TEST_DELIVERY_RESPONSE_JSON = {
    "delivery_id": "del_test_001",
    "status": "delivered",
    "response_status_code": 200,
    "response_body": '{"received":true}',
    "response_duration_ms": 55,
}

WEBHOOK_EVENT_INFO_JSON = {
    "event": "comment.received",
    "description": "A new comment was received on one of your posts",
    "category": "inbox",
}


# ---------------------------------------------------------------------------
# Existing tests (unchanged)
# ---------------------------------------------------------------------------


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


# ---------------------------------------------------------------------------
# New tests: get (webhook detail)
# ---------------------------------------------------------------------------


def test_get_webhook(httpx_mock, client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/webhooks/wh_001",
        json=WEBHOOK_DETAIL_JSON,
    )
    detail = client.webhooks.get("wh_001")
    assert detail.id == "wh_001"
    assert detail.secret_hint == "whsec_abc...xyz"
    assert detail.stats.last_24h.delivered == 42
    assert detail.stats.last_24h.failed == 3
    assert detail.stats.last_7d.delivered == 210
    assert detail.stats.last_7d.failed == 17


def test_get_webhook_no_secret_hint(httpx_mock, client) -> None:
    json_data = {**WEBHOOK_DETAIL_JSON, "secret_hint": ""}
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/webhooks/wh_001",
        json=json_data,
    )
    detail = client.webhooks.get("wh_001")
    assert detail.secret_hint == ""


async def test_get_webhook_async(httpx_mock, async_client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/webhooks/wh_001",
        json=WEBHOOK_DETAIL_JSON,
    )
    detail = await async_client.webhooks.get("wh_001")
    assert detail.id == "wh_001"
    assert detail.secret_hint == "whsec_abc...xyz"
    assert detail.stats.last_7d.delivered == 210


# ---------------------------------------------------------------------------
# New tests: list_events
# ---------------------------------------------------------------------------


def test_list_webhook_events(httpx_mock, client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/webhooks/events",
        json={"data": [WEBHOOK_EVENT_INFO_JSON], "count": 1},
    )
    events = client.webhooks.list_events()
    assert len(events) == 1
    assert events[0].event == "comment.received"
    assert events[0].description == "A new comment was received on one of your posts"
    assert events[0].category == "inbox"


async def test_list_webhook_events_async(httpx_mock, async_client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/webhooks/events",
        json={"data": [WEBHOOK_EVENT_INFO_JSON], "count": 1},
    )
    events = await async_client.webhooks.list_events()
    assert len(events) == 1
    assert events[0].event == "comment.received"
    assert events[0].category == "inbox"


# ---------------------------------------------------------------------------
# New tests: list_deliveries
# ---------------------------------------------------------------------------


def test_list_deliveries(httpx_mock, client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/webhooks/wh_001/deliveries",
        json={"data": [DELIVERY_LIST_ITEM_JSON], "next_cursor": None, "count": 1},
    )
    page = client.webhooks.list_deliveries("wh_001")
    assert len(page.data) == 1
    item = page.data[0]
    assert item.id == "del_001"
    assert item.event_type == "comment.received"
    assert item.status == "delivered"
    assert item.response_status_code == 200
    assert item.response_duration_ms == 123
    assert item.attempt_count == 1
    assert item.description == "Test delivery"


def test_list_deliveries_with_filters(httpx_mock, client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/webhooks/wh_001/deliveries?status=delivered&event_type=comment.received",
        json={"data": [DELIVERY_LIST_ITEM_JSON], "next_cursor": None, "count": 1},
    )
    page = client.webhooks.list_deliveries("wh_001", status="delivered", event_type="comment.received")
    assert len(page.data) == 1


def test_list_deliveries_pagination(httpx_mock, client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/webhooks/wh_001/deliveries",
        json={"data": [DELIVERY_LIST_ITEM_JSON], "next_cursor": "cursor_abc", "count": 2},
    )
    page = client.webhooks.list_deliveries("wh_001")
    assert page.has_next_page()
    assert page.next_cursor == "cursor_abc"


async def test_list_deliveries_async(httpx_mock, async_client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/webhooks/wh_001/deliveries",
        json={"data": [DELIVERY_LIST_ITEM_JSON], "next_cursor": None, "count": 1},
    )
    page = await async_client.webhooks.list_deliveries("wh_001")
    assert len(page.data) == 1
    assert page.data[0].id == "del_001"


# ---------------------------------------------------------------------------
# New tests: get_delivery
# ---------------------------------------------------------------------------


def test_get_delivery(httpx_mock, client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/webhooks/wh_001/deliveries/del_001",
        json=DELIVERY_DETAIL_JSON,
    )
    detail = client.webhooks.get_delivery("wh_001", "del_001")
    assert detail.id == "del_001"
    assert detail.endpoint_id == "wh_001"
    assert detail.event_type == "comment.received"
    assert detail.status == "delivered"
    assert detail.response_status_code == 200
    assert detail.attempt_count == 1
    assert detail.description == "Test delivery"
    assert len(detail.attempts) == 1
    attempt = detail.attempts[0]
    assert attempt.attempt_number == 1
    assert attempt.status_code == 200
    assert attempt.response_body == '{"ok":true}'
    assert attempt.duration_ms == 123


async def test_get_delivery_async(httpx_mock, async_client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/webhooks/wh_001/deliveries/del_001",
        json=DELIVERY_DETAIL_JSON,
    )
    detail = await async_client.webhooks.get_delivery("wh_001", "del_001")
    assert detail.id == "del_001"
    assert detail.endpoint_id == "wh_001"
    assert len(detail.attempts) == 1


# ---------------------------------------------------------------------------
# New tests: retry_delivery
# ---------------------------------------------------------------------------


def test_retry_delivery(httpx_mock, client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/webhooks/wh_001/deliveries/del_001/retry",
        json=DELIVERY_DETAIL_JSON,
    )
    detail = client.webhooks.retry_delivery("wh_001", "del_001")
    assert detail.id == "del_001"
    assert detail.status == "delivered"
    req = httpx_mock.get_requests()[0]
    assert req.method == "POST"


async def test_retry_delivery_async(httpx_mock, async_client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/webhooks/wh_001/deliveries/del_001/retry",
        json=DELIVERY_DETAIL_JSON,
    )
    detail = await async_client.webhooks.retry_delivery("wh_001", "del_001")
    assert detail.id == "del_001"


# ---------------------------------------------------------------------------
# New tests: test (send test delivery)
# ---------------------------------------------------------------------------


def test_test_webhook(httpx_mock, client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/webhooks/wh_001/test",
        json=TEST_DELIVERY_RESPONSE_JSON,
    )
    result = client.webhooks.test(
        "wh_001",
        event_type="comment.received",
        payload={"event": "comment.received", "data": {}},
    )
    assert result.delivery_id == "del_test_001"
    assert result.status == "delivered"
    assert result.response_status_code == 200
    assert result.response_body == '{"received":true}'
    assert result.response_duration_ms == 55

    req = httpx_mock.get_requests()[0]
    body = json.loads(req.content)
    assert body["event_type"] == "comment.received"
    assert "payload" in body


async def test_test_webhook_async(httpx_mock, async_client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/webhooks/wh_001/test",
        json=TEST_DELIVERY_RESPONSE_JSON,
    )
    result = await async_client.webhooks.test(
        "wh_001",
        event_type="dm.received",
        payload={"event": "dm.received", "data": {}},
    )
    assert result.delivery_id == "del_test_001"
    assert result.response_status_code == 200
