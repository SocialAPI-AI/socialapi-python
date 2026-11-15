from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostInboxCommentsPostIdBody")


@_attrs_define
class PostInboxCommentsPostIdBody:
    """
    Attributes:
        account_id (str | Unset):
        comment_id (str | Unset):
        text (str | Unset):
    """

    account_id: str | Unset = UNSET
    comment_id: str | Unset = UNSET
    text: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_id = self.account_id

        comment_id = self.comment_id

        text = self.text

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_id is not UNSET:
            field_dict["account_id"] = account_id
        if comment_id is not UNSET:
            field_dict["comment_id"] = comment_id
        if text is not UNSET:
            field_dict["text"] = text

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_id = d.pop("account_id", UNSET)

        comment_id = d.pop("comment_id", UNSET)

        text = d.pop("text", UNSET)

        post_inbox_comments_post_id_body = cls(
            account_id=account_id,
            comment_id=comment_id,
            text=text,
        )

        post_inbox_comments_post_id_body.additional_properties = d
        return post_inbox_comments_post_id_body

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
