from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.gbp_attribute_value_metadata import GBPAttributeValueMetadata


T = TypeVar("T", bound="GBPAttributeMetadata")


@_attrs_define
class GBPAttributeMetadata:
    """
    Attributes:
        display_name (str):  Example: Outdoor seating.
        name (str):  Example: has_outdoor_seating.
        value_type (str):  Example: BOOL.
        deprecated (bool | Unset): Deprecated attributes still read but should no longer be written.
        group_display_name (str | Unset):  Example: Amenities.
        repeatable (bool | Unset): Repeatable is true when the attribute accepts more than one value.
        values (list[GBPAttributeValueMetadata] | Unset): Values lists the accepted values of an ENUM or REPEATED_ENUM
            attribute,
            and true/false for a BOOL one.
    """

    display_name: str
    name: str
    value_type: str
    deprecated: bool | Unset = UNSET
    group_display_name: str | Unset = UNSET
    repeatable: bool | Unset = UNSET
    values: list[GBPAttributeValueMetadata] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        display_name = self.display_name

        name = self.name

        value_type = self.value_type

        deprecated = self.deprecated

        group_display_name = self.group_display_name

        repeatable = self.repeatable

        values: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.values, Unset):
            values = []
            for values_item_data in self.values:
                values_item = values_item_data.to_dict()
                values.append(values_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "display_name": display_name,
                "name": name,
                "value_type": value_type,
            }
        )
        if deprecated is not UNSET:
            field_dict["deprecated"] = deprecated
        if group_display_name is not UNSET:
            field_dict["group_display_name"] = group_display_name
        if repeatable is not UNSET:
            field_dict["repeatable"] = repeatable
        if values is not UNSET:
            field_dict["values"] = values

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.gbp_attribute_value_metadata import GBPAttributeValueMetadata  # noqa: PLC0415

        d = dict(src_dict)
        display_name = d.pop("display_name")

        name = d.pop("name")

        value_type = d.pop("value_type")

        deprecated = d.pop("deprecated", UNSET)

        group_display_name = d.pop("group_display_name", UNSET)

        repeatable = d.pop("repeatable", UNSET)

        _values = d.pop("values", UNSET)
        values: list[GBPAttributeValueMetadata] | Unset = UNSET
        if _values is not UNSET:
            values = []
            for values_item_data in _values:
                values_item = GBPAttributeValueMetadata.from_dict(values_item_data)

                values.append(values_item)

        gbp_attribute_metadata = cls(
            display_name=display_name,
            name=name,
            value_type=value_type,
            deprecated=deprecated,
            group_display_name=group_display_name,
            repeatable=repeatable,
            values=values,
        )

        gbp_attribute_metadata.additional_properties = d
        return gbp_attribute_metadata

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
