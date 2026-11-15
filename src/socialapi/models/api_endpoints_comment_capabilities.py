from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiEndpointsCommentCapabilities")


@_attrs_define
class ApiEndpointsCommentCapabilities:
    """
    Attributes:
        can_delete (bool | Unset):  Example: True.
        can_hide (bool | Unset):  Example: True.
        can_like (bool | Unset):  Example: True.
        can_private_reply (bool | Unset):  Example: True.
        can_reply (bool | Unset):  Example: True.
    """

    can_delete: bool | Unset = UNSET
    can_hide: bool | Unset = UNSET
    can_like: bool | Unset = UNSET
    can_private_reply: bool | Unset = UNSET
    can_reply: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        can_delete = self.can_delete

        can_hide = self.can_hide

        can_like = self.can_like

        can_private_reply = self.can_private_reply

        can_reply = self.can_reply

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if can_delete is not UNSET:
            field_dict["can_delete"] = can_delete
        if can_hide is not UNSET:
            field_dict["can_hide"] = can_hide
        if can_like is not UNSET:
            field_dict["can_like"] = can_like
        if can_private_reply is not UNSET:
            field_dict["can_private_reply"] = can_private_reply
        if can_reply is not UNSET:
            field_dict["can_reply"] = can_reply

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        can_delete = d.pop("can_delete", UNSET)

        can_hide = d.pop("can_hide", UNSET)

        can_like = d.pop("can_like", UNSET)

        can_private_reply = d.pop("can_private_reply", UNSET)

        can_reply = d.pop("can_reply", UNSET)

        api_endpoints_comment_capabilities = cls(
            can_delete=can_delete,
            can_hide=can_hide,
            can_like=can_like,
            can_private_reply=can_private_reply,
            can_reply=can_reply,
        )

        api_endpoints_comment_capabilities.additional_properties = d
        return api_endpoints_comment_capabilities

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
