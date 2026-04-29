from __future__ import annotations

from datetime import datetime  # noqa: TC003
from typing import Any

from pydantic import BaseModel, ConfigDict

from socialapi._bound import _Bound


class _ExportBase(_Bound):
    """Shared fields for Export / AsyncExport.

    The OpenAPI spec returns a free-form object for export endpoints; the SDK
    captures common fields (``id``, ``status``, ``progress``, ``download_url``,
    ``report_url``) and tolerates extras.
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id: str | None = None
    account_id: str | None = None
    status: str | None = None
    progress: float | None = None
    download_url: str | None = None
    report_url: str | None = None
    created_at: datetime | None = None
    completed_at: datetime | None = None


class Export(_ExportBase):
    """An analytics export job (sync)."""

    def refresh(self, *, timeout: float | None = None) -> Export:
        """Re-fetch the export by ID to get fresh status / progress."""
        client = self._client_or_raise_sync()
        export_id = self.id or self._ctx_value("export_id")
        data = client._get(f"/v1/exports/{export_id}", timeout=timeout)
        updated = Export.model_validate(data)
        updated._bind(client, {"export_id": export_id})
        return updated

    def list_videos(self, *, timeout: float | None = None) -> list[ExportVideo]:
        client = self._client_or_raise_sync()
        export_id = self.id or self._ctx_value("export_id")
        data = client._get(f"/exports/{export_id}/videos", timeout=timeout)
        raw_items: list[Any] = data.get("data", [])
        return [ExportVideo.model_validate(item) for item in raw_items]


class AsyncExport(_ExportBase):
    """An analytics export job (async)."""

    async def refresh(self, *, timeout: float | None = None) -> AsyncExport:
        client = self._client_or_raise_async()
        export_id = self.id or self._ctx_value("export_id")
        data = await client._get(f"/v1/exports/{export_id}", timeout=timeout)
        updated = AsyncExport.model_validate(data)
        updated._bind(client, {"export_id": export_id})
        return updated

    async def list_videos(self, *, timeout: float | None = None) -> list[ExportVideo]:
        client = self._client_or_raise_async()
        export_id = self.id or self._ctx_value("export_id")
        data = await client._get(f"/exports/{export_id}/videos", timeout=timeout)
        raw_items: list[Any] = data.get("data", [])
        return [ExportVideo.model_validate(item) for item in raw_items]


class ExportVideo(BaseModel):
    """A video record returned by ``GET /exports/:id/videos`` (untyped in spec)."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id: str | None = None
    url: str | None = None
    title: str | None = None
    transcript: str | None = None


class CreateExportRequest(BaseModel):
    """Request body for ``POST /v1/accounts/:id/export``."""

    model_config = ConfigDict(populate_by_name=True)

    include_transcript: bool | None = None
    include_vision: bool | None = None
