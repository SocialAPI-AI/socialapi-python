"""Pagination helpers for auto-following cursors."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Generic, TypeVar

from pydantic import BaseModel

if TYPE_CHECKING:
    from collections.abc import Iterator

    from socialapi._types import QueryParams

T = TypeVar("T", bound=BaseModel)


class SyncPaginator(Generic[T]):
    """Synchronous auto-pagination iterator.

    Follows cursor-based pagination until all pages are exhausted,
    yielding individual items of type ``T`` across pages.

    Args:
        client: A ``SyncAPIClient`` instance used to fetch pages.
        path: The API path for the list endpoint.
        params: Initial query parameters (limit, since, etc.).
        model: The Pydantic model class for individual items.
    """

    def __init__(
        self,
        client: object,
        path: str,
        params: QueryParams,
        model: type[T],
    ) -> None:
        from socialapi._base_client import SyncAPIClient

        if not isinstance(client, SyncAPIClient):
            msg = "SyncPaginator requires a SyncAPIClient instance"
            raise TypeError(msg)

        self._client: SyncAPIClient = client
        self._path = path
        self._params = dict(params)
        self._model = model

    def __iter__(self) -> Iterator[T]:
        """Iterate over all items across all pages.

        Yields:
            Individual items deserialized as ``T``.
        """
        params = dict(self._params)

        while True:
            body: dict[str, Any] = self._client._get(self._path, params=params)

            items: list[dict[str, object]] = body.get("data", [])
            for item in items:
                yield self._model.model_validate(item)

            # Check for next page cursor.
            cursor = body.get("cursor")
            if not cursor or not items:
                break

            params["cursor"] = cursor


class AsyncPaginator(Generic[T]):
    """Asynchronous auto-pagination iterator.

    Follows cursor-based pagination until all pages are exhausted,
    yielding individual items of type ``T`` across pages.

    Args:
        client: An ``AsyncAPIClient`` instance used to fetch pages.
        path: The API path for the list endpoint.
        params: Initial query parameters (limit, since, etc.).
        model: The Pydantic model class for individual items.
    """

    def __init__(
        self,
        client: object,
        path: str,
        params: QueryParams,
        model: type[T],
    ) -> None:
        from socialapi._base_client import AsyncAPIClient

        if not isinstance(client, AsyncAPIClient):
            msg = "AsyncPaginator requires an AsyncAPIClient instance"
            raise TypeError(msg)

        self._client: AsyncAPIClient = client
        self._path = path
        self._params = dict(params)
        self._model = model

    async def __aiter__(self):
        """Iterate over all items across all pages.

        Yields:
            Individual items deserialized as ``T``.
        """
        params = dict(self._params)

        while True:
            body: dict[str, Any] = await self._client._get(self._path, params=params)

            items: list[dict[str, object]] = body.get("data", [])
            for item in items:
                yield self._model.model_validate(item)

            # Check for next page cursor.
            cursor = body.get("cursor")
            if not cursor or not items:
                break

            params["cursor"] = cursor
