"""Shared response models."""

from __future__ import annotations

from typing import Generic, TypeVar

from pydantic import BaseModel

T = TypeVar("T")


class ListResponse(BaseModel, Generic[T]):
    """Generic list response with count."""

    data: list[T]
    count: int


class PaginatedResponse(BaseModel, Generic[T]):
    """Generic paginated response with optional cursor."""

    data: list[T]
    cursor: str | None = None


class SuccessResponse(BaseModel):
    """Generic success response."""

    success: bool


class OKResponse(BaseModel):
    """Generic OK response."""

    ok: bool
