from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SocialApiAiCoreApiConnectorsBaseGBPAddressUpdate")


@_attrs_define
class SocialApiAiCoreApiConnectorsBaseGBPAddressUpdate:
    """
    Attributes:
        address_lines (list[str] | Unset):
        administrative_area (str | Unset):
        locality (str | Unset):  Example: Paris.
        organization (str | Unset):
        postal_code (str | Unset):  Example: 75001.
        region_code (str | Unset):  Example: FR.
        sorting_code (str | Unset):
        sublocality (str | Unset):
    """

    address_lines: list[str] | Unset = UNSET
    administrative_area: str | Unset = UNSET
    locality: str | Unset = UNSET
    organization: str | Unset = UNSET
    postal_code: str | Unset = UNSET
    region_code: str | Unset = UNSET
    sorting_code: str | Unset = UNSET
    sublocality: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        address_lines: list[str] | Unset = UNSET
        if not isinstance(self.address_lines, Unset):
            address_lines = self.address_lines

        administrative_area = self.administrative_area

        locality = self.locality

        organization = self.organization

        postal_code = self.postal_code

        region_code = self.region_code

        sorting_code = self.sorting_code

        sublocality = self.sublocality

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address_lines is not UNSET:
            field_dict["address_lines"] = address_lines
        if administrative_area is not UNSET:
            field_dict["administrative_area"] = administrative_area
        if locality is not UNSET:
            field_dict["locality"] = locality
        if organization is not UNSET:
            field_dict["organization"] = organization
        if postal_code is not UNSET:
            field_dict["postal_code"] = postal_code
        if region_code is not UNSET:
            field_dict["region_code"] = region_code
        if sorting_code is not UNSET:
            field_dict["sorting_code"] = sorting_code
        if sublocality is not UNSET:
            field_dict["sublocality"] = sublocality

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        address_lines = cast(list[str], d.pop("address_lines", UNSET))

        administrative_area = d.pop("administrative_area", UNSET)

        locality = d.pop("locality", UNSET)

        organization = d.pop("organization", UNSET)

        postal_code = d.pop("postal_code", UNSET)

        region_code = d.pop("region_code", UNSET)

        sorting_code = d.pop("sorting_code", UNSET)

        sublocality = d.pop("sublocality", UNSET)

        social_api_ai_core_api_connectors_base_gbp_address_update = cls(
            address_lines=address_lines,
            administrative_area=administrative_area,
            locality=locality,
            organization=organization,
            postal_code=postal_code,
            region_code=region_code,
            sorting_code=sorting_code,
            sublocality=sublocality,
        )

        social_api_ai_core_api_connectors_base_gbp_address_update.additional_properties = d
        return social_api_ai_core_api_connectors_base_gbp_address_update

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
