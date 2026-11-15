from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.gbp_time_period import GBPTimePeriod


T = TypeVar("T", bound="GBPMoreHours")


@_attrs_define
class GBPMoreHours:
    """
    Attributes:
        hours_type_id (str | Unset):  Example: DRIVE_THROUGH.
        periods (list[GBPTimePeriod] | Unset):
    """

    hours_type_id: str | Unset = UNSET
    periods: list[GBPTimePeriod] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        hours_type_id = self.hours_type_id

        periods: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.periods, Unset):
            periods = []
            for periods_item_data in self.periods:
                periods_item = periods_item_data.to_dict()
                periods.append(periods_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if hours_type_id is not UNSET:
            field_dict["hours_type_id"] = hours_type_id
        if periods is not UNSET:
            field_dict["periods"] = periods

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.gbp_time_period import GBPTimePeriod  # noqa: PLC0415

        d = dict(src_dict)
        hours_type_id = d.pop("hours_type_id", UNSET)

        _periods = d.pop("periods", UNSET)
        periods: list[GBPTimePeriod] | Unset = UNSET
        if _periods is not UNSET:
            periods = []
            for periods_item_data in _periods:
                periods_item = GBPTimePeriod.from_dict(periods_item_data)

                periods.append(periods_item)

        gbp_more_hours = cls(
            hours_type_id=hours_type_id,
            periods=periods,
        )

        gbp_more_hours.additional_properties = d
        return gbp_more_hours

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
