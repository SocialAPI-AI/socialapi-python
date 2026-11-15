from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReviewMedia")


@_attrs_define
class ReviewMedia:
    """
    Attributes:
        thumbnail_url (str):  Example: https://lh3.googleusercontent.com/p/abc.
        thumbnail_label (str | Unset):  Example: Photo 1.
        video_url (str | Unset):  Example: https://lh3.googleusercontent.com/v/xyz.
    """

    thumbnail_url: str
    thumbnail_label: str | Unset = UNSET
    video_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        thumbnail_url = self.thumbnail_url

        thumbnail_label = self.thumbnail_label

        video_url = self.video_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "thumbnail_url": thumbnail_url,
            }
        )
        if thumbnail_label is not UNSET:
            field_dict["thumbnail_label"] = thumbnail_label
        if video_url is not UNSET:
            field_dict["video_url"] = video_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        thumbnail_url = d.pop("thumbnail_url")

        thumbnail_label = d.pop("thumbnail_label", UNSET)

        video_url = d.pop("video_url", UNSET)

        review_media = cls(
            thumbnail_url=thumbnail_url,
            thumbnail_label=thumbnail_label,
            video_url=video_url,
        )

        review_media.additional_properties = d
        return review_media

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
