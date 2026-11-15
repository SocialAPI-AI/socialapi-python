from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SocialApiAiCoreApiConnectorsBaseGBPRepeatedEnumValue")


@_attrs_define
class SocialApiAiCoreApiConnectorsBaseGBPRepeatedEnumValue:
    """
    Attributes:
        set_values (list[str] | Unset):
        unset_values (list[str] | Unset):
    """

    set_values: list[str] | Unset = UNSET
    unset_values: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        set_values: list[str] | Unset = UNSET
        if not isinstance(self.set_values, Unset):
            set_values = self.set_values

        unset_values: list[str] | Unset = UNSET
        if not isinstance(self.unset_values, Unset):
            unset_values = self.unset_values

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if set_values is not UNSET:
            field_dict["set_values"] = set_values
        if unset_values is not UNSET:
            field_dict["unset_values"] = unset_values

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        set_values = cast(list[str], d.pop("set_values", UNSET))

        unset_values = cast(list[str], d.pop("unset_values", UNSET))

        social_api_ai_core_api_connectors_base_gbp_repeated_enum_value = cls(
            set_values=set_values,
            unset_values=unset_values,
        )

        social_api_ai_core_api_connectors_base_gbp_repeated_enum_value.additional_properties = d
        return social_api_ai_core_api_connectors_base_gbp_repeated_enum_value

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
