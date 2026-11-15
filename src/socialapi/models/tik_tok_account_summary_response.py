from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="TikTokAccountSummaryResponse")


@_attrs_define
class TikTokAccountSummaryResponse:
    """
    Attributes:
        avatar_url (str):
        bio_description (str):
        display_name (str):
        follower_count (int):
        following_count (int):
        is_verified (bool):
        likes_count (int):
        profile_deep_link (str):
        username (str):
        video_count (int):
    """

    avatar_url: str
    bio_description: str
    display_name: str
    follower_count: int
    following_count: int
    is_verified: bool
    likes_count: int
    profile_deep_link: str
    username: str
    video_count: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        avatar_url = self.avatar_url

        bio_description = self.bio_description

        display_name = self.display_name

        follower_count = self.follower_count

        following_count = self.following_count

        is_verified = self.is_verified

        likes_count = self.likes_count

        profile_deep_link = self.profile_deep_link

        username = self.username

        video_count = self.video_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "avatar_url": avatar_url,
                "bio_description": bio_description,
                "display_name": display_name,
                "follower_count": follower_count,
                "following_count": following_count,
                "is_verified": is_verified,
                "likes_count": likes_count,
                "profile_deep_link": profile_deep_link,
                "username": username,
                "video_count": video_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        avatar_url = d.pop("avatar_url")

        bio_description = d.pop("bio_description")

        display_name = d.pop("display_name")

        follower_count = d.pop("follower_count")

        following_count = d.pop("following_count")

        is_verified = d.pop("is_verified")

        likes_count = d.pop("likes_count")

        profile_deep_link = d.pop("profile_deep_link")

        username = d.pop("username")

        video_count = d.pop("video_count")

        tik_tok_account_summary_response = cls(
            avatar_url=avatar_url,
            bio_description=bio_description,
            display_name=display_name,
            follower_count=follower_count,
            following_count=following_count,
            is_verified=is_verified,
            likes_count=likes_count,
            profile_deep_link=profile_deep_link,
            username=username,
            video_count=video_count,
        )

        tik_tok_account_summary_response.additional_properties = d
        return tik_tok_account_summary_response

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
