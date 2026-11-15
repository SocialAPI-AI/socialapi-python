from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiEndpointsYouTubeChannelSummaryResponse")


@_attrs_define
class ApiEndpointsYouTubeChannelSummaryResponse:
    """
    Attributes:
        handle (str | Unset):
        subscriber_count (int | Unset):
        thumbnail_url (str | Unset):
        title (str | Unset):
        video_count (int | Unset):
        view_count (int | Unset):
    """

    handle: str | Unset = UNSET
    subscriber_count: int | Unset = UNSET
    thumbnail_url: str | Unset = UNSET
    title: str | Unset = UNSET
    video_count: int | Unset = UNSET
    view_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        handle = self.handle

        subscriber_count = self.subscriber_count

        thumbnail_url = self.thumbnail_url

        title = self.title

        video_count = self.video_count

        view_count = self.view_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if handle is not UNSET:
            field_dict["handle"] = handle
        if subscriber_count is not UNSET:
            field_dict["subscriber_count"] = subscriber_count
        if thumbnail_url is not UNSET:
            field_dict["thumbnail_url"] = thumbnail_url
        if title is not UNSET:
            field_dict["title"] = title
        if video_count is not UNSET:
            field_dict["video_count"] = video_count
        if view_count is not UNSET:
            field_dict["view_count"] = view_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        handle = d.pop("handle", UNSET)

        subscriber_count = d.pop("subscriber_count", UNSET)

        thumbnail_url = d.pop("thumbnail_url", UNSET)

        title = d.pop("title", UNSET)

        video_count = d.pop("video_count", UNSET)

        view_count = d.pop("view_count", UNSET)

        api_endpoints_you_tube_channel_summary_response = cls(
            handle=handle,
            subscriber_count=subscriber_count,
            thumbnail_url=thumbnail_url,
            title=title,
            video_count=video_count,
            view_count=view_count,
        )

        api_endpoints_you_tube_channel_summary_response.additional_properties = d
        return api_endpoints_you_tube_channel_summary_response

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
