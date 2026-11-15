from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SocialApiAiCoreApiServiceTextConstraints")


@_attrs_define
class SocialApiAiCoreApiServiceTextConstraints:
    """
    Attributes:
        counting_mode (str | Unset): "chars" (default), "utf16", "bytes"
        max_hashtags (int | Unset): 0 = no limit
        max_length (int | Unset): maximum allowed length (in units defined by CountingMode)
        max_mentions (int | Unset): 0 = no limit
        photo_max_length (int | Unset): platform-specific stricter cap for photo-mode captions (e.g. TikTok); 0 = use
            MaxLength
    """

    counting_mode: str | Unset = UNSET
    max_hashtags: int | Unset = UNSET
    max_length: int | Unset = UNSET
    max_mentions: int | Unset = UNSET
    photo_max_length: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        counting_mode = self.counting_mode

        max_hashtags = self.max_hashtags

        max_length = self.max_length

        max_mentions = self.max_mentions

        photo_max_length = self.photo_max_length

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if counting_mode is not UNSET:
            field_dict["counting_mode"] = counting_mode
        if max_hashtags is not UNSET:
            field_dict["max_hashtags"] = max_hashtags
        if max_length is not UNSET:
            field_dict["max_length"] = max_length
        if max_mentions is not UNSET:
            field_dict["max_mentions"] = max_mentions
        if photo_max_length is not UNSET:
            field_dict["photo_max_length"] = photo_max_length

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        counting_mode = d.pop("counting_mode", UNSET)

        max_hashtags = d.pop("max_hashtags", UNSET)

        max_length = d.pop("max_length", UNSET)

        max_mentions = d.pop("max_mentions", UNSET)

        photo_max_length = d.pop("photo_max_length", UNSET)

        social_api_ai_core_api_service_text_constraints = cls(
            counting_mode=counting_mode,
            max_hashtags=max_hashtags,
            max_length=max_length,
            max_mentions=max_mentions,
            photo_max_length=photo_max_length,
        )

        social_api_ai_core_api_service_text_constraints.additional_properties = d
        return social_api_ai_core_api_service_text_constraints

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
