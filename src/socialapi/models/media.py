from __future__ import annotations

from datetime import datetime  # noqa: TC003

from pydantic import BaseModel, ConfigDict


class MediaItem(BaseModel):
    """An uploaded media file."""

    model_config = ConfigDict(populate_by_name=True)

    id: str
    filename: str
    content_type: str
    size_bytes: int
    status: str
    url: str
    created_at: datetime


class StorageUsage(BaseModel):
    """Storage usage for the authenticated user."""

    model_config = ConfigDict(populate_by_name=True)

    used_bytes: int
    limit_bytes: int
    count: int
