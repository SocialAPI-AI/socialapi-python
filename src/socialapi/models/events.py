from __future__ import annotations

from typing import TYPE_CHECKING, Any

from pydantic import BaseModel, ConfigDict

if TYPE_CHECKING:
    from collections.abc import Iterator


class Event(BaseModel):
    """A single entry in the unified developer event log.

    Models the ``EventResponse`` Go struct from ``types_events.go``.
    """

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
    created_at: str


class EventList:
    """Result of ``GET /v1/events``.

    The API wraps events in ``{"events": [...], "pagination": {...},
    "retention_days": N}`` rather than the standard ``{"data": [...]}``
    envelope, so ``CursorPage`` cannot be used directly. This wrapper
    mirrors the ``ReviewList`` pattern and exposes the same
    ``has_next_page`` / ``next_cursor`` attributes for manual pagination.

    Note on design: ``CursorPage`` reads ``body.get("data", [])`` which
    would miss the ``events`` key. Rather than special-casing the
    pagination machinery for a single endpoint, we use a lightweight
    wrapper that delegates next-page fetching through the resource
    method. The ``retention_days`` field is surfaced here because it
    is absent from individual ``Event`` objects.
    """

    data: list[Event]
    retention_days: int
    has_more: bool
    next_cursor: str | None

    def __init__(
        self,
        *,
        data: list[Event],
        retention_days: int,
        has_more: bool,
        next_cursor: str | None,
    ) -> None:
        self.data = data
        self.retention_days = retention_days
        self.has_more = has_more
        self.next_cursor = next_cursor

    def has_next_page(self) -> bool:
        """Return ``True`` if more pages are available."""
        return self.has_more and self.next_cursor is not None

    def __iter__(self) -> Iterator[Event]:
        """Iterate over the events in ``data``."""
        return iter(self.data)

    def __len__(self) -> int:
        """Return the number of events on the current page."""
        return len(self.data)

    def __repr__(self) -> str:
        return (
            f"EventList(data=[...{len(self.data)} items], "
            f"has_more={self.has_more}, "
            f"next_cursor={self.next_cursor!r}, "
            f"retention_days={self.retention_days})"
        )


class EventsSummary(BaseModel):
    """Aggregated event counts from ``GET /v1/events/summary``.

    Models the ``EventsSummaryResponse`` Go struct from ``types_events.go``.
    """

    model_config = ConfigDict(populate_by_name=True)

    total: int
    total_previous: int | None = None
    failed: int
    by_category: dict[str, int]
    by_error_category: dict[str, int]
    inbox_breakdown: dict[str, int]
    retention_days: int
