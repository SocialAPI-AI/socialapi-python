"""Tests for comments resource."""

from __future__ import annotations

from typing import TYPE_CHECKING

from socialapi.models.interactions import InteractionsListResponse
from socialapi.models.shared import OKResponse

if TYPE_CHECKING:
    from socialapi import AsyncSocialAPI, SocialAPI

BASE = "https://api.social-api.ai"

INTERACTION_DATA = {
    "id": "int_001",
    "platform": "instagram",
    "type": "comment",
    "author": {"id": "author_1", "name": "Jane", "avatar_url": ""},
    "content": {"text": "Nice post!", "media": []},
    "metadata": {},
    "created_at": "2025-01-15T08:30:00Z",
    "account_id": "acc_123",
    "platform_id": "ig_comment_456",
}


def test_comments_list(httpx_mock, client: SocialAPI) -> None:
    httpx_mock.add_response(
        json={"data": [INTERACTION_DATA], "count": 1},
    )
    result = client.comments.list("acc_123", "post_456")
    assert isinstance(result, InteractionsListResponse)
    assert len(result.data) == 1
    assert result.data[0].id == "int_001"
    assert result.count == 1


def test_comments_replies(httpx_mock, client: SocialAPI) -> None:
    reply_data = {**INTERACTION_DATA, "id": "int_reply_001", "content": {"text": "Thanks!", "media": []}}
    httpx_mock.add_response(
        json={"data": [reply_data], "count": 1},
    )
    result = client.comments.replies("acc_123", "int_001")
    assert isinstance(result, InteractionsListResponse)
    assert len(result.data) == 1
    assert result.data[0].id == "int_reply_001"


def test_comments_moderate(httpx_mock, client: SocialAPI) -> None:
    httpx_mock.add_response(
        json={"ok": True},
    )
    result = client.comments.moderate("acc_123", "int_001", "hide")
    assert isinstance(result, OKResponse)
    assert result.ok is True


def test_comments_toggle(httpx_mock, client: SocialAPI) -> None:
    httpx_mock.add_response(
        json={"ok": True},
    )
    result = client.comments.toggle("acc_123", "post_456", enabled=False)
    assert isinstance(result, OKResponse)
    assert result.ok is True


# -- Async tests --


async def test_async_comments_list(httpx_mock, async_client: AsyncSocialAPI) -> None:
    httpx_mock.add_response(
        json={"data": [INTERACTION_DATA], "count": 1},
    )
    result = await async_client.comments.list("acc_123", "post_456")
    assert isinstance(result, InteractionsListResponse)
    assert len(result.data) == 1


async def test_async_comments_moderate(httpx_mock, async_client: AsyncSocialAPI) -> None:
    httpx_mock.add_response(
        json={"ok": True},
    )
    result = await async_client.comments.moderate("acc_123", "int_001", "delete")
    assert isinstance(result, OKResponse)
    assert result.ok is True
