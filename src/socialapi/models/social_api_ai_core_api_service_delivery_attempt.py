from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SocialApiAiCoreApiServiceDeliveryAttempt")


@_attrs_define
class SocialApiAiCoreApiServiceDeliveryAttempt:
    """
    Attributes:
        attempt_number (int | Unset):
        created_at (str | Unset):
        duration_ms (int | Unset):
        error_message (str | Unset):
        response_body (str | Unset):
        status_code (int | Unset):
    """

    attempt_number: int | Unset = UNSET
    created_at: str | Unset = UNSET
    duration_ms: int | Unset = UNSET
    error_message: str | Unset = UNSET
    response_body: str | Unset = UNSET
    status_code: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        attempt_number = self.attempt_number

        created_at = self.created_at

        duration_ms = self.duration_ms

        error_message = self.error_message

        response_body = self.response_body

        status_code = self.status_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if attempt_number is not UNSET:
            field_dict["attempt_number"] = attempt_number
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if duration_ms is not UNSET:
            field_dict["duration_ms"] = duration_ms
        if error_message is not UNSET:
            field_dict["error_message"] = error_message
        if response_body is not UNSET:
            field_dict["response_body"] = response_body
        if status_code is not UNSET:
            field_dict["status_code"] = status_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        attempt_number = d.pop("attempt_number", UNSET)

        created_at = d.pop("created_at", UNSET)

        duration_ms = d.pop("duration_ms", UNSET)

        error_message = d.pop("error_message", UNSET)

        response_body = d.pop("response_body", UNSET)

        status_code = d.pop("status_code", UNSET)

        social_api_ai_core_api_service_delivery_attempt = cls(
            attempt_number=attempt_number,
            created_at=created_at,
            duration_ms=duration_ms,
            error_message=error_message,
            response_body=response_body,
            status_code=status_code,
        )

        social_api_ai_core_api_service_delivery_attempt.additional_properties = d
        return social_api_ai_core_api_service_delivery_attempt

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
