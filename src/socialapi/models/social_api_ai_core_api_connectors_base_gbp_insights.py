from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.social_api_ai_core_api_connectors_base_gbp_metric_series import (
        SocialApiAiCoreApiConnectorsBaseGBPMetricSeries,
    )


T = TypeVar("T", bound="SocialApiAiCoreApiConnectorsBaseGBPInsights")


@_attrs_define
class SocialApiAiCoreApiConnectorsBaseGBPInsights:
    """
    Attributes:
        end_date (str | Unset):
        metrics (list[SocialApiAiCoreApiConnectorsBaseGBPMetricSeries] | Unset):
        start_date (str | Unset):
    """

    end_date: str | Unset = UNSET
    metrics: list[SocialApiAiCoreApiConnectorsBaseGBPMetricSeries] | Unset = UNSET
    start_date: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end_date = self.end_date

        metrics: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.metrics, Unset):
            metrics = []
            for metrics_item_data in self.metrics:
                metrics_item = metrics_item_data.to_dict()
                metrics.append(metrics_item)

        start_date = self.start_date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if end_date is not UNSET:
            field_dict["end_date"] = end_date
        if metrics is not UNSET:
            field_dict["metrics"] = metrics
        if start_date is not UNSET:
            field_dict["start_date"] = start_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.social_api_ai_core_api_connectors_base_gbp_metric_series import (
            SocialApiAiCoreApiConnectorsBaseGBPMetricSeries,  # noqa: PLC0415
        )

        d = dict(src_dict)
        end_date = d.pop("end_date", UNSET)

        _metrics = d.pop("metrics", UNSET)
        metrics: list[SocialApiAiCoreApiConnectorsBaseGBPMetricSeries] | Unset = UNSET
        if _metrics is not UNSET:
            metrics = []
            for metrics_item_data in _metrics:
                metrics_item = SocialApiAiCoreApiConnectorsBaseGBPMetricSeries.from_dict(metrics_item_data)

                metrics.append(metrics_item)

        start_date = d.pop("start_date", UNSET)

        social_api_ai_core_api_connectors_base_gbp_insights = cls(
            end_date=end_date,
            metrics=metrics,
            start_date=start_date,
        )

        social_api_ai_core_api_connectors_base_gbp_insights.additional_properties = d
        return social_api_ai_core_api_connectors_base_gbp_insights

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
