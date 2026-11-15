from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="QueuedTime")


@_attrs_define
class QueuedTime:
    """
    Attributes:
        day (str): Lowercase English weekday name. Example: tuesday.
        slot_time (str): The slot's time of day as HH:MM. Example: 19:00.
        time (str): The time as RFC 3339 with the Queue's local offset. Example: 2026-10-20T19:00:00+02:00.
    """

    day: str
    slot_time: str
    time: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        day = self.day

        slot_time = self.slot_time

        time = self.time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "day": day,
                "slot_time": slot_time,
                "time": time,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        day = d.pop("day")

        slot_time = d.pop("slot_time")

        time = d.pop("time")

        queued_time = cls(
            day=day,
            slot_time=slot_time,
            time=time,
        )

        queued_time.additional_properties = d
        return queued_time

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
