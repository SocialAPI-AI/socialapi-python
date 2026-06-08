from __future__ import annotations

from datetime import datetime  # noqa: TC003
from typing import Any

from pydantic import BaseModel, ConfigDict


class MentionMedia(BaseModel):
    """Media attachment on a mention."""

    model_config = ConfigDict(populate_by_name=True)

    url: str
    type: str


class MentionAuthor(BaseModel):
    """Author of a mention interaction.

    All fields are optional because the Go ``Author`` struct uses ``omitempty``
    on every JSON tag, meaning any field may be absent on the wire.
    """

    model_config = ConfigDict(populate_by_name=True)

    id: str | None = None
    name: str | None = None
    username: str | None = None
    avatar_url: str | None = None


class MentionContent(BaseModel):
    """Content of a mention interaction."""

    model_config = ConfigDict(populate_by_name=True)

    text: str
    media: list[MentionMedia] | None = None


class Mention(BaseModel):
    """A mention of the connected account on a social platform.

    Maps to the ``base.Interaction`` struct returned by ``GET /v1/accounts/:id/mentions``.
    """

    model_config = ConfigDict(populate_by_name=True)

    id: str
    platform: str
    type: str
    author: MentionAuthor
    recipient: MentionAuthor | None = None
    content: MentionContent
    metadata: dict[str, Any] | None = None
    received_at: datetime
    account_id: str
    # Optional fields (omitempty in Go)
    platform_post_id: str | None = None
    post_id: str | None = None
    conversation_id: str | None = None
