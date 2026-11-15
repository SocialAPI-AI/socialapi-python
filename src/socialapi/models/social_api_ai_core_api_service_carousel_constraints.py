from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SocialApiAiCoreApiServiceCarouselConstraints")


@_attrs_define
class SocialApiAiCoreApiServiceCarouselConstraints:
    """
    Attributes:
        allow_video (bool | Unset): can carousel include video items
        images_only (bool | Unset): only image items allowed
        max_items (int | Unset):
        min_items (int | Unset):
        photos_only (bool | Unset): only photo items (no video, no gif - stricter than ImagesOnly)
        supported (bool | Unset):
    """

    allow_video: bool | Unset = UNSET
    images_only: bool | Unset = UNSET
    max_items: int | Unset = UNSET
    min_items: int | Unset = UNSET
    photos_only: bool | Unset = UNSET
    supported: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        allow_video = self.allow_video

        images_only = self.images_only

        max_items = self.max_items

        min_items = self.min_items

        photos_only = self.photos_only

        supported = self.supported

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if allow_video is not UNSET:
            field_dict["allow_video"] = allow_video
        if images_only is not UNSET:
            field_dict["images_only"] = images_only
        if max_items is not UNSET:
            field_dict["max_items"] = max_items
        if min_items is not UNSET:
            field_dict["min_items"] = min_items
        if photos_only is not UNSET:
            field_dict["photos_only"] = photos_only
        if supported is not UNSET:
            field_dict["supported"] = supported

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        allow_video = d.pop("allow_video", UNSET)

        images_only = d.pop("images_only", UNSET)

        max_items = d.pop("max_items", UNSET)

        min_items = d.pop("min_items", UNSET)

        photos_only = d.pop("photos_only", UNSET)

        supported = d.pop("supported", UNSET)

        social_api_ai_core_api_service_carousel_constraints = cls(
            allow_video=allow_video,
            images_only=images_only,
            max_items=max_items,
            min_items=min_items,
            photos_only=photos_only,
            supported=supported,
        )

        social_api_ai_core_api_service_carousel_constraints.additional_properties = d
        return social_api_ai_core_api_service_carousel_constraints

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
