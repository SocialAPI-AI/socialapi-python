from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SocialApiAiCoreApiServiceOverviewPlatform")


@_attrs_define
class SocialApiAiCoreApiServiceOverviewPlatform:
    """
    Attributes:
        comments (int | Unset):  Example: 412.
        engagements (int | Unset):  Example: 3810.
        likes (int | Unset):  Example: 3120.
        platform (str | Unset):  Example: instagram.
        posts (int | Unset):  Example: 42.
        saves (int | Unset):  Example: 77.
        shares (int | Unset):  Example: 201.
        views (int | Unset):  Example: 58200.
    """

    comments: int | Unset = UNSET
    engagements: int | Unset = UNSET
    likes: int | Unset = UNSET
    platform: str | Unset = UNSET
    posts: int | Unset = UNSET
    saves: int | Unset = UNSET
    shares: int | Unset = UNSET
    views: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        comments = self.comments

        engagements = self.engagements

        likes = self.likes

        platform = self.platform

        posts = self.posts

        saves = self.saves

        shares = self.shares

        views = self.views

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if comments is not UNSET:
            field_dict["comments"] = comments
        if engagements is not UNSET:
            field_dict["engagements"] = engagements
        if likes is not UNSET:
            field_dict["likes"] = likes
        if platform is not UNSET:
            field_dict["platform"] = platform
        if posts is not UNSET:
            field_dict["posts"] = posts
        if saves is not UNSET:
            field_dict["saves"] = saves
        if shares is not UNSET:
            field_dict["shares"] = shares
        if views is not UNSET:
            field_dict["views"] = views

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        comments = d.pop("comments", UNSET)

        engagements = d.pop("engagements", UNSET)

        likes = d.pop("likes", UNSET)

        platform = d.pop("platform", UNSET)

        posts = d.pop("posts", UNSET)

        saves = d.pop("saves", UNSET)

        shares = d.pop("shares", UNSET)

        views = d.pop("views", UNSET)

        social_api_ai_core_api_service_overview_platform = cls(
            comments=comments,
            engagements=engagements,
            likes=likes,
            platform=platform,
            posts=posts,
            saves=saves,
            shares=shares,
            views=views,
        )

        social_api_ai_core_api_service_overview_platform.additional_properties = d
        return social_api_ai_core_api_service_overview_platform

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
