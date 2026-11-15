from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.platform import Platform
from ..models.post_target_status import PostTargetStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.media_input import MediaInput
    from ..models.platform_media_item import PlatformMediaItem
    from ..models.post_settings import PostSettings
    from ..models.post_target_error_response import PostTargetErrorResponse
    from ..models.post_target_metrics_response import PostTargetMetricsResponse
    from ..models.post_target_response_metadata import PostTargetResponseMetadata
    from ..models.post_target_response_platform_data import PostTargetResponsePlatformData


T = TypeVar("T", bound="PostTargetResponse")


@_attrs_define
class PostTargetResponse:
    """
    Attributes:
        platform (Platform):
        status (PostTargetStatus):
        account_id (str | Unset):  Example: acc_01HZ9X3Q4R5M6N7P8V2K0W1J.
        board_id (str | Unset):  Example: 8828.
        error (PostTargetErrorResponse | Unset):
        first_comment (str | Unset):
        media (list[MediaInput] | Unset):
        media_ids (list[str] | Unset): Deprecated: use media.
        media_type (str | Unset): The kind of post, for example feed, reel, stories or carousel. Other values can
            appear. Example: reel.
        metadata (PostTargetResponseMetadata | Unset):
        metrics (PostTargetMetricsResponse | Unset):
        metrics_synced_at (datetime.datetime | Unset):  Example: 2026-04-01T12:00:00Z.
        page_id (str | Unset):  Example: sapi_page_01HZ9X3Q4R5M6N7P8V2K0W1J.
        permalink (str | Unset):  Example: https://www.instagram.com/p/ABC123/.
        platform_data (PostTargetResponsePlatformData | Unset): The platform-specific options set on this target, as
            sent in platform_data when the post was created or last updated. Chain continuation posts are returned in
            segments, not here.
        platform_media (list[PlatformMediaItem] | Unset): Every image and video Instagram or Facebook reports on the
            published post: carousel slides or album photos in order, with a cover image for each video. The links are
            temporary: download the files rather than keeping the links, and call POST /v1/accounts/{account_id}/sync to get
            fresh ones. Absent on Facebook link and share posts and on other platforms.
        platform_post_id (str | Unset):  Example: 17895695668004550.
        published_at (datetime.datetime | Unset):  Example: 2026-04-01T10:00:05Z.
        scheduled_at (datetime.datetime | Unset):  Example: 2026-04-01T10:00:00Z.
        settings (PostSettings | Unset):
        text (str | Unset):
        title (str | Unset):
        visibility (str | Unset):  Example: public.
    """

    platform: Platform
    status: PostTargetStatus
    account_id: str | Unset = UNSET
    board_id: str | Unset = UNSET
    error: PostTargetErrorResponse | Unset = UNSET
    first_comment: str | Unset = UNSET
    media: list[MediaInput] | Unset = UNSET
    media_ids: list[str] | Unset = UNSET
    media_type: str | Unset = UNSET
    metadata: PostTargetResponseMetadata | Unset = UNSET
    metrics: PostTargetMetricsResponse | Unset = UNSET
    metrics_synced_at: datetime.datetime | Unset = UNSET
    page_id: str | Unset = UNSET
    permalink: str | Unset = UNSET
    platform_data: PostTargetResponsePlatformData | Unset = UNSET
    platform_media: list[PlatformMediaItem] | Unset = UNSET
    platform_post_id: str | Unset = UNSET
    published_at: datetime.datetime | Unset = UNSET
    scheduled_at: datetime.datetime | Unset = UNSET
    settings: PostSettings | Unset = UNSET
    text: str | Unset = UNSET
    title: str | Unset = UNSET
    visibility: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        platform = self.platform.value

        status = self.status.value

        account_id = self.account_id

        board_id = self.board_id

        error: dict[str, Any] | Unset = UNSET
        if not isinstance(self.error, Unset):
            error = self.error.to_dict()

        first_comment = self.first_comment

        media: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.media, Unset):
            media = []
            for media_item_data in self.media:
                media_item = media_item_data.to_dict()
                media.append(media_item)

        media_ids: list[str] | Unset = UNSET
        if not isinstance(self.media_ids, Unset):
            media_ids = self.media_ids

        media_type = self.media_type

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        metrics: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metrics, Unset):
            metrics = self.metrics.to_dict()

        metrics_synced_at: str | Unset = UNSET
        if not isinstance(self.metrics_synced_at, Unset):
            metrics_synced_at = self.metrics_synced_at.isoformat()

        page_id = self.page_id

        permalink = self.permalink

        platform_data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.platform_data, Unset):
            platform_data = self.platform_data.to_dict()

        platform_media: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.platform_media, Unset):
            platform_media = []
            for platform_media_item_data in self.platform_media:
                platform_media_item = platform_media_item_data.to_dict()
                platform_media.append(platform_media_item)

        platform_post_id = self.platform_post_id

        published_at: str | Unset = UNSET
        if not isinstance(self.published_at, Unset):
            published_at = self.published_at.isoformat()

        scheduled_at: str | Unset = UNSET
        if not isinstance(self.scheduled_at, Unset):
            scheduled_at = self.scheduled_at.isoformat()

        settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.settings, Unset):
            settings = self.settings.to_dict()

        text = self.text

        title = self.title

        visibility = self.visibility

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "platform": platform,
                "status": status,
            }
        )
        if account_id is not UNSET:
            field_dict["account_id"] = account_id
        if board_id is not UNSET:
            field_dict["board_id"] = board_id
        if error is not UNSET:
            field_dict["error"] = error
        if first_comment is not UNSET:
            field_dict["first_comment"] = first_comment
        if media is not UNSET:
            field_dict["media"] = media
        if media_ids is not UNSET:
            field_dict["media_ids"] = media_ids
        if media_type is not UNSET:
            field_dict["media_type"] = media_type
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if metrics is not UNSET:
            field_dict["metrics"] = metrics
        if metrics_synced_at is not UNSET:
            field_dict["metrics_synced_at"] = metrics_synced_at
        if page_id is not UNSET:
            field_dict["page_id"] = page_id
        if permalink is not UNSET:
            field_dict["permalink"] = permalink
        if platform_data is not UNSET:
            field_dict["platform_data"] = platform_data
        if platform_media is not UNSET:
            field_dict["platform_media"] = platform_media
        if platform_post_id is not UNSET:
            field_dict["platform_post_id"] = platform_post_id
        if published_at is not UNSET:
            field_dict["published_at"] = published_at
        if scheduled_at is not UNSET:
            field_dict["scheduled_at"] = scheduled_at
        if settings is not UNSET:
            field_dict["settings"] = settings
        if text is not UNSET:
            field_dict["text"] = text
        if title is not UNSET:
            field_dict["title"] = title
        if visibility is not UNSET:
            field_dict["visibility"] = visibility

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.media_input import MediaInput  # noqa: PLC0415
        from ..models.platform_media_item import PlatformMediaItem  # noqa: PLC0415
        from ..models.post_settings import PostSettings  # noqa: PLC0415
        from ..models.post_target_error_response import PostTargetErrorResponse  # noqa: PLC0415
        from ..models.post_target_metrics_response import PostTargetMetricsResponse  # noqa: PLC0415
        from ..models.post_target_response_metadata import PostTargetResponseMetadata  # noqa: PLC0415
        from ..models.post_target_response_platform_data import PostTargetResponsePlatformData  # noqa: PLC0415

        d = dict(src_dict)
        platform = Platform(d.pop("platform"))

        status = PostTargetStatus(d.pop("status"))

        account_id = d.pop("account_id", UNSET)

        board_id = d.pop("board_id", UNSET)

        _error = d.pop("error", UNSET)
        error: PostTargetErrorResponse | Unset
        if isinstance(_error, Unset):
            error = UNSET
        else:
            error = PostTargetErrorResponse.from_dict(_error)

        first_comment = d.pop("first_comment", UNSET)

        _media = d.pop("media", UNSET)
        media: list[MediaInput] | Unset = UNSET
        if _media is not UNSET:
            media = []
            for media_item_data in _media:
                media_item = MediaInput.from_dict(media_item_data)

                media.append(media_item)

        media_ids = cast(list[str], d.pop("media_ids", UNSET))

        media_type = d.pop("media_type", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: PostTargetResponseMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = PostTargetResponseMetadata.from_dict(_metadata)

        _metrics = d.pop("metrics", UNSET)
        metrics: PostTargetMetricsResponse | Unset
        if isinstance(_metrics, Unset):
            metrics = UNSET
        else:
            metrics = PostTargetMetricsResponse.from_dict(_metrics)

        _metrics_synced_at = d.pop("metrics_synced_at", UNSET)
        metrics_synced_at: datetime.datetime | Unset
        if isinstance(_metrics_synced_at, Unset):
            metrics_synced_at = UNSET
        else:
            metrics_synced_at = datetime.datetime.fromisoformat(_metrics_synced_at)

        page_id = d.pop("page_id", UNSET)

        permalink = d.pop("permalink", UNSET)

        _platform_data = d.pop("platform_data", UNSET)
        platform_data: PostTargetResponsePlatformData | Unset
        if isinstance(_platform_data, Unset):
            platform_data = UNSET
        else:
            platform_data = PostTargetResponsePlatformData.from_dict(_platform_data)

        _platform_media = d.pop("platform_media", UNSET)
        platform_media: list[PlatformMediaItem] | Unset = UNSET
        if _platform_media is not UNSET:
            platform_media = []
            for platform_media_item_data in _platform_media:
                platform_media_item = PlatformMediaItem.from_dict(platform_media_item_data)

                platform_media.append(platform_media_item)

        platform_post_id = d.pop("platform_post_id", UNSET)

        _published_at = d.pop("published_at", UNSET)
        published_at: datetime.datetime | Unset
        if isinstance(_published_at, Unset):
            published_at = UNSET
        else:
            published_at = datetime.datetime.fromisoformat(_published_at)

        _scheduled_at = d.pop("scheduled_at", UNSET)
        scheduled_at: datetime.datetime | Unset
        if isinstance(_scheduled_at, Unset):
            scheduled_at = UNSET
        else:
            scheduled_at = datetime.datetime.fromisoformat(_scheduled_at)

        _settings = d.pop("settings", UNSET)
        settings: PostSettings | Unset
        if isinstance(_settings, Unset):
            settings = UNSET
        else:
            settings = PostSettings.from_dict(_settings)

        text = d.pop("text", UNSET)

        title = d.pop("title", UNSET)

        visibility = d.pop("visibility", UNSET)

        post_target_response = cls(
            platform=platform,
            status=status,
            account_id=account_id,
            board_id=board_id,
            error=error,
            first_comment=first_comment,
            media=media,
            media_ids=media_ids,
            media_type=media_type,
            metadata=metadata,
            metrics=metrics,
            metrics_synced_at=metrics_synced_at,
            page_id=page_id,
            permalink=permalink,
            platform_data=platform_data,
            platform_media=platform_media,
            platform_post_id=platform_post_id,
            published_at=published_at,
            scheduled_at=scheduled_at,
            settings=settings,
            text=text,
            title=title,
            visibility=visibility,
        )

        post_target_response.additional_properties = d
        return post_target_response

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
