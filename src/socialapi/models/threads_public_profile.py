from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ThreadsPublicProfile")


@_attrs_define
class ThreadsPublicProfile:
    """
    Attributes:
        biography (str):
        follower_count (int):
        is_verified (bool):
        likes_count (int):
        name (str):
        profile_picture_url (str):
        quotes_count (int):
        reposts_count (int):
        username (str):
        views_count (int):
    """

    biography: str
    follower_count: int
    is_verified: bool
    likes_count: int
    name: str
    profile_picture_url: str
    quotes_count: int
    reposts_count: int
    username: str
    views_count: int
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
        field_dict.update(
            {
                "biography": biography,
                "follower_count": follower_count,
                "is_verified": is_verified,
                "likes_count": likes_count,
                "name": name,
                "profile_picture_url": profile_picture_url,
                "quotes_count": quotes_count,
                "reposts_count": reposts_count,
                "username": username,
                "views_count": views_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        biography = d.pop("biography")

        follower_count = d.pop("follower_count")

        is_verified = d.pop("is_verified")

        likes_count = d.pop("likes_count")

        name = d.pop("name")

        profile_picture_url = d.pop("profile_picture_url")

        quotes_count = d.pop("quotes_count")

        reposts_count = d.pop("reposts_count")

        username = d.pop("username")

        views_count = d.pop("views_count")

        threads_public_profile = cls(
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

        threads_public_profile.additional_properties = d
        return threads_public_profile

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
