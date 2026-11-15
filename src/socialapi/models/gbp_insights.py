from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.gbp_metric_series import GBPMetricSeries


T = TypeVar("T", bound="GBPInsights")


@_attrs_define
class GBPInsights:
    """
    Attributes:
        end_date (datetime.date):
        metrics (list[GBPMetricSeries] | None):
        start_date (datetime.date):
    """

    end_date: datetime.date
    metrics: list[GBPMetricSeries] | None
    start_date: datetime.date
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end_date = self.end_date.isoformat()

        metrics: list[dict[str, Any]] | None
        if isinstance(self.metrics, list):
            metrics = []
            for metrics_type_0_item_data in self.metrics:
                metrics_type_0_item = metrics_type_0_item_data.to_dict()
                metrics.append(metrics_type_0_item)

        else:
            metrics = self.metrics

        start_date = self.start_date.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "end_date": end_date,
                "metrics": metrics,
                "start_date": start_date,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.gbp_metric_series import GBPMetricSeries  # noqa: PLC0415

        d = dict(src_dict)
        end_date = datetime.date.fromisoformat(d.pop("end_date"))

        def _parse_metrics(data: object) -> list[GBPMetricSeries] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                metrics_type_0 = []
                _metrics_type_0 = data
                for metrics_type_0_item_data in _metrics_type_0:
                    metrics_type_0_item = GBPMetricSeries.from_dict(metrics_type_0_item_data)

                    metrics_type_0.append(metrics_type_0_item)

                return metrics_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[GBPMetricSeries] | None, data)

        metrics = _parse_metrics(d.pop("metrics"))

        start_date = datetime.date.fromisoformat(d.pop("start_date"))

        gbp_insights = cls(
            end_date=end_date,
            metrics=metrics,
            start_date=start_date,
        )

        gbp_insights.additional_properties = d
        return gbp_insights

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
