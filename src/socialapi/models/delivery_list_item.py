from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DeliveryListItem")


@_attrs_define
class DeliveryListItem:
    """
    Attributes:
        attempt_count (int):
        created_at (datetime.datetime):
        description (str):
        event_type (str):
        id (str):
        response_duration_ms (int | None):
        response_status_code (int | None):
        status (str):
    """

    attempt_count: int
    created_at: datetime.datetime
    description: str
    event_type: str
    id: str
    response_duration_ms: int | None
    response_status_code: int | None
    status: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        attempt_count = self.attempt_count

        created_at = self.created_at.isoformat()

        description = self.description

        event_type = self.event_type

        id = self.id

        response_duration_ms: int | None
        response_duration_ms = self.response_duration_ms

        response_status_code: int | None
        response_status_code = self.response_status_code

        status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "attempt_count": attempt_count,
                "created_at": created_at,
                "description": description,
                "event_type": event_type,
                "id": id,
                "response_duration_ms": response_duration_ms,
                "response_status_code": response_status_code,
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        attempt_count = d.pop("attempt_count")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        description = d.pop("description")

        event_type = d.pop("event_type")

        id = d.pop("id")

        def _parse_response_duration_ms(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        response_duration_ms = _parse_response_duration_ms(d.pop("response_duration_ms"))

        def _parse_response_status_code(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        response_status_code = _parse_response_status_code(d.pop("response_status_code"))

        status = d.pop("status")

        delivery_list_item = cls(
            attempt_count=attempt_count,
            created_at=created_at,
            description=description,
            event_type=event_type,
            id=id,
            response_duration_ms=response_duration_ms,
            response_status_code=response_status_code,
            status=status,
        )

        delivery_list_item.additional_properties = d
        return delivery_list_item

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
