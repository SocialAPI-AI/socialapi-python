from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.social_api_ai_core_api_connectors_base_threads_metric_value import (
        SocialApiAiCoreApiConnectorsBaseThreadsMetricValue,
    )


T = TypeVar("T", bound="SocialApiAiCoreApiConnectorsBaseThreadsInsightsMetrics")


@_attrs_define
class SocialApiAiCoreApiConnectorsBaseThreadsInsightsMetrics:
    additional_properties: dict[str, SocialApiAiCoreApiConnectorsBaseThreadsMetricValue] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.social_api_ai_core_api_connectors_base_threads_metric_value import (
            SocialApiAiCoreApiConnectorsBaseThreadsMetricValue,  # noqa: PLC0415
        )

        d = dict(src_dict)
        social_api_ai_core_api_connectors_base_threads_insights_metrics = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = SocialApiAiCoreApiConnectorsBaseThreadsMetricValue.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        social_api_ai_core_api_connectors_base_threads_insights_metrics.additional_properties = additional_properties
        return social_api_ai_core_api_connectors_base_threads_insights_metrics

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> SocialApiAiCoreApiConnectorsBaseThreadsMetricValue:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: SocialApiAiCoreApiConnectorsBaseThreadsMetricValue) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
