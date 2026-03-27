from __future__ import annotations

from .conftest import BASE_URL

COMMENTED_POST_JSON = {
    "id": "ip_001",
    "user_id": "usr_001",
    "account_id": "acc_ig_001",
    "platform": "instagram",
    "platform_id": "17890012345",
    "content": "My first post",
    "comment_count": 5,
    "like_count": 42,
    "created_at": "2026-03-20T10:00:00Z",
    "updated_at": "2026-03-20T12:00:00Z",
}

COMMENT_JSON = {
    "id": "cmt_001",
    "inbox_post_id": "ip_001",
    "platform_id": "17890099999",
    "platform": "instagram",
    "text": "Great post!",
    "author_id": "user_external_1",
    "author_name": "Jane Doe",
    "author_username": "janedoe",
    "is_owner": False,
    "like_count": 3,
    "reply_count": 1,
    "is_hidden": False,
    "is_liked": False,
    "created_at": "2026-03-20T11:00:00Z",
    "capabilities": {
        "can_reply": True,
        "can_delete": True,
        "can_hide": True,
        "can_like": True,
        "can_private_reply": True,
    },
}


def test_list_commented_posts(httpx_mock, client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/inbox/comments",
        json={"data": [COMMENTED_POST_JSON], "pagination": {"has_more": False, "next_cursor": None}},
    )
    page = client.comments.list_posts()
    assert len(page.data) == 1
    assert page.data[0].id == "ip_001"
    assert page.data[0].comment_count == 5


def test_list_post_comments(httpx_mock, client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/inbox/comments/ip_001?account_id=acc_ig_001",
        json={"data": [COMMENT_JSON], "pagination": {"has_more": False, "next_cursor": None}},
    )
    page = client.comments.list("ip_001", account_id="acc_ig_001")
    assert len(page.data) == 1
    assert page.data[0].text == "Great post!"
    assert page.data[0].capabilities.can_reply is True


def test_reply_to_comment(httpx_mock, client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/inbox/comments/ip_001",
        json={"success": True, "comment_id": "cmt_new_001"},
    )
    result = client.comments.reply("ip_001", account_id="acc_ig_001", text="Thanks!")
    assert result.success is True
    assert result.comment_id == "cmt_new_001"


def test_delete_comment(httpx_mock, client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/inbox/comments/ip_001/cmt_001?account_id=acc_ig_001",
        status_code=204,
    )
    client.comments.delete("ip_001", "cmt_001", account_id="acc_ig_001")


def test_hide_comment(httpx_mock, client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/inbox/comments/ip_001/cmt_001/hide",
        status_code=204,
    )
    client.comments.hide("ip_001", "cmt_001", account_id="acc_ig_001")


def test_unhide_comment(httpx_mock, client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/inbox/comments/ip_001/cmt_001/hide?account_id=acc_ig_001",
        status_code=204,
    )
    client.comments.unhide("ip_001", "cmt_001", account_id="acc_ig_001")


def test_like_comment(httpx_mock, client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/inbox/comments/ip_001/cmt_001/like",
        status_code=204,
    )
    client.comments.like("ip_001", "cmt_001", account_id="acc_ig_001")


def test_unlike_comment(httpx_mock, client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/inbox/comments/ip_001/cmt_001/like?account_id=acc_ig_001",
        status_code=204,
    )
    client.comments.unlike("ip_001", "cmt_001", account_id="acc_ig_001")


def test_private_reply(httpx_mock, client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/inbox/comments/ip_001/cmt_001/private-reply",
        status_code=204,
    )
    client.comments.private_reply("ip_001", "cmt_001", account_id="acc_ig_001", text="Hi there!")


def test_list_commented_posts_with_filters(httpx_mock, client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/inbox/comments?account_id=acc_ig_001&platform=instagram&limit=5&cursor=cur_1",
        json={"data": [COMMENTED_POST_JSON], "pagination": {"has_more": False, "next_cursor": None}},
    )
    page = client.comments.list_posts(account_id="acc_ig_001", platform="instagram", limit=5, cursor="cur_1")
    assert len(page.data) == 1


def test_list_post_comments_with_pagination(httpx_mock, client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/inbox/comments/ip_001?account_id=acc_ig_001&limit=10&cursor=c1",
        json={"data": [COMMENT_JSON], "pagination": {"has_more": False, "next_cursor": None}},
    )
    page = client.comments.list("ip_001", account_id="acc_ig_001", limit=10, cursor="c1")
    assert len(page.data) == 1


