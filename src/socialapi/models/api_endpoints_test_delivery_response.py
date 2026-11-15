from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiEndpointsTestDeliveryResponse")


@_attrs_define
class ApiEndpointsTestDeliveryResponse:
    """
    Attributes:
        delivery_id (str | Unset):
        response_body (str | Unset):
        response_duration_ms (int | Unset):
        response_status_code (int | Unset):
        status (str | Unset):
    """

    delivery_id: str | Unset = UNSET
    response_body: str | Unset = UNSET
    response_duration_ms: int | Unset = UNSET
    response_status_code: int | Unset = UNSET
    status: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        delivery_id = self.delivery_id

        response_body = self.response_body

        response_duration_ms = self.response_duration_ms

        response_status_code = self.response_status_code

        status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if delivery_id is not UNSET:
            field_dict["delivery_id"] = delivery_id
        if response_body is not UNSET:
            field_dict["response_body"] = response_body
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
        delivery_id = d.pop("delivery_id", UNSET)

        response_body = d.pop("response_body", UNSET)

        response_duration_ms = d.pop("response_duration_ms", UNSET)

        response_status_code = d.pop("response_status_code", UNSET)

        status = d.pop("status", UNSET)

        api_endpoints_test_delivery_response = cls(
            delivery_id=delivery_id,
            response_body=response_body,
            response_duration_ms=response_duration_ms,
            response_status_code=response_status_code,
            status=status,
        )

        api_endpoints_test_delivery_response.additional_properties = d
        return api_endpoints_test_delivery_response

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
