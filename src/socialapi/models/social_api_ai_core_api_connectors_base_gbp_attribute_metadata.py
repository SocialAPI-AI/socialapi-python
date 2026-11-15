from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.social_api_ai_core_api_connectors_base_gbp_attribute_value_metadata import (
        SocialApiAiCoreApiConnectorsBaseGBPAttributeValueMetadata,
    )


T = TypeVar("T", bound="SocialApiAiCoreApiConnectorsBaseGBPAttributeMetadata")


@_attrs_define
class SocialApiAiCoreApiConnectorsBaseGBPAttributeMetadata:
    """
    Attributes:
        deprecated (bool | Unset): Deprecated attributes still read but should no longer be written.
        display_name (str | Unset):  Example: Outdoor seating.
        group_display_name (str | Unset):  Example: Amenities.
        name (str | Unset):  Example: has_outdoor_seating.
        repeatable (bool | Unset): Repeatable is true when the attribute accepts more than one value.
        value_type (str | Unset):  Example: BOOL.
        values (list[SocialApiAiCoreApiConnectorsBaseGBPAttributeValueMetadata] | Unset): Values lists the accepted
            values of an ENUM or REPEATED_ENUM attribute,
            and true/false for a BOOL one.
    """

    deprecated: bool | Unset = UNSET
    display_name: str | Unset = UNSET
    group_display_name: str | Unset = UNSET
    name: str | Unset = UNSET
    repeatable: bool | Unset = UNSET
    value_type: str | Unset = UNSET
    values: list[SocialApiAiCoreApiConnectorsBaseGBPAttributeValueMetadata] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        deprecated = self.deprecated

        display_name = self.display_name

        group_display_name = self.group_display_name

        name = self.name

        repeatable = self.repeatable

        value_type = self.value_type

        values: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.values, Unset):
            values = []
            for values_item_data in self.values:
                values_item = values_item_data.to_dict()
                values.append(values_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if deprecated is not UNSET:
            field_dict["deprecated"] = deprecated
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if group_display_name is not UNSET:
            field_dict["group_display_name"] = group_display_name
        if name is not UNSET:
            field_dict["name"] = name
        if repeatable is not UNSET:
            field_dict["repeatable"] = repeatable
        if value_type is not UNSET:
            field_dict["value_type"] = value_type
        if values is not UNSET:
            field_dict["values"] = values

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.social_api_ai_core_api_connectors_base_gbp_attribute_value_metadata import (
            SocialApiAiCoreApiConnectorsBaseGBPAttributeValueMetadata,  # noqa: PLC0415
        )

        d = dict(src_dict)
        deprecated = d.pop("deprecated", UNSET)

        display_name = d.pop("display_name", UNSET)

        group_display_name = d.pop("group_display_name", UNSET)

        name = d.pop("name", UNSET)

        repeatable = d.pop("repeatable", UNSET)

        value_type = d.pop("value_type", UNSET)

        _values = d.pop("values", UNSET)
        values: list[SocialApiAiCoreApiConnectorsBaseGBPAttributeValueMetadata] | Unset = UNSET
        if _values is not UNSET:
            values = []
            for values_item_data in _values:
                values_item = SocialApiAiCoreApiConnectorsBaseGBPAttributeValueMetadata.from_dict(values_item_data)

                values.append(values_item)

        social_api_ai_core_api_connectors_base_gbp_attribute_metadata = cls(
            deprecated=deprecated,
            display_name=display_name,
            group_display_name=group_display_name,
            name=name,
            repeatable=repeatable,
            value_type=value_type,
            values=values,
        )

        social_api_ai_core_api_connectors_base_gbp_attribute_metadata.additional_properties = d
        return social_api_ai_core_api_connectors_base_gbp_attribute_metadata

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
