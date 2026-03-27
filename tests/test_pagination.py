from __future__ import annotations

from socialapi import AsyncSocialAPI, SocialAPI

from .conftest import BASE_URL, TEST_API_KEY


def _post_json(post_id: str) -> dict:
    return {
        "id": post_id,
        "text": f"Post {post_id}",
        "status": "published",
        "created_at": "2026-03-20T10:00:00Z",
        "updated_at": "2026-03-20T10:00:00Z",
    }


def test_cursor_page_iteration(httpx_mock) -> None:
    """A single page should yield items via __iter__."""
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/posts",
        json={
            "data": [_post_json("p1"), _post_json("p2")],
            "pagination": {"has_more": False, "next_cursor": None},
        },
    )
    client = SocialAPI(api_key=TEST_API_KEY, base_url=BASE_URL, max_retries=0)
    page = client.posts.list()
    items = list(page)
    assert len(items) == 2
    assert items[0].id == "p1"
    assert items[1].id == "p2"
    client.close()


def test_cursor_page_auto_pagination(httpx_mock) -> None:
    """Auto-pagination should fetch multiple pages and yield all items."""
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/posts",
        json={
            "data": [_post_json("p1")],
            "pagination": {"has_more": True, "next_cursor": "cursor_abc"},
        },
    )
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/posts?cursor=cursor_abc",
        json={
            "data": [_post_json("p2")],
            "pagination": {"has_more": False, "next_cursor": None},
        },
    )
    client = SocialAPI(api_key=TEST_API_KEY, base_url=BASE_URL, max_retries=0)
    page = client.posts.list()
    items = list(page)
    assert len(items) == 2
    assert items[0].id == "p1"
    assert items[1].id == "p2"
    client.close()


async def test_async_cursor_page_iteration(httpx_mock) -> None:
    """Async auto-pagination should yield all items across pages."""
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/posts",
        json={
            "data": [_post_json("p1")],
            "pagination": {"has_more": True, "next_cursor": "cur_1"},
        },
    )
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/posts?cursor=cur_1",
        json={
            "data": [_post_json("p2")],
            "pagination": {"has_more": False, "next_cursor": None},
        },
    )
    client = AsyncSocialAPI(api_key=TEST_API_KEY, base_url=BASE_URL, max_retries=0)
    page = await client.posts.list()
    items = []
    async for item in page:
        items.append(item)
    assert len(items) == 2
    assert items[0].id == "p1"
    assert items[1].id == "p2"
    await client.close()


def test_empty_page(httpx_mock) -> None:
    """An empty page should yield no items."""
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/posts",
        json={
            "data": [],
            "pagination": {"has_more": False, "next_cursor": None},
        },
    )
    client = SocialAPI(api_key=TEST_API_KEY, base_url=BASE_URL, max_retries=0)
    page = client.posts.list()
    assert len(page) == 0
    assert list(page) == []
    client.close()


def test_single_page_no_next(httpx_mock) -> None:
    """A page with has_more=False should not have a next page."""
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/posts",
        json={
            "data": [_post_json("p1")],
            "pagination": {"has_more": False, "next_cursor": None},
        },
    )
    client = SocialAPI(api_key=TEST_API_KEY, base_url=BASE_URL, max_retries=0)
    page = client.posts.list()
    assert not page.has_next_page()
    client.close()


def test_cursor_page_repr(httpx_mock) -> None:
    """CursorPage.__repr__ should include item count and cursor info."""
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/posts",
        json={
            "data": [_post_json("p1"), _post_json("p2")],
            "pagination": {"has_more": True, "next_cursor": "abc"},
        },
    )
    client = SocialAPI(api_key=TEST_API_KEY, base_url=BASE_URL, max_retries=0)
    page = client.posts.list()
    r = repr(page)
    assert "2 items" in r
    assert "has_more=True" in r
    assert "'abc'" in r
    client.close()


def test_cursor_page_next_page_raises(httpx_mock) -> None:
    """Calling next_page when there are no more pages raises StopIteration."""
    import pytest

    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/posts",
        json={
            "data": [_post_json("p1")],
            "pagination": {"has_more": False, "next_cursor": None},
        },
    )
    client = SocialAPI(api_key=TEST_API_KEY, base_url=BASE_URL, max_retries=0)
    page = client.posts.list()
    with pytest.raises(StopIteration):
        page.next_page()
    client.close()


def test_cursor_envelope_shape(httpx_mock) -> None:
    """Detect the {data: [...], cursor: str} envelope shape."""
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/posts",
        json={
            "data": [_post_json("p1")],
            "cursor": "next_abc",
        },
    )
    client = SocialAPI(api_key=TEST_API_KEY, base_url=BASE_URL, max_retries=0)
    page = client.posts.list()
    assert page.has_more is True
    assert page.next_cursor == "next_abc"
    client.close()


async def test_async_cursor_page_repr(httpx_mock) -> None:
    """AsyncCursorPage.__repr__ should include item count and cursor info."""
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/posts",
        json={
            "data": [_post_json("p1")],
            "pagination": {"has_more": False, "next_cursor": None},
        },
    )
    client = AsyncSocialAPI(api_key=TEST_API_KEY, base_url=BASE_URL, max_retries=0)
    page = await client.posts.list()
    r = repr(page)
    assert "1 items" in r
    assert "has_more=False" in r
    await client.close()


async def test_async_cursor_page_next_page_raises(httpx_mock) -> None:
    """Calling next_page on exhausted async page raises StopAsyncIteration."""
    import pytest

    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/posts",
        json={
            "data": [_post_json("p1")],
            "pagination": {"has_more": False, "next_cursor": None},
        },
    )
    client = AsyncSocialAPI(api_key=TEST_API_KEY, base_url=BASE_URL, max_retries=0)
    page = await client.posts.list()
    with pytest.raises(StopAsyncIteration):
        await page.next_page()
    await client.close()


async def test_async_cursor_page_empty_next_page(httpx_mock) -> None:
    """Async auto-pagination should stop when next page has empty data."""
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/posts",
        json={
            "data": [_post_json("p1")],
            "pagination": {"has_more": True, "next_cursor": "cur_empty"},
        },
    )
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/posts?cursor=cur_empty",
        json={
            "data": [],
            "pagination": {"has_more": False, "next_cursor": None},
        },
    )
    client = AsyncSocialAPI(api_key=TEST_API_KEY, base_url=BASE_URL, max_retries=0)
    page = await client.posts.list()
    items = []
    async for item in page:
        items.append(item)
    assert len(items) == 1
    assert items[0].id == "p1"
    await client.close()


async def test_async_cursor_envelope_shape(httpx_mock) -> None:
    """Async client should detect the {data: [...], cursor: str} envelope."""
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/posts",
        json={
            "data": [_post_json("p1")],
            "cursor": "next_xyz",
        },
    )
    client = AsyncSocialAPI(api_key=TEST_API_KEY, base_url=BASE_URL, max_retries=0)
    page = await client.posts.list()
    assert page.has_more is True
    assert page.next_cursor == "next_xyz"
    await client.close()


async def test_async_cursor_page_len(httpx_mock) -> None:
    """AsyncCursorPage.__len__ should return the current page item count."""
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/posts",
        json={
            "data": [_post_json("p1"), _post_json("p2"), _post_json("p3")],
            "pagination": {"has_more": False, "next_cursor": None},
        },
    )
    client = AsyncSocialAPI(api_key=TEST_API_KEY, base_url=BASE_URL, max_retries=0)
    page = await client.posts.list()
    assert len(page) == 3
    await client.close()
