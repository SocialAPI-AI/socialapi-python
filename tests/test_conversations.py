from __future__ import annotations

from .conftest import BASE_URL

CONVERSATION_JSON = {
    "id": "conv_001",
    "user_id": "usr_001",
    "account_id": "acc_ig_001",
    "platform": "instagram",
    "platform_id": "ig_conv_98765",
    "participant_id": "ext_user_42",
    "participant_name": "Alice Smith",
    "participant_picture": "https://cdn.example.com/alice.jpg",
    "last_message": "Hey, loved your product!",
    "last_message_at": "2026-03-20T14:30:00Z",
    "status": "active",
    "unread_count": 2,
    "created_at": "2026-03-18T09:00:00Z",
    "updated_at": "2026-03-20T14:30:00Z",
}

MESSAGE_JSON = {
    "id": "msg_001",
    "conversation_id": "conv_001",
    "platform_id": "ig_msg_111",
    "direction": "incoming",
    "text": "Hey, loved your product!",
    "sender_id": "ext_user_42",
    "sender_name": "Alice Smith",
    "created_at": "2026-03-20T14:30:00Z",
}


def test_list_conversations(httpx_mock, client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/inbox/conversations",
        json={"data": [CONVERSATION_JSON], "pagination": {"has_more": False, "next_cursor": None}},
    )
    page = client.conversations.list()
    assert len(page.data) == 1
    assert page.data[0].participant_name == "Alice Smith"
    assert page.data[0].unread_count == 2


def test_get_conversation(httpx_mock, client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/inbox/conversations/conv_001",
        json={"data": CONVERSATION_JSON},
    )
    conv = client.conversations.get("conv_001")
    assert conv.id == "conv_001"
    assert conv.platform == "instagram"


def test_update_conversation(httpx_mock, client) -> None:
    updated = {**CONVERSATION_JSON, "status": "archived"}
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/inbox/conversations/conv_001",
        json={"data": updated},
    )
    conv = client.conversations.update("conv_001", status="archived")
    assert conv.status == "archived"


def test_list_messages(httpx_mock, client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/inbox/conversations/conv_001/messages",
        json={"data": [MESSAGE_JSON], "pagination": {"has_more": False, "next_cursor": None}},
    )
    page = client.conversations.list_messages("conv_001")
    assert len(page.data) == 1
    assert page.data[0].text == "Hey, loved your product!"
    assert page.data[0].direction == "incoming"


def test_send_message(httpx_mock, client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/inbox/conversations/conv_001/messages",
        json={"success": True, "message_id": "msg_new_001"},
    )
    result = client.conversations.send_message("conv_001", account_id="acc_ig_001", text="Thanks for reaching out!")
    assert result.success is True
    assert result.message_id == "msg_new_001"


def test_mark_as_read(httpx_mock, client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/inbox/conversations/conv_001/read",
        status_code=204,
    )
    client.conversations.mark_as_read("conv_001")


def test_list_conversations_with_filters(httpx_mock, client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/inbox/conversations?account_id=acc_ig_001&platform=instagram&status=active&limit=5&cursor=cur_x",
        json={"data": [CONVERSATION_JSON], "pagination": {"has_more": False, "next_cursor": None}},
    )
    page = client.conversations.list(
        account_id="acc_ig_001", platform="instagram", status="active", limit=5, cursor="cur_x"
    )
    assert len(page.data) == 1


def test_update_conversation_success_refetch(httpx_mock, client) -> None:
    """When update returns {success: true}, the conversation is re-fetched."""
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/inbox/conversations/conv_001",
        json={"success": True},
    )
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/inbox/conversations/conv_001",
        json={"data": {**CONVERSATION_JSON, "status": "archived"}},
    )
    conv = client.conversations.update("conv_001", status="archived")
    assert conv.status == "archived"


def test_list_messages_with_pagination(httpx_mock, client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/inbox/conversations/conv_001/messages?limit=10&cursor=msg_cur",
        json={"data": [MESSAGE_JSON], "pagination": {"has_more": False, "next_cursor": None}},
    )
    page = client.conversations.list_messages("conv_001", limit=10, cursor="msg_cur")
    assert len(page.data) == 1


async def test_list_conversations_async(httpx_mock, async_client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/inbox/conversations",
        json={"data": [CONVERSATION_JSON], "pagination": {"has_more": False, "next_cursor": None}},
    )
    page = await async_client.conversations.list()
    assert len(page.data) == 1
    assert page.data[0].id == "conv_001"


async def test_list_conversations_async_with_filters(httpx_mock, async_client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/inbox/conversations?account_id=acc_1&platform=facebook&status=archived&limit=3&cursor=c",
        json={"data": [], "pagination": {"has_more": False, "next_cursor": None}},
    )
    page = await async_client.conversations.list(
        account_id="acc_1", platform="facebook", status="archived", limit=3, cursor="c"
    )
    assert len(page.data) == 0


async def test_get_conversation_async(httpx_mock, async_client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/inbox/conversations/conv_001",
        json={"data": CONVERSATION_JSON},
    )
    conv = await async_client.conversations.get("conv_001")
    assert conv.id == "conv_001"
    assert conv.platform == "instagram"


async def test_update_conversation_async(httpx_mock, async_client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/inbox/conversations/conv_001",
        json={"data": {**CONVERSATION_JSON, "status": "archived"}},
    )
    conv = await async_client.conversations.update("conv_001", status="archived")
    assert conv.status == "archived"


async def test_update_conversation_async_refetch(httpx_mock, async_client) -> None:
    """When async update returns {success: true}, the conversation is re-fetched."""
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/inbox/conversations/conv_001",
        json={"success": True},
    )
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/inbox/conversations/conv_001",
        json={"data": {**CONVERSATION_JSON, "status": "archived"}},
    )
    conv = await async_client.conversations.update("conv_001", status="archived")
    assert conv.status == "archived"


async def test_list_messages_async(httpx_mock, async_client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/inbox/conversations/conv_001/messages",
        json={"data": [MESSAGE_JSON], "pagination": {"has_more": False, "next_cursor": None}},
    )
    page = await async_client.conversations.list_messages("conv_001")
    assert len(page.data) == 1
    assert page.data[0].text == "Hey, loved your product!"


async def test_list_messages_async_with_pagination(httpx_mock, async_client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/inbox/conversations/conv_001/messages?limit=2&cursor=mc",
        json={"data": [MESSAGE_JSON], "pagination": {"has_more": False, "next_cursor": None}},
    )
    page = await async_client.conversations.list_messages("conv_001", limit=2, cursor="mc")
    assert len(page.data) == 1


async def test_send_message_async(httpx_mock, async_client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/inbox/conversations/conv_001/messages",
        json={"success": True, "message_id": "msg_async_001"},
    )
    result = await async_client.conversations.send_message("conv_001", account_id="acc_ig_001", text="Async reply")
    assert result.success is True
    assert result.message_id == "msg_async_001"


async def test_mark_as_read_async(httpx_mock, async_client) -> None:
    httpx_mock.add_response(
        url=f"{BASE_URL}/v1/inbox/conversations/conv_001/read",
        status_code=204,
    )
    await async_client.conversations.mark_as_read("conv_001")
