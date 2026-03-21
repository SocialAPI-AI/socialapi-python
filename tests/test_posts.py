"""Tests for posts resource."""

from __future__ import annotations

from typing import TYPE_CHECKING

from socialapi.models.posts import ScheduledPost, ScheduledPostsListResponse
from socialapi.models.shared import SuccessResponse

if TYPE_CHECKING:
    from socialapi import AsyncSocialAPI, SocialAPI

BASE = "https://api.social-api.ai"

SCHEDULED_POST_DATA = {
    "id": "post_001",
    "user_id": "user_1",
    "account_ids": ["acc_123"],
    "text": "Hello world",
    "media_ids": [],
    "platform_options": {},
    "status": "scheduled",
    "scheduled_at": "2025-06-01T12:00:00Z",
    "created_at": "2025-05-01T10:00:00Z",
    "updated_at": "2025-05-01T10:00:00Z",
    "results": [],
}


def test_posts_list(httpx_mock, client: SocialAPI) -> None:
    httpx_mock.add_response(
        json={"data": [SCHEDULED_POST_DATA], "cursor": None},
    )
    result = client.posts.list("2025-01-01", "2025-12-31")
    assert isinstance(result, ScheduledPostsListResponse)
    assert len(result.data) == 1
    assert result.data[0].id == "post_001"


def test_posts_create(httpx_mock, client: SocialAPI) -> None:
    httpx_mock.add_response(
        url=f"{BASE}/v1/posts",
        json=SCHEDULED_POST_DATA,
    )
    result = client.posts.create(["acc_123"], "Hello world")
    assert isinstance(result, ScheduledPost)
    assert result.id == "post_001"
    assert result.text == "Hello world"


def test_posts_update(httpx_mock, client: SocialAPI) -> None:
    httpx_mock.add_response(
        url=f"{BASE}/v1/posts/post_001",
        json={"success": True},
    )
    result = client.posts.update("post_001", text="Updated text")
    assert isinstance(result, SuccessResponse)
    assert result.success is True


def test_posts_delete(httpx_mock, client: SocialAPI) -> None:
    httpx_mock.add_response(
        url=f"{BASE}/v1/posts/post_001",
        json={"success": True},
    )
    result = client.posts.delete("post_001")
    assert isinstance(result, SuccessResponse)
    assert result.success is True


def test_posts_retry(httpx_mock, client: SocialAPI) -> None:
    httpx_mock.add_response(
        url=f"{BASE}/v1/posts/post_001/retry",
        json={"success": True},
    )
    result = client.posts.retry("post_001")
    assert isinstance(result, SuccessResponse)
    assert result.success is True


# -- Async tests --


async def test_async_posts_create(httpx_mock, async_client: AsyncSocialAPI) -> None:
    httpx_mock.add_response(
        url=f"{BASE}/v1/posts",
        json=SCHEDULED_POST_DATA,
    )
    result = await async_client.posts.create(["acc_123"], "Hello world")
    assert isinstance(result, ScheduledPost)
    assert result.id == "post_001"
