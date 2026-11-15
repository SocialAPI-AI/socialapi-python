from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.gbp_insights_point import GBPInsightsPoint


T = TypeVar("T", bound="GBPMetricSeries")


@_attrs_define
class GBPMetricSeries:
    """
    Attributes:
        metric (str):
        points (list[GBPInsightsPoint] | None):
        total (int):
    """

    metric: str
    points: list[GBPInsightsPoint] | None
    total: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        metric = self.metric

        points: list[dict[str, Any]] | None
        if isinstance(self.points, list):
            points = []
            for points_type_0_item_data in self.points:
                points_type_0_item = points_type_0_item_data.to_dict()
                points.append(points_type_0_item)

        else:
            points = self.points

        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "metric": metric,
                "points": points,
                "total": total,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.gbp_insights_point import GBPInsightsPoint  # noqa: PLC0415

        d = dict(src_dict)
        metric = d.pop("metric")

        def _parse_points(data: object) -> list[GBPInsightsPoint] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                points_type_0 = []
                _points_type_0 = data
                for points_type_0_item_data in _points_type_0:
                    points_type_0_item = GBPInsightsPoint.from_dict(points_type_0_item_data)

                    points_type_0.append(points_type_0_item)

                return points_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[GBPInsightsPoint] | None, data)

        points = _parse_points(d.pop("points"))

        total = d.pop("total")

        gbp_metric_series = cls(
            metric=metric,
            points=points,
            total=total,
        )

        gbp_metric_series.additional_properties = d
        return gbp_metric_series

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
