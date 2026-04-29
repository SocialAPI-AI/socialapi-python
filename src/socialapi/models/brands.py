from __future__ import annotations

from datetime import datetime  # noqa: TC003

from pydantic import BaseModel, ConfigDict

from socialapi._bound import _Bound


class _BrandBase(_Bound):
    """Shared fields for Brand / AsyncBrand."""

    id: str
    name: str
    accounts_count: int = 0
    created_at: datetime
    updated_at: datetime


class Brand(_BrandBase):
    """A brand that groups connected social accounts (sync)."""

    def update(self, *, name: str, timeout: float | None = None) -> Brand:
        client = self._client_or_raise_sync()
        data = client._patch(f"/v1/brands/{self.id}", json={"name": name}, timeout=timeout)
        if isinstance(data, dict):
            updated = Brand.model_validate(data)
            updated._bind(client)
            return updated
        return self

    def delete(self, *, timeout: float | None = None) -> None:
        client = self._client_or_raise_sync()
        client._delete(f"/v1/brands/{self.id}", timeout=timeout)


class AsyncBrand(_BrandBase):
    """A brand that groups connected social accounts (async)."""

    async def update(self, *, name: str, timeout: float | None = None) -> AsyncBrand:
        client = self._client_or_raise_async()
        data = await client._patch(f"/v1/brands/{self.id}", json={"name": name}, timeout=timeout)
        if isinstance(data, dict):
            updated = AsyncBrand.model_validate(data)
            updated._bind(client)
            return updated
        return self

    async def delete(self, *, timeout: float | None = None) -> None:
        client = self._client_or_raise_async()
        await client._delete(f"/v1/brands/{self.id}", timeout=timeout)


class CreateBrandRequest(BaseModel):
    """Request body for ``POST /v1/brands``."""

    model_config = ConfigDict(populate_by_name=True)

    name: str


class UpdateBrandRequest(BaseModel):
    """Request body for ``PATCH /v1/brands/:id``."""

    model_config = ConfigDict(populate_by_name=True)

    name: str
