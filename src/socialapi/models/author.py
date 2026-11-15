from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Author")


@_attrs_define
class Author:
    """
    Attributes:
        avatar_url (str | Unset):  Example: https://example.com/avatar.jpg.
        id (str | Unset):  Example: 17841405793187218.
        name (str | Unset):  Example: Jane Smith.
        username (str | Unset):  Example: janesmith.
    """

    avatar_url: str | Unset = UNSET
    id: str | Unset = UNSET
    name: str | Unset = UNSET
    username: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        avatar_url = self.avatar_url

        id = self.id

        name = self.name

        username = self.username

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if avatar_url is not UNSET:
            field_dict["avatar_url"] = avatar_url
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if username is not UNSET:
            field_dict["username"] = username

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        avatar_url = d.pop("avatar_url", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        username = d.pop("username", UNSET)

        author = cls(
            avatar_url=avatar_url,
            id=id,
            name=name,
            username=username,
        )

        author.additional_properties = d
        return author

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
