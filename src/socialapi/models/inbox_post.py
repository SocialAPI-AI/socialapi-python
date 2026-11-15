from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.platform import Platform
from ..types import UNSET, Unset

T = TypeVar("T", bound="InboxPost")


@_attrs_define
class InboxPost:
    """
    Attributes:
        account_id (str):
        comment_count (int):
        content (None | str):
        created_at (str):
        id (str):
        like_count (int):
        permalink (None | str):
        platform (Platform):
        published_at (None | str):
        thumbnail (None | str):
        updated_at (str):
        user_id (str):
        page_id (str | Unset):
        platform_id (str | Unset):
    """

    account_id: str
    comment_count: int
    content: None | str
    created_at: str
    id: str
    like_count: int
    permalink: None | str
    platform: Platform
    published_at: None | str
    thumbnail: None | str
    updated_at: str
    user_id: str
    page_id: str | Unset = UNSET
    platform_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_id = self.account_id

        comment_count = self.comment_count

        content: None | str
        content = self.content

        created_at = self.created_at

        id = self.id

        like_count = self.like_count

        permalink: None | str
        permalink = self.permalink

        platform = self.platform.value

        published_at: None | str
        published_at = self.published_at

        thumbnail: None | str
        thumbnail = self.thumbnail

        updated_at = self.updated_at

        user_id = self.user_id

        page_id = self.page_id

        platform_id = self.platform_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "account_id": account_id,
                "comment_count": comment_count,
                "content": content,
                "created_at": created_at,
                "id": id,
                "like_count": like_count,
                "permalink": permalink,
                "platform": platform,
                "published_at": published_at,
                "thumbnail": thumbnail,
                "updated_at": updated_at,
                "user_id": user_id,
            }
        )
        if page_id is not UNSET:
            field_dict["page_id"] = page_id
        if platform_id is not UNSET:
            field_dict["platform_id"] = platform_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_id = d.pop("account_id")

        comment_count = d.pop("comment_count")

        def _parse_content(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        content = _parse_content(d.pop("content"))

        created_at = d.pop("created_at")

        id = d.pop("id")

        like_count = d.pop("like_count")

        def _parse_permalink(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        permalink = _parse_permalink(d.pop("permalink"))

        platform = Platform(d.pop("platform"))

        def _parse_published_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        published_at = _parse_published_at(d.pop("published_at"))

        def _parse_thumbnail(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        thumbnail = _parse_thumbnail(d.pop("thumbnail"))

        updated_at = d.pop("updated_at")

        user_id = d.pop("user_id")

        page_id = d.pop("page_id", UNSET)

        platform_id = d.pop("platform_id", UNSET)

        inbox_post = cls(
            account_id=account_id,
            comment_count=comment_count,
            content=content,
            created_at=created_at,
            id=id,
            like_count=like_count,
            permalink=permalink,
            platform=platform,
            published_at=published_at,
            thumbnail=thumbnail,
            updated_at=updated_at,
            user_id=user_id,
            page_id=page_id,
            platform_id=platform_id,
        )

        inbox_post.additional_properties = d
        return inbox_post

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
