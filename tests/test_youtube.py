from __future__ import annotations

from .conftest import BASE_URL

# ---------------------------------------------------------------------------
# Sync tests
# ---------------------------------------------------------------------------


def test_youtube_get_channel_summary(httpx_mock, client) -> None:
    """get_channel_summary() returns YouTubeChannelSummary with all fields."""
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/platforms/youtube/accounts/acc_yt_001/summary",
        json={
            "title": "My Channel",
            "handle": "@mychannel",
            "thumbnail_url": "https://example.com/thumb.jpg",
            "subscriber_count": 1000,
            "view_count": 50000,
            "video_count": 42,
        },
    )
    summary = client.youtube.get_channel_summary("acc_yt_001")
    assert summary.title == "My Channel"
    assert summary.handle == "@mychannel"
    assert summary.thumbnail_url == "https://example.com/thumb.jpg"
    assert summary.subscriber_count == 1000
    assert summary.view_count == 50000
    assert summary.video_count == 42


def test_youtube_sync_account(httpx_mock, client) -> None:
    """sync_account() returns None on success."""
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/platforms/youtube/accounts/acc_yt_001/sync",
        method="POST",
        json={"success": True},
    )
    result = client.youtube.sync_account("acc_yt_001")
    assert result is None


def test_youtube_sync_account_request(httpx_mock, client) -> None:
    """sync_account() sends POST to the correct path."""
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/platforms/youtube/accounts/acc_yt_002/sync",
        method="POST",
        json={"success": True},
    )
    client.youtube.sync_account("acc_yt_002")
    request = httpx_mock.get_request()
    assert request is not None
    assert request.method == "POST"
    assert "/v1/platforms/youtube/accounts/acc_yt_002/sync" in str(request.url)


def test_youtube_update_video_title_only(httpx_mock, client) -> None:
    """update_video() sends only the provided fields in the body."""
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/platforms/youtube/accounts/acc_yt_001/videos/vid_001",
        method="PATCH",
        json={"success": True},
    )
    result = client.youtube.update_video("acc_yt_001", "vid_001", title="New Title")
    assert result is None
    request = httpx_mock.get_request()
    assert request is not None
    import json as _json

    body = _json.loads(request.content)
    assert body == {"title": "New Title"}


def test_youtube_update_video_all_fields(httpx_mock, client) -> None:
    """update_video() sends all set fields in the body."""
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/platforms/youtube/accounts/acc_yt_001/videos/vid_002",
        method="PATCH",
        json={"success": True},
    )
    client.youtube.update_video(
        "acc_yt_001",
        "vid_002",
        title="Updated Title",
        description="New description",
        visibility="private",
    )
    request = httpx_mock.get_request()
    assert request is not None
    import json as _json

    body = _json.loads(request.content)
    assert body["title"] == "Updated Title"
    assert body["description"] == "New description"
    assert body["visibility"] == "private"


def test_youtube_update_video_no_fields(httpx_mock, client) -> None:
    """update_video() sends empty body when no fields are provided."""
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/platforms/youtube/accounts/acc_yt_001/videos/vid_003",
        method="PATCH",
        json={"success": True},
    )
    client.youtube.update_video("acc_yt_001", "vid_003")
    request = httpx_mock.get_request()
    assert request is not None
    import json as _json

    body = _json.loads(request.content)
    assert body == {}


def test_youtube_edit_comment(httpx_mock, client) -> None:
    """edit_comment() sends the correct body fields."""
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/platforms/youtube/comments/cmt_001",
        method="PATCH",
        json={"success": True},
    )
    result = client.youtube.edit_comment(
        "cmt_001",
        account_id="acc_yt_001",
        post_id="post_001",
        text="Updated comment text",
    )
    assert result is None
    request = httpx_mock.get_request()
    assert request is not None
    import json as _json

    body = _json.loads(request.content)
    assert body["account_id"] == "acc_yt_001"
    assert body["post_id"] == "post_001"
    assert body["text"] == "Updated comment text"


def test_youtube_moderate_comment_published(httpx_mock, client) -> None:
    """moderate_comment() with status=published sends correct body."""
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/platforms/youtube/comments/cmt_002/moderate",
        method="POST",
        json={"success": True},
    )
    result = client.youtube.moderate_comment(
        "cmt_002",
        account_id="acc_yt_001",
        post_id="post_002",
        status="published",
    )
    assert result is None
    request = httpx_mock.get_request()
    assert request is not None
    import json as _json

    body = _json.loads(request.content)
    assert body["account_id"] == "acc_yt_001"
    assert body["post_id"] == "post_002"
    assert body["status"] == "published"
    assert body.get("ban_author") is None or body.get("ban_author") is False


