from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.api_endpoints_message_button_type import ApiEndpointsMessageButtonType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiEndpointsMessageButton")


@_attrs_define
class ApiEndpointsMessageButton:
    """
    Attributes:
        payload (str | Unset):  Example: VIEW_ORDER.
        title (str | Unset):  Example: View order.
        type_ (ApiEndpointsMessageButtonType | Unset):  Example: url.
        url (str | Unset):  Example: https://shop.example.com/orders/1.
    """

    payload: str | Unset = UNSET
    title: str | Unset = UNSET
    type_: ApiEndpointsMessageButtonType | Unset = UNSET
    url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        payload = self.payload

        title = self.title

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if payload is not UNSET:
            field_dict["payload"] = payload
        if title is not UNSET:
            field_dict["title"] = title
        if type_ is not UNSET:
            field_dict["type"] = type_
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        payload = d.pop("payload", UNSET)

        title = d.pop("title", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: ApiEndpointsMessageButtonType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = ApiEndpointsMessageButtonType(_type_)

        url = d.pop("url", UNSET)

        api_endpoints_message_button = cls(
            payload=payload,
            title=title,
            type_=type_,
            url=url,
        )

        api_endpoints_message_button.additional_properties = d
        return api_endpoints_message_button

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
