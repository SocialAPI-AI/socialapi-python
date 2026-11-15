from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.social_api_ai_core_api_service_slot import SocialApiAiCoreApiServiceSlot


T = TypeVar("T", bound="SocialApiAiCoreApiServiceCreateQueueParams")


@_attrs_define
class SocialApiAiCoreApiServiceCreateQueueParams:
    """
    Attributes:
        active (bool | Unset): Set false to create the Queue paused. Defaults to true. Example: True.
        brand_id (str | Unset): ID of the Brand to create the Queue on. Required.
        is_default (bool | Unset): Set true to make this the Brand's default Queue. The Brand's first Queue is always
            the default. Example: False.
        name (str | Unset): Queue name. Required. Example: Evenings.
        slots (list[SocialApiAiCoreApiServiceSlot] | Unset): Weekly posting times, 1 to 100. Required.
        timezone (str | Unset): IANA timezone the slots are expressed in. Required. Example: Europe/Paris.
    """

    active: bool | Unset = UNSET
    brand_id: str | Unset = UNSET
    is_default: bool | Unset = UNSET
    name: str | Unset = UNSET
    slots: list[SocialApiAiCoreApiServiceSlot] | Unset = UNSET
    timezone: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        active = self.active

        brand_id = self.brand_id

        is_default = self.is_default

        name = self.name

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
        if brand_id is not UNSET:
            field_dict["brand_id"] = brand_id
        if is_default is not UNSET:
            field_dict["is_default"] = is_default
        if name is not UNSET:
            field_dict["name"] = name
        if slots is not UNSET:
            field_dict["slots"] = slots
        if timezone is not UNSET:
            field_dict["timezone"] = timezone

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.social_api_ai_core_api_service_slot import SocialApiAiCoreApiServiceSlot  # noqa: PLC0415

        d = dict(src_dict)
        active = d.pop("active", UNSET)

        brand_id = d.pop("brand_id", UNSET)

        is_default = d.pop("is_default", UNSET)

        name = d.pop("name", UNSET)

        _slots = d.pop("slots", UNSET)
        slots: list[SocialApiAiCoreApiServiceSlot] | Unset = UNSET
        if _slots is not UNSET:
            slots = []
            for slots_item_data in _slots:
                slots_item = SocialApiAiCoreApiServiceSlot.from_dict(slots_item_data)

                slots.append(slots_item)

        timezone = d.pop("timezone", UNSET)

        social_api_ai_core_api_service_create_queue_params = cls(
            active=active,
            brand_id=brand_id,
            is_default=is_default,
            name=name,
            slots=slots,
            timezone=timezone,
        )

        social_api_ai_core_api_service_create_queue_params.additional_properties = d
        return social_api_ai_core_api_service_create_queue_params

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
