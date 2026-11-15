from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.api_endpoints_update_conversation_request_status import ApiEndpointsUpdateConversationRequestStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiEndpointsUpdateConversationRequest")


@_attrs_define
class ApiEndpointsUpdateConversationRequest:
    """
    Attributes:
        status (ApiEndpointsUpdateConversationRequestStatus | Unset): Status must be "active" or "archived". Example:
            archived.
    """

    status: ApiEndpointsUpdateConversationRequestStatus | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _status = d.pop("status", UNSET)
        status: ApiEndpointsUpdateConversationRequestStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ApiEndpointsUpdateConversationRequestStatus(_status)

        api_endpoints_update_conversation_request = cls(
            status=status,
        )

        api_endpoints_update_conversation_request.additional_properties = d
        return api_endpoints_update_conversation_request

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
