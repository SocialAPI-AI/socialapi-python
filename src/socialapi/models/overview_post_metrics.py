from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="OverviewPostMetrics")


@_attrs_define
class OverviewPostMetrics:
    """
    Attributes:
        comments (int):  Example: 52.
        engagements (int):  Example: 512.
        likes (int):  Example: 430.
        saves (int):  Example: 9.
        shares (int):  Example: 21.
        views (int):  Example: 10400.
    """

    comments: int
    engagements: int
    likes: int
    saves: int
    shares: int
    views: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        comments = self.comments

        engagements = self.engagements

        likes = self.likes

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

        saves = d.pop("saves")

        shares = d.pop("shares")

        views = d.pop("views")

        overview_post_metrics = cls(
            comments=comments,
            engagements=engagements,
            likes=likes,
            saves=saves,
            shares=shares,
            views=views,
        )

        overview_post_metrics.additional_properties = d
        return overview_post_metrics

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
