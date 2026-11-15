from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.platform import Platform
from ..types import UNSET, Unset

T = TypeVar("T", bound="ExportVideoItem")


@_attrs_define
class ExportVideoItem:
    """
    Attributes:
        comment_count (int):
        cover_image_url (str):
        description (str):
        duration_seconds (int):
        height (int):
        like_count (int):
        platform (Platform):
        platform_video_id (str):
        share_count (int):
        share_url (str):
        title (str):
        view_count (int):
        width (int):
        create_time (datetime.datetime | Unset):
        transcript (str | Unset):
        transcript_lang (str | Unset):
        vision_category (str | Unset):
        vision_elements (list[str] | Unset):
        vision_summary (str | Unset):
    """

    comment_count: int
    cover_image_url: str
    description: str
    duration_seconds: int
    height: int
    like_count: int
    platform: Platform
    platform_video_id: str
    share_count: int
    share_url: str
    title: str
    view_count: int
    width: int
    create_time: datetime.datetime | Unset = UNSET
    transcript: str | Unset = UNSET
    transcript_lang: str | Unset = UNSET
    vision_category: str | Unset = UNSET
    vision_elements: list[str] | Unset = UNSET
    vision_summary: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        comment_count = self.comment_count

        cover_image_url = self.cover_image_url

        description = self.description

        duration_seconds = self.duration_seconds

        height = self.height

        like_count = self.like_count

        platform = self.platform.value

        platform_video_id = self.platform_video_id

        share_count = self.share_count

        share_url = self.share_url

        title = self.title

        view_count = self.view_count

        width = self.width

        create_time: str | Unset = UNSET
        if not isinstance(self.create_time, Unset):
            create_time = self.create_time.isoformat()

        transcript = self.transcript

        transcript_lang = self.transcript_lang

        vision_category = self.vision_category

        vision_elements: list[str] | Unset = UNSET
        if not isinstance(self.vision_elements, Unset):
            vision_elements = self.vision_elements

        vision_summary = self.vision_summary

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "comment_count": comment_count,
                "cover_image_url": cover_image_url,
                "description": description,
                "duration_seconds": duration_seconds,
                "height": height,
                "like_count": like_count,
                "platform": platform,
                "platform_video_id": platform_video_id,
                "share_count": share_count,
                "share_url": share_url,
                "title": title,
                "view_count": view_count,
                "width": width,
            }
        )
        if create_time is not UNSET:
            field_dict["create_time"] = create_time
        if transcript is not UNSET:
            field_dict["transcript"] = transcript
        if transcript_lang is not UNSET:
            field_dict["transcript_lang"] = transcript_lang
        if vision_category is not UNSET:
            field_dict["vision_category"] = vision_category
        if vision_elements is not UNSET:
            field_dict["vision_elements"] = vision_elements
        if vision_summary is not UNSET:
            field_dict["vision_summary"] = vision_summary

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        comment_count = d.pop("comment_count")

        cover_image_url = d.pop("cover_image_url")

        description = d.pop("description")

        duration_seconds = d.pop("duration_seconds")

        height = d.pop("height")

        like_count = d.pop("like_count")

        platform = Platform(d.pop("platform"))

        platform_video_id = d.pop("platform_video_id")

        share_count = d.pop("share_count")

        share_url = d.pop("share_url")

        title = d.pop("title")

        view_count = d.pop("view_count")

        width = d.pop("width")

        _create_time = d.pop("create_time", UNSET)
        create_time: datetime.datetime | Unset
        if isinstance(_create_time, Unset):
            create_time = UNSET
        else:
            create_time = datetime.datetime.fromisoformat(_create_time)

        transcript = d.pop("transcript", UNSET)

        transcript_lang = d.pop("transcript_lang", UNSET)

        vision_category = d.pop("vision_category", UNSET)

        vision_elements = cast(list[str], d.pop("vision_elements", UNSET))

        vision_summary = d.pop("vision_summary", UNSET)

        export_video_item = cls(
            comment_count=comment_count,
            cover_image_url=cover_image_url,
            description=description,
            duration_seconds=duration_seconds,
            height=height,
            like_count=like_count,
            platform=platform,
            platform_video_id=platform_video_id,
            share_count=share_count,
            share_url=share_url,
            title=title,
            view_count=view_count,
            width=width,
            create_time=create_time,
            transcript=transcript,
            transcript_lang=transcript_lang,
            vision_category=vision_category,
            vision_elements=vision_elements,
            vision_summary=vision_summary,
        )

        export_video_item.additional_properties = d
        return export_video_item

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
