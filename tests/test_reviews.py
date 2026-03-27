from __future__ import annotations

from .conftest import BASE_URL

REVIEW_JSON = {
    "id": "rev_001",
    "platform": "google",
    "account_id": "acc_goog_001",
    "rating": 5,
    "text": "Excellent service!",
    "author": "Bob Johnson",
    "created_at": "2026-03-19T08:00:00Z",
}


def test_list_reviews(httpx_mock, client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/inbox/reviews",
        json={"data": [REVIEW_JSON], "pagination": {"has_more": False, "next_cursor": None}},
    )
    page = client.reviews.list()
    assert len(page.data) == 1
    review = page.data[0]
    assert review.id == "rev_001"
    assert review.rating == 5
    assert review.author == "Bob Johnson"


def test_reply_to_review(httpx_mock, client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/inbox/reviews/rev_001/reply",
        json={"success": True, "reply_id": "reply_001"},
    )
    result = client.reviews.reply("rev_001", account_id="acc_goog_001", text="Thank you for your kind review!")
    assert result.success is True
    assert result.reply_id == "reply_001"


def test_update_review_reply(httpx_mock, client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/inbox/reviews/rev_001/reply",
        json={"success": True, "reply_id": "reply_001"},
    )
    result = client.reviews.update_reply("rev_001", account_id="acc_goog_001", text="Updated reply text")
    assert result.success is True


def test_delete_review_reply(httpx_mock, client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/inbox/reviews/rev_001/reply?account_id=acc_goog_001",
        status_code=204,
    )
    client.reviews.delete_reply("rev_001", account_id="acc_goog_001")


def test_list_reviews_with_filters(httpx_mock, client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/inbox/reviews?account_id=acc_goog_001&platform=google&limit=5&cursor=rev_cur",
        json={"data": [REVIEW_JSON], "pagination": {"has_more": False, "next_cursor": None}},
    )
    page = client.reviews.list(account_id="acc_goog_001", platform="google", limit=5, cursor="rev_cur")
    assert len(page.data) == 1


async def test_list_reviews_async(httpx_mock, async_client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/inbox/reviews",
        json={"data": [REVIEW_JSON], "pagination": {"has_more": False, "next_cursor": None}},
    )
    page = await async_client.reviews.list()
    assert len(page.data) == 1
    assert page.data[0].platform == "google"


async def test_list_reviews_async_with_filters(httpx_mock, async_client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/inbox/reviews?account_id=acc_goog_001&platform=google&limit=3&cursor=rc",
        json={"data": [], "pagination": {"has_more": False, "next_cursor": None}},
    )
    page = await async_client.reviews.list(account_id="acc_goog_001", platform="google", limit=3, cursor="rc")
    assert len(page.data) == 0


async def test_reply_to_review_async(httpx_mock, async_client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/inbox/reviews/rev_001/reply",
        json={"success": True, "reply_id": "reply_async_001"},
    )
    result = await async_client.reviews.reply("rev_001", account_id="acc_goog_001", text="Thanks!")
    assert result.success is True
    assert result.reply_id == "reply_async_001"


async def test_update_review_reply_async(httpx_mock, async_client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/inbox/reviews/rev_001/reply",
        json={"success": True, "reply_id": "reply_001"},
    )
    result = await async_client.reviews.update_reply("rev_001", account_id="acc_goog_001", text="Updated async")
    assert result.success is True


async def test_delete_review_reply_async(httpx_mock, async_client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/inbox/reviews/rev_001/reply?account_id=acc_goog_001",
        status_code=204,
    )
    await async_client.reviews.delete_reply("rev_001", account_id="acc_goog_001")
