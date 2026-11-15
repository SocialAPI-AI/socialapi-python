from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.slot import Slot


T = TypeVar("T", bound="CreateQueueParams")


@_attrs_define
class CreateQueueParams:
    """
    Attributes:
        brand_id (str): ID of the Brand to create the Queue on. Required.
        name (str): Queue name. Required. Example: Evenings.
        slots (list[Slot]): Weekly posting times, 1 to 100. Required.
        timezone (str): IANA timezone the slots are expressed in. Required. Example: Europe/Paris.
        active (bool | Unset): Set false to create the Queue paused. Defaults to true. Example: True.
        is_default (bool | Unset): Set true to make this the Brand's default Queue. The Brand's first Queue is always
            the default. Example: False.
    """

    brand_id: str
    name: str
    slots: list[Slot]
    timezone: str
    active: bool | Unset = UNSET
    is_default: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        brand_id = self.brand_id

        name = self.name

        slots = []
        for slots_item_data in self.slots:
            slots_item = slots_item_data.to_dict()
            slots.append(slots_item)

        timezone = self.timezone

        active = self.active

        is_default = self.is_default

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "brand_id": brand_id,
                "name": name,
                "slots": slots,
                "timezone": timezone,
            }
        )
        if active is not UNSET:
            field_dict["active"] = active
        if is_default is not UNSET:
            field_dict["is_default"] = is_default

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.slot import Slot  # noqa: PLC0415

        d = dict(src_dict)
        brand_id = d.pop("brand_id")

        name = d.pop("name")

        slots = []
        _slots = d.pop("slots")
        for slots_item_data in _slots:
            slots_item = Slot.from_dict(slots_item_data)

            slots.append(slots_item)

        timezone = d.pop("timezone")

        active = d.pop("active", UNSET)

        is_default = d.pop("is_default", UNSET)

        create_queue_params = cls(
            brand_id=brand_id,
            name=name,
            slots=slots,
            timezone=timezone,
            active=active,
            is_default=is_default,
        )

        create_queue_params.additional_properties = d
        return create_queue_params

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
