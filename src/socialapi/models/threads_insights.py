from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.threads_insights_metrics_type_0 import ThreadsInsightsMetricsType0


T = TypeVar("T", bound="ThreadsInsights")


@_attrs_define
class ThreadsInsights:
    """
    Attributes:
        metrics (None | ThreadsInsightsMetricsType0):
    """

    metrics: None | ThreadsInsightsMetricsType0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.threads_insights_metrics_type_0 import ThreadsInsightsMetricsType0  # noqa: PLC0415

        metrics: dict[str, Any] | None
        if isinstance(self.metrics, ThreadsInsightsMetricsType0):
            metrics = self.metrics.to_dict()
        else:
            metrics = self.metrics

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "metrics": metrics,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.threads_insights_metrics_type_0 import ThreadsInsightsMetricsType0  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_metrics(data: object) -> None | ThreadsInsightsMetricsType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metrics_type_0 = ThreadsInsightsMetricsType0.from_dict(data)

                return metrics_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ThreadsInsightsMetricsType0, data)

        metrics = _parse_metrics(d.pop("metrics"))

        threads_insights = cls(
            metrics=metrics,
        )

        threads_insights.additional_properties = d
        return threads_insights

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
