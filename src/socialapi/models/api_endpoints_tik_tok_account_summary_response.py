from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiEndpointsTikTokAccountSummaryResponse")


@_attrs_define
class ApiEndpointsTikTokAccountSummaryResponse:
    """
    Attributes:
        avatar_url (str | Unset):
        bio_description (str | Unset):
        display_name (str | Unset):
        follower_count (int | Unset):
        following_count (int | Unset):
        is_verified (bool | Unset):
        likes_count (int | Unset):
        profile_deep_link (str | Unset):
        username (str | Unset):
        video_count (int | Unset):
    """

    avatar_url: str | Unset = UNSET
    bio_description: str | Unset = UNSET
    display_name: str | Unset = UNSET
    follower_count: int | Unset = UNSET
    following_count: int | Unset = UNSET
    is_verified: bool | Unset = UNSET
    likes_count: int | Unset = UNSET
    profile_deep_link: str | Unset = UNSET
    username: str | Unset = UNSET
    video_count: int | Unset = UNSET
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
        field_dict.update({})
        if avatar_url is not UNSET:
            field_dict["avatar_url"] = avatar_url
        if bio_description is not UNSET:
            field_dict["bio_description"] = bio_description
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if follower_count is not UNSET:
            field_dict["follower_count"] = follower_count
        if following_count is not UNSET:
            field_dict["following_count"] = following_count
        if is_verified is not UNSET:
            field_dict["is_verified"] = is_verified
        if likes_count is not UNSET:
            field_dict["likes_count"] = likes_count
        if profile_deep_link is not UNSET:
            field_dict["profile_deep_link"] = profile_deep_link
        if username is not UNSET:
            field_dict["username"] = username
        if video_count is not UNSET:
            field_dict["video_count"] = video_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        avatar_url = d.pop("avatar_url", UNSET)

        bio_description = d.pop("bio_description", UNSET)

        display_name = d.pop("display_name", UNSET)

        follower_count = d.pop("follower_count", UNSET)

        following_count = d.pop("following_count", UNSET)

        is_verified = d.pop("is_verified", UNSET)

        likes_count = d.pop("likes_count", UNSET)

        profile_deep_link = d.pop("profile_deep_link", UNSET)

        username = d.pop("username", UNSET)

        video_count = d.pop("video_count", UNSET)

        api_endpoints_tik_tok_account_summary_response = cls(
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

        api_endpoints_tik_tok_account_summary_response.additional_properties = d
        return api_endpoints_tik_tok_account_summary_response

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
