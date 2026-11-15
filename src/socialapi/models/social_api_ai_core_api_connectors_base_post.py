from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.social_api_ai_core_api_connectors_base_platform_media_item import (
        SocialApiAiCoreApiConnectorsBasePlatformMediaItem,
    )
    from ..models.social_api_ai_core_api_connectors_base_post_metadata import (
        SocialApiAiCoreApiConnectorsBasePostMetadata,
    )
    from ..models.social_api_ai_core_api_connectors_base_post_settings import (
        SocialApiAiCoreApiConnectorsBasePostSettings,
    )


T = TypeVar("T", bound="SocialApiAiCoreApiConnectorsBasePost")


@_attrs_define
class SocialApiAiCoreApiConnectorsBasePost:
    """
    Attributes:
        account_id (str | Unset): [always]
        caption (str | Unset): [always] Post text body; may be empty for media-only posts
        comments_count (int | Unset): [platform: instagram, facebook, tiktok] Zero on other platforms
        id (str | Unset): [always] Platform-native post/video/media ID
        like_count (int | Unset): [platform: instagram, facebook, tiktok] Zero on other platforms
        media_type (str | Unset): [platform: instagram, facebook, threads, tiktok, youtube] Empty on linkedin and google
        media_url (str | Unset): [platform: instagram, tiktok, youtube] Cover image or media URL; empty on facebook,
            threads, linkedin, google
        metadata (SocialApiAiCoreApiConnectorsBasePostMetadata | Unset): [optional] Platform-specific keys; facebook
            sets "page_id" and "page_name"
        permalink (str | Unset): [platform: instagram, facebook, threads, tiktok, youtube, google, linkedin]
        platform (str | Unset): [always]
        platform_media (list[SocialApiAiCoreApiConnectorsBasePlatformMediaItem] | Unset): [platform: instagram,
            facebook] Every image and video on the post, carousel slides or album photos in order
        settings (SocialApiAiCoreApiConnectorsBasePostSettings | Unset):
        shares_count (int | Unset): [platform: facebook] Zero on other platforms
        timestamp (str | Unset): [always]
        view_count (int | Unset): [platform: youtube, tiktok] Zero on other platforms
    """

    account_id: str | Unset = UNSET
    caption: str | Unset = UNSET
    comments_count: int | Unset = UNSET
    id: str | Unset = UNSET
    like_count: int | Unset = UNSET
    media_type: str | Unset = UNSET
    media_url: str | Unset = UNSET
    metadata: SocialApiAiCoreApiConnectorsBasePostMetadata | Unset = UNSET
    permalink: str | Unset = UNSET
    platform: str | Unset = UNSET
    platform_media: list[SocialApiAiCoreApiConnectorsBasePlatformMediaItem] | Unset = UNSET
    settings: SocialApiAiCoreApiConnectorsBasePostSettings | Unset = UNSET
    shares_count: int | Unset = UNSET
    timestamp: str | Unset = UNSET
    view_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_id = self.account_id

        caption = self.caption

        comments_count = self.comments_count

        id = self.id

        like_count = self.like_count

        media_type = self.media_type

        media_url = self.media_url

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        permalink = self.permalink

        platform = self.platform

        platform_media: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.platform_media, Unset):
            platform_media = []
            for platform_media_item_data in self.platform_media:
                platform_media_item = platform_media_item_data.to_dict()
                platform_media.append(platform_media_item)

        settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.settings, Unset):
            settings = self.settings.to_dict()

        shares_count = self.shares_count

        timestamp = self.timestamp

        view_count = self.view_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_id is not UNSET:
            field_dict["account_id"] = account_id
        if caption is not UNSET:
            field_dict["caption"] = caption
        if comments_count is not UNSET:
            field_dict["comments_count"] = comments_count
        if id is not UNSET:
            field_dict["id"] = id
        if like_count is not UNSET:
            field_dict["like_count"] = like_count
        if media_type is not UNSET:
            field_dict["media_type"] = media_type
        if media_url is not UNSET:
            field_dict["media_url"] = media_url
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if permalink is not UNSET:
            field_dict["permalink"] = permalink
        if platform is not UNSET:
            field_dict["platform"] = platform
        if platform_media is not UNSET:
            field_dict["platform_media"] = platform_media
        if settings is not UNSET:
            field_dict["settings"] = settings
        if shares_count is not UNSET:
            field_dict["shares_count"] = shares_count
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if view_count is not UNSET:
            field_dict["view_count"] = view_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.social_api_ai_core_api_connectors_base_platform_media_item import (
            SocialApiAiCoreApiConnectorsBasePlatformMediaItem,  # noqa: PLC0415
        )
        from ..models.social_api_ai_core_api_connectors_base_post_metadata import (
            SocialApiAiCoreApiConnectorsBasePostMetadata,  # noqa: PLC0415
        )
        from ..models.social_api_ai_core_api_connectors_base_post_settings import (
            SocialApiAiCoreApiConnectorsBasePostSettings,  # noqa: PLC0415
        )

        d = dict(src_dict)
        account_id = d.pop("account_id", UNSET)

        caption = d.pop("caption", UNSET)

        comments_count = d.pop("comments_count", UNSET)

        id = d.pop("id", UNSET)

        like_count = d.pop("like_count", UNSET)

        media_type = d.pop("media_type", UNSET)

        media_url = d.pop("media_url", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: SocialApiAiCoreApiConnectorsBasePostMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = SocialApiAiCoreApiConnectorsBasePostMetadata.from_dict(_metadata)

        permalink = d.pop("permalink", UNSET)

        platform = d.pop("platform", UNSET)

        _platform_media = d.pop("platform_media", UNSET)
        platform_media: list[SocialApiAiCoreApiConnectorsBasePlatformMediaItem] | Unset = UNSET
        if _platform_media is not UNSET:
            platform_media = []
            for platform_media_item_data in _platform_media:
                platform_media_item = SocialApiAiCoreApiConnectorsBasePlatformMediaItem.from_dict(
                    platform_media_item_data
                )

                platform_media.append(platform_media_item)

        _settings = d.pop("settings", UNSET)
        settings: SocialApiAiCoreApiConnectorsBasePostSettings | Unset
        if isinstance(_settings, Unset):
            settings = UNSET
        else:
            settings = SocialApiAiCoreApiConnectorsBasePostSettings.from_dict(_settings)

        shares_count = d.pop("shares_count", UNSET)

        timestamp = d.pop("timestamp", UNSET)

        view_count = d.pop("view_count", UNSET)

        social_api_ai_core_api_connectors_base_post = cls(
            account_id=account_id,
            caption=caption,
            comments_count=comments_count,
            id=id,
            like_count=like_count,
            media_type=media_type,
            media_url=media_url,
            metadata=metadata,
            permalink=permalink,
            platform=platform,
            platform_media=platform_media,
            settings=settings,
            shares_count=shares_count,
            timestamp=timestamp,
            view_count=view_count,
        )

        social_api_ai_core_api_connectors_base_post.additional_properties = d
        return social_api_ai_core_api_connectors_base_post

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
