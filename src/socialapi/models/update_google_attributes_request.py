from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.gbp_attribute import GBPAttribute


T = TypeVar("T", bound="UpdateGoogleAttributesRequest")


@_attrs_define
class UpdateGoogleAttributesRequest:
    """
    Attributes:
        attributes (list[GBPAttribute]): Attributes to write. Each one replaces that attribute's value; one sent
            with no value field is removed. Attributes not listed are left as they are.
    """

    attributes: list[GBPAttribute]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        attributes = []
        for attributes_item_data in self.attributes:
            attributes_item = attributes_item_data.to_dict()
            attributes.append(attributes_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "attributes": attributes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.gbp_attribute import GBPAttribute  # noqa: PLC0415

        d = dict(src_dict)
        attributes = []
        _attributes = d.pop("attributes")
        for attributes_item_data in _attributes:
            attributes_item = GBPAttribute.from_dict(attributes_item_data)

            attributes.append(attributes_item)

        update_google_attributes_request = cls(
            attributes=attributes,
        )

        update_google_attributes_request.additional_properties = d
        return update_google_attributes_request

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
