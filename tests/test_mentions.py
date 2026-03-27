from __future__ import annotations

from .conftest import BASE_URL

MENTION_JSON = {
    "id": "mnt_001",
    "platform": "instagram",
    "type": "mention",
    "author": {
        "id": "ext_user_55",
        "name": "Carol Williams",
        "avatar_url": "https://cdn.example.com/carol.jpg",
    },
    "content": {
        "text": "Check out @testinsta for great products!",
        "media": [{"url": "https://cdn.example.com/img.jpg", "type": "image"}],
    },
    "metadata": None,
    "created_at": "2026-03-20T16:00:00Z",
    "account_id": "acc_ig_001",
    "platform_id": "17890054321",
}


def test_list_mentions(httpx_mock, client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/accounts/acc_ig_001/mentions",
        json={"data": [MENTION_JSON], "pagination": {"has_more": False, "next_cursor": None}},
    )
    page = client.mentions.list("acc_ig_001")
    assert len(page.data) == 1
    mention = page.data[0]
    assert mention.id == "mnt_001"
    assert mention.platform == "instagram"
    assert mention.author.name == "Carol Williams"
    assert mention.content.text.startswith("Check out")
    assert mention.content.media is not None
    assert mention.content.media[0].type == "image"


def test_list_mentions_with_filters(httpx_mock, client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/accounts/acc_ig_001/mentions?since=2026-03-01T00%3A00%3A00Z&limit=10&cursor=mc",
        json={"data": [MENTION_JSON], "pagination": {"has_more": False, "next_cursor": None}},
    )
    page = client.mentions.list("acc_ig_001", since="2026-03-01T00:00:00Z", limit=10, cursor="mc")
    assert len(page.data) == 1


async def test_list_mentions_async(httpx_mock, async_client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/accounts/acc_ig_001/mentions",
        json={"data": [MENTION_JSON], "pagination": {"has_more": False, "next_cursor": None}},
    )
    page = await async_client.mentions.list("acc_ig_001")
    assert len(page.data) == 1
    assert page.data[0].author.id == "ext_user_55"


async def test_list_mentions_async_with_filters(httpx_mock, async_client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/accounts/acc_ig_001/mentions?since=2026-03-15T00%3A00%3A00Z&limit=5&cursor=mcc",
        json={"data": [], "pagination": {"has_more": False, "next_cursor": None}},
    )
    page = await async_client.mentions.list("acc_ig_001", since="2026-03-15T00:00:00Z", limit=5, cursor="mcc")
    assert len(page.data) == 0
