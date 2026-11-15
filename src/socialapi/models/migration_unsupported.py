from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="MigrationUnsupported")


@_attrs_define
class MigrationUnsupported:
    """
    Attributes:
        count (int):
        platform (str): Platform name as your provider reports it.
        reason (str): Why the accounts stay: "unserved platform", "ads", "telephony", "commerce", "unknown platform" or
            "linked to another account".
    """

    count: int
    platform: str
    reason: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        count = self.count

        platform = self.platform

        reason = self.reason

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "count": count,
                "platform": platform,
                "reason": reason,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        count = d.pop("count")

        platform = d.pop("platform")

        reason = d.pop("reason")

        migration_unsupported = cls(
            count=count,
            platform=platform,
            reason=reason,
        )

        migration_unsupported.additional_properties = d
        return migration_unsupported

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
