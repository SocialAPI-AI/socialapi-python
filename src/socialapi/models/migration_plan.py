from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="MigrationPlan")


@_attrs_define
class MigrationPlan:
    """
    Attributes:
        brands_limit (int):
        name (str):
        pages_per_brand (int):
        tier (str):  Example: starter.
    """

    brands_limit: int
    name: str
    pages_per_brand: int
    tier: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        brands_limit = self.brands_limit

        name = self.name

        pages_per_brand = self.pages_per_brand

        tier = self.tier

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "brands_limit": brands_limit,
                "name": name,
                "pages_per_brand": pages_per_brand,
                "tier": tier,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        brands_limit = d.pop("brands_limit")

        name = d.pop("name")

        pages_per_brand = d.pop("pages_per_brand")

        tier = d.pop("tier")

        migration_plan = cls(
            brands_limit=brands_limit,
            name=name,
            pages_per_brand=pages_per_brand,
            tier=tier,
        )

        migration_plan.additional_properties = d
        return migration_plan

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
