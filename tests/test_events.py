from __future__ import annotations

from .conftest import BASE_URL

# ---------------------------------------------------------------------------
# Sync tests
# ---------------------------------------------------------------------------


def test_events_list_basic(httpx_mock, client) -> None:
    """list() returns an EventList with events and retention_days."""
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/events",
        json={
            "events": [
                {
                    "id": "evt_001",
                    "category": "post",
                    "action": "publish",
                    "status": "success",
                    "platform": "instagram",
                    "account_id": "acc_ig_001",
                    "resource_id": "post_001",
                    "summary": "Published to Instagram",
                    "metadata": {},
                    "created_at": "2026-06-01T10:00:00Z",
                }
            ],
            "pagination": {"limit": 50, "has_more": False, "next_cursor": None},
            "retention_days": 30,
        },
    )
    result = client.events.list()
    assert result.retention_days == 30
    assert len(result.data) == 1
    event = result.data[0]
    assert event.id == "evt_001"
    assert event.category == "post"
    assert event.action == "publish"
    assert event.status == "success"
    assert event.platform == "instagram"
    assert event.account_id == "acc_ig_001"
    assert event.resource_id == "post_001"
    assert event.summary == "Published to Instagram"
    assert event.metadata == {}


def test_events_list_optional_fields(httpx_mock, client) -> None:
    """list() correctly handles optional nullable fields."""
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/events",
        json={
            "events": [
                {
                    "id": "evt_002",
                    "category": "webhook",
                    "action": "delivery",
                    "status": "failed",
                    "summary": "Webhook delivery failed",
                    "error_message": "timeout",
                    "error_category": "network",
                    "status_code": 504,
                    "duration_ms": 5000,
                    "metadata": {"attempt": 1},
                    "created_at": "2026-06-01T11:00:00Z",
                }
            ],
            "pagination": {"limit": 50, "has_more": False, "next_cursor": None},
            "retention_days": 7,
        },
    )
    result = client.events.list()
    event = result.data[0]
    assert event.error_message == "timeout"
    assert event.error_category == "network"
    assert event.status_code == 504
    assert event.duration_ms == 5000
    assert event.platform is None
    assert event.account_id is None
    assert event.resource_id is None


def test_events_list_filters_sent(httpx_mock, client) -> None:
    """list() sends category, status, platform, account_id, resource_id, action, from, to filters."""
    httpx_mock.add_response(
        url=(
            f"{BASE_URL}/v1/events"
            "?category=post&status=failed&platform=instagram"
            "&account_id=acc_ig_001&resource_id=post_001&action=post.published"
            "&from=2026-06-01T00%3A00%3A00Z&to=2026-06-08T00%3A00%3A00Z&limit=10"
        ),
        json={
            "events": [],
            "pagination": {"limit": 10, "has_more": False, "next_cursor": None},
            "retention_days": 30,
        },
    )
    result = client.events.list(
        category="post",
        status="failed",
        platform="instagram",
        account_id="acc_ig_001",
        resource_id="post_001",
        action="post.published",
        since="2026-06-01T00:00:00Z",
        until="2026-06-08T00:00:00Z",
        limit=10,
        cursor=None,
    )
    assert len(result.data) == 0
    request = httpx_mock.get_request()
    assert request is not None
    qs = dict(request.url.params)
    assert qs["category"] == "post"
    assert qs["status"] == "failed"
    assert qs["platform"] == "instagram"
    assert qs["account_id"] == "acc_ig_001"
    assert qs["resource_id"] == "post_001"
    assert qs["action"] == "post.published"
    # wire names are "from" and "to"
    assert qs["from"] == "2026-06-01T00:00:00Z"
    assert qs["to"] == "2026-06-08T00:00:00Z"
    assert qs["limit"] == "10"


def test_events_list_pagination(httpx_mock, client) -> None:
    """list() result supports has_next_page / next_page."""
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/events?limit=1",
        json={
            "events": [
                {
                    "id": "evt_p1",
                    "category": "post",
                    "action": "publish",
                    "status": "success",
                    "summary": "Page 1",
                    "metadata": {},
                    "created_at": "2026-06-01T10:00:00Z",
                }
            ],
            "pagination": {"limit": 1, "has_more": True, "next_cursor": "cursor_abc"},
            "retention_days": 30,
        },
    )
    result = client.events.list(limit=1)
    assert result.has_next_page()
    assert result.next_cursor == "cursor_abc"
    assert result.data[0].id == "evt_p1"


def test_events_list_empty(httpx_mock, client) -> None:
    """list() with empty events returns empty list."""
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/events",
        json={
            "events": [],
            "pagination": {"limit": 50, "has_more": False, "next_cursor": None},
            "retention_days": 30,
        },
    )
    result = client.events.list()
    assert len(result.data) == 0
    assert not result.has_next_page()


