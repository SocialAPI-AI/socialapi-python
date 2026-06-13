from __future__ import annotations

from .conftest import BASE_URL

POST_JSON = {
    "id": "post_001",
    "text": "Hello from SocialAPI!",
    "status": "published",
    "visibility": "public",
    "created_at": "2026-03-20T10:00:00Z",
    "updated_at": "2026-03-20T10:05:00Z",
    "targets": [
        {
            "platform": "instagram",
            "status": "published",
            "platform_post_id": "17890012345",
            "permalink": "https://instagram.com/p/abc123",
            "published_at": "2026-03-20T10:01:00Z",
            "metrics": {"likes": 120, "comments": 15, "shares": 8, "saves": 5},
        }
    ],
}

DELETE_RESPONSE_JSON = {
    "success": True,
    "deleted": True,
    "results": [
        {
            "platform": "instagram",
            "account_id": "acc_ig_001",
            "outcome": "deleted",
            "message": "",
        }
    ],
}


def test_list_posts(httpx_mock, client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/posts",
        json={"data": [POST_JSON], "pagination": {"has_more": False, "next_cursor": None}},
    )
    page = client.posts.list()
    assert len(page.data) == 1
    post = page.data[0]
    assert post.id == "post_001"
    assert post.status == "published"
    assert post.targets is not None
    assert post.targets[0].platform == "instagram"
    assert post.targets[0].metrics is not None
    assert post.targets[0].metrics.likes == 120


def test_list_posts_with_filters(httpx_mock, client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/posts?status=published&platform=instagram",
        json={"data": [POST_JSON], "pagination": {"has_more": False, "next_cursor": None}},
    )
    page = client.posts.list(status="published", platform="instagram")
    assert len(page.data) == 1


def test_list_posts_with_page_id(httpx_mock, client) -> None:
    """page_id query filter must be passed through."""
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/posts?page_id=sapi_page_001",
        json={"data": [POST_JSON], "pagination": {"has_more": False, "next_cursor": None}},
    )
    page = client.posts.list(page_id="sapi_page_001")
    assert len(page.data) == 1


def test_get_post(httpx_mock, client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/posts/post_001",
        json=POST_JSON,
    )
    post = client.posts.get("post_001")
    assert post.id == "post_001"
    assert post.text == "Hello from SocialAPI!"


def test_get_post_metrics(httpx_mock, client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/posts/post_001/metrics",
        json={
            "data": {
                "post_id": "post_001",
                "targets": [
                    {
                        "platform": "instagram",
                        "status": "published",
                        "metrics": {"likes": 150, "comments": 20, "shares": 10, "saves": 7},
                    }
                ],
            }
        },
    )
    metrics = client.posts.get_metrics("post_001")
    assert metrics.post_id == "post_001"
    assert len(metrics.targets) == 1
    assert metrics.targets[0].metrics is not None
    assert metrics.targets[0].metrics.likes == 150


def test_delete_post_returns_delete_response(httpx_mock, client) -> None:
    """DELETE /v1/posts/:pid returns DeletePostResponse."""
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/posts/post_001",
        json=DELETE_RESPONSE_JSON,
    )
    result = client.posts.delete("post_001")
    assert result is not None
    assert result.success is True
    assert result.deleted is True
    assert len(result.results) == 1
    assert result.results[0].platform == "instagram"
    assert result.results[0].outcome == "deleted"


def test_delete_post_no_platform_param(httpx_mock, client) -> None:
    """DELETE /v1/posts/:pid should NOT send a platform query param."""
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/posts/post_001",
        json=DELETE_RESPONSE_JSON,
    )
    result = client.posts.delete("post_001")
    req = httpx_mock.get_requests()[0]
    assert "platform" not in str(req.url)
    assert result is not None


def test_retry_post(httpx_mock, client) -> None:
    """retry() with {success: true} returns None (does NOT re-fetch)."""
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/posts/post_001/retry",
        json={"success": True},
    )
    result = client.posts.retry("post_001")
    assert result is None
    # Only one request should have been made (no re-fetch).
    assert len(httpx_mock.get_requests()) == 1


def test_list_posts_with_all_filters(httpx_mock, client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/posts?account_ids=acc_1%2Cacc_2&status=published&platform=instagram&from=2026-03-01&to=2026-03-31&search=hello&sort=-created_at&hidden=true&limit=10&cursor=abc",
        json={"data": [POST_JSON], "pagination": {"has_more": False, "next_cursor": None}},
    )
    page = client.posts.list(
        account_ids=["acc_1", "acc_2"],
        status="published",
        platform="instagram",
        from_date="2026-03-01",
        to_date="2026-03-31",
        search="hello",
        sort="-created_at",
        hidden=True,
        limit=10,
        cursor="abc",
    )
    assert len(page.data) == 1


def test_unpublish_post(httpx_mock, client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/posts/post_001/unpublish",
        status_code=204,
    )
    client.posts.unpublish("post_001")


def test_unpublish_post_with_account_id(httpx_mock, client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/posts/post_001/unpublish",
        status_code=204,
    )
    client.posts.unpublish("post_001", account_id="acc_ig_001")

    import json

    body = json.loads(httpx_mock.get_requests()[0].content)
    assert body["account_id"] == "acc_ig_001"


