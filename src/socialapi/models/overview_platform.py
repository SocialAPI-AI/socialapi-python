from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="OverviewPlatform")


@_attrs_define
class OverviewPlatform:
    """
    Attributes:
        comments (int):  Example: 412.
        engagements (int):  Example: 3810.
        likes (int):  Example: 3120.
        platform (str):  Example: instagram.
        posts (int):  Example: 42.
        saves (int):  Example: 77.
        shares (int):  Example: 201.
        views (int):  Example: 58200.
    """

    comments: int
    engagements: int
    likes: int
    platform: str
    posts: int
    saves: int
    shares: int
    views: int
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
        field_dict.update(
            {
                "comments": comments,
                "engagements": engagements,
                "likes": likes,
                "platform": platform,
                "posts": posts,
                "saves": saves,
                "shares": shares,
                "views": views,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        comments = d.pop("comments")

        engagements = d.pop("engagements")

        likes = d.pop("likes")

        platform = d.pop("platform")

        posts = d.pop("posts")

        saves = d.pop("saves")

        shares = d.pop("shares")

        views = d.pop("views")

        overview_platform = cls(
            comments=comments,
            engagements=engagements,
            likes=likes,
            platform=platform,
            posts=posts,
            saves=saves,
            shares=shares,
            views=views,
        )

        overview_platform.additional_properties = d
        return overview_platform

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
