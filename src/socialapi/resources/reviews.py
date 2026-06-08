from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, Any

from socialapi._bound import bind_many
from socialapi.models.reviews import (
    AsyncReview,
    ReplyToReviewResponse,
    Review,
    ReviewFanoutMeta,
    ReviewList,
)

if TYPE_CHECKING:
    from socialapi._base_client import BaseAsyncClient, BaseSyncClient


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
    ) -> ReviewList:
        """List reviews across connected accounts via fan-out.

        Args:
            account_id: Filter by connected account ID.
            platform: Filter by platform (e.g. ``google``).
            since: Only return reviews created after this timestamp.
            limit: Maximum number of results (1-100, default 50).
            cursor: Pagination cursor from a previous response.
            timeout: Optional per-request timeout in seconds.

        Returns:
            A ``ReviewList`` containing ``data`` and ``meta`` (fan-out stats).

        Raises:
            AuthenticationError: If the API key is invalid.
        """
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
        body = self._client._get("/v1/inbox/reviews", params=params, timeout=timeout)
        raw_items: list[Any] = body.get("data", [])
        items = bind_many(Review, raw_items, client=self._client)
        meta = ReviewFanoutMeta.model_validate(body.get("meta", {}))
        return ReviewList(data=items, meta=meta)

    def reply(
        self,
        review_id: str,
        *,
        account_id: str,
        text: str,
        timeout: float | None = None,
    ) -> ReplyToReviewResponse:
        """Post a reply to a review.

        Args:
            review_id: The ID of the review to reply to.
            account_id: The connected account ID to reply from.
            text: The reply text to post.
            timeout: Optional per-request timeout in seconds.

        Returns:
            A response containing the reply ID and success flag.

        Raises:
            NotFoundError: If the account is not found.
            NotSupportedError: If the platform does not support review replies.
            RateLimitError: If the monthly interaction limit is exceeded.
        """
        body: dict[str, Any] = {"account_id": account_id, "text": text}
        data = self._client._post(f"/v1/inbox/reviews/{review_id}/reply", json=body, timeout=timeout)
        return ReplyToReviewResponse.model_validate(data)


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
    ) -> ReviewList:
        """List reviews across connected accounts via fan-out.

        Args:
            account_id: Filter by connected account ID.
            platform: Filter by platform (e.g. ``google``).
            since: Only return reviews created after this timestamp.
            limit: Maximum number of results (1-100, default 50).
            cursor: Pagination cursor from a previous response.
            timeout: Optional per-request timeout in seconds.

        Returns:
            A ``ReviewList`` containing ``data`` and ``meta`` (fan-out stats).

        Raises:
            AuthenticationError: If the API key is invalid.
        """
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
        body = await self._client._get("/v1/inbox/reviews", params=params, timeout=timeout)
        raw_items: list[Any] = body.get("data", [])
        items = bind_many(AsyncReview, raw_items, client=self._client)
        meta = ReviewFanoutMeta.model_validate(body.get("meta", {}))
        return ReviewList(data=items, meta=meta)

    async def reply(
        self,
        review_id: str,
        *,
        account_id: str,
        text: str,
        timeout: float | None = None,
    ) -> ReplyToReviewResponse:
        """Post a reply to a review.

        Args:
            review_id: The ID of the review to reply to.
            account_id: The connected account ID to reply from.
            text: The reply text to post.
            timeout: Optional per-request timeout in seconds.

        Returns:
            A response containing the reply ID and success flag.

        Raises:
            NotFoundError: If the account is not found.
            NotSupportedError: If the platform does not support review replies.
            RateLimitError: If the monthly interaction limit is exceeded.
        """
        body: dict[str, Any] = {"account_id": account_id, "text": text}
        data = await self._client._post(f"/v1/inbox/reviews/{review_id}/reply", json=body, timeout=timeout)
        return ReplyToReviewResponse.model_validate(data)
