from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SocialApiAiCoreApiServiceDeliveryListItem")


@_attrs_define
class SocialApiAiCoreApiServiceDeliveryListItem:
    """
    Attributes:
        attempt_count (int | Unset):
        created_at (str | Unset):
        description (str | Unset):
        event_type (str | Unset):
        id (str | Unset):
        response_duration_ms (int | Unset):
        response_status_code (int | Unset):
        status (str | Unset):
    """

    attempt_count: int | Unset = UNSET
    created_at: str | Unset = UNSET
    description: str | Unset = UNSET
    event_type: str | Unset = UNSET
    id: str | Unset = UNSET
    response_duration_ms: int | Unset = UNSET
    response_status_code: int | Unset = UNSET
    status: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        attempt_count = self.attempt_count

        created_at = self.created_at

        description = self.description

        event_type = self.event_type

        id = self.id

        response_duration_ms = self.response_duration_ms

        response_status_code = self.response_status_code

        status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if attempt_count is not UNSET:
            field_dict["attempt_count"] = attempt_count
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if description is not UNSET:
            field_dict["description"] = description
        if event_type is not UNSET:
            field_dict["event_type"] = event_type
        if id is not UNSET:
            field_dict["id"] = id
        if response_duration_ms is not UNSET:
            field_dict["response_duration_ms"] = response_duration_ms
        if response_status_code is not UNSET:
            field_dict["response_status_code"] = response_status_code
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        attempt_count = d.pop("attempt_count", UNSET)

        created_at = d.pop("created_at", UNSET)

        description = d.pop("description", UNSET)

        event_type = d.pop("event_type", UNSET)

        id = d.pop("id", UNSET)

        response_duration_ms = d.pop("response_duration_ms", UNSET)

        response_status_code = d.pop("response_status_code", UNSET)

        status = d.pop("status", UNSET)

        social_api_ai_core_api_service_delivery_list_item = cls(
            attempt_count=attempt_count,
            created_at=created_at,
            description=description,
            event_type=event_type,
            id=id,
            response_duration_ms=response_duration_ms,
            response_status_code=response_status_code,
            status=status,
        )

        social_api_ai_core_api_service_delivery_list_item.additional_properties = d
        return social_api_ai_core_api_service_delivery_list_item

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
