from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SocialApiAiCoreApiServiceQueuedTime")


@_attrs_define
class SocialApiAiCoreApiServiceQueuedTime:
    """
    Attributes:
        day (str | Unset): Lowercase English weekday name. Example: tuesday.
        slot_time (str | Unset): The slot's time of day as HH:MM. Example: 19:00.
        time (str | Unset): The time as RFC 3339 with the Queue's local offset. Example: 2026-10-20T19:00:00+02:00.
    """

    day: str | Unset = UNSET
    slot_time: str | Unset = UNSET
    time: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        day = self.day

        slot_time = self.slot_time

        time = self.time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if day is not UNSET:
            field_dict["day"] = day
        if slot_time is not UNSET:
            field_dict["slot_time"] = slot_time
        if time is not UNSET:
            field_dict["time"] = time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        day = d.pop("day", UNSET)

        slot_time = d.pop("slot_time", UNSET)

        time = d.pop("time", UNSET)

        social_api_ai_core_api_service_queued_time = cls(
            day=day,
            slot_time=slot_time,
            time=time,
        )

        social_api_ai_core_api_service_queued_time.additional_properties = d
        return social_api_ai_core_api_service_queued_time

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
