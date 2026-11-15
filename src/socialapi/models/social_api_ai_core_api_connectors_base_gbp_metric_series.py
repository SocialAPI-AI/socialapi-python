from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.social_api_ai_core_api_connectors_base_gbp_insights_point import (
        SocialApiAiCoreApiConnectorsBaseGBPInsightsPoint,
    )


T = TypeVar("T", bound="SocialApiAiCoreApiConnectorsBaseGBPMetricSeries")


@_attrs_define
class SocialApiAiCoreApiConnectorsBaseGBPMetricSeries:
    """
    Attributes:
        metric (str | Unset):
        points (list[SocialApiAiCoreApiConnectorsBaseGBPInsightsPoint] | Unset):
        total (int | Unset):
    """

    metric: str | Unset = UNSET
    points: list[SocialApiAiCoreApiConnectorsBaseGBPInsightsPoint] | Unset = UNSET
    total: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        metric = self.metric

        points: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.points, Unset):
            points = []
            for points_item_data in self.points:
                points_item = points_item_data.to_dict()
                points.append(points_item)

        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if metric is not UNSET:
            field_dict["metric"] = metric
        if points is not UNSET:
            field_dict["points"] = points
        if total is not UNSET:
            field_dict["total"] = total

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.social_api_ai_core_api_connectors_base_gbp_insights_point import (
            SocialApiAiCoreApiConnectorsBaseGBPInsightsPoint,  # noqa: PLC0415
        )

        d = dict(src_dict)
        metric = d.pop("metric", UNSET)

        _points = d.pop("points", UNSET)
        points: list[SocialApiAiCoreApiConnectorsBaseGBPInsightsPoint] | Unset = UNSET
        if _points is not UNSET:
            points = []
            for points_item_data in _points:
                points_item = SocialApiAiCoreApiConnectorsBaseGBPInsightsPoint.from_dict(points_item_data)

                points.append(points_item)

        total = d.pop("total", UNSET)

        social_api_ai_core_api_connectors_base_gbp_metric_series = cls(
            metric=metric,
            points=points,
            total=total,
        )

        social_api_ai_core_api_connectors_base_gbp_metric_series.additional_properties = d
        return social_api_ai_core_api_connectors_base_gbp_metric_series

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
