from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SocialApiAiCoreApiServiceOverviewPostMetrics")


@_attrs_define
class SocialApiAiCoreApiServiceOverviewPostMetrics:
    """
    Attributes:
        comments (int | Unset):  Example: 52.
        engagements (int | Unset):  Example: 512.
        likes (int | Unset):  Example: 430.
        saves (int | Unset):  Example: 9.
        shares (int | Unset):  Example: 21.
        views (int | Unset):  Example: 10400.
    """

    comments: int | Unset = UNSET
    engagements: int | Unset = UNSET
    likes: int | Unset = UNSET
    saves: int | Unset = UNSET
    shares: int | Unset = UNSET
    views: int | Unset = UNSET
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
        field_dict.update({})
        if comments is not UNSET:
            field_dict["comments"] = comments
        if engagements is not UNSET:
            field_dict["engagements"] = engagements
        if likes is not UNSET:
            field_dict["likes"] = likes
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

        saves = d.pop("saves", UNSET)

        shares = d.pop("shares", UNSET)

        views = d.pop("views", UNSET)

        social_api_ai_core_api_service_overview_post_metrics = cls(
            comments=comments,
            engagements=engagements,
            likes=likes,
            saves=saves,
            shares=shares,
            views=views,
        )

        social_api_ai_core_api_service_overview_post_metrics.additional_properties = d
        return social_api_ai_core_api_service_overview_post_metrics

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
