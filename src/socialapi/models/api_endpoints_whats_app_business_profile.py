from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.api_endpoints_whats_app_business_profile_vertical import ApiEndpointsWhatsAppBusinessProfileVertical
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiEndpointsWhatsAppBusinessProfile")


@_attrs_define
class ApiEndpointsWhatsAppBusinessProfile:
    """
    Attributes:
        about (str | Unset): About is the profile tagline shown in the chat header. Example: Reach us 9-5 weekdays..
        address (str | Unset): Address is the business address (max 256 characters). Example: 1 Hacker Way, Menlo Park,
            CA.
        description (str | Unset): Description is the business description. Example: Acme Corp customer support..
        email (str | Unset): Email is the contact email. Example: support@acme.com.
        messaging_product (str | Unset): MessagingProduct is always "whatsapp". Example: whatsapp.
        profile_picture_url (str | Unset): ProfilePictureURL is the public URL of the current profile picture (read-
            only; use profile_picture_handle to update). Example: https://cdn.example.com/logo.png.
        vertical (ApiEndpointsWhatsAppBusinessProfileVertical | Unset): Vertical is the business category. Example:
            RETAIL.
        websites (list[str] | Unset): Websites lists the business websites (max 2). Example: ['https://acme.com'].
    """

    about: str | Unset = UNSET
    address: str | Unset = UNSET
    description: str | Unset = UNSET
    email: str | Unset = UNSET
    messaging_product: str | Unset = UNSET
    profile_picture_url: str | Unset = UNSET
    vertical: ApiEndpointsWhatsAppBusinessProfileVertical | Unset = UNSET
    websites: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        about = self.about

        address = self.address

        description = self.description

        email = self.email

        messaging_product = self.messaging_product

        profile_picture_url = self.profile_picture_url

        vertical: str | Unset = UNSET
        if not isinstance(self.vertical, Unset):
            vertical = self.vertical.value

        websites: list[str] | Unset = UNSET
        if not isinstance(self.websites, Unset):
            websites = self.websites

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if about is not UNSET:
            field_dict["about"] = about
        if address is not UNSET:
            field_dict["address"] = address
        if description is not UNSET:
            field_dict["description"] = description
        if email is not UNSET:
            field_dict["email"] = email
        if messaging_product is not UNSET:
            field_dict["messaging_product"] = messaging_product
        if profile_picture_url is not UNSET:
            field_dict["profile_picture_url"] = profile_picture_url
        if vertical is not UNSET:
            field_dict["vertical"] = vertical
        if websites is not UNSET:
            field_dict["websites"] = websites

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        about = d.pop("about", UNSET)

        address = d.pop("address", UNSET)

        description = d.pop("description", UNSET)

        email = d.pop("email", UNSET)

        messaging_product = d.pop("messaging_product", UNSET)

        profile_picture_url = d.pop("profile_picture_url", UNSET)

        _vertical = d.pop("vertical", UNSET)
        vertical: ApiEndpointsWhatsAppBusinessProfileVertical | Unset
        if isinstance(_vertical, Unset):
            vertical = UNSET
        else:
            vertical = ApiEndpointsWhatsAppBusinessProfileVertical(_vertical)

        websites = cast(list[str], d.pop("websites", UNSET))

        api_endpoints_whats_app_business_profile = cls(
            about=about,
            address=address,
            description=description,
            email=email,
            messaging_product=messaging_product,
            profile_picture_url=profile_picture_url,
            vertical=vertical,
            websites=websites,
        )

        api_endpoints_whats_app_business_profile.additional_properties = d
        return api_endpoints_whats_app_business_profile

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
