from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.social_api_ai_core_api_service_slot import SocialApiAiCoreApiServiceSlot


T = TypeVar("T", bound="ApiEndpointsUpdateQueueResponse")


@_attrs_define
class ApiEndpointsUpdateQueueResponse:
    """
    Attributes:
        active (bool | Unset): False when the Queue is paused: no new post can join it. Example: True.
        brand_id (str | Unset): ID of the Brand the Queue belongs to.
        created_at (str | Unset): When the Queue was created.
        id (str | Unset): Queue ID. Example: que_01J9Z8Y7X6W5V4T3S2R1Q0P9N8.
        is_default (bool | Unset): True for the Brand's default Queue, the one queue_id "default" refers to. Example:
            True.
        name (str | Unset): Queue name. Example: Evenings.
        reshuffled_count (int | Unset): Number of queued posts moved to the new times. Present only when the request
            sent reshuffle_existing: true.
        slots (list[SocialApiAiCoreApiServiceSlot] | Unset): Weekly posting times, sorted by day (Monday first) then
            time.
        timezone (str | Unset): IANA timezone the slots are expressed in. Example: Europe/Paris.
        updated_at (str | Unset): When the Queue was last changed.
    """

    active: bool | Unset = UNSET
    brand_id: str | Unset = UNSET
    created_at: str | Unset = UNSET
    id: str | Unset = UNSET
    is_default: bool | Unset = UNSET
    name: str | Unset = UNSET
    reshuffled_count: int | Unset = UNSET
    slots: list[SocialApiAiCoreApiServiceSlot] | Unset = UNSET
    timezone: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        active = self.active

        brand_id = self.brand_id

        created_at = self.created_at

        id = self.id

        is_default = self.is_default

        name = self.name

        reshuffled_count = self.reshuffled_count

        slots: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.slots, Unset):
            slots = []
            for slots_item_data in self.slots:
                slots_item = slots_item_data.to_dict()
                slots.append(slots_item)

        timezone = self.timezone

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if active is not UNSET:
            field_dict["active"] = active
        if brand_id is not UNSET:
            field_dict["brand_id"] = brand_id
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if id is not UNSET:
            field_dict["id"] = id
        if is_default is not UNSET:
            field_dict["is_default"] = is_default
        if name is not UNSET:
            field_dict["name"] = name
        if reshuffled_count is not UNSET:
            field_dict["reshuffled_count"] = reshuffled_count
        if slots is not UNSET:
            field_dict["slots"] = slots
        if timezone is not UNSET:
            field_dict["timezone"] = timezone
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.social_api_ai_core_api_service_slot import SocialApiAiCoreApiServiceSlot  # noqa: PLC0415

        d = dict(src_dict)
        active = d.pop("active", UNSET)

        brand_id = d.pop("brand_id", UNSET)

        created_at = d.pop("created_at", UNSET)

        id = d.pop("id", UNSET)

        is_default = d.pop("is_default", UNSET)

        name = d.pop("name", UNSET)

        reshuffled_count = d.pop("reshuffled_count", UNSET)

        _slots = d.pop("slots", UNSET)
        slots: list[SocialApiAiCoreApiServiceSlot] | Unset = UNSET
        if _slots is not UNSET:
            slots = []
            for slots_item_data in _slots:
                slots_item = SocialApiAiCoreApiServiceSlot.from_dict(slots_item_data)

                slots.append(slots_item)

        timezone = d.pop("timezone", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        api_endpoints_update_queue_response = cls(
            active=active,
            brand_id=brand_id,
            created_at=created_at,
            id=id,
            is_default=is_default,
            name=name,
            reshuffled_count=reshuffled_count,
            slots=slots,
            timezone=timezone,
            updated_at=updated_at,
        )

        api_endpoints_update_queue_response.additional_properties = d
        return api_endpoints_update_queue_response

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
