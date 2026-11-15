from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SocialApiAiCoreApiConnectorsBaseGBPAttributeValueMetadata")


@_attrs_define
class SocialApiAiCoreApiConnectorsBaseGBPAttributeValueMetadata:
    """
    Attributes:
        bool_value (bool | Unset):
        display_name (str | Unset):  Example: Yes.
        enum_value (str | Unset):
    """

    bool_value: bool | Unset = UNSET
    display_name: str | Unset = UNSET
    enum_value: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bool_value = self.bool_value

        display_name = self.display_name

        enum_value = self.enum_value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bool_value is not UNSET:
            field_dict["bool_value"] = bool_value
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if enum_value is not UNSET:
            field_dict["enum_value"] = enum_value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bool_value = d.pop("bool_value", UNSET)

        display_name = d.pop("display_name", UNSET)

        enum_value = d.pop("enum_value", UNSET)

        social_api_ai_core_api_connectors_base_gbp_attribute_value_metadata = cls(
            bool_value=bool_value,
            display_name=display_name,
            enum_value=enum_value,
        )

        social_api_ai_core_api_connectors_base_gbp_attribute_value_metadata.additional_properties = d
        return social_api_ai_core_api_connectors_base_gbp_attribute_value_metadata

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
