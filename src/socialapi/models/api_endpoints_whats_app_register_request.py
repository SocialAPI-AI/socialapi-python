from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiEndpointsWhatsAppRegisterRequest")


@_attrs_define
class ApiEndpointsWhatsAppRegisterRequest:
    """
    Attributes:
        pin (str | Unset): PIN is the 6-digit two-step verification PIN to set on the phone number.
            This PIN is required for future re-registration and must be stored securely. Example: 123456.
    """

    pin: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pin = self.pin

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pin is not UNSET:
            field_dict["pin"] = pin

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        pin = d.pop("pin", UNSET)

        api_endpoints_whats_app_register_request = cls(
            pin=pin,
        )

        api_endpoints_whats_app_register_request.additional_properties = d
        return api_endpoints_whats_app_register_request

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
