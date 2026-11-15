from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiEndpointsUpdateYouTubeVideoRequest")


@_attrs_define
class ApiEndpointsUpdateYouTubeVideoRequest:
    """
    Attributes:
        cover_url (str | Unset): Public URL of a JPG or PNG image (50 MB max) to set as the video's custom thumbnail.
            The channel must be verified to use custom thumbnails, otherwise the request fails with 403
            platform.youtube.custom_thumbnail_forbidden. If the thumbnail is refused, no other field in the request is
            applied. Example: https://example.com/cover.jpg.
        description (str | Unset):
        tags (list[str] | Unset):
        title (str | Unset):
        visibility (str | Unset): public | unlisted | private
    """

    cover_url: str | Unset = UNSET
    description: str | Unset = UNSET
    tags: list[str] | Unset = UNSET
    title: str | Unset = UNSET
    visibility: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cover_url = self.cover_url

        description = self.description

        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        title = self.title

        visibility = self.visibility

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cover_url is not UNSET:
            field_dict["cover_url"] = cover_url
        if description is not UNSET:
            field_dict["description"] = description
        if tags is not UNSET:
            field_dict["tags"] = tags
        if title is not UNSET:
            field_dict["title"] = title
        if visibility is not UNSET:
            field_dict["visibility"] = visibility

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cover_url = d.pop("cover_url", UNSET)

        description = d.pop("description", UNSET)

        tags = cast(list[str], d.pop("tags", UNSET))

        title = d.pop("title", UNSET)

        visibility = d.pop("visibility", UNSET)

        api_endpoints_update_you_tube_video_request = cls(
            cover_url=cover_url,
            description=description,
            tags=tags,
            title=title,
            visibility=visibility,
        )

        api_endpoints_update_you_tube_video_request.additional_properties = d
        return api_endpoints_update_you_tube_video_request

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
