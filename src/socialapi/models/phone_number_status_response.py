from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PhoneNumberStatusResponse")


@_attrs_define
class PhoneNumberStatusResponse:
    """
    Attributes:
        business_app (bool): True for a number that stays on the WhatsApp Business app alongside the API (coexistence).
            It is already verified and registered: request-code, verify-code and register are refused with 409
            whatsapp.business_app_number.
        registered (bool): True when the number can send and receive messages.
        verified (bool): True once the number has proven ownership, either with verify-code or in the WhatsApp Business
            app.
    """

    business_app: bool
    registered: bool
    verified: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        business_app = self.business_app

        registered = self.registered

        verified = self.verified

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "business_app": business_app,
                "registered": registered,
                "verified": verified,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        business_app = d.pop("business_app")

        registered = d.pop("registered")

        verified = d.pop("verified")

        phone_number_status_response = cls(
            business_app=business_app,
            registered=registered,
            verified=verified,
        )

        phone_number_status_response.additional_properties = d
        return phone_number_status_response

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
