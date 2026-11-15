from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GBPTimePeriod")


@_attrs_define
class GBPTimePeriod:
    """
    Attributes:
        close_day (str | Unset):  Example: MONDAY.
        close_time (str | Unset):  Example: 17:30.
        open_day (str | Unset):  Example: MONDAY.
        open_time (str | Unset):  Example: 09:00.
    """

    close_day: str | Unset = UNSET
    close_time: str | Unset = UNSET
    open_day: str | Unset = UNSET
    open_time: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        close_day = self.close_day

        close_time = self.close_time

        open_day = self.open_day

        open_time = self.open_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if close_day is not UNSET:
            field_dict["close_day"] = close_day
        if close_time is not UNSET:
            field_dict["close_time"] = close_time
        if open_day is not UNSET:
            field_dict["open_day"] = open_day
        if open_time is not UNSET:
            field_dict["open_time"] = open_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        close_day = d.pop("close_day", UNSET)

        close_time = d.pop("close_time", UNSET)

        open_day = d.pop("open_day", UNSET)

        open_time = d.pop("open_time", UNSET)

        gbp_time_period = cls(
            close_day=close_day,
            close_time=close_time,
            open_day=open_day,
            open_time=open_time,
        )

        gbp_time_period.additional_properties = d
        return gbp_time_period

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
