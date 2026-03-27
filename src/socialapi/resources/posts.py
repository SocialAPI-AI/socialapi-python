from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, Any

from socialapi.models.posts import Post, PostMetrics

if TYPE_CHECKING:
    from socialapi._base_client import BaseAsyncClient, BaseSyncClient
    from socialapi._pagination import AsyncCursorPage, CursorPage


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
        from_date: datetime | str | None = None,
        to_date: datetime | str | None = None,
        search: str | None = None,
        sort: str | None = None,
        hidden: bool | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        timeout: float | None = None,
    ) -> CursorPage[Post]:
        """List posts with rich filtering.

        Args:
            account_ids: Filter by connected account IDs.
            status: Filter by post status.
            platform: Filter by platform.
            from_date: Start date filter (datetime or ISO 8601 string).
            to_date: End date filter (datetime or ISO 8601 string).
            search: Full-text search query.
            sort: Sort field and direction.
            hidden: Filter by hidden/visible state.
            limit: Maximum number of results per page.
            cursor: Pagination cursor from a previous response.
            timeout: Override the client-level timeout for this request.

        Returns:
            A paginated list of posts.

        Raises:
            AuthenticationError: If the API key is invalid.
            BadRequestError: If query parameters are invalid.
        """
        params: dict[str, Any] = {}
        if account_ids is not None:
            params["account_ids"] = account_ids
        if status is not None:
            params["status"] = status
        if platform is not None:
            params["platform"] = platform
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
        return self._client._get_paginated(
            "/v1/posts",
            params=params,
            model=Post,
            timeout=timeout,
        )

    def get(
        self,
        post_id: str,
        *,
        timeout: float | None = None,
    ) -> Post:
        """Get a single post by ID.

        Args:
            post_id: The post ID.
            timeout: Override the client-level timeout for this request.

        Returns:
            The post details with targets.

        Raises:
            NotFoundError: If the post does not exist.
            AuthenticationError: If the API key is invalid.
        """
        data = self._client._get(f"/v1/posts/{post_id}", timeout=timeout)
        return Post.model_validate(data)

    def delete(
        self,
        post_id: str,
        *,
        platform: str | None = None,
        timeout: float | None = None,
    ) -> None:
        """Delete a post or a specific platform target.

        Args:
            post_id: The post ID.
            platform: Optional platform to scope the deletion to a single target.
            timeout: Override the client-level timeout for this request.

        Raises:
            NotFoundError: If the post does not exist.
            AuthenticationError: If the API key is invalid.
        """
        params: dict[str, Any] = {}
        if platform is not None:
            params["platform"] = platform
        self._client._delete(f"/v1/posts/{post_id}", params=params, timeout=timeout)

    def retry(
        self,
        post_id: str,
        *,
        timeout: float | None = None,
    ) -> Post:
        """Retry publishing a failed post.

        Args:
            post_id: The post ID to retry.
            timeout: Override the client-level timeout for this request.

        Returns:
            The updated post.

        Raises:
            NotFoundError: If the post does not exist.
            BadRequestError: If the post is not in a retryable state.
            AuthenticationError: If the API key is invalid.
        """
        data = self._client._post(f"/v1/posts/{post_id}/retry", timeout=timeout)
        # API may return {"success": true} for retry
        if isinstance(data, dict) and "success" in data and "id" not in data:
            return self.get(post_id, timeout=timeout)
        return Post.model_validate(data)

    def unpublish(
        self,
        post_id: str,
        *,
        account_id: str | None = None,
        timeout: float | None = None,
    ) -> None:
        """Unpublish a post from one or all platforms.

        Args:
            post_id: The post ID.
            account_id: Optional account ID to scope unpublish to a single target.
            timeout: Override the client-level timeout for this request.

        Raises:
            NotFoundError: If the post does not exist.
            AuthenticationError: If the API key is invalid.
        """
        body: dict[str, Any] = {}
        if account_id is not None:
            body["account_id"] = account_id
        self._client._post(
            f"/v1/posts/{post_id}/unpublish",
            json=body if body else None,
            timeout=timeout,
        )

    def get_metrics(
        self,
        post_id: str,
        *,
        timeout: float | None = None,
    ) -> PostMetrics:
        """Get live engagement metrics for a post.

        Args:
            post_id: The post ID.
            timeout: Override the client-level timeout for this request.

        Returns:
            Per-target engagement metrics.

        Raises:
            NotFoundError: If the post does not exist.
            AuthenticationError: If the API key is invalid.
        """
        data = self._client._get(f"/v1/posts/{post_id}/metrics", timeout=timeout)
        # Response is {"data": {"post_id": ..., "targets": [...]}}
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
        from_date: datetime | str | None = None,
        to_date: datetime | str | None = None,
        search: str | None = None,
        sort: str | None = None,
        hidden: bool | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        timeout: float | None = None,
    ) -> AsyncCursorPage[Post]:
        """List posts with rich filtering.

        Args:
            account_ids: Filter by connected account IDs.
            status: Filter by post status.
            platform: Filter by platform.
            from_date: Start date filter (datetime or ISO 8601 string).
            to_date: End date filter (datetime or ISO 8601 string).
            search: Full-text search query.
            sort: Sort field and direction.
            hidden: Filter by hidden/visible state.
            limit: Maximum number of results per page.
            cursor: Pagination cursor from a previous response.
            timeout: Override the client-level timeout for this request.

        Returns:
            A paginated list of posts.

        Raises:
            AuthenticationError: If the API key is invalid.
            BadRequestError: If query parameters are invalid.
        """
        params: dict[str, Any] = {}
        if account_ids is not None:
            params["account_ids"] = account_ids
        if status is not None:
            params["status"] = status
        if platform is not None:
            params["platform"] = platform
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
        return await self._client._get_paginated(
            "/v1/posts",
            params=params,
            model=Post,
            timeout=timeout,
        )

    async def get(
        self,
        post_id: str,
        *,
        timeout: float | None = None,
    ) -> Post:
        """Get a single post by ID.

        Args:
            post_id: The post ID.
            timeout: Override the client-level timeout for this request.

        Returns:
            The post details with targets.

        Raises:
            NotFoundError: If the post does not exist.
            AuthenticationError: If the API key is invalid.
        """
        data = await self._client._get(f"/v1/posts/{post_id}", timeout=timeout)
        return Post.model_validate(data)

    async def delete(
        self,
        post_id: str,
        *,
        platform: str | None = None,
        timeout: float | None = None,
    ) -> None:
        """Delete a post or a specific platform target.

        Args:
            post_id: The post ID.
            platform: Optional platform to scope the deletion to a single target.
            timeout: Override the client-level timeout for this request.

        Raises:
            NotFoundError: If the post does not exist.
            AuthenticationError: If the API key is invalid.
        """
        params: dict[str, Any] = {}
        if platform is not None:
            params["platform"] = platform
        await self._client._delete(f"/v1/posts/{post_id}", params=params, timeout=timeout)

    async def retry(
        self,
        post_id: str,
        *,
        timeout: float | None = None,
    ) -> Post:
        """Retry publishing a failed post.

        Args:
            post_id: The post ID to retry.
            timeout: Override the client-level timeout for this request.

        Returns:
            The updated post.

        Raises:
            NotFoundError: If the post does not exist.
            BadRequestError: If the post is not in a retryable state.
            AuthenticationError: If the API key is invalid.
        """
        data = await self._client._post(f"/v1/posts/{post_id}/retry", timeout=timeout)
        if isinstance(data, dict) and "success" in data and "id" not in data:
            return await self.get(post_id, timeout=timeout)
        return Post.model_validate(data)

    async def unpublish(
        self,
        post_id: str,
        *,
        account_id: str | None = None,
        timeout: float | None = None,
    ) -> None:
        """Unpublish a post from one or all platforms.

        Args:
            post_id: The post ID.
            account_id: Optional account ID to scope unpublish to a single target.
            timeout: Override the client-level timeout for this request.

        Raises:
            NotFoundError: If the post does not exist.
            AuthenticationError: If the API key is invalid.
        """
        body: dict[str, Any] = {}
        if account_id is not None:
            body["account_id"] = account_id
        await self._client._post(
            f"/v1/posts/{post_id}/unpublish",
            json=body if body else None,
            timeout=timeout,
        )

    async def get_metrics(
        self,
        post_id: str,
        *,
        timeout: float | None = None,
    ) -> PostMetrics:
        """Get live engagement metrics for a post.

        Args:
            post_id: The post ID.
            timeout: Override the client-level timeout for this request.

        Returns:
            Per-target engagement metrics.

        Raises:
            NotFoundError: If the post does not exist.
            AuthenticationError: If the API key is invalid.
        """
        data = await self._client._get(f"/v1/posts/{post_id}/metrics", timeout=timeout)
        raw: dict[str, Any] = data.get("data", data)
        return PostMetrics.model_validate(raw)