def test_events_get_summary_basic(httpx_mock, client) -> None:
    """get_summary() returns EventsSummary with all fields."""
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/events/summary",
        json={
            "total": 100,
            "total_previous": 80,
            "failed": 5,
            "by_category": {"post": 60, "webhook": 40},
            "by_error_category": {"network": 3, "validation": 2},
            "inbox_breakdown": {"comment": 20, "review": 10},
            "retention_days": 30,
        },
    )
    summary = client.events.get_summary()
    assert summary.total == 100
    assert summary.total_previous == 80
    assert summary.failed == 5
    assert summary.by_category == {"post": 60, "webhook": 40}
    assert summary.by_error_category == {"network": 3, "validation": 2}
    assert summary.inbox_breakdown == {"comment": 20, "review": 10}
    assert summary.retention_days == 30


def test_events_get_summary_filters_sent(httpx_mock, client) -> None:
    """get_summary() sends from/to query params."""
    httpx_mock.add_response(
        url=(f"{BASE_URL}/v1/events/summary?from=2026-06-01T00%3A00%3A00Z&to=2026-06-08T00%3A00%3A00Z"),
        json={
            "total": 0,
            "failed": 0,
            "by_category": {},
            "by_error_category": {},
            "inbox_breakdown": {},
            "retention_days": 30,
        },
    )
    client.events.get_summary(
        since="2026-06-01T00:00:00Z",
        until="2026-06-08T00:00:00Z",
    )
    request = httpx_mock.get_request()
    assert request is not None
    qs = dict(request.url.params)
    assert qs["from"] == "2026-06-01T00:00:00Z"
    assert qs["to"] == "2026-06-08T00:00:00Z"


def test_events_get_summary_no_total_previous(httpx_mock, client) -> None:
    """get_summary() handles missing total_previous (null / omitted)."""
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/events/summary",
        json={
            "total": 10,
            "failed": 1,
            "by_category": {},
            "by_error_category": {},
            "inbox_breakdown": {},
            "retention_days": 7,
        },
    )
    summary = client.events.get_summary()
    assert summary.total_previous is None


# ---------------------------------------------------------------------------
# Async tests
# ---------------------------------------------------------------------------


async def test_events_list_async_basic(httpx_mock, async_client) -> None:
    """Async list() returns EventList with correct fields."""
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/events",
        json={
            "events": [
                {
                    "id": "evt_async_001",
                    "category": "inbox",
                    "action": "comment.received",
                    "status": "success",
                    "summary": "New comment",
                    "metadata": {"post_id": "p1"},
                    "created_at": "2026-06-01T12:00:00Z",
                }
            ],
            "pagination": {"limit": 50, "has_more": False, "next_cursor": None},
            "retention_days": 14,
        },
    )
    result = await async_client.events.list()
    assert result.retention_days == 14
    assert result.data[0].id == "evt_async_001"
    assert result.data[0].category == "inbox"


async def test_events_list_async_filters(httpx_mock, async_client) -> None:
    """Async list() sends all filter params including from/to wire names."""
    httpx_mock.add_response(
        url=(
            f"{BASE_URL}/v1/events?category=webhook&from=2026-06-01T00%3A00%3A00Z&to=2026-06-07T00%3A00%3A00Z&limit=5"
        ),
        json={
            "events": [],
            "pagination": {"limit": 5, "has_more": False, "next_cursor": None},
            "retention_days": 30,
        },
    )
    await async_client.events.list(
        category="webhook",
        since="2026-06-01T00:00:00Z",
        until="2026-06-07T00:00:00Z",
        limit=5,
    )
    request = httpx_mock.get_request()
    assert request is not None
    qs = dict(request.url.params)
    assert qs["category"] == "webhook"
    assert qs["from"] == "2026-06-01T00:00:00Z"
    assert qs["to"] == "2026-06-07T00:00:00Z"
    assert qs["limit"] == "5"


async def test_events_get_summary_async(httpx_mock, async_client) -> None:
    """Async get_summary() returns EventsSummary model."""
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/events/summary",
        json={
            "total": 50,
            "total_previous": None,
            "failed": 2,
            "by_category": {"post": 50},
            "by_error_category": {},
            "inbox_breakdown": {},
            "retention_days": 30,
        },
    )
    summary = await async_client.events.get_summary()
    assert summary.total == 50
    assert summary.failed == 2
    assert summary.by_category == {"post": 50}


async def test_events_get_summary_async_filters(httpx_mock, async_client) -> None:
    """Async get_summary() sends from/to params."""
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/events/summary?from=2026-06-01T00%3A00%3A00Z",
        json={
            "total": 0,
            "failed": 0,
            "by_category": {},
            "by_error_category": {},
            "inbox_breakdown": {},
            "retention_days": 30,
        },
    )
    await async_client.events.get_summary(since="2026-06-01T00:00:00Z")
    request = httpx_mock.get_request()
    assert request is not None
    qs = dict(request.url.params)
    assert qs["from"] == "2026-06-01T00:00:00Z"
    assert "to" not in qs
