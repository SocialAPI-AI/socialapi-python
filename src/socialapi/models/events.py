from __future__ import annotations

from datetime import datetime  # noqa: TC003
from typing import Any

from pydantic import BaseModel, ConfigDict


class Event(BaseModel):
    """A developer event (audit log entry)."""

    model_config = ConfigDict(populate_by_name=True)

    id: str
    category: str
    action: str
    status: str
    platform: str | None = None
    account_id: str | None = None
    resource_id: str | None = None
    summary: str
    error_message: str | None = None
    error_category: str | None = None
    status_code: int | None = None
    duration_ms: int | None = None
    metadata: dict[str, Any] = {}
    created_at: datetime


class EventsListResponse(BaseModel):
    """Response from ``GET /v1/events``."""

    model_config = ConfigDict(populate_by_name=True)

    events: list[Event]
    retention_days: int
