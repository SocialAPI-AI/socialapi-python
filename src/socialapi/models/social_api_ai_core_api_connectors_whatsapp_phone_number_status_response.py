from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SocialApiAiCoreApiConnectorsWhatsappPhoneNumberStatusResponse")


@_attrs_define
class SocialApiAiCoreApiConnectorsWhatsappPhoneNumberStatusResponse:
    """
    Attributes:
        business_app (bool | Unset): True for a number that stays on the WhatsApp Business app alongside the API
            (coexistence). It is already verified and registered: request-code, verify-code and register are refused with
            409 whatsapp.business_app_number.
        registered (bool | Unset): True when the number can send and receive messages.
        verified (bool | Unset): True once the number has proven ownership, either with verify-code or in the WhatsApp
            Business app.
    """

    business_app: bool | Unset = UNSET
    registered: bool | Unset = UNSET
    verified: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        business_app = self.business_app

        registered = self.registered

        verified = self.verified

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if business_app is not UNSET:
            field_dict["business_app"] = business_app
        if registered is not UNSET:
            field_dict["registered"] = registered
        if verified is not UNSET:
            field_dict["verified"] = verified

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        business_app = d.pop("business_app", UNSET)

        registered = d.pop("registered", UNSET)

        verified = d.pop("verified", UNSET)

        social_api_ai_core_api_connectors_whatsapp_phone_number_status_response = cls(
            business_app=business_app,
            registered=registered,
            verified=verified,
        )

        social_api_ai_core_api_connectors_whatsapp_phone_number_status_response.additional_properties = d
        return social_api_ai_core_api_connectors_whatsapp_phone_number_status_response

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