def test_post_target_has_page_id(httpx_mock, client) -> None:
    """PostTarget must parse page_id from PostTargetResponse."""
    post_with_page_id = {
        **POST_JSON,
        "targets": [
            {
                "platform": "facebook",
                "status": "published",
                "page_id": "sapi_page_001",
                "account_id": "acc_fb_001",
            }
        ],
    }
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/posts/post_001",
        json=post_with_page_id,
    )
    post = client.posts.get("post_001")
    assert post.targets is not None
    assert post.targets[0].page_id == "sapi_page_001"


def test_post_target_error_has_code(httpx_mock, client) -> None:
    """PostTargetError must include code field from PostTargetErrorResponse."""
    post_with_error = {
        **POST_JSON,
        "targets": [
            {
                "platform": "tiktok",
                "status": "failed",
                "error": {
                    "code": "platform.tiktok.media_required",
                    "message": "Video posts require at least one media URL",
                    "category": "validation",
                    "caused_by": "user",
                },
            }
        ],
    }
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/posts/post_001",
        json=post_with_error,
    )
    post = client.posts.get("post_001")
    assert post.targets is not None
    err = post.targets[0].error
    assert err is not None
    assert err.code == "platform.tiktok.media_required"
    assert err.message == "Video posts require at least one media URL"
    assert err.category == "validation"
    assert err.caused_by == "user"


async def test_list_posts_async(httpx_mock, async_client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/posts",
        json={"data": [POST_JSON], "pagination": {"has_more": False, "next_cursor": None}},
    )
    page = await async_client.posts.list()
    assert len(page.data) == 1
    assert page.data[0].id == "post_001"


async def test_list_posts_async_with_filters(httpx_mock, async_client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/posts?status=draft&platform=linkedin&limit=5",
        json={"data": [], "pagination": {"has_more": False, "next_cursor": None}},
    )
    page = await async_client.posts.list(status="draft", platform="linkedin", limit=5)
    assert len(page.data) == 0


async def test_list_posts_async_with_page_id(httpx_mock, async_client) -> None:
    """page_id query filter must be passed through (async)."""
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/posts?page_id=sapi_page_001",
        json={"data": [], "pagination": {"has_more": False, "next_cursor": None}},
    )
    page = await async_client.posts.list(page_id="sapi_page_001")
    assert len(page.data) == 0


async def test_list_posts_async_with_all_filters(httpx_mock, async_client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/posts?account_ids=a1%2Ca2&status=published&platform=instagram&from=2026-03-01&to=2026-03-31&search=test&sort=-created_at&hidden=false&limit=20&cursor=xyz",
        json={"data": [POST_JSON], "pagination": {"has_more": False, "next_cursor": None}},
    )
    page = await async_client.posts.list(
        account_ids=["a1", "a2"],
        status="published",
        platform="instagram",
        from_date="2026-03-01",
        to_date="2026-03-31",
        search="test",
        sort="-created_at",
        hidden=False,
        limit=20,
        cursor="xyz",
    )
    assert len(page.data) == 1


async def test_get_post_async(httpx_mock, async_client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/posts/post_001",
        json=POST_JSON,
    )
    post = await async_client.posts.get("post_001")
    assert post.id == "post_001"
    assert post.text == "Hello from SocialAPI!"


async def test_delete_post_async_returns_delete_response(httpx_mock, async_client) -> None:
    """DELETE /v1/posts/:pid returns DeletePostResponse (async)."""
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/posts/post_001",
        json=DELETE_RESPONSE_JSON,
    )
    result = await async_client.posts.delete("post_001")
    assert result is not None
    assert result.success is True
    assert result.deleted is True
    assert len(result.results) == 1
    assert result.results[0].platform == "instagram"


async def test_delete_post_async_no_platform_param(httpx_mock, async_client) -> None:
    """DELETE /v1/posts/:pid should NOT send a platform query param (async)."""
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/posts/post_001",
        json=DELETE_RESPONSE_JSON,
    )
    result = await async_client.posts.delete("post_001")
    req = httpx_mock.get_requests()[0]
    assert "platform" not in str(req.url)
    assert result is not None


async def test_retry_post_async(httpx_mock, async_client) -> None:
    """retry() with {success: true} returns None (does NOT re-fetch) (async)."""
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/posts/post_001/retry",
        json={"success": True},
    )
    result = await async_client.posts.retry("post_001")
    assert result is None
    assert len(httpx_mock.get_requests()) == 1


async def test_unpublish_post_async(httpx_mock, async_client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/posts/post_001/unpublish",
        status_code=204,
    )
    await async_client.posts.unpublish("post_001")


async def test_unpublish_post_async_with_account_id(httpx_mock, async_client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/posts/post_001/unpublish",
        status_code=204,
    )
    await async_client.posts.unpublish("post_001", account_id="acc_ig_001")


async def test_get_metrics_async(httpx_mock, async_client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/posts/post_001/metrics",
        json={
            "data": {
                "post_id": "post_001",
                "targets": [
                    {
                        "platform": "instagram",
                        "status": "published",
                        "metrics": {"likes": 200, "comments": 30},
                    }
                ],
            }
        },
    )
    metrics = await async_client.posts.get_metrics("post_001")
    assert metrics.post_id == "post_001"
    assert len(metrics.targets) == 1
