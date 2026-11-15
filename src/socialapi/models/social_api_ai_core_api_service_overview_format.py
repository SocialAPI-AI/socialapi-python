from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SocialApiAiCoreApiServiceOverviewFormat")


@_attrs_define
class SocialApiAiCoreApiServiceOverviewFormat:
    """
    Attributes:
        engagements (int | Unset):  Example: 1900.
        media_type (str | Unset): MediaType is the platform's own media kind, lowercased (image, video,
            reel, carousel_album, ...), or unknown when the platform did not say. Example: reel.
        posts (int | Unset):  Example: 12.
    """

    engagements: int | Unset = UNSET
    media_type: str | Unset = UNSET
    posts: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        engagements = self.engagements

        media_type = self.media_type

        posts = self.posts

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if engagements is not UNSET:
            field_dict["engagements"] = engagements
        if media_type is not UNSET:
            field_dict["media_type"] = media_type
        if posts is not UNSET:
            field_dict["posts"] = posts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        engagements = d.pop("engagements", UNSET)

        media_type = d.pop("media_type", UNSET)

        posts = d.pop("posts", UNSET)

        social_api_ai_core_api_service_overview_format = cls(
            engagements=engagements,
            media_type=media_type,
            posts=posts,
        )

        social_api_ai_core_api_service_overview_format.additional_properties = d
        return social_api_ai_core_api_service_overview_format

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
