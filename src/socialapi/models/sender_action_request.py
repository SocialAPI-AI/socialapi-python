from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.sender_action import SenderAction

T = TypeVar("T", bound="SenderActionRequest")


@_attrs_define
class SenderActionRequest:
    """
    Attributes:
        account_id (str): Connected account ID that owns the conversation. Example: acc_01HZ9X3Q4R5M6N7P8V2K0W1J.
        action (SenderAction):
    """

    account_id: str
    action: SenderAction
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

        action = SenderAction(d.pop("action"))

        sender_action_request = cls(
            account_id=account_id,
            action=action,
        )

        sender_action_request.additional_properties = d
        return sender_action_request

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
