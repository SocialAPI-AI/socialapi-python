from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.social_api_ai_core_api_connectors_base_gbp_time_period import (
        SocialApiAiCoreApiConnectorsBaseGBPTimePeriod,
    )


T = TypeVar("T", bound="SocialApiAiCoreApiConnectorsBaseGBPHoursUpdate")


@_attrs_define
class SocialApiAiCoreApiConnectorsBaseGBPHoursUpdate:
    """
    Attributes:
        periods (list[SocialApiAiCoreApiConnectorsBaseGBPTimePeriod] | Unset):
    """

    periods: list[SocialApiAiCoreApiConnectorsBaseGBPTimePeriod] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        periods: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.periods, Unset):
            periods = []
            for periods_item_data in self.periods:
                periods_item = periods_item_data.to_dict()
                periods.append(periods_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if periods is not UNSET:
            field_dict["periods"] = periods

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.social_api_ai_core_api_connectors_base_gbp_time_period import (
            SocialApiAiCoreApiConnectorsBaseGBPTimePeriod,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _periods = d.pop("periods", UNSET)
        periods: list[SocialApiAiCoreApiConnectorsBaseGBPTimePeriod] | Unset = UNSET
        if _periods is not UNSET:
            periods = []
            for periods_item_data in _periods:
                periods_item = SocialApiAiCoreApiConnectorsBaseGBPTimePeriod.from_dict(periods_item_data)

                periods.append(periods_item)

        social_api_ai_core_api_connectors_base_gbp_hours_update = cls(
            periods=periods,
        )

        social_api_ai_core_api_connectors_base_gbp_hours_update.additional_properties = d
        return social_api_ai_core_api_connectors_base_gbp_hours_update

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
