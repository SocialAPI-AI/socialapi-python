from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DailyInsight")


@_attrs_define
class DailyInsight:
    """
    Attributes:
        date (datetime.date): Day in YYYY-MM-DD. Example: 2026-09-27.
        followers (int):
        interactions (int):
        reach (int):
        views (int):
    """

    date: datetime.date
    followers: int
    interactions: int
    reach: int
    views: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date = self.date.isoformat()

        followers = self.followers

        interactions = self.interactions

        reach = self.reach

        views = self.views

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "date": date,
                "followers": followers,
                "interactions": interactions,
                "reach": reach,
                "views": views,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        date = datetime.date.fromisoformat(d.pop("date"))

        followers = d.pop("followers")

        interactions = d.pop("interactions")

        reach = d.pop("reach")

        views = d.pop("views")

        daily_insight = cls(
            date=date,
            followers=followers,
            interactions=interactions,
            reach=reach,
            views=views,
        )

        daily_insight.additional_properties = d
        return daily_insight

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
