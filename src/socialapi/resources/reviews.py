from __future__ import annotations

from typing import TYPE_CHECKING, Any

from socialapi.models.reviews import ReplyToReviewResponse, Review

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
        limit: int | None = None,
        cursor: str | None = None,
        timeout: float | None = None,
    ) -> CursorPage[Review]:
        """List reviews across connected accounts.

        Reviews are proxied in real-time from platforms and not stored.
        Currently only Google Business Profile returns reviews.

        Args:
            account_id: Filter by connected account.
            platform: Filter by platform.
            limit: Maximum number of results.
            cursor: Pagination cursor from a previous response.
            timeout: Override the client-level timeout for this request.

        Returns:
            A paginated list of reviews.

        Raises:
            AuthenticationError: If the API key is invalid.
            NotSupportedError: If the platform does not support reviews.
        """
        params: dict[str, Any] = {}
        if account_id is not None:
            params["account_id"] = account_id
        if platform is not None:
            params["platform"] = platform
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
        """Reply to a review.

        Args:
            review_id: The review ID to reply to.
            account_id: The connected account ID.
            text: Reply text content.
            timeout: Override the client-level timeout for this request.

        Returns:
            The reply result.

        Raises:
            NotFoundError: If the review does not exist.
            NotSupportedError: If the platform does not support review replies.
            AuthenticationError: If the API key is invalid.
        """
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
        """Update an existing review reply.

        Args:
            review_id: The review ID.
            account_id: The connected account ID.
            text: Updated reply text content.
            timeout: Override the client-level timeout for this request.

        Returns:
            The updated reply result.

        Raises:
            NotFoundError: If the review does not exist.
            NotSupportedError: If the platform does not support reply updates.
            AuthenticationError: If the API key is invalid.
        """
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
        """Delete a review reply.

        Args:
            review_id: The review ID whose reply to delete.
            account_id: The connected account ID.
            timeout: Override the client-level timeout for this request.

        Raises:
            NotFoundError: If the review does not exist.
            NotSupportedError: If the platform does not support reply deletion.
            AuthenticationError: If the API key is invalid.
        """
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
        limit: int | None = None,
        cursor: str | None = None,
        timeout: float | None = None,
    ) -> AsyncCursorPage[Review]:
        """List reviews across connected accounts.

        Reviews are proxied in real-time from platforms and not stored.
        Currently only Google Business Profile returns reviews.

        Args:
            account_id: Filter by connected account.
            platform: Filter by platform.
            limit: Maximum number of results.
            cursor: Pagination cursor from a previous response.
            timeout: Override the client-level timeout for this request.

        Returns:
            A paginated list of reviews.

        Raises:
            AuthenticationError: If the API key is invalid.
            NotSupportedError: If the platform does not support reviews.
        """
        params: dict[str, Any] = {}
        if account_id is not None:
            params["account_id"] = account_id
        if platform is not None:
            params["platform"] = platform
        if limit is not None:
            params["limit"] = limit
        if cursor is not None:
            params["cursor"] = cursor
        return await self._client._get_paginated(
            "/v1/inbox/reviews",
            params=params,
            model=Review,
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
        """Reply to a review.

        Args:
            review_id: The review ID to reply to.
            account_id: The connected account ID.
            text: Reply text content.
            timeout: Override the client-level timeout for this request.

        Returns:
            The reply result.

        Raises:
            NotFoundError: If the review does not exist.
            NotSupportedError: If the platform does not support review replies.
            AuthenticationError: If the API key is invalid.
        """
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
        """Update an existing review reply.

        Args:
            review_id: The review ID.
            account_id: The connected account ID.
            text: Updated reply text content.
            timeout: Override the client-level timeout for this request.

        Returns:
            The updated reply result.

        Raises:
            NotFoundError: If the review does not exist.
            NotSupportedError: If the platform does not support reply updates.
            AuthenticationError: If the API key is invalid.
        """
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
        """Delete a review reply.

        Args:
            review_id: The review ID whose reply to delete.
            account_id: The connected account ID.
            timeout: Override the client-level timeout for this request.

        Raises:
            NotFoundError: If the review does not exist.
            NotSupportedError: If the platform does not support reply deletion.
            AuthenticationError: If the API key is invalid.
        """
        await self._client._delete(
            f"/v1/inbox/reviews/{review_id}/reply",
            params={"account_id": account_id},
            timeout=timeout,
        )
