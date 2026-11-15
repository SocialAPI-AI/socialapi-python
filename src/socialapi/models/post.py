from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.platform import Platform
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.platform_media_item import PlatformMediaItem
    from ..models.post_metadata import PostMetadata
    from ..models.post_settings import PostSettings


T = TypeVar("T", bound="Post")


@_attrs_define
class Post:
    """
    Attributes:
        account_id (str): [always]
        caption (str): [always] Post text body; may be empty for media-only posts
        comments_count (int): [platform: instagram, facebook, tiktok] Zero on other platforms
        id (str): [always] Platform-native post/video/media ID
        like_count (int): [platform: instagram, facebook, tiktok] Zero on other platforms
        permalink (str): [platform: instagram, facebook, threads, tiktok, youtube, google, linkedin]
        platform (Platform):
        shares_count (int): [platform: facebook] Zero on other platforms
        timestamp (datetime.datetime): [always]
        view_count (int): [platform: youtube, tiktok] Zero on other platforms
        media_type (str | Unset): [platform: instagram, facebook, threads, tiktok, youtube] Empty on linkedin and google
        media_url (str | Unset): [platform: instagram, tiktok, youtube] Cover image or media URL; empty on facebook,
            threads, linkedin, google
        metadata (PostMetadata | Unset): [optional] Platform-specific keys; facebook sets "page_id" and "page_name"
        platform_media (list[PlatformMediaItem] | Unset): [platform: instagram, facebook] Every image and video on the
            post, carousel slides or album photos in order
        settings (PostSettings | Unset):
    """

    account_id: str
    caption: str
    comments_count: int
    id: str
    like_count: int
    permalink: str
    platform: Platform
    shares_count: int
    timestamp: datetime.datetime
    view_count: int
    media_type: str | Unset = UNSET
    media_url: str | Unset = UNSET
    metadata: PostMetadata | Unset = UNSET
    platform_media: list[PlatformMediaItem] | Unset = UNSET
    settings: PostSettings | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_id = self.account_id

        caption = self.caption

        comments_count = self.comments_count

        id = self.id

        like_count = self.like_count

        permalink = self.permalink

        platform = self.platform.value

        shares_count = self.shares_count

        timestamp = self.timestamp.isoformat()

        view_count = self.view_count

        media_type = self.media_type

        media_url = self.media_url

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        platform_media: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.platform_media, Unset):
            platform_media = []
            for platform_media_item_data in self.platform_media:
                platform_media_item = platform_media_item_data.to_dict()
                platform_media.append(platform_media_item)

        settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.settings, Unset):
            settings = self.settings.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "account_id": account_id,
                "caption": caption,
                "comments_count": comments_count,
                "id": id,
                "like_count": like_count,
                "permalink": permalink,
                "platform": platform,
                "shares_count": shares_count,
                "timestamp": timestamp,
                "view_count": view_count,
            }
        )
        if media_type is not UNSET:
            field_dict["media_type"] = media_type
        if media_url is not UNSET:
            field_dict["media_url"] = media_url
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if platform_media is not UNSET:
            field_dict["platform_media"] = platform_media
        if settings is not UNSET:
            field_dict["settings"] = settings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.platform_media_item import PlatformMediaItem  # noqa: PLC0415
        from ..models.post_metadata import PostMetadata  # noqa: PLC0415
        from ..models.post_settings import PostSettings  # noqa: PLC0415

        d = dict(src_dict)
        account_id = d.pop("account_id")

        caption = d.pop("caption")

        comments_count = d.pop("comments_count")

        id = d.pop("id")

        like_count = d.pop("like_count")

        permalink = d.pop("permalink")

        platform = Platform(d.pop("platform"))

        shares_count = d.pop("shares_count")

        timestamp = datetime.datetime.fromisoformat(d.pop("timestamp"))

        view_count = d.pop("view_count")

        media_type = d.pop("media_type", UNSET)

        media_url = d.pop("media_url", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: PostMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = PostMetadata.from_dict(_metadata)

        _platform_media = d.pop("platform_media", UNSET)
        platform_media: list[PlatformMediaItem] | Unset = UNSET
        if _platform_media is not UNSET:
            platform_media = []
            for platform_media_item_data in _platform_media:
                platform_media_item = PlatformMediaItem.from_dict(platform_media_item_data)

                platform_media.append(platform_media_item)

        _settings = d.pop("settings", UNSET)
        settings: PostSettings | Unset
        if isinstance(_settings, Unset):
            settings = UNSET
        else:
            settings = PostSettings.from_dict(_settings)

        post = cls(
            account_id=account_id,
            caption=caption,
            comments_count=comments_count,
            id=id,
            like_count=like_count,
            permalink=permalink,
            platform=platform,
            shares_count=shares_count,
            timestamp=timestamp,
            view_count=view_count,
            media_type=media_type,
            media_url=media_url,
            metadata=metadata,
            platform_media=platform_media,
            settings=settings,
        )

        post.additional_properties = d
        return post

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
