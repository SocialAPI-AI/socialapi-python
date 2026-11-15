from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.social_api_ai_core_api_service_delivery_attempt import SocialApiAiCoreApiServiceDeliveryAttempt


T = TypeVar("T", bound="ApiEndpointsDeliveryDetailResponse")


@_attrs_define
class ApiEndpointsDeliveryDetailResponse:
    """
    Attributes:
        attempt_count (int | Unset):
        attempts (list[SocialApiAiCoreApiServiceDeliveryAttempt] | Unset):
        created_at (str | Unset):
        description (str | Unset):
        endpoint_id (str | Unset):
        event_type (str | Unset):
        id (str | Unset):
        payload (list[int] | Unset):
        response_duration_ms (int | Unset):
        response_status_code (int | Unset):
        status (str | Unset):
    """

    attempt_count: int | Unset = UNSET
    attempts: list[SocialApiAiCoreApiServiceDeliveryAttempt] | Unset = UNSET
    created_at: str | Unset = UNSET
    description: str | Unset = UNSET
    endpoint_id: str | Unset = UNSET
    event_type: str | Unset = UNSET
    id: str | Unset = UNSET
    payload: list[int] | Unset = UNSET
    response_duration_ms: int | Unset = UNSET
    response_status_code: int | Unset = UNSET
    status: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        attempt_count = self.attempt_count

        attempts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.attempts, Unset):
            attempts = []
            for attempts_item_data in self.attempts:
                attempts_item = attempts_item_data.to_dict()
                attempts.append(attempts_item)

        created_at = self.created_at

        description = self.description

        endpoint_id = self.endpoint_id

        event_type = self.event_type

        id = self.id

        payload: list[int] | Unset = UNSET
        if not isinstance(self.payload, Unset):
            payload = self.payload

        response_duration_ms = self.response_duration_ms

        response_status_code = self.response_status_code

        status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if attempt_count is not UNSET:
            field_dict["attempt_count"] = attempt_count
        if attempts is not UNSET:
            field_dict["attempts"] = attempts
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if description is not UNSET:
            field_dict["description"] = description
        if endpoint_id is not UNSET:
            field_dict["endpoint_id"] = endpoint_id
        if event_type is not UNSET:
            field_dict["event_type"] = event_type
        if id is not UNSET:
            field_dict["id"] = id
        if payload is not UNSET:
            field_dict["payload"] = payload
        if response_duration_ms is not UNSET:
            field_dict["response_duration_ms"] = response_duration_ms
        if response_status_code is not UNSET:
            field_dict["response_status_code"] = response_status_code
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.social_api_ai_core_api_service_delivery_attempt import (
            SocialApiAiCoreApiServiceDeliveryAttempt,  # noqa: PLC0415
        )

        d = dict(src_dict)
        attempt_count = d.pop("attempt_count", UNSET)

        _attempts = d.pop("attempts", UNSET)
        attempts: list[SocialApiAiCoreApiServiceDeliveryAttempt] | Unset = UNSET
        if _attempts is not UNSET:
            attempts = []
            for attempts_item_data in _attempts:
                attempts_item = SocialApiAiCoreApiServiceDeliveryAttempt.from_dict(attempts_item_data)

                attempts.append(attempts_item)

        created_at = d.pop("created_at", UNSET)

        description = d.pop("description", UNSET)

        endpoint_id = d.pop("endpoint_id", UNSET)

        event_type = d.pop("event_type", UNSET)

        id = d.pop("id", UNSET)

        payload = cast(list[int], d.pop("payload", UNSET))

        response_duration_ms = d.pop("response_duration_ms", UNSET)

        response_status_code = d.pop("response_status_code", UNSET)

        status = d.pop("status", UNSET)

        api_endpoints_delivery_detail_response = cls(
            attempt_count=attempt_count,
            attempts=attempts,
            created_at=created_at,
            description=description,
            endpoint_id=endpoint_id,
            event_type=event_type,
            id=id,
            payload=payload,
            response_duration_ms=response_duration_ms,
            response_status_code=response_status_code,
            status=status,
        )

        api_endpoints_delivery_detail_response.additional_properties = d
        return api_endpoints_delivery_detail_response

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
