from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.api_endpoints_post_target_response_media_type import ApiEndpointsPostTargetResponseMediaType
from ..models.api_endpoints_post_target_response_platform import ApiEndpointsPostTargetResponsePlatform
from ..models.api_endpoints_post_target_response_status import ApiEndpointsPostTargetResponseStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_endpoints_media_input import ApiEndpointsMediaInput
    from ..models.api_endpoints_post_target_error_response import ApiEndpointsPostTargetErrorResponse
    from ..models.api_endpoints_post_target_metrics_response import ApiEndpointsPostTargetMetricsResponse
    from ..models.api_endpoints_post_target_response_metadata import ApiEndpointsPostTargetResponseMetadata
    from ..models.api_endpoints_post_target_response_platform_data import ApiEndpointsPostTargetResponsePlatformData
    from ..models.social_api_ai_core_api_connectors_base_platform_media_item import (
        SocialApiAiCoreApiConnectorsBasePlatformMediaItem,
    )
    from ..models.social_api_ai_core_api_connectors_base_post_settings import (
        SocialApiAiCoreApiConnectorsBasePostSettings,
    )


T = TypeVar("T", bound="ApiEndpointsPostTargetResponse")


@_attrs_define
class ApiEndpointsPostTargetResponse:
    """
    Attributes:
        account_id (str | Unset):  Example: acc_01HZ9X3Q4R5M6N7P8V2K0W1J.
        board_id (str | Unset):  Example: 8828.
        error (ApiEndpointsPostTargetErrorResponse | Unset):
        first_comment (str | Unset):
        media (list[ApiEndpointsMediaInput] | Unset):
        media_ids (list[str] | Unset): Deprecated: use media.
        media_type (ApiEndpointsPostTargetResponseMediaType | Unset):  Example: reel.
        metadata (ApiEndpointsPostTargetResponseMetadata | Unset):
        metrics (ApiEndpointsPostTargetMetricsResponse | Unset):
        metrics_synced_at (str | Unset):  Example: 2026-04-01T12:00:00Z.
        page_id (str | Unset):  Example: sapi_page_01HZ9X3Q4R5M6N7P8V2K0W1J.
        permalink (str | Unset):  Example: https://www.instagram.com/p/ABC123/.
        platform (ApiEndpointsPostTargetResponsePlatform | Unset):  Example: instagram.
        platform_data (ApiEndpointsPostTargetResponsePlatformData | Unset): The platform-specific options set on this
            target, as sent in platform_data when the post was created or last updated. Chain continuation posts are
            returned in segments, not here.
        platform_media (list[SocialApiAiCoreApiConnectorsBasePlatformMediaItem] | Unset): Every image and video
            Instagram or Facebook reports on the published post: carousel slides or album photos in order, with a cover
            image for each video. The links are temporary: download the files rather than keeping the links, and call POST
            /v1/accounts/{id}/sync to get fresh ones. Absent on Facebook link and share posts and on other platforms.
        platform_post_id (str | Unset):  Example: 17895695668004550.
        published_at (str | Unset):  Example: 2026-04-01T10:00:05Z.
        scheduled_at (str | Unset):  Example: 2026-04-01T10:00:00Z.
        settings (SocialApiAiCoreApiConnectorsBasePostSettings | Unset):
        status (ApiEndpointsPostTargetResponseStatus | Unset):  Example: published.
        text (str | Unset):
        title (str | Unset):
        visibility (str | Unset):  Example: public.
    """

    account_id: str | Unset = UNSET
    board_id: str | Unset = UNSET
    error: ApiEndpointsPostTargetErrorResponse | Unset = UNSET
    first_comment: str | Unset = UNSET
    media: list[ApiEndpointsMediaInput] | Unset = UNSET
    media_ids: list[str] | Unset = UNSET
    media_type: ApiEndpointsPostTargetResponseMediaType | Unset = UNSET
    metadata: ApiEndpointsPostTargetResponseMetadata | Unset = UNSET
    metrics: ApiEndpointsPostTargetMetricsResponse | Unset = UNSET
    metrics_synced_at: str | Unset = UNSET
    page_id: str | Unset = UNSET
    permalink: str | Unset = UNSET
    platform: ApiEndpointsPostTargetResponsePlatform | Unset = UNSET
    platform_data: ApiEndpointsPostTargetResponsePlatformData | Unset = UNSET
    platform_media: list[SocialApiAiCoreApiConnectorsBasePlatformMediaItem] | Unset = UNSET
    platform_post_id: str | Unset = UNSET
    published_at: str | Unset = UNSET
    scheduled_at: str | Unset = UNSET
    settings: SocialApiAiCoreApiConnectorsBasePostSettings | Unset = UNSET
    status: ApiEndpointsPostTargetResponseStatus | Unset = UNSET
    text: str | Unset = UNSET
    title: str | Unset = UNSET
    visibility: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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

        media_type: str | Unset = UNSET
        if not isinstance(self.media_type, Unset):
            media_type = self.media_type.value

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        metrics: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metrics, Unset):
            metrics = self.metrics.to_dict()

        metrics_synced_at = self.metrics_synced_at

        page_id = self.page_id

        permalink = self.permalink

        platform: str | Unset = UNSET
        if not isinstance(self.platform, Unset):
            platform = self.platform.value

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

        published_at = self.published_at

        scheduled_at = self.scheduled_at

        settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.settings, Unset):
            settings = self.settings.to_dict()

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        text = self.text

        title = self.title

        visibility = self.visibility

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
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
        if platform is not UNSET:
            field_dict["platform"] = platform
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
        if status is not UNSET:
            field_dict["status"] = status
        if text is not UNSET:
            field_dict["text"] = text
        if title is not UNSET:
            field_dict["title"] = title
        if visibility is not UNSET:
            field_dict["visibility"] = visibility

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_endpoints_media_input import ApiEndpointsMediaInput  # noqa: PLC0415
        from ..models.api_endpoints_post_target_error_response import (
            ApiEndpointsPostTargetErrorResponse,  # noqa: PLC0415
        )
        from ..models.api_endpoints_post_target_metrics_response import (
            ApiEndpointsPostTargetMetricsResponse,  # noqa: PLC0415
        )
        from ..models.api_endpoints_post_target_response_metadata import (
            ApiEndpointsPostTargetResponseMetadata,  # noqa: PLC0415
        )
        from ..models.api_endpoints_post_target_response_platform_data import (
            ApiEndpointsPostTargetResponsePlatformData,  # noqa: PLC0415
        )
        from ..models.social_api_ai_core_api_connectors_base_platform_media_item import (
            SocialApiAiCoreApiConnectorsBasePlatformMediaItem,  # noqa: PLC0415
        )
        from ..models.social_api_ai_core_api_connectors_base_post_settings import (
            SocialApiAiCoreApiConnectorsBasePostSettings,  # noqa: PLC0415
        )

        d = dict(src_dict)
        account_id = d.pop("account_id", UNSET)

        board_id = d.pop("board_id", UNSET)

        _error = d.pop("error", UNSET)
        error: ApiEndpointsPostTargetErrorResponse | Unset
        if isinstance(_error, Unset):
            error = UNSET
        else:
            error = ApiEndpointsPostTargetErrorResponse.from_dict(_error)

        first_comment = d.pop("first_comment", UNSET)

        _media = d.pop("media", UNSET)
        media: list[ApiEndpointsMediaInput] | Unset = UNSET
        if _media is not UNSET:
            media = []
            for media_item_data in _media:
                media_item = ApiEndpointsMediaInput.from_dict(media_item_data)

                media.append(media_item)

        media_ids = cast(list[str], d.pop("media_ids", UNSET))

        _media_type = d.pop("media_type", UNSET)
        media_type: ApiEndpointsPostTargetResponseMediaType | Unset
        if isinstance(_media_type, Unset):
            media_type = UNSET
        else:
            media_type = ApiEndpointsPostTargetResponseMediaType(_media_type)

        _metadata = d.pop("metadata", UNSET)
        metadata: ApiEndpointsPostTargetResponseMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = ApiEndpointsPostTargetResponseMetadata.from_dict(_metadata)

        _metrics = d.pop("metrics", UNSET)
        metrics: ApiEndpointsPostTargetMetricsResponse | Unset
        if isinstance(_metrics, Unset):
            metrics = UNSET
        else:
            metrics = ApiEndpointsPostTargetMetricsResponse.from_dict(_metrics)

        metrics_synced_at = d.pop("metrics_synced_at", UNSET)

        page_id = d.pop("page_id", UNSET)

        permalink = d.pop("permalink", UNSET)

        _platform = d.pop("platform", UNSET)
        platform: ApiEndpointsPostTargetResponsePlatform | Unset
        if isinstance(_platform, Unset):
            platform = UNSET
        else:
            platform = ApiEndpointsPostTargetResponsePlatform(_platform)

        _platform_data = d.pop("platform_data", UNSET)
        platform_data: ApiEndpointsPostTargetResponsePlatformData | Unset
        if isinstance(_platform_data, Unset):
            platform_data = UNSET
        else:
            platform_data = ApiEndpointsPostTargetResponsePlatformData.from_dict(_platform_data)

        _platform_media = d.pop("platform_media", UNSET)
        platform_media: list[SocialApiAiCoreApiConnectorsBasePlatformMediaItem] | Unset = UNSET
        if _platform_media is not UNSET:
            platform_media = []
            for platform_media_item_data in _platform_media:
                platform_media_item = SocialApiAiCoreApiConnectorsBasePlatformMediaItem.from_dict(
                    platform_media_item_data
                )

                platform_media.append(platform_media_item)

        platform_post_id = d.pop("platform_post_id", UNSET)

        published_at = d.pop("published_at", UNSET)

        scheduled_at = d.pop("scheduled_at", UNSET)

        _settings = d.pop("settings", UNSET)
        settings: SocialApiAiCoreApiConnectorsBasePostSettings | Unset
        if isinstance(_settings, Unset):
            settings = UNSET
        else:
            settings = SocialApiAiCoreApiConnectorsBasePostSettings.from_dict(_settings)

        _status = d.pop("status", UNSET)
        status: ApiEndpointsPostTargetResponseStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ApiEndpointsPostTargetResponseStatus(_status)

        text = d.pop("text", UNSET)

        title = d.pop("title", UNSET)

        visibility = d.pop("visibility", UNSET)

        api_endpoints_post_target_response = cls(
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
            platform=platform,
            platform_data=platform_data,
            platform_media=platform_media,
            platform_post_id=platform_post_id,
            published_at=published_at,
            scheduled_at=scheduled_at,
            settings=settings,
            status=status,
            text=text,
            title=title,
            visibility=visibility,
        )

        api_endpoints_post_target_response.additional_properties = d
        return api_endpoints_post_target_response

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
