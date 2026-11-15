from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiEndpointsExportVideoItem")


@_attrs_define
class ApiEndpointsExportVideoItem:
    """
    Attributes:
        comment_count (int | Unset):
        cover_image_url (str | Unset):
        create_time (str | Unset):
        description (str | Unset):
        duration_seconds (int | Unset):
        height (int | Unset):
        like_count (int | Unset):
        platform (str | Unset):
        platform_video_id (str | Unset):
        share_count (int | Unset):
        share_url (str | Unset):
        title (str | Unset):
        transcript (str | Unset):
        transcript_lang (str | Unset):
        view_count (int | Unset):
        vision_category (str | Unset):
        vision_elements (list[str] | Unset):
        vision_summary (str | Unset):
        width (int | Unset):
    """

    comment_count: int | Unset = UNSET
    cover_image_url: str | Unset = UNSET
    create_time: str | Unset = UNSET
    description: str | Unset = UNSET
    duration_seconds: int | Unset = UNSET
    height: int | Unset = UNSET
    like_count: int | Unset = UNSET
    platform: str | Unset = UNSET
    platform_video_id: str | Unset = UNSET
    share_count: int | Unset = UNSET
    share_url: str | Unset = UNSET
    title: str | Unset = UNSET
    transcript: str | Unset = UNSET
    transcript_lang: str | Unset = UNSET
    view_count: int | Unset = UNSET
    vision_category: str | Unset = UNSET
    vision_elements: list[str] | Unset = UNSET
    vision_summary: str | Unset = UNSET
    width: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        comment_count = self.comment_count

        cover_image_url = self.cover_image_url

        create_time = self.create_time

        description = self.description

        duration_seconds = self.duration_seconds

        height = self.height

        like_count = self.like_count

        platform = self.platform

        platform_video_id = self.platform_video_id

        share_count = self.share_count

        share_url = self.share_url

        title = self.title

        transcript = self.transcript

        transcript_lang = self.transcript_lang

        view_count = self.view_count

        vision_category = self.vision_category

        vision_elements: list[str] | Unset = UNSET
        if not isinstance(self.vision_elements, Unset):
            vision_elements = self.vision_elements

        vision_summary = self.vision_summary

        width = self.width

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if comment_count is not UNSET:
            field_dict["comment_count"] = comment_count
        if cover_image_url is not UNSET:
            field_dict["cover_image_url"] = cover_image_url
        if create_time is not UNSET:
            field_dict["create_time"] = create_time
        if description is not UNSET:
            field_dict["description"] = description
        if duration_seconds is not UNSET:
            field_dict["duration_seconds"] = duration_seconds
        if height is not UNSET:
            field_dict["height"] = height
        if like_count is not UNSET:
            field_dict["like_count"] = like_count
        if platform is not UNSET:
            field_dict["platform"] = platform
        if platform_video_id is not UNSET:
            field_dict["platform_video_id"] = platform_video_id
        if share_count is not UNSET:
            field_dict["share_count"] = share_count
        if share_url is not UNSET:
            field_dict["share_url"] = share_url
        if title is not UNSET:
            field_dict["title"] = title
        if transcript is not UNSET:
            field_dict["transcript"] = transcript
        if transcript_lang is not UNSET:
            field_dict["transcript_lang"] = transcript_lang
        if view_count is not UNSET:
            field_dict["view_count"] = view_count
        if vision_category is not UNSET:
            field_dict["vision_category"] = vision_category
        if vision_elements is not UNSET:
            field_dict["vision_elements"] = vision_elements
        if vision_summary is not UNSET:
            field_dict["vision_summary"] = vision_summary
        if width is not UNSET:
            field_dict["width"] = width

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        comment_count = d.pop("comment_count", UNSET)

        cover_image_url = d.pop("cover_image_url", UNSET)

        create_time = d.pop("create_time", UNSET)

        description = d.pop("description", UNSET)

        duration_seconds = d.pop("duration_seconds", UNSET)

        height = d.pop("height", UNSET)

        like_count = d.pop("like_count", UNSET)

        platform = d.pop("platform", UNSET)

        platform_video_id = d.pop("platform_video_id", UNSET)

        share_count = d.pop("share_count", UNSET)

        share_url = d.pop("share_url", UNSET)

        title = d.pop("title", UNSET)

        transcript = d.pop("transcript", UNSET)

        transcript_lang = d.pop("transcript_lang", UNSET)

        view_count = d.pop("view_count", UNSET)

        vision_category = d.pop("vision_category", UNSET)

        vision_elements = cast(list[str], d.pop("vision_elements", UNSET))

        vision_summary = d.pop("vision_summary", UNSET)

        width = d.pop("width", UNSET)

        api_endpoints_export_video_item = cls(
            comment_count=comment_count,
            cover_image_url=cover_image_url,
            create_time=create_time,
            description=description,
            duration_seconds=duration_seconds,
            height=height,
            like_count=like_count,
            platform=platform,
            platform_video_id=platform_video_id,
            share_count=share_count,
            share_url=share_url,
            title=title,
            transcript=transcript,
            transcript_lang=transcript_lang,
            view_count=view_count,
            vision_category=vision_category,
            vision_elements=vision_elements,
            vision_summary=vision_summary,
            width=width,
        )

        api_endpoints_export_video_item.additional_properties = d
        return api_endpoints_export_video_item

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
