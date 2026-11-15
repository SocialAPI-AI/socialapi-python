from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SocialApiAiCoreApiConnectorsBaseGBPPlaceActionLink")


@_attrs_define
class SocialApiAiCoreApiConnectorsBaseGBPPlaceActionLink:
    """
    Attributes:
        create_time (str | Unset):  Example: 2026-11-09T10:00:00Z.
        id (str | Unset):  Example: 7341992850181928347.
        is_editable (bool | Unset): IsEditable is false for a link added by a third-party provider, which
            cannot be changed or deleted here.
        is_preferred (bool | Unset): IsPreferred marks the link Google shows first for its action type.
        place_action_type (str | Unset):  Example: DINING_RESERVATION.
        provider_type (str | Unset): ProviderType is MERCHANT or AGGREGATOR_3P. Example: MERCHANT.
        update_time (str | Unset):  Example: 2026-11-09T10:00:00Z.
        uri (str | Unset):  Example: https://book.example/joes.
    """

    create_time: str | Unset = UNSET
    id: str | Unset = UNSET
    is_editable: bool | Unset = UNSET
    is_preferred: bool | Unset = UNSET
    place_action_type: str | Unset = UNSET
    provider_type: str | Unset = UNSET
    update_time: str | Unset = UNSET
    uri: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        create_time = self.create_time

        id = self.id

        is_editable = self.is_editable

        is_preferred = self.is_preferred

        place_action_type = self.place_action_type

        provider_type = self.provider_type

        update_time = self.update_time

        uri = self.uri

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if create_time is not UNSET:
            field_dict["create_time"] = create_time
        if id is not UNSET:
            field_dict["id"] = id
        if is_editable is not UNSET:
            field_dict["is_editable"] = is_editable
        if is_preferred is not UNSET:
            field_dict["is_preferred"] = is_preferred
        if place_action_type is not UNSET:
            field_dict["place_action_type"] = place_action_type
        if provider_type is not UNSET:
            field_dict["provider_type"] = provider_type
        if update_time is not UNSET:
            field_dict["update_time"] = update_time
        if uri is not UNSET:
            field_dict["uri"] = uri

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        create_time = d.pop("create_time", UNSET)

        id = d.pop("id", UNSET)

        is_editable = d.pop("is_editable", UNSET)

        is_preferred = d.pop("is_preferred", UNSET)

        place_action_type = d.pop("place_action_type", UNSET)

        provider_type = d.pop("provider_type", UNSET)

        update_time = d.pop("update_time", UNSET)

        uri = d.pop("uri", UNSET)

        social_api_ai_core_api_connectors_base_gbp_place_action_link = cls(
            create_time=create_time,
            id=id,
            is_editable=is_editable,
            is_preferred=is_preferred,
            place_action_type=place_action_type,
            provider_type=provider_type,
            update_time=update_time,
            uri=uri,
        )

        social_api_ai_core_api_connectors_base_gbp_place_action_link.additional_properties = d
        return social_api_ai_core_api_connectors_base_gbp_place_action_link

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
