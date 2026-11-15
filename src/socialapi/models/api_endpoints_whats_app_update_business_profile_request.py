from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.api_endpoints_whats_app_update_business_profile_request_vertical import (
    ApiEndpointsWhatsAppUpdateBusinessProfileRequestVertical,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiEndpointsWhatsAppUpdateBusinessProfileRequest")


@_attrs_define
class ApiEndpointsWhatsAppUpdateBusinessProfileRequest:
    """
    Attributes:
        about (str | Unset): About is the profile tagline (max 139 characters). Example: Reach us 9-5 weekdays..
        address (str | Unset): Address is the business address (max 256 characters). Example: 1 Hacker Way, Menlo Park,
            CA.
        description (str | Unset): Description is the business description. Example: Acme Corp customer support..
        email (str | Unset): Email is the contact email. Example: support@acme.com.
        profile_picture_handle (str | Unset): ProfilePictureHandle is a handle returned by the Resumable Upload API.
            Use this to change the profile picture; the picture URL is read-only. Example: 4::aW1hZ2UvanBlZw==.
        vertical (ApiEndpointsWhatsAppUpdateBusinessProfileRequestVertical | Unset): Vertical is the business category.
            Example: RETAIL.
        websites (list[str] | Unset): Websites lists the business websites (max 2). Example: ['https://acme.com'].
    """

    about: str | Unset = UNSET
    address: str | Unset = UNSET
    description: str | Unset = UNSET
    email: str | Unset = UNSET
    profile_picture_handle: str | Unset = UNSET
    vertical: ApiEndpointsWhatsAppUpdateBusinessProfileRequestVertical | Unset = UNSET
    websites: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        about = self.about

        address = self.address

        description = self.description

        email = self.email

        profile_picture_handle = self.profile_picture_handle

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
        if profile_picture_handle is not UNSET:
            field_dict["profile_picture_handle"] = profile_picture_handle
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

        profile_picture_handle = d.pop("profile_picture_handle", UNSET)

        _vertical = d.pop("vertical", UNSET)
        vertical: ApiEndpointsWhatsAppUpdateBusinessProfileRequestVertical | Unset
        if isinstance(_vertical, Unset):
            vertical = UNSET
        else:
            vertical = ApiEndpointsWhatsAppUpdateBusinessProfileRequestVertical(_vertical)

        websites = cast(list[str], d.pop("websites", UNSET))

        api_endpoints_whats_app_update_business_profile_request = cls(
            about=about,
            address=address,
            description=description,
            email=email,
            profile_picture_handle=profile_picture_handle,
            vertical=vertical,
            websites=websites,
        )

        api_endpoints_whats_app_update_business_profile_request.additional_properties = d
        return api_endpoints_whats_app_update_business_profile_request

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
