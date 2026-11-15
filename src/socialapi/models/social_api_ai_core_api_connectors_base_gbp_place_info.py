from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SocialApiAiCoreApiConnectorsBaseGBPPlaceInfo")


@_attrs_define
class SocialApiAiCoreApiConnectorsBaseGBPPlaceInfo:
    """
    Attributes:
        place_id (str | Unset):
        place_name (str | Unset):  Example: Paris.
    """

    place_id: str | Unset = UNSET
    place_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        place_id = self.place_id

        place_name = self.place_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if place_id is not UNSET:
            field_dict["place_id"] = place_id
        if place_name is not UNSET:
            field_dict["place_name"] = place_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        place_id = d.pop("place_id", UNSET)

        place_name = d.pop("place_name", UNSET)

        social_api_ai_core_api_connectors_base_gbp_place_info = cls(
            place_id=place_id,
            place_name=place_name,
        )

        social_api_ai_core_api_connectors_base_gbp_place_info.additional_properties = d
        return social_api_ai_core_api_connectors_base_gbp_place_info

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
