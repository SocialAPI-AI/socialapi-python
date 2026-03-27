from __future__ import annotations

from datetime import datetime  # noqa: TC003

from pydantic import BaseModel, ConfigDict


class Brand(BaseModel):
    """A brand that groups connected social accounts."""

    model_config = ConfigDict(populate_by_name=True)

    id: str
    name: str
    accounts_count: int = 0
    created_at: datetime
    updated_at: datetime


class CreateBrandRequest(BaseModel):
    """Request body for ``POST /v1/brands``."""

    model_config = ConfigDict(populate_by_name=True)

    name: str


class UpdateBrandRequest(BaseModel):
    """Request body for ``PATCH /v1/brands/:id``."""

    model_config = ConfigDict(populate_by_name=True)

    name: str
