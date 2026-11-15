from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiEndpointsMessageQuickReply")


@_attrs_define
class ApiEndpointsMessageQuickReply:
    """
    Attributes:
        payload (str | Unset):  Example: TRACK_ORDER.
        title (str | Unset):  Example: Track my order.
    """

    payload: str | Unset = UNSET
    title: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        payload = self.payload

        title = self.title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if payload is not UNSET:
            field_dict["payload"] = payload
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        payload = d.pop("payload", UNSET)

        title = d.pop("title", UNSET)

        api_endpoints_message_quick_reply = cls(
            payload=payload,
            title=title,
        )

        api_endpoints_message_quick_reply.additional_properties = d
        return api_endpoints_message_quick_reply

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
