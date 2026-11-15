from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="YouTubeChannelSummaryResponse")


@_attrs_define
class YouTubeChannelSummaryResponse:
    """
    Attributes:
        handle (str):
        subscriber_count (int):
        thumbnail_url (str):
        title (str):
        video_count (int):
        view_count (int):
    """

    handle: str
    subscriber_count: int
    thumbnail_url: str
    title: str
    video_count: int
    view_count: int
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
        field_dict.update(
            {
                "handle": handle,
                "subscriber_count": subscriber_count,
                "thumbnail_url": thumbnail_url,
                "title": title,
                "video_count": video_count,
                "view_count": view_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        handle = d.pop("handle")

        subscriber_count = d.pop("subscriber_count")

        thumbnail_url = d.pop("thumbnail_url")

        title = d.pop("title")

        video_count = d.pop("video_count")

        view_count = d.pop("view_count")

        you_tube_channel_summary_response = cls(
            handle=handle,
            subscriber_count=subscriber_count,
            thumbnail_url=thumbnail_url,
            title=title,
            video_count=video_count,
            view_count=view_count,
        )

        you_tube_channel_summary_response.additional_properties = d
        return you_tube_channel_summary_response

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
