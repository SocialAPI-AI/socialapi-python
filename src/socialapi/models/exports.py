from __future__ import annotations

from datetime import datetime  # noqa: TC003
from typing import Any

from pydantic import BaseModel, ConfigDict

from socialapi._bound import _Bound


class ExportResult(BaseModel):
    """Download URLs returned when an export completes successfully.

    Maps to ``ExportResultURLs`` in the Go types. Both fields use omitempty
    so either may be absent.
    """

    model_config = ConfigDict(populate_by_name=True)

    excel_url: str | None = None
    report_url: str | None = None


class _ExportBase(_Bound):
    """Shared fields for Export / AsyncExport.

    Maps to ``ExportItem`` (list) and ``ExportStatusResponse`` (detail) in the
    Go endpoint types.
    """

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id: str | None = None
    account_id: str | None = None
    platform: str | None = None
    status: str | None = None
    total_videos: int | None = None
    processed_videos: int | None = None
    error: str | None = None
    created_at: datetime | None = None
    completed_at: datetime | None = None
    expires_at: datetime | None = None
    # Result block present only on a completed GET /v1/exports/{id} response
    result: ExportResult | None = None


class Export(_ExportBase):
    """An analytics export job (sync)."""

    def refresh(self, *, timeout: float | None = None) -> Export:
        """Re-fetch the export by ID to get fresh status / result.

        Returns:
            A new Export bound to the same client.

        Raises:
            UnboundModelError: If the model is not bound to a client.
        """
        client = self._client_or_raise_sync()
        export_id = self.id or self._ctx_value("export_id")
        data = client._get(f"/v1/exports/{export_id}", timeout=timeout)
        updated = Export.model_validate(data)
        updated._bind(client, {"export_id": export_id})
        return updated

    def list_videos(self, *, timeout: float | None = None) -> list[ExportVideo]:
        """List videos for this completed export.

        Returns:
            A list of ExportVideo objects.

        Raises:
            UnboundModelError: If the model is not bound to a client.
        """
        client = self._client_or_raise_sync()
        export_id = self.id or self._ctx_value("export_id")
        data = client._get(f"/v1/exports/{export_id}/videos", timeout=timeout)
        raw_items: list[Any] = data.get("data", [])
        return [ExportVideo.model_validate(item) for item in raw_items]


class AsyncExport(_ExportBase):
    """An analytics export job (async)."""

    async def refresh(self, *, timeout: float | None = None) -> AsyncExport:
        """Re-fetch the export by ID to get fresh status / result.

        Returns:
            A new AsyncExport bound to the same client.

        Raises:
            UnboundModelError: If the model is not bound to a client.
        """
        client = self._client_or_raise_async()
        export_id = self.id or self._ctx_value("export_id")
        data = await client._get(f"/v1/exports/{export_id}", timeout=timeout)
        updated = AsyncExport.model_validate(data)
        updated._bind(client, {"export_id": export_id})
        return updated

    async def list_videos(self, *, timeout: float | None = None) -> list[ExportVideo]:
        """List videos for this completed export.

        Returns:
            A list of ExportVideo objects.

        Raises:
            UnboundModelError: If the model is not bound to a client.
        """
        client = self._client_or_raise_async()
        export_id = self.id or self._ctx_value("export_id")
        data = await client._get(f"/v1/exports/{export_id}/videos", timeout=timeout)
        raw_items: list[Any] = data.get("data", [])
        return [ExportVideo.model_validate(item) for item in raw_items]


class ExportVideo(BaseModel):
    """A video record returned by ``GET /v1/exports/:id/videos`` (untyped in spec)."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id: str | None = None
    url: str | None = None
    title: str | None = None
    transcript: str | None = None


class CreateExportRequest(BaseModel):
    """Request body for ``POST /v1/accounts/:id/export``."""

    model_config = ConfigDict(populate_by_name=True)

    include_transcript: bool = False
    include_vision: bool = False
