from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, Any

from socialapi.models.comments import (
    AsyncCommentedPost,
    AsyncInboxComment,
    CommentedPost,
    InboxComment,
    ReplyToCommentResponse,
)

if TYPE_CHECKING:
    from socialapi._base_client import BaseAsyncClient, BaseSyncClient
    from socialapi._pagination import AsyncCursorPage, CursorPage


class Comments:
    """Manage inbox comments across platforms (sync)."""

    _client: BaseSyncClient

    def __init__(self, client: BaseSyncClient) -> None:
        self._client = client

    def list_posts(
        self,
        *,
        account_id: str | None = None,
        platform: str | None = None,
        min_comments: int | None = None,
        since: datetime | str | None = None,
        sort_by: str | None = None,
        sort_order: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        timeout: float | None = None,
    ) -> CursorPage[CommentedPost]:
        params: dict[str, Any] = {}
        if account_id is not None:
            params["account_id"] = account_id
        if platform is not None:
            params["platform"] = platform
        if min_comments is not None:
            params["min_comments"] = min_comments
        if since is not None:
            params["since"] = since.isoformat() if isinstance(since, datetime) else since
        if sort_by is not None:
            params["sort_by"] = sort_by
        if sort_order is not None:
            params["sort_order"] = sort_order
        if limit is not None:
            params["limit"] = limit
        if cursor is not None:
            params["cursor"] = cursor
        return self._client._get_paginated(
            "/v1/inbox/comments",
            params=params,
            model=CommentedPost,
            timeout=timeout,
        )

    def list(
        self,
        inbox_post_id: str,
        *,
        account_id: str,
        limit: int | None = None,
        cursor: str | None = None,
        timeout: float | None = None,
    ) -> CursorPage[InboxComment]:
        params: dict[str, Any] = {"account_id": account_id}
        if limit is not None:
            params["limit"] = limit
        if cursor is not None:
            params["cursor"] = cursor
        return self._client._get_paginated(
            f"/v1/inbox/comments/{inbox_post_id}",
            params=params,
            model=InboxComment,
            timeout=timeout,
            bind_ctx={"account_id": account_id, "inbox_post_id": inbox_post_id},
        )

    def list_replies(
        self,
        post_id: str,
        comment_id: str,
        *,
        account_id: str,
        limit: int | None = None,
        cursor: str | None = None,
        timeout: float | None = None,
    ) -> CursorPage[InboxComment]:
        """List replies to a comment."""
        params: dict[str, Any] = {"account_id": account_id}
        if limit is not None:
            params["limit"] = limit
        if cursor is not None:
            params["cursor"] = cursor
        return self._client._get_paginated(
            f"/v1/inbox/comments/{post_id}/{comment_id}/replies",
            params=params,
            model=InboxComment,
            timeout=timeout,
            bind_ctx={"account_id": account_id, "inbox_post_id": post_id},
        )

    def reply(
        self,
        post_id: str,
        *,
        account_id: str,
        text: str,
        comment_id: str | None = None,
        timeout: float | None = None,
    ) -> ReplyToCommentResponse:
        body: dict[str, Any] = {"account_id": account_id, "text": text}
        if comment_id is not None:
            body["comment_id"] = comment_id
        data = self._client._post(f"/v1/inbox/comments/{post_id}", json=body, timeout=timeout)
        return ReplyToCommentResponse.model_validate(data)

    def delete(
        self,
        post_id: str,
        comment_id: str,
        *,
        account_id: str,
        timeout: float | None = None,
    ) -> None:
        self._client._delete(
            f"/v1/inbox/comments/{post_id}/{comment_id}",
            params={"account_id": account_id},
            timeout=timeout,
        )

    def hide(
        self,
        post_id: str,
        comment_id: str,
        *,
        account_id: str,
        timeout: float | None = None,
    ) -> None:
        self._client._post(
            f"/v1/inbox/comments/{post_id}/{comment_id}/hide",
            json={"account_id": account_id},
            timeout=timeout,
        )

    def unhide(
        self,
        post_id: str,
        comment_id: str,
        *,
        account_id: str,
        timeout: float | None = None,
    ) -> None:
        self._client._delete(
            f"/v1/inbox/comments/{post_id}/{comment_id}/hide",
            params={"account_id": account_id},
            timeout=timeout,
        )

    def like(
        self,
        post_id: str,
        comment_id: str,
        *,
        account_id: str,
        timeout: float | None = None,
    ) -> None:
        self._client._post(
            f"/v1/inbox/comments/{post_id}/{comment_id}/like",
            json={"account_id": account_id},
            timeout=timeout,
        )

    def unlike(
        self,
        post_id: str,
        comment_id: str,
        *,
        account_id: str,
        timeout: float | None = None,
    ) -> None:
        self._client._delete(
            f"/v1/inbox/comments/{post_id}/{comment_id}/like",
            params={"account_id": account_id},
            timeout=timeout,
        )

    def private_reply(
        self,
        post_id: str,
        comment_id: str,
        *,
        account_id: str,
        text: str,
        timeout: float | None = None,
    ) -> None:
        self._client._post(
            f"/v1/inbox/comments/{post_id}/{comment_id}/private-reply",
            json={"account_id": account_id, "text": text},
            timeout=timeout,
        )


