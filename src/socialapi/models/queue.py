from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.slot import Slot


T = TypeVar("T", bound="Queue")


@_attrs_define
class Queue:
    """
    Attributes:
        active (bool): False when the Queue is paused: no new post can join it. Example: True.
        brand_id (str): ID of the Brand the Queue belongs to.
        created_at (datetime.datetime): When the Queue was created.
        id (str): Queue ID. Example: que_01J9Z8Y7X6W5V4T3S2R1Q0P9N8.
        is_default (bool): True for the Brand's default Queue, the one queue_id "default" refers to. Example: True.
        name (str): Queue name. Example: Evenings.
        slots (list[Slot] | None): Weekly posting times, sorted by day (Monday first) then time.
        timezone (str): IANA timezone the slots are expressed in. Example: Europe/Paris.
        updated_at (datetime.datetime): When the Queue was last changed.
    """

    active: bool
    brand_id: str
    created_at: datetime.datetime
    id: str
    is_default: bool
    name: str
    slots: list[Slot] | None
    timezone: str
    updated_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        active = self.active

        brand_id = self.brand_id

        created_at = self.created_at.isoformat()

        id = self.id

        is_default = self.is_default

        name = self.name

        slots: list[dict[str, Any]] | None
        if isinstance(self.slots, list):
            slots = []
            for slots_type_0_item_data in self.slots:
                slots_type_0_item = slots_type_0_item_data.to_dict()
                slots.append(slots_type_0_item)

        else:
            slots = self.slots

        timezone = self.timezone

        updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "active": active,
                "brand_id": brand_id,
                "created_at": created_at,
                "id": id,
                "is_default": is_default,
                "name": name,
                "slots": slots,
                "timezone": timezone,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.slot import Slot  # noqa: PLC0415

        d = dict(src_dict)
        active = d.pop("active")

        brand_id = d.pop("brand_id")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        id = d.pop("id")

        is_default = d.pop("is_default")

        name = d.pop("name")

        def _parse_slots(data: object) -> list[Slot] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                slots_type_0 = []
                _slots_type_0 = data
                for slots_type_0_item_data in _slots_type_0:
                    slots_type_0_item = Slot.from_dict(slots_type_0_item_data)

                    slots_type_0.append(slots_type_0_item)

                return slots_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Slot] | None, data)

        slots = _parse_slots(d.pop("slots"))

        timezone = d.pop("timezone")

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        queue = cls(
            active=active,
            brand_id=brand_id,
            created_at=created_at,
            id=id,
            is_default=is_default,
            name=name,
            slots=slots,
            timezone=timezone,
            updated_at=updated_at,
        )

        queue.additional_properties = d
        return queue

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
