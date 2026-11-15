from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiEndpointsWhatsAppMessageRef")


@_attrs_define
class ApiEndpointsWhatsAppMessageRef:
    """
    Attributes:
        id (str | Unset):  Example: wamid.HBgLMTU1NTEyMzQ1NjcVAgARGBI....
        message_status (str | Unset):  Example: accepted.
    """

    id: str | Unset = UNSET
    message_status: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        message_status = self.message_status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if message_status is not UNSET:
            field_dict["message_status"] = message_status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        message_status = d.pop("message_status", UNSET)

        api_endpoints_whats_app_message_ref = cls(
            id=id,
            message_status=message_status,
        )

        api_endpoints_whats_app_message_ref.additional_properties = d
        return api_endpoints_whats_app_message_ref

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
