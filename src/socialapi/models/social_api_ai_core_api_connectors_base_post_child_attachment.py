from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SocialApiAiCoreApiConnectorsBasePostChildAttachment")


@_attrs_define
class SocialApiAiCoreApiConnectorsBasePostChildAttachment:
    """
    Attributes:
        description (str | Unset): Description text of the card.
        link (str | Unset): Destination URL of the card.
        name (str | Unset): Title of the card.
        picture (str | Unset): Image URL of the card.
    """

    description: str | Unset = UNSET
    link: str | Unset = UNSET
    name: str | Unset = UNSET
    picture: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        link = self.link

        name = self.name

        picture = self.picture

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if link is not UNSET:
            field_dict["link"] = link
        if name is not UNSET:
            field_dict["name"] = name
        if picture is not UNSET:
            field_dict["picture"] = picture

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        description = d.pop("description", UNSET)

        link = d.pop("link", UNSET)

        name = d.pop("name", UNSET)

        picture = d.pop("picture", UNSET)

        social_api_ai_core_api_connectors_base_post_child_attachment = cls(
            description=description,
            link=link,
            name=name,
            picture=picture,
        )

        social_api_ai_core_api_connectors_base_post_child_attachment.additional_properties = d
        return social_api_ai_core_api_connectors_base_post_child_attachment

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
