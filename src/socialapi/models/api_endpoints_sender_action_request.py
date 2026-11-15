from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.api_endpoints_sender_action_request_action import ApiEndpointsSenderActionRequestAction

T = TypeVar("T", bound="ApiEndpointsSenderActionRequest")


@_attrs_define
class ApiEndpointsSenderActionRequest:
    """
    Attributes:
        account_id (str): Connected account ID that owns the conversation. Example: acc_01HZ9X3Q4R5M6N7P8V2K0W1J.
        action (ApiEndpointsSenderActionRequestAction): What to show the other participant: typing_on, typing_off, or
            mark_seen. Example: typing_on.
    """

    account_id: str
    action: ApiEndpointsSenderActionRequestAction
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_id = self.account_id

        action = self.action.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "account_id": account_id,
                "action": action,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_id = d.pop("account_id")

        action = ApiEndpointsSenderActionRequestAction(d.pop("action"))

        api_endpoints_sender_action_request = cls(
            account_id=account_id,
            action=action,
        )

        api_endpoints_sender_action_request.additional_properties = d
        return api_endpoints_sender_action_request

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
