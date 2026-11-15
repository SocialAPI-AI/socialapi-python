from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.social_api_ai_core_api_service_slot_day import SocialApiAiCoreApiServiceSlotDay
from ..types import UNSET, Unset

T = TypeVar("T", bound="SocialApiAiCoreApiServiceSlot")


@_attrs_define
class SocialApiAiCoreApiServiceSlot:
    """
    Attributes:
        day (SocialApiAiCoreApiServiceSlotDay | Unset): Lowercase English weekday name. Example: tuesday.
        time (str | Unset): Time of day as HH:MM, 24-hour, in the Queue's timezone. Example: 19:00.
    """

    day: SocialApiAiCoreApiServiceSlotDay | Unset = UNSET
    time: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        day: str | Unset = UNSET
        if not isinstance(self.day, Unset):
            day = self.day.value

        time = self.time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if day is not UNSET:
            field_dict["day"] = day
        if time is not UNSET:
            field_dict["time"] = time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _day = d.pop("day", UNSET)
        day: SocialApiAiCoreApiServiceSlotDay | Unset
        if isinstance(_day, Unset):
            day = UNSET
        else:
            day = SocialApiAiCoreApiServiceSlotDay(_day)

        time = d.pop("time", UNSET)

        social_api_ai_core_api_service_slot = cls(
            day=day,
            time=time,
        )

        social_api_ai_core_api_service_slot.additional_properties = d
        return social_api_ai_core_api_service_slot

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
