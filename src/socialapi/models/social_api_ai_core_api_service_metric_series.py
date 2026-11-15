from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.social_api_ai_core_api_service_analytics_point import SocialApiAiCoreApiServiceAnalyticsPoint


T = TypeVar("T", bound="SocialApiAiCoreApiServiceMetricSeries")


@_attrs_define
class SocialApiAiCoreApiServiceMetricSeries:
    """
    Attributes:
        day_tz (str | Unset): DayTZ names the boundary these days were cut on, or mixed when a rollup
            combines platforms that cut differently. A Brand rollup genuinely mixes
            boundaries: up to eight hours of activity sits on the wrong side of a day
            edge for Meta platforms next to a UTC-cut platform in the same sum. The
            error is bounded and does not compound, and this field is how a reader
            tells it from a real discrepancy. Example: America/Los_Angeles.
        kind (str | Unset): Kind is gauge (a level, diff it) or flow (a per-day count, sum it). Example: gauge.
        metric (str | Unset): Metric is the platform's own name for a platform Metric. Example: page_follows.
        points (list[SocialApiAiCoreApiServiceAnalyticsPoint] | Unset): Points are ordered oldest first.
        source (str | Unset): Source is reported, sampled, owned, or mixed when a rollup combines more
            than one. Example: reported.
    """

    day_tz: str | Unset = UNSET
    kind: str | Unset = UNSET
    metric: str | Unset = UNSET
    points: list[SocialApiAiCoreApiServiceAnalyticsPoint] | Unset = UNSET
    source: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        day_tz = self.day_tz

        kind = self.kind

        metric = self.metric

        points: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.points, Unset):
            points = []
            for points_item_data in self.points:
                points_item = points_item_data.to_dict()
                points.append(points_item)

        source = self.source

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if day_tz is not UNSET:
            field_dict["day_tz"] = day_tz
        if kind is not UNSET:
            field_dict["kind"] = kind
        if metric is not UNSET:
            field_dict["metric"] = metric
        if points is not UNSET:
            field_dict["points"] = points
        if source is not UNSET:
            field_dict["source"] = source

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.social_api_ai_core_api_service_analytics_point import (
            SocialApiAiCoreApiServiceAnalyticsPoint,  # noqa: PLC0415
        )

        d = dict(src_dict)
        day_tz = d.pop("day_tz", UNSET)

        kind = d.pop("kind", UNSET)

        metric = d.pop("metric", UNSET)

        _points = d.pop("points", UNSET)
        points: list[SocialApiAiCoreApiServiceAnalyticsPoint] | Unset = UNSET
        if _points is not UNSET:
            points = []
            for points_item_data in _points:
                points_item = SocialApiAiCoreApiServiceAnalyticsPoint.from_dict(points_item_data)

                points.append(points_item)

        source = d.pop("source", UNSET)

        social_api_ai_core_api_service_metric_series = cls(
            day_tz=day_tz,
            kind=kind,
            metric=metric,
            points=points,
            source=source,
        )

        social_api_ai_core_api_service_metric_series.additional_properties = d
        return social_api_ai_core_api_service_metric_series

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
