from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.gbp_place_info import GBPPlaceInfo


T = TypeVar("T", bound="GBPServiceArea")


@_attrs_define
class GBPServiceArea:
    """
    Attributes:
        business_type (str | Unset): BusinessType is CUSTOMER_LOCATION_ONLY or CUSTOMER_AND_BUSINESS_LOCATION. Example:
            CUSTOMER_LOCATION_ONLY.
        places (list[GBPPlaceInfo] | Unset):
        region_code (str | Unset):  Example: FR.
    """

    business_type: str | Unset = UNSET
    places: list[GBPPlaceInfo] | Unset = UNSET
    region_code: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        business_type = self.business_type

        places: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.places, Unset):
            places = []
            for places_item_data in self.places:
                places_item = places_item_data.to_dict()
                places.append(places_item)

        region_code = self.region_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if business_type is not UNSET:
            field_dict["business_type"] = business_type
        if places is not UNSET:
            field_dict["places"] = places
        if region_code is not UNSET:
            field_dict["region_code"] = region_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.gbp_place_info import GBPPlaceInfo  # noqa: PLC0415

        d = dict(src_dict)
        business_type = d.pop("business_type", UNSET)

        _places = d.pop("places", UNSET)
        places: list[GBPPlaceInfo] | Unset = UNSET
        if _places is not UNSET:
            places = []
            for places_item_data in _places:
                places_item = GBPPlaceInfo.from_dict(places_item_data)

                places.append(places_item)

        region_code = d.pop("region_code", UNSET)

        gbp_service_area = cls(
            business_type=business_type,
            places=places,
            region_code=region_code,
        )

        gbp_service_area.additional_properties = d
        return gbp_service_area

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
