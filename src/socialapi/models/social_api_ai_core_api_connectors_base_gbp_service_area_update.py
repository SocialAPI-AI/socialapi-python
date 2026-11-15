from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SocialApiAiCoreApiConnectorsBaseGBPServiceAreaUpdate")


@_attrs_define
class SocialApiAiCoreApiConnectorsBaseGBPServiceAreaUpdate:
    """
    Attributes:
        business_type (str | Unset): BusinessType is CUSTOMER_LOCATION_ONLY or CUSTOMER_AND_BUSINESS_LOCATION. Example:
            CUSTOMER_LOCATION_ONLY.
        place_ids (list[str] | Unset): PlaceIDs replaces the covered areas, as Google place ids.
    """

    business_type: str | Unset = UNSET
    place_ids: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        business_type = self.business_type

        place_ids: list[str] | Unset = UNSET
        if not isinstance(self.place_ids, Unset):
            place_ids = self.place_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if business_type is not UNSET:
            field_dict["business_type"] = business_type
        if place_ids is not UNSET:
            field_dict["place_ids"] = place_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        business_type = d.pop("business_type", UNSET)

        place_ids = cast(list[str], d.pop("place_ids", UNSET))

        social_api_ai_core_api_connectors_base_gbp_service_area_update = cls(
            business_type=business_type,
            place_ids=place_ids,
        )

        social_api_ai_core_api_connectors_base_gbp_service_area_update.additional_properties = d
        return social_api_ai_core_api_connectors_base_gbp_service_area_update

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
