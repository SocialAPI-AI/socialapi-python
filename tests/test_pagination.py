"""Tests for auto-pagination."""

from __future__ import annotations

from unittest.mock import MagicMock

from pydantic import BaseModel

from socialapi._base_client import SyncAPIClient
from socialapi._pagination import SyncPaginator


class Item(BaseModel):
    id: str
    name: str


def _make_sync_client() -> SyncAPIClient:
    """Create a mock SyncAPIClient for pagination tests."""
    client = MagicMock(spec=SyncAPIClient)
    # Make isinstance checks pass.
    client.__class__ = SyncAPIClient
    return client


def test_sync_paginator_follows_cursor() -> None:
    client = _make_sync_client()

    # Simulate two pages: first has cursor, second has no cursor.
    client._get.side_effect = [
        {"data": [{"id": "1", "name": "First"}], "cursor": "page2"},
        {"data": [{"id": "2", "name": "Second"}], "cursor": None},
    ]

    paginator = SyncPaginator(
        client=client,
        path="/v1/items",
        params={"limit": 1},
        model=Item,
    )

    items = list(paginator)
    assert len(items) == 2
    assert items[0].id == "1"
    assert items[0].name == "First"
    assert items[1].id == "2"
    assert items[1].name == "Second"

    # Verify the second call used the cursor.
    assert client._get.call_count == 2


def test_sync_paginator_stops_when_cursor_is_none() -> None:
    client = _make_sync_client()

    client._get.side_effect = [
        {"data": [{"id": "1", "name": "Only"}], "cursor": None},
    ]

    paginator = SyncPaginator(
        client=client,
        path="/v1/items",
        params={"limit": 10},
        model=Item,
    )

    items = list(paginator)
    assert len(items) == 1
    assert client._get.call_count == 1


def test_sync_paginator_yields_individual_items() -> None:
    client = _make_sync_client()

    client._get.side_effect = [
        {
            "data": [
                {"id": "1", "name": "A"},
                {"id": "2", "name": "B"},
                {"id": "3", "name": "C"},
            ],
            "cursor": None,
        },
    ]

    paginator = SyncPaginator(
        client=client,
        path="/v1/items",
        params={"limit": 10},
        model=Item,
    )

    items = list(paginator)
    assert len(items) == 3
    assert all(isinstance(item, Item) for item in items)
    assert [item.id for item in items] == ["1", "2", "3"]


def test_sync_paginator_stops_on_empty_data() -> None:
    client = _make_sync_client()

    client._get.side_effect = [
        {"data": [], "cursor": "should_not_follow"},
    ]

    paginator = SyncPaginator(
        client=client,
        path="/v1/items",
        params={"limit": 10},
        model=Item,
    )

    items = list(paginator)
    assert len(items) == 0
    assert client._get.call_count == 1
