from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="StorageUsageResponse")


@_attrs_define
class StorageUsageResponse:
    """
    Attributes:
        count (int):  Example: 12.
        limit_bytes (int):  Example: 104857600.
        used_bytes (int):  Example: 52428800.
    """

    count: int
    limit_bytes: int
    used_bytes: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        count = self.count

        limit_bytes = self.limit_bytes

        used_bytes = self.used_bytes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "count": count,
                "limit_bytes": limit_bytes,
                "used_bytes": used_bytes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        count = d.pop("count")

        limit_bytes = d.pop("limit_bytes")

        used_bytes = d.pop("used_bytes")

        storage_usage_response = cls(
            count=count,
            limit_bytes=limit_bytes,
            used_bytes=used_bytes,
        )

        storage_usage_response.additional_properties = d
        return storage_usage_response

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
