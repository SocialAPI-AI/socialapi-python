from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, Any

from socialapi.models.posts import AsyncPost, DeletePostResponse, Post, PostMetrics

if TYPE_CHECKING:
    from socialapi._base_client import BaseAsyncClient, BaseSyncClient
    from socialapi._pagination import AsyncCursorPage, CursorPage


def _build_list_params(
    *,
    account_ids: list[str] | None,
    status: str | None,
    platform: str | None,
    page_id: str | None,
    from_date: datetime | str | None,
    to_date: datetime | str | None,
    search: str | None,
    sort: str | None,
    hidden: bool | None,
    limit: int | None,
    cursor: str | None,
) -> dict[str, Any]:
    params: dict[str, Any] = {}
    if account_ids is not None:
        params["account_ids"] = account_ids
    if status is not None:
        params["status"] = status
    if platform is not None:
        params["platform"] = platform
    if page_id is not None:
        params["page_id"] = page_id
    if from_date is not None:
        params["from"] = from_date.isoformat() if isinstance(from_date, datetime) else from_date
    if to_date is not None:
        params["to"] = to_date.isoformat() if isinstance(to_date, datetime) else to_date
    if search is not None:
        params["search"] = search
    if sort is not None:
        params["sort"] = sort
    if hidden is not None:
        params["hidden"] = hidden
    if limit is not None:
        params["limit"] = limit
    if cursor is not None:
        params["cursor"] = cursor
    return params


class Posts:
    """Read and manage posts (sync)."""

    _client: BaseSyncClient

    def __init__(self, client: BaseSyncClient) -> None:
        self._client = client

    def list(
        self,
        *,
        account_ids: list[str] | None = None,
        status: str | None = None,
        platform: str | None = None,
        page_id: str | None = None,
        from_date: datetime | str | None = None,
        to_date: datetime | str | None = None,
        search: str | None = None,
        sort: str | None = None,
        hidden: bool | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        timeout: float | None = None,
    ) -> CursorPage[Post]:
        """List posts with optional filtering.

        Args:
            account_ids: Filter by connected account IDs.
            status: Filter by post status.
            platform: Filter by platform slug.
            page_id: Filter by specific page ID (for multi-page accounts).
            from_date: Start of date range (RFC3339 or datetime).
            to_date: End of date range (RFC3339 or datetime).
            search: Case-insensitive text search.
            sort: Sort order (e.g. ``scheduled_asc``, ``created_desc``).
            hidden: Include hidden posts when ``True``.
            limit: Max results per page (default 25, max 100).
            cursor: Pagination cursor from previous response.
            timeout: Per-request timeout in seconds.

        Returns:
            Cursor-paginated page of Post objects.

        Raises:
            AuthenticationError: If the API key is invalid.
        """
        params = _build_list_params(
            account_ids=account_ids,
            status=status,
            platform=platform,
            page_id=page_id,
            from_date=from_date,
            to_date=to_date,
            search=search,
            sort=sort,
            hidden=hidden,
            limit=limit,
            cursor=cursor,
        )
        return self._client._get_paginated(
            "/v1/posts",
            params=params,
            model=Post,
            timeout=timeout,
        )

    def get(self, post_id: str, *, timeout: float | None = None) -> Post:
        """Get a single post by ID.

        Args:
            post_id: Post ID.
            timeout: Per-request timeout in seconds.

        Returns:
            Post object.

        Raises:
            NotFoundError: If the post does not exist.
        """
        data = self._client._get(f"/v1/posts/{post_id}", timeout=timeout)
        post = Post.model_validate(data)
        post._bind(self._client)
        return post

    def delete(
        self,
        post_id: str,
        *,
        timeout: float | None = None,
    ) -> DeletePostResponse:
        """Delete a post.

        Args:
            post_id: Post ID to delete.
            timeout: Per-request timeout in seconds.

        Returns:
            DeletePostResponse with per-platform deletion results.

        Raises:
            NotFoundError: If the post does not exist.
        """
        data = self._client._delete(f"/v1/posts/{post_id}", timeout=timeout)
        return DeletePostResponse.model_validate(data)

    def retry(self, post_id: str, *, timeout: float | None = None) -> None:
        """Retry a failed post.

        Args:
            post_id: Post ID.
            timeout: Per-request timeout in seconds.

        Raises:
            NotFoundError: If the post does not exist.
        """
        self._client._post(f"/v1/posts/{post_id}/retry", timeout=timeout)

    def unpublish(
        self,
        post_id: str,
        *,
        account_id: str | None = None,
        timeout: float | None = None,
    ) -> None:
        """Unpublish a post from one or all accounts.

        Args:
            post_id: Post ID.
            account_id: Optional account ID to unpublish from (otherwise all).
            timeout: Per-request timeout in seconds.

        Raises:
            NotFoundError: If the post does not exist.
        """
        body: dict[str, Any] = {}
        if account_id is not None:
            body["account_id"] = account_id
        self._client._post(
            f"/v1/posts/{post_id}/unpublish",
            json=body if body else None,
            timeout=timeout,
        )

    def get_metrics(self, post_id: str, *, timeout: float | None = None) -> PostMetrics:
        """Fetch live engagement metrics for a post.

        Args:
            post_id: Post ID.
            timeout: Per-request timeout in seconds.

        Returns:
            PostMetrics with per-platform engagement data.

        Raises:
            NotFoundError: If the post does not exist.
        """
        data = self._client._get(f"/v1/posts/{post_id}/metrics", timeout=timeout)
        raw: dict[str, Any] = data.get("data", data)
        return PostMetrics.model_validate(raw)


