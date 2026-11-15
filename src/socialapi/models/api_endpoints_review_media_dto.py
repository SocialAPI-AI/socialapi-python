from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiEndpointsReviewMediaDTO")


@_attrs_define
class ApiEndpointsReviewMediaDTO:
    """
    Attributes:
        thumbnail_label (str | Unset):  Example: Photo 1.
        thumbnail_url (str | Unset):  Example: https://lh3.googleusercontent.com/p/abc.
        video_url (str | Unset):  Example: https://lh3.googleusercontent.com/v/xyz.
    """

    thumbnail_label: str | Unset = UNSET
    thumbnail_url: str | Unset = UNSET
    video_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        thumbnail_label = self.thumbnail_label

        thumbnail_url = self.thumbnail_url

        video_url = self.video_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if thumbnail_label is not UNSET:
            field_dict["thumbnail_label"] = thumbnail_label
        if thumbnail_url is not UNSET:
            field_dict["thumbnail_url"] = thumbnail_url
        if video_url is not UNSET:
            field_dict["video_url"] = video_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        thumbnail_label = d.pop("thumbnail_label", UNSET)

        thumbnail_url = d.pop("thumbnail_url", UNSET)

        video_url = d.pop("video_url", UNSET)

        api_endpoints_review_media_dto = cls(
            thumbnail_label=thumbnail_label,
            thumbnail_url=thumbnail_url,
            video_url=video_url,
        )

        api_endpoints_review_media_dto.additional_properties = d
        return api_endpoints_review_media_dto

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