def test_reply_with_comment_id(httpx_mock, client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/inbox/comments/ip_001",
        json={"success": True, "comment_id": "cmt_new_002"},
    )
    result = client.comments.reply("ip_001", account_id="acc_ig_001", text="Thread reply", comment_id="cmt_001")
    assert result.comment_id == "cmt_new_002"

    import json

    body = json.loads(httpx_mock.get_requests()[0].content)
    assert body["comment_id"] == "cmt_001"


async def test_list_commented_posts_async(httpx_mock, async_client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/inbox/comments",
        json={"data": [COMMENTED_POST_JSON], "pagination": {"has_more": False, "next_cursor": None}},
    )
    page = await async_client.comments.list_posts()
    assert len(page.data) == 1
    assert page.data[0].id == "ip_001"


async def test_list_commented_posts_async_with_filters(httpx_mock, async_client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/inbox/comments?account_id=acc_ig_001&platform=instagram&limit=3&cursor=x",
        json={"data": [], "pagination": {"has_more": False, "next_cursor": None}},
    )
    page = await async_client.comments.list_posts(account_id="acc_ig_001", platform="instagram", limit=3, cursor="x")
    assert len(page.data) == 0


async def test_list_post_comments_async(httpx_mock, async_client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/inbox/comments/ip_001?account_id=acc_ig_001",
        json={"data": [COMMENT_JSON], "pagination": {"has_more": False, "next_cursor": None}},
    )
    page = await async_client.comments.list("ip_001", account_id="acc_ig_001")
    assert len(page.data) == 1
    assert page.data[0].author_name == "Jane Doe"


async def test_list_post_comments_async_with_pagination(httpx_mock, async_client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/inbox/comments/ip_001?account_id=acc_ig_001&limit=5&cursor=cc",
        json={"data": [COMMENT_JSON], "pagination": {"has_more": False, "next_cursor": None}},
    )
    page = await async_client.comments.list("ip_001", account_id="acc_ig_001", limit=5, cursor="cc")
    assert len(page.data) == 1


async def test_reply_async(httpx_mock, async_client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/inbox/comments/ip_001",
        json={"success": True, "comment_id": "cmt_async_001"},
    )
    result = await async_client.comments.reply("ip_001", account_id="acc_ig_001", text="Async reply")
    assert result.success is True
    assert result.comment_id == "cmt_async_001"


async def test_reply_async_with_comment_id(httpx_mock, async_client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/inbox/comments/ip_001",
        json={"success": True, "comment_id": "cmt_async_002"},
    )
    result = await async_client.comments.reply("ip_001", account_id="acc_ig_001", text="Threaded", comment_id="cmt_001")
    assert result.comment_id == "cmt_async_002"


async def test_delete_comment_async(httpx_mock, async_client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/inbox/comments/ip_001/cmt_001?account_id=acc_ig_001",
        status_code=204,
    )
    await async_client.comments.delete("ip_001", "cmt_001", account_id="acc_ig_001")


async def test_hide_comment_async(httpx_mock, async_client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/inbox/comments/ip_001/cmt_001/hide",
        status_code=204,
    )
    await async_client.comments.hide("ip_001", "cmt_001", account_id="acc_ig_001")


async def test_unhide_comment_async(httpx_mock, async_client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/inbox/comments/ip_001/cmt_001/hide?account_id=acc_ig_001",
        status_code=204,
    )
    await async_client.comments.unhide("ip_001", "cmt_001", account_id="acc_ig_001")


async def test_like_comment_async(httpx_mock, async_client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/inbox/comments/ip_001/cmt_001/like",
        status_code=204,
    )
    await async_client.comments.like("ip_001", "cmt_001", account_id="acc_ig_001")


async def test_unlike_comment_async(httpx_mock, async_client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/inbox/comments/ip_001/cmt_001/like?account_id=acc_ig_001",
        status_code=204,
    )
    await async_client.comments.unlike("ip_001", "cmt_001", account_id="acc_ig_001")


async def test_private_reply_async(httpx_mock, async_client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/inbox/comments/ip_001/cmt_001/private-reply",
        status_code=204,
    )
    await async_client.comments.private_reply("ip_001", "cmt_001", account_id="acc_ig_001", text="Private msg")
