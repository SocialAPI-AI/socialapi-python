from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.social_api_ai_core_api_connectors_base_threads_breakdown_result import (
        SocialApiAiCoreApiConnectorsBaseThreadsBreakdownResult,
    )
    from ..models.social_api_ai_core_api_connectors_base_threads_time_series_point import (
        SocialApiAiCoreApiConnectorsBaseThreadsTimeSeriesPoint,
    )


T = TypeVar("T", bound="SocialApiAiCoreApiConnectorsBaseThreadsMetricValue")


@_attrs_define
class SocialApiAiCoreApiConnectorsBaseThreadsMetricValue:
    """
    Attributes:
        breakdown (list[SocialApiAiCoreApiConnectorsBaseThreadsBreakdownResult] | Unset): Breakdown is set only for
            follower_demographics.
        value (int | Unset):
        values (list[SocialApiAiCoreApiConnectorsBaseThreadsTimeSeriesPoint] | Unset):
    """

    breakdown: list[SocialApiAiCoreApiConnectorsBaseThreadsBreakdownResult] | Unset = UNSET
    value: int | Unset = UNSET
    values: list[SocialApiAiCoreApiConnectorsBaseThreadsTimeSeriesPoint] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        breakdown: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.breakdown, Unset):
            breakdown = []
            for breakdown_item_data in self.breakdown:
                breakdown_item = breakdown_item_data.to_dict()
                breakdown.append(breakdown_item)

        value = self.value

        values: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.values, Unset):
            values = []
            for values_item_data in self.values:
                values_item = values_item_data.to_dict()
                values.append(values_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if breakdown is not UNSET:
            field_dict["breakdown"] = breakdown
        if value is not UNSET:
            field_dict["value"] = value
        if values is not UNSET:
            field_dict["values"] = values

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.social_api_ai_core_api_connectors_base_threads_breakdown_result import (
            SocialApiAiCoreApiConnectorsBaseThreadsBreakdownResult,  # noqa: PLC0415
        )
        from ..models.social_api_ai_core_api_connectors_base_threads_time_series_point import (
            SocialApiAiCoreApiConnectorsBaseThreadsTimeSeriesPoint,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _breakdown = d.pop("breakdown", UNSET)
        breakdown: list[SocialApiAiCoreApiConnectorsBaseThreadsBreakdownResult] | Unset = UNSET
        if _breakdown is not UNSET:
            breakdown = []
            for breakdown_item_data in _breakdown:
                breakdown_item = SocialApiAiCoreApiConnectorsBaseThreadsBreakdownResult.from_dict(breakdown_item_data)

                breakdown.append(breakdown_item)

        value = d.pop("value", UNSET)

        _values = d.pop("values", UNSET)
        values: list[SocialApiAiCoreApiConnectorsBaseThreadsTimeSeriesPoint] | Unset = UNSET
        if _values is not UNSET:
            values = []
            for values_item_data in _values:
                values_item = SocialApiAiCoreApiConnectorsBaseThreadsTimeSeriesPoint.from_dict(values_item_data)

                values.append(values_item)

        social_api_ai_core_api_connectors_base_threads_metric_value = cls(
            breakdown=breakdown,
            value=value,
            values=values,
        )

        social_api_ai_core_api_connectors_base_threads_metric_value.additional_properties = d
        return social_api_ai_core_api_connectors_base_threads_metric_value

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
