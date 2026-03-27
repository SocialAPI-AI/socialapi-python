from __future__ import annotations

from datetime import UTC, datetime

from .conftest import BASE_URL


def test_get_usage(httpx_mock, client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/usage",
        json={
            "brands_used": 3,
            "brands_limit": 10,
            "posts_used": 45,
            "posts_limit": -1,
            "interactions_used": 120,
            "interactions_limit": -1,
            "period_start": "2026-03-01T00:00:00Z",
            "period_end": "2026-03-31T23:59:59Z",
        },
    )
    usage = client.usage.get()
    assert usage.brands_used == 3
    assert usage.brands_limit == 10
    assert usage.posts_used == 45
    assert usage.posts_limit == -1
    assert usage.period_start == datetime(2026, 3, 1, tzinfo=UTC)


def test_get_account_limits(httpx_mock, client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/accounts/acc_ig_001/limits",
        json={"posts_remaining": 95, "api_calls_remaining": 4800},
    )
    limits = client.usage.get_account_limits("acc_ig_001")
    assert limits.limits["posts_remaining"] == 95
    assert limits.limits["api_calls_remaining"] == 4800


def test_get_account_limits_with_limits_key(httpx_mock, client) -> None:
    """Test the branch where the API returns {"limits": {...}}."""
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/accounts/acc_ig_001/limits",
        json={"limits": {"posts_remaining": 50, "api_calls_remaining": 2000}},
    )
    limits = client.usage.get_account_limits("acc_ig_001")
    assert limits.limits["posts_remaining"] == 50


async def test_get_usage_async(httpx_mock, async_client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/usage",
        json={
            "brands_used": 1,
            "brands_limit": 2,
            "posts_used": 5,
            "posts_limit": 10,
            "interactions_used": 20,
            "interactions_limit": 50,
            "period_start": "2026-03-01T00:00:00Z",
            "period_end": "2026-03-31T23:59:59Z",
        },
    )
    usage = await async_client.usage.get()
    assert usage.brands_used == 1


async def test_get_account_limits_async(httpx_mock, async_client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/accounts/acc_ig_001/limits",
        json={"posts_remaining": 80},
    )
    limits = await async_client.usage.get_account_limits("acc_ig_001")
    assert limits.limits["posts_remaining"] == 80


async def test_get_account_limits_async_with_limits_key(httpx_mock, async_client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/accounts/acc_ig_001/limits",
        json={"limits": {"posts_remaining": 30}},
    )
    limits = await async_client.usage.get_account_limits("acc_ig_001")
    assert limits.limits["posts_remaining"] == 30
