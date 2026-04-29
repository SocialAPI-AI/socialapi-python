from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, Any

from socialapi.models.posts import AsyncPost, Post, ValidationResult
from socialapi.models.publishing import ImportPostsResponse, MediaUploadURL, PlatformConstraints

if TYPE_CHECKING:
    from socialapi._base_client import BaseAsyncClient, BaseSyncClient


def _build_create_body(
    *,
    text: str,
    title: str | None,
    media_ids: list[str] | None,
    visibility: str | None,
    first_comment: str | None,
    scheduled_at: datetime | str | None,
    publish_now: bool,
    skip_duplicate_check: bool,
    targets: list[dict[str, Any]] | None,
) -> dict[str, Any]:
    body: dict[str, Any] = {"text": text}
    if title is not None:
        body["title"] = title
    if media_ids is not None:
        body["media_ids"] = media_ids
    if visibility is not None:
        body["visibility"] = visibility
    if first_comment is not None:
        body["first_comment"] = first_comment
    if scheduled_at is not None:
        body["scheduled_at"] = scheduled_at.isoformat() if isinstance(scheduled_at, datetime) else scheduled_at
    if publish_now:
        body["publish_now"] = True
    if skip_duplicate_check:
        body["skip_duplicate_check"] = True
    if targets is not None:
        body["targets"] = targets
    return body


def _build_update_body(
    *,
    text: str | None,
    title: str | None,
    media_ids: list[str] | None,
    visibility: str | None,
    first_comment: str | None,
    scheduled_at: datetime | str | None,
    hidden: bool | None,
    targets: list[dict[str, Any]] | None,
) -> dict[str, Any]:
    body: dict[str, Any] = {}
    if text is not None:
        body["text"] = text
    if title is not None:
        body["title"] = title
    if media_ids is not None:
        body["media_ids"] = media_ids
    if visibility is not None:
        body["visibility"] = visibility
    if first_comment is not None:
        body["first_comment"] = first_comment
    if scheduled_at is not None:
        body["scheduled_at"] = scheduled_at.isoformat() if isinstance(scheduled_at, datetime) else scheduled_at
    if hidden is not None:
        body["hidden"] = hidden
    if targets is not None:
        body["targets"] = targets
    return body


def _build_validate_body(
    *,
    text: str,
    platforms: list[str] | None,
    account_ids: list[str] | None,
    media_ids: list[str] | None,
    scheduled_at: datetime | str | None,
    targets: list[dict[str, Any]] | None,
) -> dict[str, Any]:
    body: dict[str, Any] = {"text": text}
    if platforms is not None:
        body["platforms"] = platforms
    if account_ids is not None:
        body["account_ids"] = account_ids
    if media_ids is not None:
        body["media_ids"] = media_ids
    if scheduled_at is not None:
        body["scheduled_at"] = scheduled_at.isoformat() if isinstance(scheduled_at, datetime) else scheduled_at
    if targets is not None:
        body["targets"] = targets
    return body


class Publishing:
    """Create, update, and validate posts for publishing (sync)."""

    _client: BaseSyncClient

    def __init__(self, client: BaseSyncClient) -> None:
        self._client = client

    def create(
        self,
        *,
        text: str,
        title: str | None = None,
        media_ids: list[str] | None = None,
        visibility: str | None = None,
        first_comment: str | None = None,
        scheduled_at: datetime | str | None = None,
        publish_now: bool = False,
        skip_duplicate_check: bool = False,
        targets: list[dict[str, Any]] | None = None,
        timeout: float | None = None,
    ) -> Post:
        body = _build_create_body(
            text=text,
            title=title,
            media_ids=media_ids,
            visibility=visibility,
            first_comment=first_comment,
            scheduled_at=scheduled_at,
            publish_now=publish_now,
            skip_duplicate_check=skip_duplicate_check,
            targets=targets,
        )
        data = self._client._post("/v1/posts", json=body, timeout=timeout)
        post = Post.model_validate(data)
        post._bind(self._client)
        return post

    def update(
        self,
        post_id: str,
        *,
        text: str | None = None,
        title: str | None = None,
        media_ids: list[str] | None = None,
        visibility: str | None = None,
        first_comment: str | None = None,
        scheduled_at: datetime | str | None = None,
        hidden: bool | None = None,
        targets: list[dict[str, Any]] | None = None,
        timeout: float | None = None,
    ) -> Post:
        body = _build_update_body(
            text=text,
            title=title,
            media_ids=media_ids,
            visibility=visibility,
            first_comment=first_comment,
            scheduled_at=scheduled_at,
            hidden=hidden,
            targets=targets,
        )
        data = self._client._patch(f"/v1/posts/{post_id}", json=body, timeout=timeout)
        post = Post.model_validate(data)
        post._bind(self._client)
        return post

    def get_constraints(
        self,
        *,
        platform: str | None = None,
        timeout: float | None = None,
    ) -> dict[str, PlatformConstraints]:
        params: dict[str, Any] = {}
        if platform is not None:
            params["platform"] = platform
        data = self._client._get("/v1/posts/validate", params=params or None, timeout=timeout)
        raw: dict[str, Any] = data.get("data", data)
        return {k: PlatformConstraints.model_validate({**v, "platform": k}) for k, v in raw.items()}

    def validate(
        self,
        *,
        text: str,
        platforms: list[str] | None = None,
        account_ids: list[str] | None = None,
        media_ids: list[str] | None = None,
        scheduled_at: datetime | str | None = None,
        targets: list[dict[str, Any]] | None = None,
        timeout: float | None = None,
    ) -> ValidationResult:
        body = _build_validate_body(
            text=text,
            platforms=platforms,
            account_ids=account_ids,
            media_ids=media_ids,
            scheduled_at=scheduled_at,
            targets=targets,
        )
        data = self._client._post("/v1/posts/validate", json=body, timeout=timeout)
        return ValidationResult.model_validate(data)

    def get_upload_url(
        self,
        *,
        media_type: str,
        filename: str,
        timeout: float | None = None,
    ) -> MediaUploadURL:
        params: dict[str, Any] = {"content_type": media_type, "filename": filename}
        data = self._client._get("/v1/media/upload-url", params=params, timeout=timeout)
        return MediaUploadURL.model_validate(data)

    def verify_upload(self, media_id: str, *, timeout: float | None = None) -> None:
        self._client._post(f"/v1/media/{media_id}/verify", timeout=timeout)

    def import_posts(
        self,
        *,
        file: Any,
        dry_run: bool = False,
        timeout: float | None = None,
    ) -> ImportPostsResponse:
        params: dict[str, Any] = {}
        if dry_run:
            params["dry_run"] = "true"
        data = self._client._post(
            "/v1/posts/import",
            json={"file": "csv"},
            params=params or None,
            timeout=timeout,
        )
        return ImportPostsResponse.model_validate(data)


