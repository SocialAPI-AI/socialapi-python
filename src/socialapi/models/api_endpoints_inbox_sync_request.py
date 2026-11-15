from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiEndpointsInboxSyncRequest")


@_attrs_define
class ApiEndpointsInboxSyncRequest:
    """
    Attributes:
        account_id (str | Unset):  Example: acc_01H....
        conversation_id (str | Unset):  Example: 6f1c....
    """

    account_id: str | Unset = UNSET
    conversation_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_id = self.account_id

        conversation_id = self.conversation_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_id is not UNSET:
            field_dict["account_id"] = account_id
        if conversation_id is not UNSET:
            field_dict["conversation_id"] = conversation_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_id = d.pop("account_id", UNSET)

        conversation_id = d.pop("conversation_id", UNSET)

        api_endpoints_inbox_sync_request = cls(
            account_id=account_id,
            conversation_id=conversation_id,
        )

        api_endpoints_inbox_sync_request.additional_properties = d
        return api_endpoints_inbox_sync_request

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
