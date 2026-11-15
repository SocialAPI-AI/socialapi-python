from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.social_api_ai_core_api_service_metric_series import SocialApiAiCoreApiServiceMetricSeries


T = TypeVar("T", bound="SocialApiAiCoreApiServiceAnalyticsResponse")


@_attrs_define
class SocialApiAiCoreApiServiceAnalyticsResponse:
    """
    Attributes:
        from_ (str | Unset): From and To are the resolved range, echoed so a caller that named neither
            knows what it got. Example: 2026-08-21.
        series (list[SocialApiAiCoreApiServiceMetricSeries] | Unset):
        to (str | Unset):  Example: 2026-09-19.
    """

    from_: str | Unset = UNSET
    series: list[SocialApiAiCoreApiServiceMetricSeries] | Unset = UNSET
    to: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from_ = self.from_

        series: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.series, Unset):
            series = []
            for series_item_data in self.series:
                series_item = series_item_data.to_dict()
                series.append(series_item)

        to = self.to

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if from_ is not UNSET:
            field_dict["from"] = from_
        if series is not UNSET:
            field_dict["series"] = series
        if to is not UNSET:
            field_dict["to"] = to

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.social_api_ai_core_api_service_metric_series import (
            SocialApiAiCoreApiServiceMetricSeries,  # noqa: PLC0415
        )

        d = dict(src_dict)
        from_ = d.pop("from", UNSET)

        _series = d.pop("series", UNSET)
        series: list[SocialApiAiCoreApiServiceMetricSeries] | Unset = UNSET
        if _series is not UNSET:
            series = []
            for series_item_data in _series:
                series_item = SocialApiAiCoreApiServiceMetricSeries.from_dict(series_item_data)

                series.append(series_item)

        to = d.pop("to", UNSET)

        social_api_ai_core_api_service_analytics_response = cls(
            from_=from_,
            series=series,
            to=to,
        )

        social_api_ai_core_api_service_analytics_response.additional_properties = d
        return social_api_ai_core_api_service_analytics_response

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
