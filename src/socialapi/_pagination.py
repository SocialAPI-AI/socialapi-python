from __future__ import annotations

from typing import TYPE_CHECKING, Any, Generic, TypeVar

from pydantic import BaseModel

from socialapi._bound import _Bound

if TYPE_CHECKING:
    from collections.abc import Iterator

    from socialapi._base_client import BaseAsyncClient, BaseSyncClient

T = TypeVar("T", bound=BaseModel)


def _rebind_items(items: list[Any], client: Any, ctx: dict[str, Any] | None) -> None:
    """Attach client + ctx to every item that subclasses ``_Bound``."""
    if not items:
        return
    for item in items:
        if isinstance(item, _Bound):
            item._bind(client, ctx)


class CursorPage(Generic[T]):
    """Sync cursor-paginated result set.

    Supports iteration over all pages via ``__iter__`` (auto-pagination)
    and manual control via ``has_next_page`` / ``next_page``.

    Example::

        # Auto-paginate all pages
        for post in client.posts.list(status="published"):
            print(post.id)

        # Manual pagination
        page = client.posts.list(status="published", limit=10)
        while page.has_next_page():
            page = page.next_page()
    """

    data: list[T]
    has_more: bool
    next_cursor: str | None

    _client: BaseSyncClient
    _path: str
    _params: dict[str, Any]
    _model: type[T]
    _bind_ctx: dict[str, Any] | None

    def __init__(
        self,
        *,
        data: list[T],
        has_more: bool,
        next_cursor: str | None,
        client: BaseSyncClient,
        path: str,
        params: dict[str, Any],
        model: type[T],
        bind_ctx: dict[str, Any] | None = None,
    ) -> None:
        self.data = data
        self.has_more = has_more
        self.next_cursor = next_cursor
        self._client = client
        self._path = path
        self._params = params
        self._model = model
        self._bind_ctx = bind_ctx
        _rebind_items(list(self.data), client, bind_ctx)

    def has_next_page(self) -> bool:
        """Return ``True`` if more pages are available."""
        return self.has_more and self.next_cursor is not None

    def next_page(self) -> CursorPage[T]:
        """Fetch the next page of results.

        Returns:
            The next page.

        Raises:
            StopIteration: If there is no next page.
        """
        if not self.has_next_page():
            raise StopIteration
        params = {**self._params, "cursor": self.next_cursor}
        return self._client._get_paginated(
            self._path,
            params=params,
            model=self._model,
            bind_ctx=self._bind_ctx,
        )

    def __iter__(self) -> Iterator[T]:
        """Yield items across all pages (auto-pagination)."""
        page: CursorPage[T] = self
        while True:
            yield from page.data
            if not page.has_next_page():
                break
            page = page.next_page()

    def __len__(self) -> int:
        """Return the number of items on the current page."""
        return len(self.data)

    def __repr__(self) -> str:
        return (
            f"CursorPage(data=[...{len(self.data)} items], has_more={self.has_more}, next_cursor={self.next_cursor!r})"
        )


class AsyncCursorPage(Generic[T]):
    """Async cursor-paginated result set.

    Supports iteration over all pages via ``async for`` (auto-pagination)
    and manual control via ``has_next_page`` / ``next_page``.

    Example::

        # Auto-paginate all pages
        async for post in await async_client.posts.list(status="published"):
            print(post.id)

        # Manual pagination
        page = await async_client.posts.list(status="published", limit=10)
        while page.has_next_page():
            page = await page.next_page()
    """

    data: list[T]
    has_more: bool
    next_cursor: str | None

    _client: BaseAsyncClient
    _path: str
    _params: dict[str, Any]
    _model: type[T]
    _bind_ctx: dict[str, Any] | None

    # Internal state for __aiter__ / __anext__
    _current_index: int
    _exhausted: bool

    def __init__(
        self,
        *,
        data: list[T],
        has_more: bool,
        next_cursor: str | None,
        client: BaseAsyncClient,
        path: str,
        params: dict[str, Any],
        model: type[T],
        bind_ctx: dict[str, Any] | None = None,
    ) -> None:
        self.data = data
        self.has_more = has_more
        self.next_cursor = next_cursor
        self._client = client
        self._path = path
        self._params = params
        self._model = model
        self._bind_ctx = bind_ctx
        self._current_index = 0
        self._exhausted = False
        _rebind_items(list(self.data), client, bind_ctx)

    def has_next_page(self) -> bool:
        """Return ``True`` if more pages are available."""
        return self.has_more and self.next_cursor is not None

    async def next_page(self) -> AsyncCursorPage[T]:
        """Fetch the next page of results.

        Returns:
            The next page.

        Raises:
            StopAsyncIteration: If there is no next page.
        """
        if not self.has_next_page():
            raise StopAsyncIteration
        params = {**self._params, "cursor": self.next_cursor}
        return await self._client._get_paginated(
            self._path,
            params=params,
            model=self._model,
            bind_ctx=self._bind_ctx,
        )

    def __aiter__(self) -> AsyncCursorPage[T]:
        """Return self as the async iterator."""
        self._current_index = 0
        self._exhausted = False
        return self

    async def __anext__(self) -> T:
        """Yield the next item, auto-fetching subsequent pages as needed."""
        while True:
            if self._current_index < len(self.data):
                item = self.data[self._current_index]
                self._current_index += 1
                return item
            if self._exhausted or not self.has_next_page():
                raise StopAsyncIteration
            # Fetch the next page and replace our state
            next_pg = await self.next_page()
            self.data = next_pg.data
            self.has_more = next_pg.has_more
            self.next_cursor = next_pg.next_cursor
            self._current_index = 0
            if not self.data:
                self._exhausted = True
                raise StopAsyncIteration

    def __len__(self) -> int:
        """Return the number of items on the current page."""
        return len(self.data)

    def __repr__(self) -> str:
        return (
            f"AsyncCursorPage(data=[...{len(self.data)} items], "
            f"has_more={self.has_more}, "
            f"next_cursor={self.next_cursor!r})"
        )
