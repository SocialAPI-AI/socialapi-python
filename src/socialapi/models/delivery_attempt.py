from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeliveryAttempt")


@_attrs_define
class DeliveryAttempt:
    """
    Attributes:
        attempt_number (int):
        created_at (datetime.datetime):
        duration_ms (int):
        response_body (str):
        status_code (int | None):
        error_message (str | Unset):
    """

    attempt_number: int
    created_at: datetime.datetime
    duration_ms: int
    response_body: str
    status_code: int | None
    error_message: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        attempt_number = self.attempt_number

        created_at = self.created_at.isoformat()

        duration_ms = self.duration_ms

        response_body = self.response_body

        status_code: int | None
        status_code = self.status_code

        error_message = self.error_message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "attempt_number": attempt_number,
                "created_at": created_at,
                "duration_ms": duration_ms,
                "response_body": response_body,
                "status_code": status_code,
            }
        )
        if error_message is not UNSET:
            field_dict["error_message"] = error_message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        attempt_number = d.pop("attempt_number")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        duration_ms = d.pop("duration_ms")

        response_body = d.pop("response_body")

        def _parse_status_code(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        status_code = _parse_status_code(d.pop("status_code"))

        error_message = d.pop("error_message", UNSET)

        delivery_attempt = cls(
            attempt_number=attempt_number,
            created_at=created_at,
            duration_ms=duration_ms,
            response_body=response_body,
            status_code=status_code,
            error_message=error_message,
        )

        delivery_attempt.additional_properties = d
        return delivery_attempt

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
