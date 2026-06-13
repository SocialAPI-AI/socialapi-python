from __future__ import annotations

from typing import TYPE_CHECKING, Any

from socialapi.models.exports import AsyncExport, Export, ExportVideo

if TYPE_CHECKING:
    from socialapi._base_client import BaseAsyncClient, BaseSyncClient


class Exports:
    """Access analytics export jobs (sync)."""

    _client: BaseSyncClient

    def __init__(self, client: BaseSyncClient) -> None:
        self._client = client

    def list(self, *, status: str | None = None, timeout: float | None = None) -> list[Export]:
        """List recent export jobs (50 most recent).

        Args:
            status: Optional filter by export status (pending, processing, completed, failed).
            timeout: Optional per-request timeout override in seconds.

        Returns:
            A list of Export objects.

        Raises:
            AuthenticationError: If the API key is invalid.
        """
        params: dict[str, Any] = {}
        if status is not None:
            params["status"] = status
        data = self._client._get("/v1/exports", params=params or None, timeout=timeout)
        raw_items: list[Any] = data.get("exports", [])
        items = [Export.model_validate(item) for item in raw_items]
        for item in items:
            ctx = {"export_id": item.id} if item.id else {}
            item._bind(self._client, ctx)
        return items

    def get(self, export_id: str, *, timeout: float | None = None) -> Export:
        """Get export status and result.

        Args:
            export_id: The export job ID.
            timeout: Optional per-request timeout override in seconds.

        Returns:
            An Export object with current status and optional result URLs.

        Raises:
            NotFoundError: If the export does not exist.
        """
        data = self._client._get(f"/v1/exports/{export_id}", timeout=timeout)
        export = Export.model_validate(data)
        export._bind(self._client, {"export_id": export_id})
        return export

    def list_videos(self, export_id: str, *, timeout: float | None = None) -> list[ExportVideo]:
        """List videos in a completed export.

        Args:
            export_id: The export job ID.
            timeout: Optional per-request timeout override in seconds.

        Returns:
            A list of ExportVideo objects.

        Raises:
            NotFoundError: If the export does not exist or is not completed.
        """
        data = self._client._get(f"/v1/exports/{export_id}/videos", timeout=timeout)
        raw_items: list[Any] = data.get("data", [])
        return [ExportVideo.model_validate(item) for item in raw_items]


class AsyncExports:
    """Access analytics export jobs (async)."""

    _client: BaseAsyncClient

    def __init__(self, client: BaseAsyncClient) -> None:
        self._client = client

    async def list(self, *, status: str | None = None, timeout: float | None = None) -> list[AsyncExport]:
        """List recent export jobs (50 most recent).

        Args:
            status: Optional filter by export status (pending, processing, completed, failed).
            timeout: Optional per-request timeout override in seconds.

        Returns:
            A list of AsyncExport objects.

        Raises:
            AuthenticationError: If the API key is invalid.
        """
        params: dict[str, Any] = {}
        if status is not None:
            params["status"] = status
        data = await self._client._get("/v1/exports", params=params or None, timeout=timeout)
        raw_items: list[Any] = data.get("exports", [])
        items = [AsyncExport.model_validate(item) for item in raw_items]
        for item in items:
            ctx = {"export_id": item.id} if item.id else {}
            item._bind(self._client, ctx)
        return items

    async def get(self, export_id: str, *, timeout: float | None = None) -> AsyncExport:
        """Get export status and result.

        Args:
            export_id: The export job ID.
            timeout: Optional per-request timeout override in seconds.

        Returns:
            An AsyncExport object with current status and optional result URLs.

        Raises:
            NotFoundError: If the export does not exist.
        """
        data = await self._client._get(f"/v1/exports/{export_id}", timeout=timeout)
        export = AsyncExport.model_validate(data)
        export._bind(self._client, {"export_id": export_id})
        return export

    async def list_videos(self, export_id: str, *, timeout: float | None = None) -> list[ExportVideo]:
        """List videos in a completed export.

        Args:
            export_id: The export job ID.
            timeout: Optional per-request timeout override in seconds.

        Returns:
            A list of ExportVideo objects.

        Raises:
            NotFoundError: If the export does not exist or is not completed.
        """
        data = await self._client._get(f"/v1/exports/{export_id}/videos", timeout=timeout)
        raw_items: list[Any] = data.get("data", [])
        return [ExportVideo.model_validate(item) for item in raw_items]
