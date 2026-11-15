from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="LostPageAccess")


@_attrs_define
class LostPageAccess:
    """
    Attributes:
        brand_id (str):
        brand_name (str):
        name (str):
        platform_page_id (str):
    """

    brand_id: str
    brand_name: str
    name: str
    platform_page_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        brand_id = self.brand_id

        brand_name = self.brand_name

        name = self.name

        platform_page_id = self.platform_page_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "brand_id": brand_id,
                "brand_name": brand_name,
                "name": name,
                "platform_page_id": platform_page_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        brand_id = d.pop("brand_id")

        brand_name = d.pop("brand_name")

        name = d.pop("name")

        platform_page_id = d.pop("platform_page_id")

        lost_page_access = cls(
            brand_id=brand_id,
            brand_name=brand_name,
            name=name,
            platform_page_id=platform_page_id,
        )

        lost_page_access.additional_properties = d
        return lost_page_access

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