class AsyncPublishing:
    """Create, update, and validate posts for publishing (async)."""

    _client: BaseAsyncClient

    def __init__(self, client: BaseAsyncClient) -> None:
        self._client = client

    async def create(
        self,
        *,
        text: str,
        title: str | None = None,
        media_ids: list[str] | None = None,
        visibility: str | None = None,
        first_comment: str | None = None,
        scheduled_at: datetime | str | None = None,
        publish_now: bool = False,
        skip_duplicate_check: bool = False,
        targets: list[dict[str, Any]] | None = None,
        timeout: float | None = None,
    ) -> AsyncPost:
        body = _build_create_body(
            text=text,
            title=title,
            media_ids=media_ids,
            visibility=visibility,
            first_comment=first_comment,
            scheduled_at=scheduled_at,
            publish_now=publish_now,
            skip_duplicate_check=skip_duplicate_check,
            targets=targets,
        )
        data = await self._client._post("/v1/posts", json=body, timeout=timeout)
        post = AsyncPost.model_validate(data)
        post._bind(self._client)
        return post

    async def update(
        self,
        post_id: str,
        *,
        text: str | None = None,
        title: str | None = None,
        media_ids: list[str] | None = None,
        visibility: str | None = None,
        first_comment: str | None = None,
        scheduled_at: datetime | str | None = None,
        hidden: bool | None = None,
        targets: list[dict[str, Any]] | None = None,
        timeout: float | None = None,
    ) -> AsyncPost:
        body = _build_update_body(
            text=text,
            title=title,
            media_ids=media_ids,
            visibility=visibility,
            first_comment=first_comment,
            scheduled_at=scheduled_at,
            hidden=hidden,
            targets=targets,
        )
        data = await self._client._patch(f"/v1/posts/{post_id}", json=body, timeout=timeout)
        post = AsyncPost.model_validate(data)
        post._bind(self._client)
        return post

    async def get_constraints(
        self,
        *,
        platform: str | None = None,
        timeout: float | None = None,
    ) -> dict[str, PlatformConstraints]:
        params: dict[str, Any] = {}
        if platform is not None:
            params["platform"] = platform
        data = await self._client._get("/v1/posts/validate", params=params or None, timeout=timeout)
        raw: dict[str, Any] = data.get("data", data)
        return {k: PlatformConstraints.model_validate({**v, "platform": k}) for k, v in raw.items()}

    async def validate(
        self,
        *,
        text: str,
        platforms: list[str] | None = None,
        account_ids: list[str] | None = None,
        media_ids: list[str] | None = None,
        scheduled_at: datetime | str | None = None,
        targets: list[dict[str, Any]] | None = None,
        timeout: float | None = None,
    ) -> ValidationResult:
        body = _build_validate_body(
            text=text,
            platforms=platforms,
            account_ids=account_ids,
            media_ids=media_ids,
            scheduled_at=scheduled_at,
            targets=targets,
        )
        data = await self._client._post("/v1/posts/validate", json=body, timeout=timeout)
        return ValidationResult.model_validate(data)

    async def get_upload_url(
        self,
        *,
        media_type: str,
        filename: str,
        timeout: float | None = None,
    ) -> MediaUploadURL:
        params: dict[str, Any] = {"content_type": media_type, "filename": filename}
        data = await self._client._get("/v1/media/upload-url", params=params, timeout=timeout)
        return MediaUploadURL.model_validate(data)

    async def verify_upload(self, media_id: str, *, timeout: float | None = None) -> None:
        await self._client._post(f"/v1/media/{media_id}/verify", timeout=timeout)

    async def import_posts(
        self,
        *,
        file: Any,
        dry_run: bool = False,
        timeout: float | None = None,
    ) -> ImportPostsResponse:
        params: dict[str, Any] = {}
        if dry_run:
            params["dry_run"] = "true"
        data = await self._client._post(
            "/v1/posts/import",
            json={"file": "csv"},
            params=params or None,
            timeout=timeout,
        )
        return ImportPostsResponse.model_validate(data)
