from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SocialApiAiCoreApiServiceOverviewBestTimeCell")


@_attrs_define
class SocialApiAiCoreApiServiceOverviewBestTimeCell:
    """
    Attributes:
        avg_engagements (float | Unset): AvgEngagements is the mean engagements of the posts published in this
            hour. It describes your past posts, not when your audience is online. Example: 118.4.
        hour (int | Unset): Hour is 0 to 23. Example: 9.
        posts (int | Unset):  Example: 5.
        weekday (int | Unset): Weekday is 1 (Monday) to 7 (Sunday). Example: 4.
    """

    avg_engagements: float | Unset = UNSET
    hour: int | Unset = UNSET
    posts: int | Unset = UNSET
    weekday: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        avg_engagements = self.avg_engagements

        hour = self.hour

        posts = self.posts

        weekday = self.weekday

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if avg_engagements is not UNSET:
            field_dict["avg_engagements"] = avg_engagements
        if hour is not UNSET:
            field_dict["hour"] = hour
        if posts is not UNSET:
            field_dict["posts"] = posts
        if weekday is not UNSET:
            field_dict["weekday"] = weekday

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        avg_engagements = d.pop("avg_engagements", UNSET)

        hour = d.pop("hour", UNSET)

        posts = d.pop("posts", UNSET)

        weekday = d.pop("weekday", UNSET)

        social_api_ai_core_api_service_overview_best_time_cell = cls(
            avg_engagements=avg_engagements,
            hour=hour,
            posts=posts,
            weekday=weekday,
        )

        social_api_ai_core_api_service_overview_best_time_cell.additional_properties = d
        return social_api_ai_core_api_service_overview_best_time_cell

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
