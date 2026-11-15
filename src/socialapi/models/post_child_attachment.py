from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostChildAttachment")


@_attrs_define
class PostChildAttachment:
    """
    Attributes:
        link (str): Destination URL of the card.
        description (str | Unset): Description text of the card.
        name (str | Unset): Title of the card.
        picture (str | Unset): Image URL of the card.
    """

    link: str
    description: str | Unset = UNSET
    name: str | Unset = UNSET
    picture: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        link = self.link

        description = self.description

        name = self.name

        picture = self.picture

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "link": link,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if name is not UNSET:
            field_dict["name"] = name
        if picture is not UNSET:
            field_dict["picture"] = picture

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        link = d.pop("link")

        description = d.pop("description", UNSET)

        name = d.pop("name", UNSET)

        picture = d.pop("picture", UNSET)

        post_child_attachment = cls(
            link=link,
            description=description,
            name=name,
            picture=picture,
        )

        post_child_attachment.additional_properties = d
        return post_child_attachment

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
