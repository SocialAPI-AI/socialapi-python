from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PendingProfile")


@_attrs_define
class PendingProfile:
    """
    Attributes:
        bio (str):  Example: Wood-fired pizza since 1998.
        display_name (str):  Example: Joe's Pizza (Downtown).
        platform_account_id (str):  Example: accounts/123/locations/456.
        profile_picture_url (str):
        username (str):
    """

    bio: str
    display_name: str
    platform_account_id: str
    profile_picture_url: str
    username: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bio = self.bio

        display_name = self.display_name

        platform_account_id = self.platform_account_id

        profile_picture_url = self.profile_picture_url

        username = self.username

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "bio": bio,
                "display_name": display_name,
                "platform_account_id": platform_account_id,
                "profile_picture_url": profile_picture_url,
                "username": username,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bio = d.pop("bio")

        display_name = d.pop("display_name")

        platform_account_id = d.pop("platform_account_id")

        profile_picture_url = d.pop("profile_picture_url")

        username = d.pop("username")

        pending_profile = cls(
            bio=bio,
            display_name=display_name,
            platform_account_id=platform_account_id,
            profile_picture_url=profile_picture_url,
            username=username,
        )

        pending_profile.additional_properties = d
        return pending_profile

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
