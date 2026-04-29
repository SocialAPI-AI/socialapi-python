"""Tests for active-record-style bound action methods on domain models.

Each bound method has a parallel sync + async variant; this file exercises
both, plus the unbound / missing-context error paths.
"""

from __future__ import annotations

import pytest

from socialapi import (
    AsyncInboxComment,
    AsyncSocialAPI,
    InboxComment,
    MissingContextError,
    SocialAPI,
    UnboundModelError,
)

from .conftest import BASE_URL

ACCOUNT_JSON = {
    "id": "acc_001",
    "platform": "instagram",
    "name": "Acme",
    "username": "acme",
    "brand_id": "b_001",
    "bio": "Hello world",
    "profile_picture_url": "https://example.com/pic.jpg",
    "status": "active",
}

BRAND_JSON = {
    "id": "b_001",
    "name": "Acme Brand",
    "accounts_count": 2,
    "created_at": "2026-01-01T00:00:00Z",
    "updated_at": "2026-01-02T00:00:00Z",
}

COMMENT_JSON = {
    "id": "cmt_001",
    "inbox_post_id": "ip_001",
    "platform_id": "17890099999",
    "platform": "instagram",
    "text": "Great post!",
    "author_id": "user_external_1",
    "author_name": "Jane",
    "is_owner": False,
    "like_count": 0,
    "reply_count": 0,
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

CONVERSATION_JSON = {
    "id": "conv_001",
    "user_id": "usr_001",
    "account_id": "acc_001",
    "platform": "instagram",
    "platform_id": "17890099999",
    "participant_id": "p_001",
    "participant_name": "Alice",
    "status": "active",
    "unread_count": 0,
    "created_at": "2026-03-20T10:00:00Z",
    "updated_at": "2026-03-20T11:00:00Z",
}

POST_JSON = {
    "id": "post_001",
    "text": "Hello world",
    "status": "draft",
    "hidden": False,
    "retry_count": 0,
    "created_at": "2026-03-20T10:00:00Z",
    "updated_at": "2026-03-20T10:00:00Z",
}

REVIEW_JSON = {
    "id": "rev_001",
    "platform": "google",
    "account_id": "acc_001",
    "rating": 5,
    "text": "Awesome",
    "author": "Jane",
    "created_at": "2026-03-20T10:00:00Z",
}

WEBHOOK_JSON = {
    "id": "wh_001",
    "url": "https://example.com/webhook",
    "events": ["post.published"],
    "is_active": True,
    "created_at": "2026-03-20T10:00:00Z",
}

KEY_JSON = {
    "id": "key_001",
    "name": "My App",
    "preview": "sapi_key_...abc",
    "is_active": True,
    "created_at": "2026-03-20T10:00:00Z",
}

INVITE_LIST_JSON = {
    "id": "inv_001",
    "platform": "facebook",
    "token": "tok_abc",
    "url": "https://app.test.local/invite/tok_abc",
    "is_active": True,
    "expires_at": "2026-04-20T10:00:00Z",
    "created_at": "2026-03-20T10:00:00Z",
}

MEDIA_JSON = {
    "id": "med_001",
    "filename": "pic.jpg",
    "content_type": "image/jpeg",
    "size_bytes": 12345,
    "status": "verified",
    "url": "https://cdn.example.com/pic.jpg",
    "created_at": "2026-03-20T10:00:00Z",
}


# ---------------------------------------------------------------------------
# Unbound / missing-context error paths
# ---------------------------------------------------------------------------


def test_unbound_comment_reply_raises() -> None:
    """A comment built via model_validate() has no client; .reply() must raise."""
    comment = InboxComment.model_validate(COMMENT_JSON)
    with pytest.raises(UnboundModelError):
        comment.reply(text="hi")


def test_async_unbound_comment_reply_raises() -> None:
    comment = AsyncInboxComment.model_validate(COMMENT_JSON)
    with pytest.raises(UnboundModelError):

        async def _call() -> None:
            await comment.reply(text="hi")

        # The check happens before any await; we can call synchronously here
        import asyncio

        asyncio.run(_call())


def test_bound_comment_without_account_id_raises(httpx_mock, client: SocialAPI) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/posts/post_001",
        json=POST_JSON,
    )
    # Build a comment via Pydantic and bind only a client (no ctx) — like a
    # non-resource path might. Then calling .hide() should fail with a clear
    # error because account_id is required.
    client.posts.get("post_001")
    # Manually attach a comment without ctx
    comment = InboxComment.model_validate(COMMENT_JSON)
    comment._bind(client._client, {})  # bound but no account_id
    with pytest.raises(MissingContextError):
        comment.hide()