class AsyncPosts:
    """Read and manage posts (async)."""

    _client: BaseAsyncClient

    def __init__(self, client: BaseAsyncClient) -> None:
        self._client = client

    async def list(
        self,
        *,
        account_ids: list[str] | None = None,
        status: str | None = None,
        platform: str | None = None,
        page_id: str | None = None,
        from_date: datetime | str | None = None,
        to_date: datetime | str | None = None,
        search: str | None = None,
        sort: str | None = None,
        hidden: bool | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        timeout: float | None = None,
    ) -> AsyncCursorPage[AsyncPost]:
        """List posts with optional filtering.

        Args:
            account_ids: Filter by connected account IDs.
            status: Filter by post status.
            platform: Filter by platform slug.
            page_id: Filter by specific page ID (for multi-page accounts).
            from_date: Start of date range (RFC3339 or datetime).
            to_date: End of date range (RFC3339 or datetime).
            search: Case-insensitive text search.
            sort: Sort order (e.g. ``scheduled_asc``, ``created_desc``).
            hidden: Include hidden posts when ``True``.
            limit: Max results per page (default 25, max 100).
            cursor: Pagination cursor from previous response.
            timeout: Per-request timeout in seconds.

        Returns:
            Cursor-paginated page of AsyncPost objects.

        Raises:
            AuthenticationError: If the API key is invalid.
        """
        params = _build_list_params(
            account_ids=account_ids,
            status=status,
            platform=platform,
            page_id=page_id,
            from_date=from_date,
            to_date=to_date,
            search=search,
            sort=sort,
            hidden=hidden,
            limit=limit,
            cursor=cursor,
        )
        return await self._client._get_paginated(
            "/v1/posts",
            params=params,
            model=AsyncPost,
            timeout=timeout,
        )

    async def get(self, post_id: str, *, timeout: float | None = None) -> AsyncPost:
        """Get a single post by ID.

        Args:
            post_id: Post ID.
            timeout: Per-request timeout in seconds.

        Returns:
            AsyncPost object.

        Raises:
            NotFoundError: If the post does not exist.
        """
        data = await self._client._get(f"/v1/posts/{post_id}", timeout=timeout)
        post = AsyncPost.model_validate(data)
        post._bind(self._client)
        return post

    async def delete(
        self,
        post_id: str,
        *,
        timeout: float | None = None,
    ) -> DeletePostResponse:
        """Delete a post.

        Args:
            post_id: Post ID to delete.
            timeout: Per-request timeout in seconds.

        Returns:
            DeletePostResponse with per-platform deletion results.

        Raises:
            NotFoundError: If the post does not exist.
        """
        data = await self._client._delete(f"/v1/posts/{post_id}", timeout=timeout)
        return DeletePostResponse.model_validate(data)

    async def retry(self, post_id: str, *, timeout: float | None = None) -> None:
        """Retry a failed post.

        Args:
            post_id: Post ID.
            timeout: Per-request timeout in seconds.

        Raises:
            NotFoundError: If the post does not exist.
        """
        await self._client._post(f"/v1/posts/{post_id}/retry", timeout=timeout)

    async def unpublish(
        self,
        post_id: str,
        *,
        account_id: str | None = None,
        timeout: float | None = None,
    ) -> None:
        """Unpublish a post from one or all accounts.

        Args:
            post_id: Post ID.
            account_id: Optional account ID to unpublish from (otherwise all).
            timeout: Per-request timeout in seconds.

        Raises:
            NotFoundError: If the post does not exist.
        """
        body: dict[str, Any] = {}
        if account_id is not None:
            body["account_id"] = account_id
        await self._client._post(
            f"/v1/posts/{post_id}/unpublish",
            json=body if body else None,
            timeout=timeout,
        )

    async def get_metrics(self, post_id: str, *, timeout: float | None = None) -> PostMetrics:
        """Fetch live engagement metrics for a post.

        Args:
            post_id: Post ID.
            timeout: Per-request timeout in seconds.

        Returns:
            PostMetrics with per-platform engagement data.

        Raises:
            NotFoundError: If the post does not exist.
        """
        data = await self._client._get(f"/v1/posts/{post_id}/metrics", timeout=timeout)
        raw: dict[str, Any] = data.get("data", data)
        return PostMetrics.model_validate(raw)
