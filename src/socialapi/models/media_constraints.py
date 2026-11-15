from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MediaConstraints")


@_attrs_define
class MediaConstraints:
    """
    Attributes:
        max_image_size_bytes (int | Unset): 0 = not supported
        max_video_duration_sec (int | Unset): 0 = no max
        max_video_fps (int | Unset): 0 = no limit
        max_video_size_bytes (int | Unset): 0 = not supported
        min_video_duration_sec (int | Unset): 0 = no min
        supported_image_types (list[str] | Unset): MIME types, e.g. "image/jpeg"
        supported_video_types (list[str] | Unset): MIME types, e.g. "video/mp4"
    """

    max_image_size_bytes: int | Unset = UNSET
    max_video_duration_sec: int | Unset = UNSET
    max_video_fps: int | Unset = UNSET
    max_video_size_bytes: int | Unset = UNSET
    min_video_duration_sec: int | Unset = UNSET
    supported_image_types: list[str] | Unset = UNSET
    supported_video_types: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        max_image_size_bytes = self.max_image_size_bytes

        max_video_duration_sec = self.max_video_duration_sec

        max_video_fps = self.max_video_fps

        max_video_size_bytes = self.max_video_size_bytes

        min_video_duration_sec = self.min_video_duration_sec

        supported_image_types: list[str] | Unset = UNSET
        if not isinstance(self.supported_image_types, Unset):
            supported_image_types = self.supported_image_types

        supported_video_types: list[str] | Unset = UNSET
        if not isinstance(self.supported_video_types, Unset):
            supported_video_types = self.supported_video_types

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if max_image_size_bytes is not UNSET:
            field_dict["max_image_size_bytes"] = max_image_size_bytes
        if max_video_duration_sec is not UNSET:
            field_dict["max_video_duration_sec"] = max_video_duration_sec
        if max_video_fps is not UNSET:
            field_dict["max_video_fps"] = max_video_fps
        if max_video_size_bytes is not UNSET:
            field_dict["max_video_size_bytes"] = max_video_size_bytes
        if min_video_duration_sec is not UNSET:
            field_dict["min_video_duration_sec"] = min_video_duration_sec
        if supported_image_types is not UNSET:
            field_dict["supported_image_types"] = supported_image_types
        if supported_video_types is not UNSET:
            field_dict["supported_video_types"] = supported_video_types

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        max_image_size_bytes = d.pop("max_image_size_bytes", UNSET)

        max_video_duration_sec = d.pop("max_video_duration_sec", UNSET)

        max_video_fps = d.pop("max_video_fps", UNSET)

        max_video_size_bytes = d.pop("max_video_size_bytes", UNSET)

        min_video_duration_sec = d.pop("min_video_duration_sec", UNSET)

        supported_image_types = cast(list[str], d.pop("supported_image_types", UNSET))

        supported_video_types = cast(list[str], d.pop("supported_video_types", UNSET))

        media_constraints = cls(
            max_image_size_bytes=max_image_size_bytes,
            max_video_duration_sec=max_video_duration_sec,
            max_video_fps=max_video_fps,
            max_video_size_bytes=max_video_size_bytes,
            min_video_duration_sec=min_video_duration_sec,
            supported_image_types=supported_image_types,
            supported_video_types=supported_video_types,
        )

        media_constraints.additional_properties = d
        return media_constraints

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
