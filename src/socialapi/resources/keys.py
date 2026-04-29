from __future__ import annotations

from typing import TYPE_CHECKING, Any

from socialapi.models.keys import APIKey, AsyncAPIKey, CreateKeyResponse

if TYPE_CHECKING:
    from socialapi._base_client import BaseAsyncClient, BaseSyncClient


class Keys:
    """Manage API keys (sync)."""

    _client: BaseSyncClient

    def __init__(self, client: BaseSyncClient) -> None:
        self._client = client

    def list(self, *, timeout: float | None = None) -> list[APIKey]:
        data = self._client._get("/v1/keys", timeout=timeout)
        raw_items: list[Any] = data.get("data", [])
        items = [APIKey.model_validate(item) for item in raw_items]
        for item in items:
            item._bind(self._client)
        return items

    def create(self, *, name: str, timeout: float | None = None) -> CreateKeyResponse:
        data = self._client._post("/v1/keys", json={"name": name}, timeout=timeout)
        return CreateKeyResponse.model_validate(data)

    def revoke(self, key_id: str, *, timeout: float | None = None) -> None:
        self._client._delete(f"/v1/keys/{key_id}", timeout=timeout)


class AsyncKeys:
    """Manage API keys (async)."""

    _client: BaseAsyncClient

    def __init__(self, client: BaseAsyncClient) -> None:
        self._client = client

    async def list(self, *, timeout: float | None = None) -> list[AsyncAPIKey]:
        data = await self._client._get("/v1/keys", timeout=timeout)
        raw_items: list[Any] = data.get("data", [])
        items = [AsyncAPIKey.model_validate(item) for item in raw_items]
        for item in items:
            item._bind(self._client)
        return items

    async def create(self, *, name: str, timeout: float | None = None) -> CreateKeyResponse:
        data = await self._client._post("/v1/keys", json={"name": name}, timeout=timeout)
        return CreateKeyResponse.model_validate(data)

    async def revoke(self, key_id: str, *, timeout: float | None = None) -> None:
        await self._client._delete(f"/v1/keys/{key_id}", timeout=timeout)
