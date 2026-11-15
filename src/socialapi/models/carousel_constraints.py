from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CarouselConstraints")


@_attrs_define
class CarouselConstraints:
    """
    Attributes:
        allow_video (bool): can carousel include video items
        images_only (bool): only image items allowed
        max_items (int):
        min_items (int):
        photos_only (bool): only photo items (no video, no gif - stricter than ImagesOnly)
        supported (bool):
    """

    allow_video: bool
    images_only: bool
    max_items: int
    min_items: int
    photos_only: bool
    supported: bool
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
        field_dict.update(
            {
                "allow_video": allow_video,
                "images_only": images_only,
                "max_items": max_items,
                "min_items": min_items,
                "photos_only": photos_only,
                "supported": supported,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        allow_video = d.pop("allow_video")

        images_only = d.pop("images_only")

        max_items = d.pop("max_items")

        min_items = d.pop("min_items")

        photos_only = d.pop("photos_only")

        supported = d.pop("supported")

        carousel_constraints = cls(
            allow_video=allow_video,
            images_only=images_only,
            max_items=max_items,
            min_items=min_items,
            photos_only=photos_only,
            supported=supported,
        )

        carousel_constraints.additional_properties = d
        return carousel_constraints

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
