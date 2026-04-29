from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, Any

from socialapi.models.reviews import AsyncReview, ReplyToReviewResponse, Review

if TYPE_CHECKING:
    from socialapi._base_client import BaseAsyncClient, BaseSyncClient
    from socialapi._pagination import AsyncCursorPage, CursorPage


class Reviews:
    """Manage reviews in the unified inbox (sync)."""

    _client: BaseSyncClient

    def __init__(self, client: BaseSyncClient) -> None:
        self._client = client

    def list(
        self,
        *,
        account_id: str | None = None,
        platform: str | None = None,
        since: datetime | str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        timeout: float | None = None,
    ) -> CursorPage[Review]:
        params: dict[str, Any] = {}
        if account_id is not None:
            params["account_id"] = account_id
        if platform is not None:
            params["platform"] = platform
        if since is not None:
            params["since"] = since.isoformat() if isinstance(since, datetime) else since
        if limit is not None:
            params["limit"] = limit
        if cursor is not None:
            params["cursor"] = cursor
        return self._client._get_paginated(
            "/v1/inbox/reviews",
            params=params,
            model=Review,
            timeout=timeout,
        )

    def reply(
        self,
        review_id: str,
        *,
        account_id: str,
        text: str,
        timeout: float | None = None,
    ) -> ReplyToReviewResponse:
        body: dict[str, Any] = {"account_id": account_id, "text": text}
        data = self._client._post(f"/v1/inbox/reviews/{review_id}/reply", json=body, timeout=timeout)
        return ReplyToReviewResponse.model_validate(data)

    def update_reply(
        self,
        review_id: str,
        *,
        account_id: str,
        text: str,
        timeout: float | None = None,
    ) -> ReplyToReviewResponse:
        body: dict[str, Any] = {"account_id": account_id, "text": text}
        data = self._client._put(f"/v1/inbox/reviews/{review_id}/reply", json=body, timeout=timeout)
        return ReplyToReviewResponse.model_validate(data)

    def delete_reply(
        self,
        review_id: str,
        *,
        account_id: str,
        timeout: float | None = None,
    ) -> None:
        self._client._delete(
            f"/v1/inbox/reviews/{review_id}/reply",
            params={"account_id": account_id},
            timeout=timeout,
        )


class AsyncReviews:
    """Manage reviews in the unified inbox (async)."""

    _client: BaseAsyncClient

    def __init__(self, client: BaseAsyncClient) -> None:
        self._client = client

    async def list(
        self,
        *,
        account_id: str | None = None,
        platform: str | None = None,
        since: datetime | str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        timeout: float | None = None,
    ) -> AsyncCursorPage[AsyncReview]:
        params: dict[str, Any] = {}
        if account_id is not None:
            params["account_id"] = account_id
        if platform is not None:
            params["platform"] = platform
        if since is not None:
            params["since"] = since.isoformat() if isinstance(since, datetime) else since
        if limit is not None:
            params["limit"] = limit
        if cursor is not None:
            params["cursor"] = cursor
        return await self._client._get_paginated(
            "/v1/inbox/reviews",
            params=params,
            model=AsyncReview,
            timeout=timeout,
        )

    async def reply(
        self,
        review_id: str,
        *,
        account_id: str,
        text: str,
        timeout: float | None = None,
    ) -> ReplyToReviewResponse:
        body: dict[str, Any] = {"account_id": account_id, "text": text}
        data = await self._client._post(f"/v1/inbox/reviews/{review_id}/reply", json=body, timeout=timeout)
        return ReplyToReviewResponse.model_validate(data)

    async def update_reply(
        self,
        review_id: str,
        *,
        account_id: str,
        text: str,
        timeout: float | None = None,
    ) -> ReplyToReviewResponse:
        body: dict[str, Any] = {"account_id": account_id, "text": text}
        data = await self._client._put(f"/v1/inbox/reviews/{review_id}/reply", json=body, timeout=timeout)
        return ReplyToReviewResponse.model_validate(data)

    async def delete_reply(
        self,
        review_id: str,
        *,
        account_id: str,
        timeout: float | None = None,
    ) -> None:
        await self._client._delete(
            f"/v1/inbox/reviews/{review_id}/reply",
            params={"account_id": account_id},
            timeout=timeout,
        )
