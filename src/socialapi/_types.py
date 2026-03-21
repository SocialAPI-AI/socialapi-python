"""Common type aliases and shared type definitions."""

from __future__ import annotations

from typing import Any, TypeAlias

# Generic JSON-compatible types.
JSONValue: TypeAlias = "str | int | float | bool | None | dict[str, Any] | list[Any]"
JSONDict: TypeAlias = dict[str, Any]
Headers: TypeAlias = dict[str, str]

# Query parameter types.
QueryParams: TypeAlias = dict[str, str | int | None]
