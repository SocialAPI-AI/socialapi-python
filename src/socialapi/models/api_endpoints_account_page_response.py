from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiEndpointsAccountPageResponse")


@_attrs_define
class ApiEndpointsAccountPageResponse:
    """
    Attributes:
        about (str | Unset):
        category (str | Unset):
        cover_photo_url (str | Unset):
        enriched_at (str | Unset):
        followers_count (int | Unset):
        id (str | Unset):
        is_active (bool | Unset):
        is_default (bool | Unset):
        link (str | Unset):
        name (str | Unset):
        platform_page_id (str | Unset):
        profile_picture_url (str | Unset):
        username (str | Unset):
        verification_status (str | Unset):
    """

    about: str | Unset = UNSET
    category: str | Unset = UNSET
    cover_photo_url: str | Unset = UNSET
    enriched_at: str | Unset = UNSET
    followers_count: int | Unset = UNSET
    id: str | Unset = UNSET
    is_active: bool | Unset = UNSET
    is_default: bool | Unset = UNSET
    link: str | Unset = UNSET
    name: str | Unset = UNSET
    platform_page_id: str | Unset = UNSET
    profile_picture_url: str | Unset = UNSET
    username: str | Unset = UNSET
    verification_status: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        about = self.about

        category = self.category

        cover_photo_url = self.cover_photo_url

        enriched_at = self.enriched_at

        followers_count = self.followers_count

        id = self.id

        is_active = self.is_active

        is_default = self.is_default

        link = self.link

        name = self.name

        platform_page_id = self.platform_page_id

        profile_picture_url = self.profile_picture_url

        username = self.username

        verification_status = self.verification_status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
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
        if id is not UNSET:
            field_dict["id"] = id
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if is_default is not UNSET:
            field_dict["is_default"] = is_default
        if link is not UNSET:
            field_dict["link"] = link
        if name is not UNSET:
            field_dict["name"] = name
        if platform_page_id is not UNSET:
            field_dict["platform_page_id"] = platform_page_id
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
        about = d.pop("about", UNSET)

        category = d.pop("category", UNSET)

        cover_photo_url = d.pop("cover_photo_url", UNSET)

        enriched_at = d.pop("enriched_at", UNSET)

        followers_count = d.pop("followers_count", UNSET)

        id = d.pop("id", UNSET)

        is_active = d.pop("is_active", UNSET)

        is_default = d.pop("is_default", UNSET)

        link = d.pop("link", UNSET)

        name = d.pop("name", UNSET)

        platform_page_id = d.pop("platform_page_id", UNSET)

        profile_picture_url = d.pop("profile_picture_url", UNSET)

        username = d.pop("username", UNSET)

        verification_status = d.pop("verification_status", UNSET)

        api_endpoints_account_page_response = cls(
            about=about,
            category=category,
            cover_photo_url=cover_photo_url,
            enriched_at=enriched_at,
            followers_count=followers_count,
            id=id,
            is_active=is_active,
            is_default=is_default,
            link=link,
            name=name,
            platform_page_id=platform_page_id,
            profile_picture_url=profile_picture_url,
            username=username,
            verification_status=verification_status,
        )

        api_endpoints_account_page_response.additional_properties = d
        return api_endpoints_account_page_response

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
