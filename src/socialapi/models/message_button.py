from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.message_button_type import MessageButtonType
from ..types import UNSET, Unset

T = TypeVar("T", bound="MessageButton")


@_attrs_define
class MessageButton:
    """
    Attributes:
        title (str):  Example: View order.
        type_ (MessageButtonType):
        payload (str | Unset):  Example: VIEW_ORDER.
        url (str | Unset):  Example: https://shop.example.com/orders/1.
    """

    title: str
    type_: MessageButtonType
    payload: str | Unset = UNSET
    url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        type_ = self.type_.value

        payload = self.payload

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
                "type": type_,
            }
        )
        if payload is not UNSET:
            field_dict["payload"] = payload
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        title = d.pop("title")

        type_ = MessageButtonType(d.pop("type"))

        payload = d.pop("payload", UNSET)

        url = d.pop("url", UNSET)

        message_button = cls(
            title=title,
            type_=type_,
            payload=payload,
            url=url,
        )

        message_button.additional_properties = d
        return message_button

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
