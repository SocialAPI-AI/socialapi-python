from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.social_api_ai_core_api_connectors_base_gbp_attribute import (
        SocialApiAiCoreApiConnectorsBaseGBPAttribute,
    )


T = TypeVar("T", bound="ApiEndpointsUpdateGoogleAttributesRequest")


@_attrs_define
class ApiEndpointsUpdateGoogleAttributesRequest:
    """
    Attributes:
        attributes (list[SocialApiAiCoreApiConnectorsBaseGBPAttribute] | Unset): Attributes to write. Each one replaces
            that attribute's value; one sent
            with no value field is removed. Attributes not listed are left as they are.
    """

    attributes: list[SocialApiAiCoreApiConnectorsBaseGBPAttribute] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        attributes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = []
            for attributes_item_data in self.attributes:
                attributes_item = attributes_item_data.to_dict()
                attributes.append(attributes_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if attributes is not UNSET:
            field_dict["attributes"] = attributes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.social_api_ai_core_api_connectors_base_gbp_attribute import (
            SocialApiAiCoreApiConnectorsBaseGBPAttribute,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _attributes = d.pop("attributes", UNSET)
        attributes: list[SocialApiAiCoreApiConnectorsBaseGBPAttribute] | Unset = UNSET
        if _attributes is not UNSET:
            attributes = []
            for attributes_item_data in _attributes:
                attributes_item = SocialApiAiCoreApiConnectorsBaseGBPAttribute.from_dict(attributes_item_data)

                attributes.append(attributes_item)

        api_endpoints_update_google_attributes_request = cls(
            attributes=attributes,
        )

        api_endpoints_update_google_attributes_request.additional_properties = d
        return api_endpoints_update_google_attributes_request

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
