from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SocialApiAiCoreApiConnectorsBasePostInsight")


@_attrs_define
class SocialApiAiCoreApiConnectorsBasePostInsight:
    """
    Attributes:
        clicks (int | Unset):
        comments (int | Unset):
        created_at (str | Unset):
        engagement_rate (float | Unset):
        impressions (int | Unset):
        likes (int | Unset):
        permalink (str | Unset):
        post_id (str | Unset):
        shares (int | Unset):
        text (str | Unset):
        unique_views (int | Unset):
    """

    clicks: int | Unset = UNSET
    comments: int | Unset = UNSET
    created_at: str | Unset = UNSET
    engagement_rate: float | Unset = UNSET
    impressions: int | Unset = UNSET
    likes: int | Unset = UNSET
    permalink: str | Unset = UNSET
    post_id: str | Unset = UNSET
    shares: int | Unset = UNSET
    text: str | Unset = UNSET
    unique_views: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        clicks = self.clicks

        comments = self.comments

        created_at = self.created_at

        engagement_rate = self.engagement_rate

        impressions = self.impressions

        likes = self.likes

        permalink = self.permalink

        post_id = self.post_id

        shares = self.shares

        text = self.text

        unique_views = self.unique_views

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if clicks is not UNSET:
            field_dict["clicks"] = clicks
        if comments is not UNSET:
            field_dict["comments"] = comments
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if engagement_rate is not UNSET:
            field_dict["engagement_rate"] = engagement_rate
        if impressions is not UNSET:
            field_dict["impressions"] = impressions
        if likes is not UNSET:
            field_dict["likes"] = likes
        if permalink is not UNSET:
            field_dict["permalink"] = permalink
        if post_id is not UNSET:
            field_dict["post_id"] = post_id
        if shares is not UNSET:
            field_dict["shares"] = shares
        if text is not UNSET:
            field_dict["text"] = text
        if unique_views is not UNSET:
            field_dict["unique_views"] = unique_views

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        clicks = d.pop("clicks", UNSET)

        comments = d.pop("comments", UNSET)

        created_at = d.pop("created_at", UNSET)

        engagement_rate = d.pop("engagement_rate", UNSET)

        impressions = d.pop("impressions", UNSET)

        likes = d.pop("likes", UNSET)

        permalink = d.pop("permalink", UNSET)

        post_id = d.pop("post_id", UNSET)

        shares = d.pop("shares", UNSET)

        text = d.pop("text", UNSET)

        unique_views = d.pop("unique_views", UNSET)

        social_api_ai_core_api_connectors_base_post_insight = cls(
            clicks=clicks,
            comments=comments,
            created_at=created_at,
            engagement_rate=engagement_rate,
            impressions=impressions,
            likes=likes,
            permalink=permalink,
            post_id=post_id,
            shares=shares,
            text=text,
            unique_views=unique_views,
        )

        social_api_ai_core_api_connectors_base_post_insight.additional_properties = d
        return social_api_ai_core_api_connectors_base_post_insight

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
