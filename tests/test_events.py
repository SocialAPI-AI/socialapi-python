from __future__ import annotations

from .conftest import BASE_URL

EVENT_JSON = {
    "id": "evt_001",
    "category": "post",
    "action": "publish",
    "status": "success",
    "platform": "instagram",
    "account_id": "acc_ig_001",
    "resource_id": "p_001",
    "summary": "Published to Instagram",
    "metadata": {},
    "created_at": "2026-03-27T10:00:00Z",
}


def test_list_events(httpx_mock, client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/events",
        json={
            "events": [EVENT_JSON],
            "pagination": {"has_more": False, "next_cursor": None},
            "retention_days": 30,
        },
    )
    result = client.events.list()
    assert len(result.events) == 1
    assert result.events[0].category == "post"
    assert result.events[0].action == "publish"
    assert result.retention_days == 30


def test_list_events_with_filters(httpx_mock, client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/events?category=post&status=success&limit=10",
        json={
            "events": [EVENT_JSON],
            "pagination": {"has_more": False, "next_cursor": None},
            "retention_days": 30,
        },
    )
    result = client.events.list(category="post", status="success", limit=10)
    assert len(result.events) == 1


async def test_list_events_async(httpx_mock, async_client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/events",
        json={
            "events": [EVENT_JSON],
            "pagination": {"has_more": False, "next_cursor": None},
            "retention_days": 7,
        },
    )
    result = await async_client.events.list()
    assert len(result.events) == 1
    assert result.retention_days == 7
