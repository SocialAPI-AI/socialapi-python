from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SocialApiAiCoreApiConnectorsBaseStory")


@_attrs_define
class SocialApiAiCoreApiConnectorsBaseStory:
    """
    Attributes:
        expires_at (str | Unset): when media_url stops working; omitted when it cannot be determined Example:
            2026-09-12T14:03:00Z.
        id (str | Unset): platform-native story id Example: 17901.
        media_type (str | Unset): [platform: facebook] photo or video Example: photo.
        media_url (str | Unset): downloadable media link Example:
            https://lookaside.fbsbx.com/ig_messaging_cdn/?asset_id=17901.
        permalink (str | Unset): [platform: facebook] story permalink Example: https://facebook.com/stories/1784.
    """

    expires_at: str | Unset = UNSET
    id: str | Unset = UNSET
    media_type: str | Unset = UNSET
    media_url: str | Unset = UNSET
    permalink: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        expires_at = self.expires_at

        id = self.id

        media_type = self.media_type

        media_url = self.media_url

        permalink = self.permalink

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at
        if id is not UNSET:
            field_dict["id"] = id
        if media_type is not UNSET:
            field_dict["media_type"] = media_type
        if media_url is not UNSET:
            field_dict["media_url"] = media_url
        if permalink is not UNSET:
            field_dict["permalink"] = permalink

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        expires_at = d.pop("expires_at", UNSET)

        id = d.pop("id", UNSET)

        media_type = d.pop("media_type", UNSET)

        media_url = d.pop("media_url", UNSET)

        permalink = d.pop("permalink", UNSET)

        social_api_ai_core_api_connectors_base_story = cls(
            expires_at=expires_at,
            id=id,
            media_type=media_type,
            media_url=media_url,
            permalink=permalink,
        )

        social_api_ai_core_api_connectors_base_story.additional_properties = d
        return social_api_ai_core_api_connectors_base_story

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
