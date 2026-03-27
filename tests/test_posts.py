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


def test_delete_post(httpx_mock, client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/posts/post_001",
        status_code=204,
    )
    client.posts.delete("post_001")


def test_retry_post(httpx_mock, client) -> None:
    retried = {**POST_JSON, "status": "publishing", "retry_count": 1}
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/posts/post_001/retry",
        json=retried,
    )
    post = client.posts.retry("post_001")
    assert post.status == "publishing"


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


def test_delete_post_with_platform(httpx_mock, client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/posts/post_001?platform=instagram",
        status_code=204,
    )
    client.posts.delete("post_001", platform="instagram")


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


def test_retry_post_success_response(httpx_mock, client) -> None:
    """When retry returns {"success": true}, it re-fetches the post."""
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/posts/post_001/retry",
        json={"success": True},
    )
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/posts/post_001",
        json={**POST_JSON, "status": "publishing"},
    )
    post = client.posts.retry("post_001")
    assert post.status == "publishing"


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


async def test_delete_post_async(httpx_mock, async_client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/posts/post_001",
        status_code=204,
    )
    await async_client.posts.delete("post_001")


async def test_delete_post_async_with_platform(httpx_mock, async_client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/posts/post_001?platform=facebook",
        status_code=204,
    )
    await async_client.posts.delete("post_001", platform="facebook")


async def test_retry_post_async(httpx_mock, async_client) -> None:
    retried = {**POST_JSON, "status": "publishing"}
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/posts/post_001/retry",
        json=retried,
    )
    post = await async_client.posts.retry("post_001")
    assert post.status == "publishing"


async def test_retry_post_async_success_response(httpx_mock, async_client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/posts/post_001/retry",
        json={"success": True},
    )
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/posts/post_001",
        json={**POST_JSON, "status": "publishing"},
    )
    post = await async_client.posts.retry("post_001")
    assert post.status == "publishing"


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
