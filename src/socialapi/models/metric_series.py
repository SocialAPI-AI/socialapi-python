from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.analytics_point import AnalyticsPoint


T = TypeVar("T", bound="MetricSeries")


@_attrs_define
class MetricSeries:
    """
    Attributes:
        day_tz (str): DayTZ names the boundary these days were cut on, or mixed when a rollup
            combines platforms that cut differently. A Brand rollup genuinely mixes
            boundaries: up to eight hours of activity sits on the wrong side of a day
            edge for Meta platforms next to a UTC-cut platform in the same sum. The
            error is bounded and does not compound, and this field is how a reader
            tells it from a real discrepancy. Example: America/Los_Angeles.
        kind (str): Kind is gauge (a level, diff it) or flow (a per-day count, sum it). Example: gauge.
        metric (str): Metric is the platform's own name for a platform Metric. Example: page_follows.
        points (list[AnalyticsPoint]): Points are ordered oldest first.
        source (str): Source is reported, sampled, owned, or mixed when a rollup combines more
            than one. Example: reported.
    """

    day_tz: str
    kind: str
    metric: str
    points: list[AnalyticsPoint]
    source: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        day_tz = self.day_tz

        kind = self.kind

        metric = self.metric

        points = []
        for points_item_data in self.points:
            points_item = points_item_data.to_dict()
            points.append(points_item)

        source = self.source

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "day_tz": day_tz,
                "kind": kind,
                "metric": metric,
                "points": points,
                "source": source,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.analytics_point import AnalyticsPoint  # noqa: PLC0415

        d = dict(src_dict)
        day_tz = d.pop("day_tz")

        kind = d.pop("kind")

        metric = d.pop("metric")

        points = []
        _points = d.pop("points")
        for points_item_data in _points:
            points_item = AnalyticsPoint.from_dict(points_item_data)

            points.append(points_item)

        source = d.pop("source")

        metric_series = cls(
            day_tz=day_tz,
            kind=kind,
            metric=metric,
            points=points,
            source=source,
        )

        metric_series.additional_properties = d
        return metric_series

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
