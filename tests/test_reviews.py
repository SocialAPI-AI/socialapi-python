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

FANOUT_META = {
    "accounts_queried": 2,
    "accounts_failed": 1,
    "failed_accounts": [
        {
            "account_id": "acc_fail_001",
            "platform": "instagram",
            "error": "not supported",
            "code": "not_supported",
        }
    ],
}


def test_list_reviews_returns_review_list(httpx_mock, client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/inbox/reviews",
        json={"data": [REVIEW_JSON], "meta": FANOUT_META},
    )
    result = client.reviews.list()
    from socialapi.models.reviews import ReviewList

    assert isinstance(result, ReviewList)
    assert len(result.data) == 1
    review = result.data[0]
    assert review.id == "rev_001"
    assert review.rating == 5
    assert review.author == "Bob Johnson"


def test_list_reviews_meta(httpx_mock, client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/inbox/reviews",
        json={"data": [REVIEW_JSON], "meta": FANOUT_META},
    )
    result = client.reviews.list()
    assert result.meta.accounts_queried == 2
    assert result.meta.accounts_failed == 1
    assert result.meta.failed_accounts[0].code == "not_supported"
    assert result.meta.failed_accounts[0].platform == "instagram"


def test_list_reviews_iterable(httpx_mock, client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/inbox/reviews",
        json={"data": [REVIEW_JSON], "meta": FANOUT_META},
    )
    result = client.reviews.list()
    items = list(result)
    assert len(items) == 1
    assert items[0].id == "rev_001"


def test_list_reviews_len(httpx_mock, client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/inbox/reviews",
        json={"data": [REVIEW_JSON], "meta": FANOUT_META},
    )
    result = client.reviews.list()
    assert len(result) == 1


def test_reply_to_review(httpx_mock, client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/inbox/reviews/rev_001/reply",
        json={"success": True, "reply_id": "reply_001"},
    )
    result = client.reviews.reply("rev_001", account_id="acc_goog_001", text="Thank you for your kind review!")
    assert result.success is True
    assert result.reply_id == "reply_001"


def test_list_reviews_with_filters(httpx_mock, client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/inbox/reviews?account_id=acc_goog_001&platform=google&limit=5&cursor=rev_cur",
        json={"data": [REVIEW_JSON], "meta": FANOUT_META},
    )
    result = client.reviews.list(account_id="acc_goog_001", platform="google", limit=5, cursor="rev_cur")
    assert len(result.data) == 1


def test_update_reply_does_not_exist(client) -> None:
    assert not hasattr(client.reviews, "update_reply")


def test_delete_reply_does_not_exist(client) -> None:
    assert not hasattr(client.reviews, "delete_reply")


async def test_list_reviews_async_returns_review_list(httpx_mock, async_client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/inbox/reviews",
        json={"data": [REVIEW_JSON], "meta": FANOUT_META},
    )
    result = await async_client.reviews.list()
    from socialapi.models.reviews import ReviewList

    assert isinstance(result, ReviewList)
    assert len(result.data) == 1
    assert result.data[0].platform == "google"


async def test_list_reviews_async_meta(httpx_mock, async_client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/inbox/reviews",
        json={"data": [REVIEW_JSON], "meta": FANOUT_META},
    )
    result = await async_client.reviews.list()
    assert result.meta.accounts_queried == 2
    assert result.meta.failed_accounts[0].code == "not_supported"


async def test_list_reviews_async_with_filters(httpx_mock, async_client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/inbox/reviews?account_id=acc_goog_001&platform=google&limit=3&cursor=rc",
        json={"data": [], "meta": {"accounts_queried": 1, "accounts_failed": 0, "failed_accounts": []}},
    )
    result = await async_client.reviews.list(account_id="acc_goog_001", platform="google", limit=3, cursor="rc")
    assert len(result.data) == 0


async def test_reply_to_review_async(httpx_mock, async_client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/inbox/reviews/rev_001/reply",
        json={"success": True, "reply_id": "reply_async_001"},
    )
    result = await async_client.reviews.reply("rev_001", account_id="acc_goog_001", text="Thanks!")
    assert result.success is True
    assert result.reply_id == "reply_async_001"


async def test_async_update_reply_does_not_exist(async_client) -> None:
    assert not hasattr(async_client.reviews, "update_reply")


async def test_async_delete_reply_does_not_exist(async_client) -> None:
    assert not hasattr(async_client.reviews, "delete_reply")
