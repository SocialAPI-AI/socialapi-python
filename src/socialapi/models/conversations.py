from __future__ import annotations

from datetime import datetime  # noqa: TC003
from typing import TYPE_CHECKING, Any

from pydantic import BaseModel, ConfigDict

from socialapi._bound import _Bound

if TYPE_CHECKING:
    from socialapi._pagination import AsyncCursorPage, CursorPage


# ---------------------------------------------------------------------------
# Conversation
# ---------------------------------------------------------------------------


class _ConversationBase(_Bound):
    """Shared fields for Conversation / AsyncConversation."""

    id: str
    user_id: str
    account_id: str
    platform: str
    platform_id: str
    participant_id: str
    participant_name: str
    participant_picture: str | None = None
    last_message: str | None = None
    last_message_at: datetime | None = None
    status: str = "active"
    unread_count: int = 0
    created_at: datetime
    updated_at: datetime


class Conversation(_ConversationBase):
    """A DM conversation (sync)."""

    def update(self, *, status: str, timeout: float | None = None) -> Conversation:
        client = self._client_or_raise_sync()
        data = client._patch(
            f"/v1/inbox/conversations/{self.id}",
            json={"status": status},
            timeout=timeout,
        )
        if isinstance(data, dict) and "data" in data:
            updated = Conversation.model_validate(data["data"])
            updated._bind(client, {"account_id": self.account_id})
            return updated
        # API may return {"success": true} -- re-fetch
        refetch = client._get(f"/v1/inbox/conversations/{self.id}", timeout=timeout)
        updated = Conversation.model_validate(refetch.get("data", refetch))
        updated._bind(client, {"account_id": self.account_id})
        return updated

    def list_messages(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        timeout: float | None = None,
    ) -> CursorPage[Message]:
        client = self._client_or_raise_sync()
        params: dict[str, Any] = {}
        if limit is not None:
            params["limit"] = limit
        if cursor is not None:
            params["cursor"] = cursor
        return client._get_paginated(
            f"/v1/inbox/conversations/{self.id}/messages",
            params=params,
            model=Message,
            timeout=timeout,
            bind_ctx={"account_id": self.account_id, "conversation_id": self.id},
        )

    def send_message(
        self,
        *,
        text: str,
        attachment_url: str | None = None,
        timeout: float | None = None,
    ) -> SendMessageResponse:
        client = self._client_or_raise_sync()
        body: dict[str, Any] = {"account_id": self.account_id, "text": text}
        if attachment_url is not None:
            body["attachment_url"] = attachment_url
        data = client._post(
            f"/v1/inbox/conversations/{self.id}/messages",
            json=body,
            timeout=timeout,
        )
        return SendMessageResponse.model_validate(data)

    def mark_as_read(self, *, timeout: float | None = None) -> None:
        client = self._client_or_raise_sync()
        client._post(f"/v1/inbox/conversations/{self.id}/read", timeout=timeout)


class AsyncConversation(_ConversationBase):
    """A DM conversation (async)."""

    async def update(self, *, status: str, timeout: float | None = None) -> AsyncConversation:
        client = self._client_or_raise_async()
        data = await client._patch(
            f"/v1/inbox/conversations/{self.id}",
            json={"status": status},
            timeout=timeout,
        )
        if isinstance(data, dict) and "data" in data:
            updated = AsyncConversation.model_validate(data["data"])
            updated._bind(client, {"account_id": self.account_id})
            return updated
        refetch = await client._get(f"/v1/inbox/conversations/{self.id}", timeout=timeout)
        updated = AsyncConversation.model_validate(refetch.get("data", refetch))
        updated._bind(client, {"account_id": self.account_id})
        return updated

    async def list_messages(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        timeout: float | None = None,
    ) -> AsyncCursorPage[Message]:
        client = self._client_or_raise_async()
        params: dict[str, Any] = {}
        if limit is not None:
            params["limit"] = limit
        if cursor is not None:
            params["cursor"] = cursor
        return await client._get_paginated(
            f"/v1/inbox/conversations/{self.id}/messages",
            params=params,
            model=Message,
            timeout=timeout,
            bind_ctx={"account_id": self.account_id, "conversation_id": self.id},
        )

    async def send_message(
        self,
        *,
        text: str,
        attachment_url: str | None = None,
        timeout: float | None = None,
    ) -> SendMessageResponse:
        client = self._client_or_raise_async()
        body: dict[str, Any] = {"account_id": self.account_id, "text": text}
        if attachment_url is not None:
            body["attachment_url"] = attachment_url
        data = await client._post(
            f"/v1/inbox/conversations/{self.id}/messages",
            json=body,
            timeout=timeout,
        )
        return SendMessageResponse.model_validate(data)

    async def mark_as_read(self, *, timeout: float | None = None) -> None:
        client = self._client_or_raise_async()
        await client._post(f"/v1/inbox/conversations/{self.id}/read", timeout=timeout)


# ---------------------------------------------------------------------------
# Message (data only)
# ---------------------------------------------------------------------------


class Message(BaseModel):
    """A single message within a conversation."""

    model_config = ConfigDict(populate_by_name=True)

    id: str
    conversation_id: str
    platform_id: str
    direction: str
    text: str | None = None
    sender_id: str
    sender_name: str
    attachment_type: str | None = None
    attachment_url: str | None = None
    created_at: datetime


class SendMessageRequest(BaseModel):
    """Request body for ``POST /v1/inbox/conversations/:id/messages``."""

    model_config = ConfigDict(populate_by_name=True)

    account_id: str
    text: str
    attachment_url: str | None = None


class SendMessageResponse(BaseModel):
    """Response after sending a DM."""

    model_config = ConfigDict(populate_by_name=True)

    success: bool
    message_id: str


class UpdateConversationRequest(BaseModel):
    """Request body for ``PATCH /v1/inbox/conversations/:id``."""

    model_config = ConfigDict(populate_by_name=True)

    status: str
