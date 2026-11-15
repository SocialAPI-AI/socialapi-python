from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SocialApiAiCoreApiServiceInboxPostRow")


@_attrs_define
class SocialApiAiCoreApiServiceInboxPostRow:
    """
    Attributes:
        account_id (str | Unset):
        comment_count (int | Unset):
        content (str | Unset):
        created_at (str | Unset):
        id (str | Unset):
        like_count (int | Unset):
        page_id (str | Unset):
        permalink (str | Unset):
        platform (str | Unset):
        platform_id (str | Unset):
        published_at (str | Unset):
        thumbnail (str | Unset):
        updated_at (str | Unset):
        user_id (str | Unset):
    """

    account_id: str | Unset = UNSET
    comment_count: int | Unset = UNSET
    content: str | Unset = UNSET
    created_at: str | Unset = UNSET
    id: str | Unset = UNSET
    like_count: int | Unset = UNSET
    page_id: str | Unset = UNSET
    permalink: str | Unset = UNSET
    platform: str | Unset = UNSET
    platform_id: str | Unset = UNSET
    published_at: str | Unset = UNSET
    thumbnail: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    user_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_id = self.account_id

        comment_count = self.comment_count

        content = self.content

        created_at = self.created_at

        id = self.id

        like_count = self.like_count

        page_id = self.page_id

        permalink = self.permalink

        platform = self.platform

        platform_id = self.platform_id

        published_at = self.published_at

        thumbnail = self.thumbnail

        updated_at = self.updated_at

        user_id = self.user_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_id is not UNSET:
            field_dict["account_id"] = account_id
        if comment_count is not UNSET:
            field_dict["comment_count"] = comment_count
        if content is not UNSET:
            field_dict["content"] = content
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if id is not UNSET:
            field_dict["id"] = id
        if like_count is not UNSET:
            field_dict["like_count"] = like_count
        if page_id is not UNSET:
            field_dict["page_id"] = page_id
        if permalink is not UNSET:
            field_dict["permalink"] = permalink
        if platform is not UNSET:
            field_dict["platform"] = platform
        if platform_id is not UNSET:
            field_dict["platform_id"] = platform_id
        if published_at is not UNSET:
            field_dict["published_at"] = published_at
        if thumbnail is not UNSET:
            field_dict["thumbnail"] = thumbnail
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if user_id is not UNSET:
            field_dict["user_id"] = user_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_id = d.pop("account_id", UNSET)

        comment_count = d.pop("comment_count", UNSET)

        content = d.pop("content", UNSET)

        created_at = d.pop("created_at", UNSET)

        id = d.pop("id", UNSET)

        like_count = d.pop("like_count", UNSET)

        page_id = d.pop("page_id", UNSET)

        permalink = d.pop("permalink", UNSET)

        platform = d.pop("platform", UNSET)

        platform_id = d.pop("platform_id", UNSET)

        published_at = d.pop("published_at", UNSET)

        thumbnail = d.pop("thumbnail", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        user_id = d.pop("user_id", UNSET)

        social_api_ai_core_api_service_inbox_post_row = cls(
            account_id=account_id,
            comment_count=comment_count,
            content=content,
            created_at=created_at,
            id=id,
            like_count=like_count,
            page_id=page_id,
            permalink=permalink,
            platform=platform,
            platform_id=platform_id,
            published_at=published_at,
            thumbnail=thumbnail,
            updated_at=updated_at,
            user_id=user_id,
        )

        social_api_ai_core_api_service_inbox_post_row.additional_properties = d
        return social_api_ai_core_api_service_inbox_post_row

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