def test_youtube_moderate_comment_rejected_with_ban(httpx_mock, client) -> None:
    """moderate_comment() with status=rejected and ban_author=True."""
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/platforms/youtube/comments/cmt_003/moderate",
        method="POST",
        json={"success": True},
    )
    client.youtube.moderate_comment(
        "cmt_003",
        account_id="acc_yt_001",
        post_id="post_003",
        status="rejected",
        ban_author=True,
    )
    request = httpx_mock.get_request()
    assert request is not None
    import json as _json

    body = _json.loads(request.content)
    assert body["status"] == "rejected"
    assert body["ban_author"] is True


def test_youtube_moderate_comment_held(httpx_mock, client) -> None:
    """moderate_comment() with status=held_for_review sends correct body."""
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/platforms/youtube/comments/cmt_004/moderate",
        method="POST",
        json={"success": True},
    )
    client.youtube.moderate_comment(
        "cmt_004",
        account_id="acc_yt_001",
        post_id="post_004",
        status="held_for_review",
    )
    request = httpx_mock.get_request()
    assert request is not None
    import json as _json

    body = _json.loads(request.content)
    assert body["status"] == "held_for_review"


# ---------------------------------------------------------------------------
# Async tests
# ---------------------------------------------------------------------------


async def test_youtube_get_channel_summary_async(httpx_mock, async_client) -> None:
    """Async get_channel_summary() returns YouTubeChannelSummary."""
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/platforms/youtube/accounts/acc_yt_001/summary",
        json={
            "title": "Async Channel",
            "handle": "@async",
            "thumbnail_url": "https://example.com/t.jpg",
            "subscriber_count": 500,
            "view_count": 10000,
            "video_count": 5,
        },
    )
    summary = await async_client.youtube.get_channel_summary("acc_yt_001")
    assert summary.title == "Async Channel"
    assert summary.subscriber_count == 500


async def test_youtube_sync_account_async(httpx_mock, async_client) -> None:
    """Async sync_account() returns None."""
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/platforms/youtube/accounts/acc_yt_001/sync",
        method="POST",
        json={"success": True},
    )
    result = await async_client.youtube.sync_account("acc_yt_001")
    assert result is None


async def test_youtube_update_video_async(httpx_mock, async_client) -> None:
    """Async update_video() sends only set fields."""
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/platforms/youtube/accounts/acc_yt_001/videos/vid_a1",
        method="PATCH",
        json={"success": True},
    )
    result = await async_client.youtube.update_video("acc_yt_001", "vid_a1", description="New desc")
    assert result is None
    request = httpx_mock.get_request()
    assert request is not None
    import json as _json

    body = _json.loads(request.content)
    assert body == {"description": "New desc"}


async def test_youtube_edit_comment_async(httpx_mock, async_client) -> None:
    """Async edit_comment() sends correct body."""
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/platforms/youtube/comments/cmt_a1",
        method="PATCH",
        json={"success": True},
    )
    result = await async_client.youtube.edit_comment(
        "cmt_a1",
        account_id="acc_yt_001",
        post_id="post_a1",
        text="Async edited text",
    )
    assert result is None
    request = httpx_mock.get_request()
    assert request is not None
    import json as _json

    body = _json.loads(request.content)
    assert body["text"] == "Async edited text"
    assert body["account_id"] == "acc_yt_001"
    assert body["post_id"] == "post_a1"


async def test_youtube_moderate_comment_async(httpx_mock, async_client) -> None:
    """Async moderate_comment() sends correct body with status."""
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/platforms/youtube/comments/cmt_a2/moderate",
        method="POST",
        json={"success": True},
    )
    result = await async_client.youtube.moderate_comment(
        "cmt_a2",
        account_id="acc_yt_001",
        post_id="post_a2",
        status="held_for_review",
    )
    assert result is None
    request = httpx_mock.get_request()
    assert request is not None
    import json as _json

    body = _json.loads(request.content)
    assert body["status"] == "held_for_review"
    assert body["account_id"] == "acc_yt_001"
