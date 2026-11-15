from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.social_api_ai_core_api_connectors_base_gbp_repeated_enum_value import (
        SocialApiAiCoreApiConnectorsBaseGBPRepeatedEnumValue,
    )


T = TypeVar("T", bound="SocialApiAiCoreApiConnectorsBaseGBPAttribute")


@_attrs_define
class SocialApiAiCoreApiConnectorsBaseGBPAttribute:
    """
    Attributes:
        bool_value (bool | Unset): BoolValue is set for a BOOL attribute. False is a real answer. Example: True.
        enum_value (str | Unset): EnumValue is set for an ENUM attribute.
        name (str | Unset): Name is the attribute id, as listed by the available-attributes endpoint. Example:
            has_outdoor_seating.
        repeated_enum_value (SocialApiAiCoreApiConnectorsBaseGBPRepeatedEnumValue | Unset):
        uri_values (list[str] | Unset): URIValues is set for a URL attribute.
        value_type (str | Unset): ValueType is BOOL, ENUM, URL or REPEATED_ENUM. It is ignored on write. Example: BOOL.
    """

    bool_value: bool | Unset = UNSET
    enum_value: str | Unset = UNSET
    name: str | Unset = UNSET
    repeated_enum_value: SocialApiAiCoreApiConnectorsBaseGBPRepeatedEnumValue | Unset = UNSET
    uri_values: list[str] | Unset = UNSET
    value_type: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bool_value = self.bool_value

        enum_value = self.enum_value

        name = self.name

        repeated_enum_value: dict[str, Any] | Unset = UNSET
        if not isinstance(self.repeated_enum_value, Unset):
            repeated_enum_value = self.repeated_enum_value.to_dict()

        uri_values: list[str] | Unset = UNSET
        if not isinstance(self.uri_values, Unset):
            uri_values = self.uri_values

        value_type = self.value_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bool_value is not UNSET:
            field_dict["bool_value"] = bool_value
        if enum_value is not UNSET:
            field_dict["enum_value"] = enum_value
        if name is not UNSET:
            field_dict["name"] = name
        if repeated_enum_value is not UNSET:
            field_dict["repeated_enum_value"] = repeated_enum_value
        if uri_values is not UNSET:
            field_dict["uri_values"] = uri_values
        if value_type is not UNSET:
            field_dict["value_type"] = value_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.social_api_ai_core_api_connectors_base_gbp_repeated_enum_value import (
            SocialApiAiCoreApiConnectorsBaseGBPRepeatedEnumValue,  # noqa: PLC0415
        )

        d = dict(src_dict)
        bool_value = d.pop("bool_value", UNSET)

        enum_value = d.pop("enum_value", UNSET)

        name = d.pop("name", UNSET)

        _repeated_enum_value = d.pop("repeated_enum_value", UNSET)
        repeated_enum_value: SocialApiAiCoreApiConnectorsBaseGBPRepeatedEnumValue | Unset
        if isinstance(_repeated_enum_value, Unset):
            repeated_enum_value = UNSET
        else:
            repeated_enum_value = SocialApiAiCoreApiConnectorsBaseGBPRepeatedEnumValue.from_dict(_repeated_enum_value)

        uri_values = cast(list[str], d.pop("uri_values", UNSET))

        value_type = d.pop("value_type", UNSET)

        social_api_ai_core_api_connectors_base_gbp_attribute = cls(
            bool_value=bool_value,
            enum_value=enum_value,
            name=name,
            repeated_enum_value=repeated_enum_value,
            uri_values=uri_values,
            value_type=value_type,
        )

        social_api_ai_core_api_connectors_base_gbp_attribute.additional_properties = d
        return social_api_ai_core_api_connectors_base_gbp_attribute

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
