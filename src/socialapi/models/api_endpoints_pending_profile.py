from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiEndpointsPendingProfile")


@_attrs_define
class ApiEndpointsPendingProfile:
    """
    Attributes:
        bio (str | Unset):  Example: Wood-fired pizza since 1998.
        display_name (str | Unset):  Example: Joe's Pizza (Downtown).
        platform_account_id (str | Unset):  Example: accounts/123/locations/456.
        profile_picture_url (str | Unset):
        username (str | Unset):
    """

    bio: str | Unset = UNSET
    display_name: str | Unset = UNSET
    platform_account_id: str | Unset = UNSET
    profile_picture_url: str | Unset = UNSET
    username: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bio = self.bio

        display_name = self.display_name

        platform_account_id = self.platform_account_id

        profile_picture_url = self.profile_picture_url

        username = self.username

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bio is not UNSET:
            field_dict["bio"] = bio
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if platform_account_id is not UNSET:
            field_dict["platform_account_id"] = platform_account_id
        if profile_picture_url is not UNSET:
            field_dict["profile_picture_url"] = profile_picture_url
        if username is not UNSET:
            field_dict["username"] = username

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bio = d.pop("bio", UNSET)

        display_name = d.pop("display_name", UNSET)

        platform_account_id = d.pop("platform_account_id", UNSET)

        profile_picture_url = d.pop("profile_picture_url", UNSET)

        username = d.pop("username", UNSET)

        api_endpoints_pending_profile = cls(
            bio=bio,
            display_name=display_name,
            platform_account_id=platform_account_id,
            profile_picture_url=profile_picture_url,
            username=username,
        )

        api_endpoints_pending_profile.additional_properties = d
        return api_endpoints_pending_profile

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
