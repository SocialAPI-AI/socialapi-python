from __future__ import annotations

from pydantic import BaseModel, ConfigDict


class Conversation(BaseModel):
    """A DM conversation in the unified inbox."""

    model_config = ConfigDict(populate_by_name=True)

    id: str
    user_id: str
    account_id: str
    platform: str
    platform_id: str
    participant_id: str
    participant_name: str
    participant_picture: str | None = None
    last_message: str | None = None
    last_message_at: str | None = None
    status: str = "active"
    unread_count: int = 0
    created_at: str
    updated_at: str


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
    created_at: str


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
