from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GBPSpecialHourPeriod")


@_attrs_define
class GBPSpecialHourPeriod:
    """
    Attributes:
        close_time (str | Unset):
        closed (bool | Unset): Closed marks the location shut for the whole period, in which case the
            times are absent. Absent when Google said nothing.
        end_date (str | Unset):  Example: 2026-12-25.
        open_time (str | Unset):
        start_date (str | Unset):  Example: 2026-12-25.
    """

    close_time: str | Unset = UNSET
    closed: bool | Unset = UNSET
    end_date: str | Unset = UNSET
    open_time: str | Unset = UNSET
    start_date: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        close_time = self.close_time

        closed = self.closed

        end_date = self.end_date

        open_time = self.open_time

        start_date = self.start_date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if close_time is not UNSET:
            field_dict["close_time"] = close_time
        if closed is not UNSET:
            field_dict["closed"] = closed
        if end_date is not UNSET:
            field_dict["end_date"] = end_date
        if open_time is not UNSET:
            field_dict["open_time"] = open_time
        if start_date is not UNSET:
            field_dict["start_date"] = start_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        close_time = d.pop("close_time", UNSET)

        closed = d.pop("closed", UNSET)

        end_date = d.pop("end_date", UNSET)

        open_time = d.pop("open_time", UNSET)

        start_date = d.pop("start_date", UNSET)

        gbp_special_hour_period = cls(
            close_time=close_time,
            closed=closed,
            end_date=end_date,
            open_time=open_time,
            start_date=start_date,
        )

        gbp_special_hour_period.additional_properties = d
        return gbp_special_hour_period

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
