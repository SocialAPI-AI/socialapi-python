from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.social_api_ai_core_api_connectors_base_platform_media_item_type import (
    SocialApiAiCoreApiConnectorsBasePlatformMediaItemType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="SocialApiAiCoreApiConnectorsBasePlatformMediaItem")


@_attrs_define
class SocialApiAiCoreApiConnectorsBasePlatformMediaItem:
    """
    Attributes:
        thumbnail_url (str | Unset): Link to a video's cover image, hosted by the platform. Temporary, like url. Absent
            on images. Example: https://scontent.cdninstagram.com/v/t51.29350-15/456_n.jpg.
        type_ (SocialApiAiCoreApiConnectorsBasePlatformMediaItemType | Unset): image or video. Example: image.
        url (str | Unset): Link to the file, hosted by the platform. Temporary: download the file rather than keeping
            the link. Absent when the platform withholds the file, as Instagram does for media with licensed audio. Example:
            https://scontent.cdninstagram.com/v/t51.29350-15/123_n.jpg.
    """

    thumbnail_url: str | Unset = UNSET
    type_: SocialApiAiCoreApiConnectorsBasePlatformMediaItemType | Unset = UNSET
    url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        thumbnail_url = self.thumbnail_url

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if thumbnail_url is not UNSET:
            field_dict["thumbnail_url"] = thumbnail_url
        if type_ is not UNSET:
            field_dict["type"] = type_
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        thumbnail_url = d.pop("thumbnail_url", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: SocialApiAiCoreApiConnectorsBasePlatformMediaItemType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = SocialApiAiCoreApiConnectorsBasePlatformMediaItemType(_type_)

        url = d.pop("url", UNSET)

        social_api_ai_core_api_connectors_base_platform_media_item = cls(
            thumbnail_url=thumbnail_url,
            type_=type_,
            url=url,
        )

        social_api_ai_core_api_connectors_base_platform_media_item.additional_properties = d
        return social_api_ai_core_api_connectors_base_platform_media_item

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
