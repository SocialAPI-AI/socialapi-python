from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AccountPage")


@_attrs_define
class AccountPage:
    """
    Attributes:
        id (str):
        is_active (bool):
        is_default (bool):
        name (str):
        platform_page_id (str):
        about (str | Unset):
        category (str | Unset):
        cover_photo_url (str | Unset):
        enriched_at (str | Unset):
        followers_count (int | Unset):
        link (str | Unset):
        profile_picture_url (str | Unset):
        username (str | Unset):
        verification_status (str | Unset):
    """

    id: str
    is_active: bool
    is_default: bool
    name: str
    platform_page_id: str
    about: str | Unset = UNSET
    category: str | Unset = UNSET
    cover_photo_url: str | Unset = UNSET
    enriched_at: str | Unset = UNSET
    followers_count: int | Unset = UNSET
    link: str | Unset = UNSET
    profile_picture_url: str | Unset = UNSET
    username: str | Unset = UNSET
    verification_status: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        is_active = self.is_active

        is_default = self.is_default

        name = self.name

        platform_page_id = self.platform_page_id

        about = self.about

        category = self.category

        cover_photo_url = self.cover_photo_url

        enriched_at = self.enriched_at

        followers_count = self.followers_count

        link = self.link

        profile_picture_url = self.profile_picture_url

        username = self.username

        verification_status = self.verification_status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "is_active": is_active,
                "is_default": is_default,
                "name": name,
                "platform_page_id": platform_page_id,
            }
        )
        if about is not UNSET:
            field_dict["about"] = about
        if category is not UNSET:
            field_dict["category"] = category
        if cover_photo_url is not UNSET:
            field_dict["cover_photo_url"] = cover_photo_url
        if enriched_at is not UNSET:
            field_dict["enriched_at"] = enriched_at
        if followers_count is not UNSET:
            field_dict["followers_count"] = followers_count
        if link is not UNSET:
            field_dict["link"] = link
        if profile_picture_url is not UNSET:
            field_dict["profile_picture_url"] = profile_picture_url
        if username is not UNSET:
            field_dict["username"] = username
        if verification_status is not UNSET:
            field_dict["verification_status"] = verification_status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        is_active = d.pop("is_active")

        is_default = d.pop("is_default")

        name = d.pop("name")

        platform_page_id = d.pop("platform_page_id")

        about = d.pop("about", UNSET)

        category = d.pop("category", UNSET)

        cover_photo_url = d.pop("cover_photo_url", UNSET)

        enriched_at = d.pop("enriched_at", UNSET)

        followers_count = d.pop("followers_count", UNSET)

        link = d.pop("link", UNSET)

        profile_picture_url = d.pop("profile_picture_url", UNSET)

        username = d.pop("username", UNSET)

        verification_status = d.pop("verification_status", UNSET)

        account_page = cls(
            id=id,
            is_active=is_active,
            is_default=is_default,
            name=name,
            platform_page_id=platform_page_id,
            about=about,
            category=category,
            cover_photo_url=cover_photo_url,
            enriched_at=enriched_at,
            followers_count=followers_count,
            link=link,
            profile_picture_url=profile_picture_url,
            username=username,
            verification_status=verification_status,
        )

        account_page.additional_properties = d
        return account_page

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
