from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="StaggerRequest")


@_attrs_define
class StaggerRequest:
    """
    Attributes:
        max_seconds (int | Unset): MaxSeconds is the longest delay between two consecutive targets. Must be at least
            min_seconds and at most 86400 (24 hours). Example: 300.
        min_seconds (int | Unset): MinSeconds is the shortest delay between two consecutive targets. Must be 0 or more.
            Example: 60.
    """

    max_seconds: int | Unset = UNSET
    min_seconds: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        max_seconds = self.max_seconds

        min_seconds = self.min_seconds

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if max_seconds is not UNSET:
            field_dict["max_seconds"] = max_seconds
        if min_seconds is not UNSET:
            field_dict["min_seconds"] = min_seconds

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        max_seconds = d.pop("max_seconds", UNSET)

        min_seconds = d.pop("min_seconds", UNSET)

        stagger_request = cls(
            max_seconds=max_seconds,
            min_seconds=min_seconds,
        )

        stagger_request.additional_properties = d
        return stagger_request

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