def test_sync_client_used_with_async_model_raises() -> None:
    """An AsyncInboxComment bound to a sync client raises on action."""
    client_sync = SocialAPI(api_key="sapi_key_test", base_url=BASE_URL, max_retries=0)
    comment = AsyncInboxComment.model_validate(COMMENT_JSON)
    comment._bind(client_sync._client, {"account_id": "acc_001"})

    async def _call() -> None:
        await comment.reply(text="hi")

    import asyncio

    with pytest.raises(UnboundModelError):
        asyncio.run(_call())


# ---------------------------------------------------------------------------
# Brand bound actions
# ---------------------------------------------------------------------------


def test_brand_update_via_bound_method(httpx_mock, client: SocialAPI) -> None:
    httpx_mock.add_response(url=f"{BASE_URL}/v1/brands", json={"data": [BRAND_JSON]})
    brands = client.brands.list()
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/brands/b_001",
        json={**BRAND_JSON, "name": "New Name"},
    )
    updated = brands[0].update(name="New Name")
    assert updated.name == "New Name"


def test_brand_delete_via_bound_method(httpx_mock, client: SocialAPI) -> None:
    httpx_mock.add_response(url=f"{BASE_URL}/v1/brands", json={"data": [BRAND_JSON]})
    brands = client.brands.list()
    httpx_mock.add_response(url=f"{BASE_URL}/v1/brands/b_001", status_code=204)
    brands[0].delete()


async def test_async_brand_update_via_bound_method(httpx_mock, async_client: AsyncSocialAPI) -> None:
    httpx_mock.add_response(url=f"{BASE_URL}/v1/brands", json={"data": [BRAND_JSON]})
    brands = await async_client.brands.list()
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/brands/b_001",
        json={**BRAND_JSON, "name": "New Name"},
    )
    updated = await brands[0].update(name="New Name")
    assert updated.name == "New Name"


# ---------------------------------------------------------------------------
# Comment bound actions (with ctx propagation)
# ---------------------------------------------------------------------------


def test_comment_reply_via_bound_method(httpx_mock, client: SocialAPI) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/inbox/comments/ip_001?account_id=acc_001",
        json={"data": [COMMENT_JSON], "pagination": {"has_more": False, "next_cursor": None}},
    )
    page = client.comments.list("ip_001", account_id="acc_001")
    comment = page.data[0]
    # ctx was seeded by list()
    assert comment._ctx == {"account_id": "acc_001", "inbox_post_id": "ip_001"}
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/inbox/comments/ip_001",
        json={"success": True, "comment_id": "new_cmt"},
    )
    result = comment.reply(text="Thanks!")
    assert result.comment_id == "new_cmt"


def test_comment_hide_via_bound_method(httpx_mock, client: SocialAPI) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/inbox/comments/ip_001?account_id=acc_001",
        json={"data": [COMMENT_JSON], "pagination": {"has_more": False, "next_cursor": None}},
    )
    page = client.comments.list("ip_001", account_id="acc_001")
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/inbox/comments/ip_001/cmt_001/hide",
        method="POST",
        status_code=200,
        json={"success": True},
    )
    page.data[0].hide()


async def test_async_comment_reply_via_bound_method(httpx_mock, async_client: AsyncSocialAPI) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/inbox/comments/ip_001?account_id=acc_001",
        json={"data": [COMMENT_JSON], "pagination": {"has_more": False, "next_cursor": None}},
    )
    page = await async_client.comments.list("ip_001", account_id="acc_001")
    comment = page.data[0]
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/inbox/comments/ip_001",
        json={"success": True, "comment_id": "new_cmt"},
    )
    result = await comment.reply(text="Thanks!")
    assert result.comment_id == "new_cmt"


