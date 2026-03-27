from __future__ import annotations

from typing import Any

from pydantic import BaseModel, ConfigDict


class MentionMedia(BaseModel):
    """Media attachment on a mention."""

    model_config = ConfigDict(populate_by_name=True)

    url: str
    type: str


class MentionAuthor(BaseModel):
    """Author of a mention interaction."""

    model_config = ConfigDict(populate_by_name=True)

    id: str
    name: str
    avatar_url: str | None = None


class MentionContent(BaseModel):
    """Content of a mention interaction."""

    model_config = ConfigDict(populate_by_name=True)

    text: str
    media: list[MentionMedia] | None = None


class Mention(BaseModel):
    """A mention of the connected account on a social platform."""

    model_config = ConfigDict(populate_by_name=True)

    id: str
    platform: str
    type: str
    author: MentionAuthor
    content: MentionContent
    metadata: dict[str, Any] | None = None
    created_at: str
    account_id: str
    platform_id: str
