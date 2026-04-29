from __future__ import annotations

from datetime import datetime  # noqa: TC003
from typing import Any

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
        client = self._client_or_raise_sync()
        body: dict[str, Any] = {"account_id": self.account_id, "text": text}
        data = client._post(f"/v1/inbox/reviews/{self.id}/reply", json=body, timeout=timeout)
        return ReplyToReviewResponse.model_validate(data)

    def update_reply(self, *, text: str, timeout: float | None = None) -> ReplyToReviewResponse:
        client = self._client_or_raise_sync()
        body: dict[str, Any] = {"account_id": self.account_id, "text": text}
        data = client._put(f"/v1/inbox/reviews/{self.id}/reply", json=body, timeout=timeout)
        return ReplyToReviewResponse.model_validate(data)

    def delete_reply(self, *, timeout: float | None = None) -> None:
        client = self._client_or_raise_sync()
        client._delete(
            f"/v1/inbox/reviews/{self.id}/reply",
            params={"account_id": self.account_id},
            timeout=timeout,
        )


class AsyncReview(_ReviewBase):
    """A platform review (async)."""

    async def reply(self, *, text: str, timeout: float | None = None) -> ReplyToReviewResponse:
        client = self._client_or_raise_async()
        body: dict[str, Any] = {"account_id": self.account_id, "text": text}
        data = await client._post(f"/v1/inbox/reviews/{self.id}/reply", json=body, timeout=timeout)
        return ReplyToReviewResponse.model_validate(data)

    async def update_reply(self, *, text: str, timeout: float | None = None) -> ReplyToReviewResponse:
        client = self._client_or_raise_async()
        body: dict[str, Any] = {"account_id": self.account_id, "text": text}
        data = await client._put(f"/v1/inbox/reviews/{self.id}/reply", json=body, timeout=timeout)
        return ReplyToReviewResponse.model_validate(data)

    async def delete_reply(self, *, timeout: float | None = None) -> None:
        client = self._client_or_raise_async()
        await client._delete(
            f"/v1/inbox/reviews/{self.id}/reply",
            params={"account_id": self.account_id},
            timeout=timeout,
        )


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


class UpdateReviewReplyRequest(BaseModel):
    """Request body for ``PUT /v1/inbox/reviews/:id/reply``."""

    model_config = ConfigDict(populate_by_name=True)

    account_id: str
    text: str