def test_commented_post_list_comments_propagates_ctx(httpx_mock, client: SocialAPI) -> None:
    commented_post_json = {
        "id": "ip_001",
        "user_id": "usr_001",
        "account_id": "acc_001",
        "platform": "instagram",
        "platform_id": "17890",
        "comment_count": 5,
        "like_count": 0,
        "created_at": "2026-03-20T10:00:00Z",
        "updated_at": "2026-03-20T10:00:00Z",
    }
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/inbox/comments",
        json={"data": [commented_post_json], "pagination": {"has_more": False, "next_cursor": None}},
    )
    posts = client.comments.list_posts()
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/inbox/comments/ip_001?account_id=acc_001",
        json={"data": [COMMENT_JSON], "pagination": {"has_more": False, "next_cursor": None}},
    )
    sub_page = posts.data[0].list_comments()
    # ctx propagated to children
    assert sub_page.data[0]._ctx["account_id"] == "acc_001"
    assert sub_page.data[0]._ctx["inbox_post_id"] == "ip_001"


# ---------------------------------------------------------------------------
# Conversation bound actions
# ---------------------------------------------------------------------------


def test_conversation_send_message_via_bound_method(httpx_mock, client: SocialAPI) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/inbox/conversations/conv_001",
        json=CONVERSATION_JSON,
    )
    conv = client.conversations.get("conv_001")
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/inbox/conversations/conv_001/messages",
        json={"success": True, "message_id": "msg_001"},
    )
    result = conv.send_message(text="Hi!")
    assert result.message_id == "msg_001"


def test_conversation_mark_as_read_via_bound_method(httpx_mock, client: SocialAPI) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/inbox/conversations/conv_001",
        json=CONVERSATION_JSON,
    )
    conv = client.conversations.get("conv_001")
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/inbox/conversations/conv_001/read",
        method="POST",
        status_code=200,
        json={"success": True},
    )
    conv.mark_as_read()


# ---------------------------------------------------------------------------
# Post bound actions
# ---------------------------------------------------------------------------


def test_post_update_via_bound_method(httpx_mock, client: SocialAPI) -> None:
    httpx_mock.add_response(url=f"{BASE_URL}/v1/posts/post_001", json=POST_JSON)
    post = client.posts.get("post_001")
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/posts/post_001",
        method="PATCH",
        json={**POST_JSON, "text": "updated"},
    )
    updated = post.update(text="updated")
    assert updated.text == "updated"


def test_post_delete_via_bound_method(httpx_mock, client: SocialAPI) -> None:
    httpx_mock.add_response(url=f"{BASE_URL}/v1/posts/post_001", json=POST_JSON)
    post = client.posts.get("post_001")
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/posts/post_001",
        method="DELETE",
        status_code=204,
    )
    post.delete()


def test_post_get_metrics_via_bound_method(httpx_mock, client: SocialAPI) -> None:
    httpx_mock.add_response(url=f"{BASE_URL}/v1/posts/post_001", json=POST_JSON)
    post = client.posts.get("post_001")
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/posts/post_001/metrics",
        json={"data": {"post_id": "post_001", "targets": []}},
    )
    metrics = post.get_metrics()
    assert metrics.post_id == "post_001"


# ---------------------------------------------------------------------------
# Review bound actions
# ---------------------------------------------------------------------------


def test_review_reply_via_bound_method(httpx_mock, client: SocialAPI) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/inbox/reviews",
        json={"data": [REVIEW_JSON], "pagination": {"has_more": False, "next_cursor": None}},
    )
    page = client.reviews.list()
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/inbox/reviews/rev_001/reply",
        json={"success": True, "reply_id": "rep_001"},
    )
    result = page.data[0].reply(text="Thanks!")
    assert result.reply_id == "rep_001"


# ---------------------------------------------------------------------------
# Webhook bound actions
# ---------------------------------------------------------------------------


def test_webhook_update_via_bound_method(httpx_mock, client: SocialAPI) -> None:
    httpx_mock.add_response(url=f"{BASE_URL}/v1/webhooks", json={"data": [WEBHOOK_JSON]})
    hooks = client.webhooks.list()
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/webhooks/wh_001",
        method="PATCH",
        json={**WEBHOOK_JSON, "is_active": False},
    )
    updated = hooks[0].update(is_active=False)
    assert updated.is_active is False


def test_webhook_delete_via_bound_method(httpx_mock, client: SocialAPI) -> None:
    httpx_mock.add_response(url=f"{BASE_URL}/v1/webhooks", json={"data": [WEBHOOK_JSON]})
    hooks = client.webhooks.list()
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/webhooks/wh_001",
        method="DELETE",
        status_code=204,
    )
    hooks[0].delete()


