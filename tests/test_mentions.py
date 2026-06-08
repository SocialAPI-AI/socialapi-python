from __future__ import annotations

from .conftest import BASE_URL

# Real Interaction shape from Go (base.Interaction):
# received_at (not created_at), no platform_id, optional platform_post_id/post_id/conversation_id
# Author has id/name/username/avatar_url all optional (omitempty)
# recipient is optional (*Author)
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
    "received_at": "2026-03-20T16:00:00Z",
    "account_id": "acc_ig_001",
    # optional fields (omitempty in Go)
    "platform_post_id": "17890054321",
    "post_id": "post_uuid_abc",
    "conversation_id": "conv_uuid_xyz",
}

# Minimal mention: no optional fields
MENTION_MINIMAL_JSON = {
    "id": "mnt_002",
    "platform": "facebook",
    "type": "mention",
    "author": {},
    "content": {"text": "Hello"},
    "metadata": None,
    "received_at": "2026-04-01T10:00:00Z",
    "account_id": "acc_fb_001",
}

# Mention with recipient (IG-only)
MENTION_WITH_RECIPIENT_JSON = {
    "id": "mnt_003",
    "platform": "instagram",
    "type": "mention",
    "author": {"username": "janesmith"},
    "recipient": {"id": "me_456", "name": "My Brand"},
    "content": {"text": "Hey @mybrand!"},
    "metadata": None,
    "received_at": "2026-04-02T12:00:00Z",
    "account_id": "acc_ig_002",
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
    # received_at (not created_at)
    assert mention.received_at is not None
    # optional fields
    assert mention.platform_post_id == "17890054321"
    assert mention.post_id == "post_uuid_abc"
    assert mention.conversation_id == "conv_uuid_xyz"


def test_list_mentions_no_platform_id(httpx_mock, client) -> None:
    """Mention without platform_id must parse successfully (no such field in Interaction)."""
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/accounts/acc_ig_001/mentions",
        json={"data": [MENTION_JSON], "pagination": {"has_more": False, "next_cursor": None}},
    )
    page = client.mentions.list("acc_ig_001")
    mention = page.data[0]
    # The model must NOT have a platform_id field
    assert not hasattr(mention, "platform_id")


def test_list_mentions_minimal(httpx_mock, client) -> None:
    """Mention with minimal author (all omitted) must parse without error."""
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/accounts/acc_ig_001/mentions",
        json={"data": [MENTION_MINIMAL_JSON], "pagination": {"has_more": False, "next_cursor": None}},
    )
    page = client.mentions.list("acc_ig_001")
    assert len(page.data) == 1
    mention = page.data[0]
    # author fields are optional
    assert mention.author.id is None
    assert mention.author.name is None
    # optional fields absent
    assert mention.platform_post_id is None
    assert mention.post_id is None
    assert mention.conversation_id is None
    assert mention.recipient is None


def test_list_mentions_with_recipient(httpx_mock, client) -> None:
    """Mention with recipient field (IG-only) parses correctly."""
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/accounts/acc_ig_002/mentions",
        json={"data": [MENTION_WITH_RECIPIENT_JSON], "pagination": {"has_more": False, "next_cursor": None}},
    )
    page = client.mentions.list("acc_ig_002")
    mention = page.data[0]
    assert mention.recipient is not None
    assert mention.recipient.id == "me_456"
    assert mention.recipient.name == "My Brand"
    # author username
    assert mention.author.username == "janesmith"


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
    # received_at (not created_at)
    assert page.data[0].received_at is not None


async def test_list_mentions_async_with_filters(httpx_mock, async_client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/accounts/acc_ig_001/mentions?since=2026-03-15T00%3A00%3A00Z&limit=5&cursor=mcc",
        json={"data": [], "pagination": {"has_more": False, "next_cursor": None}},
    )
    page = await async_client.mentions.list("acc_ig_001", since="2026-03-15T00:00:00Z", limit=5, cursor="mcc")
    assert len(page.data) == 0


def test_mention_author_and_sub_models_re_exported() -> None:
    """MentionAuthor, MentionContent, MentionMedia must be importable from top-level package."""
    from socialapi import MentionAuthor, MentionContent, MentionMedia

    assert MentionAuthor is not None
    assert MentionContent is not None
    assert MentionMedia is not None
