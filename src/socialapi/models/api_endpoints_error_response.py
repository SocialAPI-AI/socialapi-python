from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_endpoints_error_body import ApiEndpointsErrorBody


T = TypeVar("T", bound="ApiEndpointsErrorResponse")


@_attrs_define
class ApiEndpointsErrorResponse:
    """
    Attributes:
        error (ApiEndpointsErrorBody | Unset):
        request_id (str | Unset): RequestID matches the X-Request-ID response header. Include it when contacting
            support. Example: 01HZ9X3Q4R5M6N7P8V2K0W1J.
    """

    error: ApiEndpointsErrorBody | Unset = UNSET
    request_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        error: dict[str, Any] | Unset = UNSET
        if not isinstance(self.error, Unset):
            error = self.error.to_dict()

        request_id = self.request_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if error is not UNSET:
            field_dict["error"] = error
        if request_id is not UNSET:
            field_dict["request_id"] = request_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_endpoints_error_body import ApiEndpointsErrorBody  # noqa: PLC0415

        d = dict(src_dict)
        _error = d.pop("error", UNSET)
        error: ApiEndpointsErrorBody | Unset
        if isinstance(_error, Unset):
            error = UNSET
        else:
            error = ApiEndpointsErrorBody.from_dict(_error)

        request_id = d.pop("request_id", UNSET)

        api_endpoints_error_response = cls(
            error=error,
            request_id=request_id,
        )

        api_endpoints_error_response.additional_properties = d
        return api_endpoints_error_response

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
