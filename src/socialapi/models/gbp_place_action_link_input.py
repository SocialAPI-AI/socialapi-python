from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GBPPlaceActionLinkInput")


@_attrs_define
class GBPPlaceActionLinkInput:
    """
    Attributes:
        is_preferred (bool | Unset):
        place_action_type (str | Unset):  Example: DINING_RESERVATION.
        uri (str | Unset):  Example: https://book.example/joes.
    """

    is_preferred: bool | Unset = UNSET
    place_action_type: str | Unset = UNSET
    uri: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_preferred = self.is_preferred

        place_action_type = self.place_action_type

        uri = self.uri

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_preferred is not UNSET:
            field_dict["is_preferred"] = is_preferred
        if place_action_type is not UNSET:
            field_dict["place_action_type"] = place_action_type
        if uri is not UNSET:
            field_dict["uri"] = uri

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_preferred = d.pop("is_preferred", UNSET)

        place_action_type = d.pop("place_action_type", UNSET)

        uri = d.pop("uri", UNSET)

        gbp_place_action_link_input = cls(
            is_preferred=is_preferred,
            place_action_type=place_action_type,
            uri=uri,
        )

        gbp_place_action_link_input.additional_properties = d
        return gbp_place_action_link_input

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
