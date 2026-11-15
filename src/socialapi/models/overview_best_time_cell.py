from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="OverviewBestTimeCell")


@_attrs_define
class OverviewBestTimeCell:
    """
    Attributes:
        avg_engagements (float): AvgEngagements is the mean engagements of the posts published in this
            hour. It describes your past posts, not when your audience is online. Example: 118.4.
        hour (int): Hour is 0 to 23. Example: 9.
        posts (int):  Example: 5.
        weekday (int): Weekday is 1 (Monday) to 7 (Sunday). Example: 4.
    """

    avg_engagements: float
    hour: int
    posts: int
    weekday: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        avg_engagements = self.avg_engagements

        hour = self.hour

        posts = self.posts

        weekday = self.weekday

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "avg_engagements": avg_engagements,
                "hour": hour,
                "posts": posts,
                "weekday": weekday,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        avg_engagements = d.pop("avg_engagements")

        hour = d.pop("hour")

        posts = d.pop("posts")

        weekday = d.pop("weekday")

        overview_best_time_cell = cls(
            avg_engagements=avg_engagements,
            hour=hour,
            posts=posts,
            weekday=weekday,
        )

        overview_best_time_cell.additional_properties = d
        return overview_best_time_cell

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
