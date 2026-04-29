from __future__ import annotations

from typing import TYPE_CHECKING, Any

from socialapi.models.conversations import (
    AsyncConversation,
    Conversation,
    Message,
    SendMessageResponse,
)

if TYPE_CHECKING:
    from socialapi._base_client import BaseAsyncClient, BaseSyncClient
    from socialapi._pagination import AsyncCursorPage, CursorPage


class Conversations:
    """Manage DM conversations in the unified inbox (sync)."""

    _client: BaseSyncClient

    def __init__(self, client: BaseSyncClient) -> None:
        self._client = client

    def list(
        self,
        *,
        account_id: str | None = None,
        platform: str | None = None,
        status: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        timeout: float | None = None,
    ) -> CursorPage[Conversation]:
        params: dict[str, Any] = {}
        if account_id is not None:
            params["account_id"] = account_id
        if platform is not None:
            params["platform"] = platform
        if status is not None:
            params["status"] = status
        if limit is not None:
            params["limit"] = limit
        if cursor is not None:
            params["cursor"] = cursor
        return self._client._get_paginated(
            "/v1/inbox/conversations",
            params=params,
            model=Conversation,
            timeout=timeout,
        )

    def get(self, conversation_id: str, *, timeout: float | None = None) -> Conversation:
        data = self._client._get(f"/v1/inbox/conversations/{conversation_id}", timeout=timeout)
        conv = Conversation.model_validate(data.get("data", data))
        conv._bind(self._client)
        return conv

    def update(
        self,
        conversation_id: str,
        *,
        status: str,
        timeout: float | None = None,
    ) -> Conversation:
        data = self._client._patch(
            f"/v1/inbox/conversations/{conversation_id}",
            json={"status": status},
            timeout=timeout,
        )
        if isinstance(data, dict) and "data" in data:
            conv = Conversation.model_validate(data["data"])
            conv._bind(self._client)
            return conv
        return self.get(conversation_id, timeout=timeout)

    def list_messages(
        self,
        conversation_id: str,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        timeout: float | None = None,
    ) -> CursorPage[Message]:
        params: dict[str, Any] = {}
        if limit is not None:
            params["limit"] = limit
        if cursor is not None:
            params["cursor"] = cursor
        return self._client._get_paginated(
            f"/v1/inbox/conversations/{conversation_id}/messages",
            params=params,
            model=Message,
            timeout=timeout,
        )

    def send_message(
        self,
        conversation_id: str,
        *,
        account_id: str,
        text: str,
        attachment_url: str | None = None,
        timeout: float | None = None,
    ) -> SendMessageResponse:
        body: dict[str, Any] = {"account_id": account_id, "text": text}
        if attachment_url is not None:
            body["attachment_url"] = attachment_url
        data = self._client._post(
            f"/v1/inbox/conversations/{conversation_id}/messages",
            json=body,
            timeout=timeout,
        )
        return SendMessageResponse.model_validate(data)

    def mark_as_read(self, conversation_id: str, *, timeout: float | None = None) -> None:
        self._client._post(f"/v1/inbox/conversations/{conversation_id}/read", timeout=timeout)


class AsyncConversations:
    """Manage DM conversations in the unified inbox (async)."""

    _client: BaseAsyncClient

    def __init__(self, client: BaseAsyncClient) -> None:
        self._client = client

    async def list(
        self,
        *,
        account_id: str | None = None,
        platform: str | None = None,
        status: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        timeout: float | None = None,
    ) -> AsyncCursorPage[AsyncConversation]:
        params: dict[str, Any] = {}
        if account_id is not None:
            params["account_id"] = account_id
        if platform is not None:
            params["platform"] = platform
        if status is not None:
            params["status"] = status
        if limit is not None:
            params["limit"] = limit
        if cursor is not None:
            params["cursor"] = cursor
        return await self._client._get_paginated(
            "/v1/inbox/conversations",
            params=params,
            model=AsyncConversation,
            timeout=timeout,
        )

    async def get(self, conversation_id: str, *, timeout: float | None = None) -> AsyncConversation:
        data = await self._client._get(f"/v1/inbox/conversations/{conversation_id}", timeout=timeout)
        conv = AsyncConversation.model_validate(data.get("data", data))
        conv._bind(self._client)
        return conv

    async def update(
        self,
        conversation_id: str,
        *,
        status: str,
        timeout: float | None = None,
    ) -> AsyncConversation:
        data = await self._client._patch(
            f"/v1/inbox/conversations/{conversation_id}",
            json={"status": status},
            timeout=timeout,
        )
        if isinstance(data, dict) and "data" in data:
            conv = AsyncConversation.model_validate(data["data"])
            conv._bind(self._client)
            return conv
        return await self.get(conversation_id, timeout=timeout)

    async def list_messages(
        self,
        conversation_id: str,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        timeout: float | None = None,
    ) -> AsyncCursorPage[Message]:
        params: dict[str, Any] = {}
        if limit is not None:
            params["limit"] = limit
        if cursor is not None:
            params["cursor"] = cursor
        return await self._client._get_paginated(
            f"/v1/inbox/conversations/{conversation_id}/messages",
            params=params,
            model=Message,
            timeout=timeout,
        )

    async def send_message(
        self,
        conversation_id: str,
        *,
        account_id: str,
        text: str,
        attachment_url: str | None = None,
        timeout: float | None = None,
    ) -> SendMessageResponse:
        body: dict[str, Any] = {"account_id": account_id, "text": text}
        if attachment_url is not None:
            body["attachment_url"] = attachment_url
        data = await self._client._post(
            f"/v1/inbox/conversations/{conversation_id}/messages",
            json=body,
            timeout=timeout,
        )
        return SendMessageResponse.model_validate(data)

    async def mark_as_read(self, conversation_id: str, *, timeout: float | None = None) -> None:
        await self._client._post(f"/v1/inbox/conversations/{conversation_id}/read", timeout=timeout)