class AsyncComments:
    """Manage inbox comments across platforms (async)."""

    _client: BaseAsyncClient

    def __init__(self, client: BaseAsyncClient) -> None:
        self._client = client

    async def list_posts(
        self,
        *,
        account_id: str | None = None,
        platform: str | None = None,
        min_comments: int | None = None,
        since: datetime | str | None = None,
        sort_by: str | None = None,
        sort_order: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        timeout: float | None = None,
    ) -> AsyncCursorPage[AsyncCommentedPost]:
        params: dict[str, Any] = {}
        if account_id is not None:
            params["account_id"] = account_id
        if platform is not None:
            params["platform"] = platform
        if min_comments is not None:
            params["min_comments"] = min_comments
        if since is not None:
            params["since"] = since.isoformat() if isinstance(since, datetime) else since
        if sort_by is not None:
            params["sort_by"] = sort_by
        if sort_order is not None:
            params["sort_order"] = sort_order
        if limit is not None:
            params["limit"] = limit
        if cursor is not None:
            params["cursor"] = cursor
        return await self._client._get_paginated(
            "/v1/inbox/comments",
            params=params,
            model=AsyncCommentedPost,
            timeout=timeout,
        )

    async def list(
        self,
        inbox_post_id: str,
        *,
        account_id: str,
        limit: int | None = None,
        cursor: str | None = None,
        timeout: float | None = None,
    ) -> AsyncCursorPage[AsyncInboxComment]:
        params: dict[str, Any] = {"account_id": account_id}
        if limit is not None:
            params["limit"] = limit
        if cursor is not None:
            params["cursor"] = cursor
        return await self._client._get_paginated(
            f"/v1/inbox/comments/{inbox_post_id}",
            params=params,
            model=AsyncInboxComment,
            timeout=timeout,
            bind_ctx={"account_id": account_id, "inbox_post_id": inbox_post_id},
        )

    async def list_replies(
        self,
        post_id: str,
        comment_id: str,
        *,
        account_id: str,
        limit: int | None = None,
        cursor: str | None = None,
        timeout: float | None = None,
    ) -> AsyncCursorPage[AsyncInboxComment]:
        params: dict[str, Any] = {"account_id": account_id}
        if limit is not None:
            params["limit"] = limit
        if cursor is not None:
            params["cursor"] = cursor
        return await self._client._get_paginated(
            f"/v1/inbox/comments/{post_id}/{comment_id}/replies",
            params=params,
            model=AsyncInboxComment,
            timeout=timeout,
            bind_ctx={"account_id": account_id, "inbox_post_id": post_id},
        )

    async def reply(
        self,
        post_id: str,
        *,
        account_id: str,
        text: str,
        comment_id: str | None = None,
        timeout: float | None = None,
    ) -> ReplyToCommentResponse:
        body: dict[str, Any] = {"account_id": account_id, "text": text}
        if comment_id is not None:
            body["comment_id"] = comment_id
        data = await self._client._post(f"/v1/inbox/comments/{post_id}", json=body, timeout=timeout)
        return ReplyToCommentResponse.model_validate(data)

    async def delete(
        self,
        post_id: str,
        comment_id: str,
        *,
        account_id: str,
        timeout: float | None = None,
    ) -> None:
        await self._client._delete(
            f"/v1/inbox/comments/{post_id}/{comment_id}",
            params={"account_id": account_id},
            timeout=timeout,
        )

    async def hide(
        self,
        post_id: str,
        comment_id: str,
        *,
        account_id: str,
        timeout: float | None = None,
    ) -> None:
        await self._client._post(
            f"/v1/inbox/comments/{post_id}/{comment_id}/hide",
            json={"account_id": account_id},
            timeout=timeout,
        )

    async def unhide(
        self,
        post_id: str,
        comment_id: str,
        *,
        account_id: str,
        timeout: float | None = None,
    ) -> None:
        await self._client._delete(
            f"/v1/inbox/comments/{post_id}/{comment_id}/hide",
            params={"account_id": account_id},
            timeout=timeout,
        )

    async def like(
        self,
        post_id: str,
        comment_id: str,
        *,
        account_id: str,
        timeout: float | None = None,
    ) -> None:
        await self._client._post(
            f"/v1/inbox/comments/{post_id}/{comment_id}/like",
            json={"account_id": account_id},
            timeout=timeout,
        )

    async def unlike(
        self,
        post_id: str,
        comment_id: str,
        *,
        account_id: str,
        timeout: float | None = None,
    ) -> None:
        await self._client._delete(
            f"/v1/inbox/comments/{post_id}/{comment_id}/like",
            params={"account_id": account_id},
            timeout=timeout,
        )

    async def private_reply(
        self,
        post_id: str,
        comment_id: str,
        *,
        account_id: str,
        text: str,
        timeout: float | None = None,
    ) -> None:
        await self._client._post(
            f"/v1/inbox/comments/{post_id}/{comment_id}/private-reply",
            json={"account_id": account_id, "text": text},
            timeout=timeout,
        )
