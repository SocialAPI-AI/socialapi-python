from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.social_api_ai_core_api_connectors_base_threads_insights_metrics import (
        SocialApiAiCoreApiConnectorsBaseThreadsInsightsMetrics,
    )


T = TypeVar("T", bound="SocialApiAiCoreApiConnectorsBaseThreadsInsights")


@_attrs_define
class SocialApiAiCoreApiConnectorsBaseThreadsInsights:
    """
    Attributes:
        metrics (SocialApiAiCoreApiConnectorsBaseThreadsInsightsMetrics | Unset):
    """

    metrics: SocialApiAiCoreApiConnectorsBaseThreadsInsightsMetrics | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        metrics: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metrics, Unset):
            metrics = self.metrics.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if metrics is not UNSET:
            field_dict["metrics"] = metrics

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.social_api_ai_core_api_connectors_base_threads_insights_metrics import (
            SocialApiAiCoreApiConnectorsBaseThreadsInsightsMetrics,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _metrics = d.pop("metrics", UNSET)
        metrics: SocialApiAiCoreApiConnectorsBaseThreadsInsightsMetrics | Unset
        if isinstance(_metrics, Unset):
            metrics = UNSET
        else:
            metrics = SocialApiAiCoreApiConnectorsBaseThreadsInsightsMetrics.from_dict(_metrics)

        social_api_ai_core_api_connectors_base_threads_insights = cls(
            metrics=metrics,
        )

        social_api_ai_core_api_connectors_base_threads_insights.additional_properties = d
        return social_api_ai_core_api_connectors_base_threads_insights

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
