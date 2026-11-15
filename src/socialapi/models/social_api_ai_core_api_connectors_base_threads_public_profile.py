from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SocialApiAiCoreApiConnectorsBaseThreadsPublicProfile")


@_attrs_define
class SocialApiAiCoreApiConnectorsBaseThreadsPublicProfile:
    """
    Attributes:
        biography (str | Unset):
        follower_count (int | Unset):
        is_verified (bool | Unset):
        likes_count (int | Unset):
        name (str | Unset):
        profile_picture_url (str | Unset):
        quotes_count (int | Unset):
        reposts_count (int | Unset):
        username (str | Unset):
        views_count (int | Unset):
    """

    biography: str | Unset = UNSET
    follower_count: int | Unset = UNSET
    is_verified: bool | Unset = UNSET
    likes_count: int | Unset = UNSET
    name: str | Unset = UNSET
    profile_picture_url: str | Unset = UNSET
    quotes_count: int | Unset = UNSET
    reposts_count: int | Unset = UNSET
    username: str | Unset = UNSET
    views_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        biography = self.biography

        follower_count = self.follower_count

        is_verified = self.is_verified

        likes_count = self.likes_count

        name = self.name

        profile_picture_url = self.profile_picture_url

        quotes_count = self.quotes_count

        reposts_count = self.reposts_count

        username = self.username

        views_count = self.views_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if biography is not UNSET:
            field_dict["biography"] = biography
        if follower_count is not UNSET:
            field_dict["follower_count"] = follower_count
        if is_verified is not UNSET:
            field_dict["is_verified"] = is_verified
        if likes_count is not UNSET:
            field_dict["likes_count"] = likes_count
        if name is not UNSET:
            field_dict["name"] = name
        if profile_picture_url is not UNSET:
            field_dict["profile_picture_url"] = profile_picture_url
        if quotes_count is not UNSET:
            field_dict["quotes_count"] = quotes_count
        if reposts_count is not UNSET:
            field_dict["reposts_count"] = reposts_count
        if username is not UNSET:
            field_dict["username"] = username
        if views_count is not UNSET:
            field_dict["views_count"] = views_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        biography = d.pop("biography", UNSET)

        follower_count = d.pop("follower_count", UNSET)

        is_verified = d.pop("is_verified", UNSET)

        likes_count = d.pop("likes_count", UNSET)

        name = d.pop("name", UNSET)

        profile_picture_url = d.pop("profile_picture_url", UNSET)

        quotes_count = d.pop("quotes_count", UNSET)

        reposts_count = d.pop("reposts_count", UNSET)

        username = d.pop("username", UNSET)

        views_count = d.pop("views_count", UNSET)

        social_api_ai_core_api_connectors_base_threads_public_profile = cls(
            biography=biography,
            follower_count=follower_count,
            is_verified=is_verified,
            likes_count=likes_count,
            name=name,
            profile_picture_url=profile_picture_url,
            quotes_count=quotes_count,
            reposts_count=reposts_count,
            username=username,
            views_count=views_count,
        )

        social_api_ai_core_api_connectors_base_threads_public_profile.additional_properties = d
        return social_api_ai_core_api_connectors_base_threads_public_profile

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
