from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SendMessageResponse")


@_attrs_define
class SendMessageResponse:
    """
    Attributes:
        message_id (str): MessageID is the first sent message's ID; for a multi-attachment send it is
            only the first of several IDs.

            Deprecated: use MessageIDs instead. Example: m_1234567890.
        message_ids (list[str]): MessageIDs holds every sent message's ID, in send order. Example: ['m_1234567890'].
        success (bool):  Example: True.
    """

    message_id: str
    message_ids: list[str]
    success: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        message_id = self.message_id

        message_ids = self.message_ids

        success = self.success

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "message_id": message_id,
                "message_ids": message_ids,
                "success": success,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        message_id = d.pop("message_id")

        message_ids = cast(list[str], d.pop("message_ids"))

        success = d.pop("success")

        send_message_response = cls(
            message_id=message_id,
            message_ids=message_ids,
            success=success,
        )

        send_message_response.additional_properties = d
        return send_message_response

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
