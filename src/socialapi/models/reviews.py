from __future__ import annotations

from datetime import datetime  # noqa: TC003
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from collections.abc import Iterator

from pydantic import BaseModel, ConfigDict

from socialapi._bound import _Bound


class _ReviewBase(_Bound):
    """Shared fields for Review / AsyncReview."""

    id: str
    platform: str
    account_id: str
    rating: int
    text: str | None = None
    author: str
    created_at: datetime


class Review(_ReviewBase):
    """A platform review (sync)."""

    def reply(self, *, text: str, timeout: float | None = None) -> ReplyToReviewResponse:
        """Post a reply to this review.

        Args:
            text: The reply text to post.
            timeout: Optional per-request timeout in seconds.

        Returns:
            A response containing the reply ID and success flag.

        Raises:
            UnboundModelError: If this model is not bound to a client.
        """
        client = self._client_or_raise_sync()
        body: dict[str, Any] = {"account_id": self.account_id, "text": text}
        data = client._post(f"/v1/inbox/reviews/{self.id}/reply", json=body, timeout=timeout)
        return ReplyToReviewResponse.model_validate(data)


class AsyncReview(_ReviewBase):
    """A platform review (async)."""

    async def reply(self, *, text: str, timeout: float | None = None) -> ReplyToReviewResponse:
        """Post a reply to this review.

        Args:
            text: The reply text to post.
            timeout: Optional per-request timeout in seconds.

        Returns:
            A response containing the reply ID and success flag.

        Raises:
            UnboundModelError: If this model is not bound to an async client.
        """
        client = self._client_or_raise_async()
        body: dict[str, Any] = {"account_id": self.account_id, "text": text}
        data = await client._post(f"/v1/inbox/reviews/{self.id}/reply", json=body, timeout=timeout)
        return ReplyToReviewResponse.model_validate(data)


class ReplyToReviewRequest(BaseModel):
    """Request body for ``POST /v1/inbox/reviews/:id/reply``."""

    model_config = ConfigDict(populate_by_name=True)

    account_id: str
    text: str


class ReplyToReviewResponse(BaseModel):
    """Response after replying to a review."""

    model_config = ConfigDict(populate_by_name=True)

    success: bool
    reply_id: str


class FailedAccount(BaseModel):
    """A single account that could not be queried during fan-out.

    Mirrors the Go ``service.FailedAccount`` struct exactly.
    """

    model_config = ConfigDict(populate_by_name=True)

    account_id: str
    platform: str
    error: str
    code: str | None = None


class ReviewFanoutMeta(BaseModel):
    """Aggregate statistics about a completed reviews fan-out query."""

    model_config = ConfigDict(populate_by_name=True)

    accounts_queried: int
    accounts_failed: int
    failed_accounts: list[FailedAccount]


class ReviewList:
    """Result of ``GET /v1/inbox/reviews``.

    Holds the fan-out data and meta. Supports iteration over ``data``
    and ``len()`` for ergonomic use.
    """

    def __init__(self, *, data: list[Review] | list[AsyncReview], meta: ReviewFanoutMeta) -> None:
        self.data = data
        self.meta = meta

    def __iter__(self) -> Iterator[Review | AsyncReview]:
        """Iterate over the reviews in ``data``."""
        return iter(self.data)

    def __len__(self) -> int:
        """Return the number of reviews in ``data``."""
        return len(self.data)

    def __repr__(self) -> str:
        return f"ReviewList(data={self.data!r}, meta={self.meta!r})"
