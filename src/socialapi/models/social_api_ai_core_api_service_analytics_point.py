from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SocialApiAiCoreApiServiceAnalyticsPoint")


@_attrs_define
class SocialApiAiCoreApiServiceAnalyticsPoint:
    """
    Attributes:
        change (int | Unset): Change is the difference from the previous point in this series. Present
            on gauges only, and absent on the first point of a range, which has no
            predecessor to diff against. Example: 18.
        day (str | Unset): Day is YYYY-MM-DD, cut on the boundary named by the series' day_tz. Example: 2026-09-19.
        days_spanned (int | Unset): DaysSpanned is how many days Change covers. It is 1 in the normal case
            and larger when a day is missing from the series. A chart must divide by
            it and style the segment as interpolated: otherwise a gap draws a spike
            that never happened. Example: 1.
        subjects_counted (int | Unset): SubjectsCounted is how many Subjects contributed to this point's summed
            value. Always at least 1. Read it before charting: a day on which not
            every Subject reported sums lower, and without the count that reads as a
            decline instead of a gap. Example: 3.
        value (int | Unset): Value is the figure for that day, verbatim from the platform for a
            reported point. Example: 12430.
    """

    change: int | Unset = UNSET
    day: str | Unset = UNSET
    days_spanned: int | Unset = UNSET
    subjects_counted: int | Unset = UNSET
    value: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        change = self.change

        day = self.day

        days_spanned = self.days_spanned

        subjects_counted = self.subjects_counted

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if change is not UNSET:
            field_dict["change"] = change
        if day is not UNSET:
            field_dict["day"] = day
        if days_spanned is not UNSET:
            field_dict["days_spanned"] = days_spanned
        if subjects_counted is not UNSET:
            field_dict["subjects_counted"] = subjects_counted
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        change = d.pop("change", UNSET)

        day = d.pop("day", UNSET)

        days_spanned = d.pop("days_spanned", UNSET)

        subjects_counted = d.pop("subjects_counted", UNSET)

        value = d.pop("value", UNSET)

        social_api_ai_core_api_service_analytics_point = cls(
            change=change,
            day=day,
            days_spanned=days_spanned,
            subjects_counted=subjects_counted,
            value=value,
        )

        social_api_ai_core_api_service_analytics_point.additional_properties = d
        return social_api_ai_core_api_service_analytics_point

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