# ---------------------------------------------------------------------------
# Key / Media / Invite bound actions
# ---------------------------------------------------------------------------


def test_apikey_revoke_via_bound_method(httpx_mock, client: SocialAPI) -> None:
    httpx_mock.add_response(url=f"{BASE_URL}/v1/keys", json={"data": [KEY_JSON]})
    keys = client.keys.list()
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/keys/key_001",
        method="DELETE",
        status_code=204,
    )
    keys[0].revoke()


def test_media_delete_via_bound_method(httpx_mock, client: SocialAPI) -> None:
    httpx_mock.add_response(url=f"{BASE_URL}/v1/media", json={"data": [MEDIA_JSON]})
    items = client.media.list()
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/media/med_001",
        method="DELETE",
        status_code=204,
    )
    items[0].delete()


def test_invite_revoke_via_bound_method(httpx_mock, client: SocialAPI) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/invites?brand_id=b_001",
        json={"data": [INVITE_LIST_JSON]},
    )
    invites = client.invites.list("b_001")
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/invites/inv_001",
        method="DELETE",
        status_code=204,
    )
    invites[0].revoke()


# ---------------------------------------------------------------------------
# Account bound actions (new endpoints)
# ---------------------------------------------------------------------------


def test_account_disconnect_via_bound_method(httpx_mock, client: SocialAPI) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/accounts",
        json={"data": [ACCOUNT_JSON], "pagination": {"has_more": False, "next_cursor": None}},
    )
    page = client.accounts.list()
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/accounts/acc_001",
        method="DELETE",
        status_code=204,
    )
    page.data[0].disconnect()


def test_account_get_creator_info_via_bound_method(httpx_mock, client: SocialAPI) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/accounts",
        json={"data": [ACCOUNT_JSON], "pagination": {"has_more": False, "next_cursor": None}},
    )
    page = client.accounts.list()
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/accounts/acc_001/creator-info",
        json={
            "platform": "tiktok",
            "nickname": "creator",
            "can_post": True,
            "max_video_duration_sec": 60,
        },
    )
    info = page.data[0].get_creator_info()
    assert info.platform == "tiktok"
    assert info.can_post is True


def test_account_list_pages_via_bound_method(httpx_mock, client: SocialAPI) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/accounts",
        json={"data": [ACCOUNT_JSON], "pagination": {"has_more": False, "next_cursor": None}},
    )
    page = client.accounts.list()
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/accounts/acc_001/pages",
        json={"data": [{"id": "pg_001", "name": "Page A", "is_default": True}]},
    )
    pages = page.data[0].list_pages()
    assert len(pages) == 1
    assert pages[0].id == "pg_001"
    # ctx seeded so .update() can build path
    assert pages[0]._ctx == {"account_id": "acc_001"}


def test_account_get_limits_via_bound_method(httpx_mock, client: SocialAPI) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/accounts",
        json={"data": [ACCOUNT_JSON], "pagination": {"has_more": False, "next_cursor": None}},
    )
    page = client.accounts.list()
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/accounts/acc_001/limits",
        json={"posts_remaining": 25},
    )
    limits = page.data[0].get_limits()
    assert limits.limits == {"posts_remaining": 25}


def test_account_export_via_bound_method(httpx_mock, client: SocialAPI) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/accounts",
        json={"data": [ACCOUNT_JSON], "pagination": {"has_more": False, "next_cursor": None}},
    )
    page = client.accounts.list()
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/accounts/acc_001/export",
        method="POST",
        status_code=202,
        json={"export_id": "exp_001", "status": "pending"},
    )
    result = page.data[0].export(include_transcript=True)
    assert result == {"export_id": "exp_001", "status": "pending"}


# ---------------------------------------------------------------------------
# Account schema additions (drift fix)
# ---------------------------------------------------------------------------


def test_account_new_fields_parse(httpx_mock, client: SocialAPI) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/accounts",
        json={"data": [ACCOUNT_JSON], "pagination": {"has_more": False, "next_cursor": None}},
    )
    page = client.accounts.list()
    acc = page.data[0]
    assert acc.bio == "Hello world"
    assert acc.profile_picture_url == "https://example.com/pic.jpg"
    assert acc.status == "active"
    assert acc.reconnect_reason is None
