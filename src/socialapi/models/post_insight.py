from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostInsight")


@_attrs_define
class PostInsight:
    """
    Attributes:
        clicks (int):
        comments (int):
        engagement_rate (float):
        impressions (int):
        likes (int):
        post_id (str):
        shares (int):
        unique_views (int):
        created_at (datetime.datetime | Unset):
        permalink (str | Unset):
        text (str | Unset):
    """

    clicks: int
    comments: int
    engagement_rate: float
    impressions: int
    likes: int
    post_id: str
    shares: int
    unique_views: int
    created_at: datetime.datetime | Unset = UNSET
    permalink: str | Unset = UNSET
    text: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        clicks = self.clicks

        comments = self.comments

        engagement_rate = self.engagement_rate

        impressions = self.impressions

        likes = self.likes

        post_id = self.post_id

        shares = self.shares

        unique_views = self.unique_views

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        permalink = self.permalink

        text = self.text

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "clicks": clicks,
                "comments": comments,
                "engagement_rate": engagement_rate,
                "impressions": impressions,
                "likes": likes,
                "post_id": post_id,
                "shares": shares,
                "unique_views": unique_views,
            }
        )
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if permalink is not UNSET:
            field_dict["permalink"] = permalink
        if text is not UNSET:
            field_dict["text"] = text

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        clicks = d.pop("clicks")

        comments = d.pop("comments")

        engagement_rate = d.pop("engagement_rate")

        impressions = d.pop("impressions")

        likes = d.pop("likes")

        post_id = d.pop("post_id")

        shares = d.pop("shares")

        unique_views = d.pop("unique_views")

        _created_at = d.pop("created_at", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)

        permalink = d.pop("permalink", UNSET)

        text = d.pop("text", UNSET)

        post_insight = cls(
            clicks=clicks,
            comments=comments,
            engagement_rate=engagement_rate,
            impressions=impressions,
            likes=likes,
            post_id=post_id,
            shares=shares,
            unique_views=unique_views,
            created_at=created_at,
            permalink=permalink,
            text=text,
        )

        post_insight.additional_properties = d
        return post_insight

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
