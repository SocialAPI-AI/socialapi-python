from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SocialApiAiCoreApiConnectorsBaseGBPPhoneNumbersUpdate")


@_attrs_define
class SocialApiAiCoreApiConnectorsBaseGBPPhoneNumbersUpdate:
    """
    Attributes:
        additional_phones (list[str] | Unset): AdditionalPhones replaces the whole list; an empty list clears it.
        primary_phone (str | Unset):  Example: +33 1 23 45 67 89.
    """

    additional_phones: list[str] | Unset = UNSET
    primary_phone: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        additional_phones: list[str] | Unset = UNSET
        if not isinstance(self.additional_phones, Unset):
            additional_phones = self.additional_phones

        primary_phone = self.primary_phone

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if additional_phones is not UNSET:
            field_dict["additional_phones"] = additional_phones
        if primary_phone is not UNSET:
            field_dict["primary_phone"] = primary_phone

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        additional_phones = cast(list[str], d.pop("additional_phones", UNSET))

        primary_phone = d.pop("primary_phone", UNSET)

        social_api_ai_core_api_connectors_base_gbp_phone_numbers_update = cls(
            additional_phones=additional_phones,
            primary_phone=primary_phone,
        )

        social_api_ai_core_api_connectors_base_gbp_phone_numbers_update.additional_properties = d
        return social_api_ai_core_api_connectors_base_gbp_phone_numbers_update

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
