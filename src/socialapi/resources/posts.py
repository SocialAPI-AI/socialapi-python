from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, Any

from socialapi.models.posts import AsyncPost, Post, PostMetrics

if TYPE_CHECKING:
    from socialapi._base_client import BaseAsyncClient, BaseSyncClient
    from socialapi._pagination import AsyncCursorPage, CursorPage


def _build_list_params(
    *,
    account_ids: list[str] | None,
    status: str | None,
    platform: str | None,
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
        from_date: datetime | str | None = None,
        to_date: datetime | str | None = None,
        search: str | None = None,
        sort: str | None = None,
        hidden: bool | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        timeout: float | None = None,
    ) -> CursorPage[Post]:
        params = _build_list_params(
            account_ids=account_ids,
            status=status,
            platform=platform,
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
        data = self._client._get(f"/v1/posts/{post_id}", timeout=timeout)
        post = Post.model_validate(data)
        post._bind(self._client)
        return post

    def delete(
        self,
        post_id: str,
        *,
        platform: str | None = None,
        timeout: float | None = None,
    ) -> None:
        params: dict[str, Any] = {}
        if platform is not None:
            params["platform"] = platform
        self._client._delete(f"/v1/posts/{post_id}", params=params or None, timeout=timeout)

    def retry(self, post_id: str, *, timeout: float | None = None) -> Post:
        data = self._client._post(f"/v1/posts/{post_id}/retry", timeout=timeout)
        if isinstance(data, dict) and "id" in data:
            post = Post.model_validate(data)
            post._bind(self._client)
            return post
        return self.get(post_id, timeout=timeout)

    def unpublish(
        self,
        post_id: str,
        *,
        account_id: str | None = None,
        timeout: float | None = None,
    ) -> None:
        body: dict[str, Any] = {}
        if account_id is not None:
            body["account_id"] = account_id
        self._client._post(
            f"/v1/posts/{post_id}/unpublish",
            json=body if body else None,
            timeout=timeout,
        )

    def get_metrics(self, post_id: str, *, timeout: float | None = None) -> PostMetrics:
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
        from_date: datetime | str | None = None,
        to_date: datetime | str | None = None,
        search: str | None = None,
        sort: str | None = None,
        hidden: bool | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        timeout: float | None = None,
    ) -> AsyncCursorPage[AsyncPost]:
        params = _build_list_params(
            account_ids=account_ids,
            status=status,
            platform=platform,
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
        data = await self._client._get(f"/v1/posts/{post_id}", timeout=timeout)
        post = AsyncPost.model_validate(data)
        post._bind(self._client)
        return post

    async def delete(
        self,
        post_id: str,
        *,
        platform: str | None = None,
        timeout: float | None = None,
    ) -> None:
        params: dict[str, Any] = {}
        if platform is not None:
            params["platform"] = platform
        await self._client._delete(f"/v1/posts/{post_id}", params=params or None, timeout=timeout)

    async def retry(self, post_id: str, *, timeout: float | None = None) -> AsyncPost:
        data = await self._client._post(f"/v1/posts/{post_id}/retry", timeout=timeout)
        if isinstance(data, dict) and "id" in data:
            post = AsyncPost.model_validate(data)
            post._bind(self._client)
            return post
        return await self.get(post_id, timeout=timeout)

    async def unpublish(
        self,
        post_id: str,
        *,
        account_id: str | None = None,
        timeout: float | None = None,
    ) -> None:
        body: dict[str, Any] = {}
        if account_id is not None:
            body["account_id"] = account_id
        await self._client._post(
            f"/v1/posts/{post_id}/unpublish",
            json=body if body else None,
            timeout=timeout,
        )

    async def get_metrics(self, post_id: str, *, timeout: float | None = None) -> PostMetrics:
        data = await self._client._get(f"/v1/posts/{post_id}/metrics", timeout=timeout)
        raw: dict[str, Any] = data.get("data", data)
        return PostMetrics.model_validate(raw)
