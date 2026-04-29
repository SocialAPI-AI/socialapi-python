from __future__ import annotations

from typing import TYPE_CHECKING, Any

from socialapi.models.brands import AsyncBrand, Brand

if TYPE_CHECKING:
    from socialapi._base_client import BaseAsyncClient, BaseSyncClient


class Brands:
    """Manage brands (sync)."""

    _client: BaseSyncClient

    def __init__(self, client: BaseSyncClient) -> None:
        self._client = client

    def list(self, *, timeout: float | None = None) -> list[Brand]:
        data = self._client._get("/v1/brands", timeout=timeout)
        raw_items: list[Any] = data.get("data", [])
        items = [Brand.model_validate(item) for item in raw_items]
        for item in items:
            item._bind(self._client)
        return items

    def create(self, *, name: str, timeout: float | None = None) -> Brand:
        data = self._client._post("/v1/brands", json={"name": name}, timeout=timeout)
        brand = Brand.model_validate(data)
        brand._bind(self._client)
        return brand

    def update(self, brand_id: str, *, name: str, timeout: float | None = None) -> Brand:
        data = self._client._patch(f"/v1/brands/{brand_id}", json={"name": name}, timeout=timeout)
        brand = Brand.model_validate(data)
        brand._bind(self._client)
        return brand

    def delete(self, brand_id: str, *, timeout: float | None = None) -> None:
        self._client._delete(f"/v1/brands/{brand_id}", timeout=timeout)


class AsyncBrands:
    """Manage brands (async)."""

    _client: BaseAsyncClient

    def __init__(self, client: BaseAsyncClient) -> None:
        self._client = client

    async def list(self, *, timeout: float | None = None) -> list[AsyncBrand]:
        data = await self._client._get("/v1/brands", timeout=timeout)
        raw_items: list[Any] = data.get("data", [])
        items = [AsyncBrand.model_validate(item) for item in raw_items]
        for item in items:
            item._bind(self._client)
        return items

    async def create(self, *, name: str, timeout: float | None = None) -> AsyncBrand:
        data = await self._client._post("/v1/brands", json={"name": name}, timeout=timeout)
        brand = AsyncBrand.model_validate(data)
        brand._bind(self._client)
        return brand

    async def update(self, brand_id: str, *, name: str, timeout: float | None = None) -> AsyncBrand:
        data = await self._client._patch(f"/v1/brands/{brand_id}", json={"name": name}, timeout=timeout)
        brand = AsyncBrand.model_validate(data)
        brand._bind(self._client)
        return brand

    async def delete(self, brand_id: str, *, timeout: float | None = None) -> None:
        await self._client._delete(f"/v1/brands/{brand_id}", timeout=timeout)
