from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.slot import Slot


T = TypeVar("T", bound="UpdateQueueParams")


@_attrs_define
class UpdateQueueParams:
    """
    Attributes:
        active (bool | Unset): False pauses the Queue, true resumes it. Example: True.
        is_default (bool | Unset): Only true is accepted: it makes this the Brand's default Queue. Example: True.
        name (str | Unset): New name. Example: Evenings.
        reshuffle_existing (bool | Unset): Set true to move the Queue's posts onto the new slots, in their current
            order. The response then carries reshuffled_count. Example: False.
        slots (list[Slot] | Unset): Weekly posting times. Replaces the whole list when sent; omit to keep the current
            list.
        timezone (str | Unset): New IANA timezone. Example: Europe/Paris.
    """

    active: bool | Unset = UNSET
    is_default: bool | Unset = UNSET
    name: str | Unset = UNSET
    reshuffle_existing: bool | Unset = UNSET
    slots: list[Slot] | Unset = UNSET
    timezone: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        active = self.active

        is_default = self.is_default

        name = self.name

        reshuffle_existing = self.reshuffle_existing

        slots: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.slots, Unset):
            slots = []
            for slots_item_data in self.slots:
                slots_item = slots_item_data.to_dict()
                slots.append(slots_item)

        timezone = self.timezone

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if active is not UNSET:
            field_dict["active"] = active
        if is_default is not UNSET:
            field_dict["is_default"] = is_default
        if name is not UNSET:
            field_dict["name"] = name
        if reshuffle_existing is not UNSET:
            field_dict["reshuffle_existing"] = reshuffle_existing
        if slots is not UNSET:
            field_dict["slots"] = slots
        if timezone is not UNSET:
            field_dict["timezone"] = timezone

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.slot import Slot  # noqa: PLC0415

        d = dict(src_dict)
        active = d.pop("active", UNSET)

        is_default = d.pop("is_default", UNSET)

        name = d.pop("name", UNSET)

        reshuffle_existing = d.pop("reshuffle_existing", UNSET)

        _slots = d.pop("slots", UNSET)
        slots: list[Slot] | Unset = UNSET
        if _slots is not UNSET:
            slots = []
            for slots_item_data in _slots:
                slots_item = Slot.from_dict(slots_item_data)

                slots.append(slots_item)

        timezone = d.pop("timezone", UNSET)

        update_queue_params = cls(
            active=active,
            is_default=is_default,
            name=name,
            reshuffle_existing=reshuffle_existing,
            slots=slots,
            timezone=timezone,
        )

        update_queue_params.additional_properties = d
        return update_queue_params

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
