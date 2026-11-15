from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.delivery_attempt import DeliveryAttempt
    from ..models.delivery_detail_response_payload_type_0 import DeliveryDetailResponsePayloadType0


T = TypeVar("T", bound="DeliveryDetailResponse")


@_attrs_define
class DeliveryDetailResponse:
    """
    Attributes:
        attempt_count (int):
        attempts (list[DeliveryAttempt]):
        created_at (datetime.datetime):
        description (str):
        endpoint_id (str):
        event_type (str):
        id (str):
        payload (DeliveryDetailResponsePayloadType0 | None):
        response_duration_ms (int | None):
        response_status_code (int | None):
        status (str):
    """

    attempt_count: int
    attempts: list[DeliveryAttempt]
    created_at: datetime.datetime
    description: str
    endpoint_id: str
    event_type: str
    id: str
    payload: DeliveryDetailResponsePayloadType0 | None
    response_duration_ms: int | None
    response_status_code: int | None
    status: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.delivery_detail_response_payload_type_0 import DeliveryDetailResponsePayloadType0  # noqa: PLC0415

        attempt_count = self.attempt_count

        attempts = []
        for attempts_item_data in self.attempts:
            attempts_item = attempts_item_data.to_dict()
            attempts.append(attempts_item)

        created_at = self.created_at.isoformat()

        description = self.description

        endpoint_id = self.endpoint_id

        event_type = self.event_type

        id = self.id

        payload: dict[str, Any] | None
        if isinstance(self.payload, DeliveryDetailResponsePayloadType0):
            payload = self.payload.to_dict()
        else:
            payload = self.payload

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
                "attempts": attempts,
                "created_at": created_at,
                "description": description,
                "endpoint_id": endpoint_id,
                "event_type": event_type,
                "id": id,
                "payload": payload,
                "response_duration_ms": response_duration_ms,
                "response_status_code": response_status_code,
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.delivery_attempt import DeliveryAttempt  # noqa: PLC0415
        from ..models.delivery_detail_response_payload_type_0 import DeliveryDetailResponsePayloadType0  # noqa: PLC0415

        d = dict(src_dict)
        attempt_count = d.pop("attempt_count")

        attempts = []
        _attempts = d.pop("attempts")
        for attempts_item_data in _attempts:
            attempts_item = DeliveryAttempt.from_dict(attempts_item_data)

            attempts.append(attempts_item)

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        description = d.pop("description")

        endpoint_id = d.pop("endpoint_id")

        event_type = d.pop("event_type")

        id = d.pop("id")

        def _parse_payload(data: object) -> DeliveryDetailResponsePayloadType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                payload_type_0 = DeliveryDetailResponsePayloadType0.from_dict(data)

                return payload_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DeliveryDetailResponsePayloadType0 | None, data)

        payload = _parse_payload(d.pop("payload"))

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

        delivery_detail_response = cls(
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

        delivery_detail_response.additional_properties = d
        return delivery_detail_response

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
