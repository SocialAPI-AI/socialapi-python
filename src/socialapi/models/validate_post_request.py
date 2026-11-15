from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.platform import Platform
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.media_input import MediaInput
    from ..models.segment_request import SegmentRequest
    from ..models.target_request import TargetRequest
    from ..models.validate_post_request_platform_data import ValidatePostRequestPlatformData


T = TypeVar("T", bound="ValidatePostRequest")


@_attrs_define
class ValidatePostRequest:
    """
    Attributes:
        account_ids (list[str] | Unset): AccountIDs lists connected account IDs - their platforms are resolved
            automatically.
        media (list[MediaInput] | Unset): Media is the ordered, agnostic media list. Each item is a url, a media_id,
            or a platform_attachment_id; order and mixing are preserved. Supersedes media_ids.
        media_ids (list[str] | Unset): MediaIDs are media file IDs to validate (checks count and type limits).

            Deprecated: use Media with source_type "media_id". Ignored when media is set.
        platform_data (ValidatePostRequestPlatformData | Unset): PlatformData passes platform-specific fields keyed by
            platform name (e.g. {"instagram": {"content_type": "feed"}}). Folded into each matching target; a target's own
            platform_data wins on conflicts.
        platforms (list[Platform] | Unset): Platforms lists platform names to validate against (e.g. ["instagram",
            "linkedin"]).
        scheduled_at (datetime.datetime | Unset): ScheduledAt validates the schedule time (must be in the future, within
            platform limits). Example: 2026-04-01T10:00:00Z.
        segments (list[SegmentRequest] | Unset): Segments are continuation posts that publish as a native thread on X.
            Threads chaining is temporarily unavailable.
        targets (list[TargetRequest] | Unset): Targets validates per-target overrides if provided.
        text (str | Unset): Text is the post content to validate against platform constraints. Example: Check out our
            new product! #launch.
    """

    account_ids: list[str] | Unset = UNSET
    media: list[MediaInput] | Unset = UNSET
    media_ids: list[str] | Unset = UNSET
    platform_data: ValidatePostRequestPlatformData | Unset = UNSET
    platforms: list[Platform] | Unset = UNSET
    scheduled_at: datetime.datetime | Unset = UNSET
    segments: list[SegmentRequest] | Unset = UNSET
    targets: list[TargetRequest] | Unset = UNSET
    text: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_ids: list[str] | Unset = UNSET
        if not isinstance(self.account_ids, Unset):
            account_ids = self.account_ids

        media: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.media, Unset):
            media = []
            for media_item_data in self.media:
                media_item = media_item_data.to_dict()
                media.append(media_item)

        media_ids: list[str] | Unset = UNSET
        if not isinstance(self.media_ids, Unset):
            media_ids = self.media_ids

        platform_data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.platform_data, Unset):
            platform_data = self.platform_data.to_dict()

        platforms: list[str] | Unset = UNSET
        if not isinstance(self.platforms, Unset):
            platforms = []
            for platforms_item_data in self.platforms:
                platforms_item = platforms_item_data.value
                platforms.append(platforms_item)

        scheduled_at: str | Unset = UNSET
        if not isinstance(self.scheduled_at, Unset):
            scheduled_at = self.scheduled_at.isoformat()

        segments: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.segments, Unset):
            segments = []
            for segments_item_data in self.segments:
                segments_item = segments_item_data.to_dict()
                segments.append(segments_item)

        targets: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.targets, Unset):
            targets = []
            for targets_item_data in self.targets:
                targets_item = targets_item_data.to_dict()
                targets.append(targets_item)

        text = self.text

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_ids is not UNSET:
            field_dict["account_ids"] = account_ids
        if media is not UNSET:
            field_dict["media"] = media
        if media_ids is not UNSET:
            field_dict["media_ids"] = media_ids
        if platform_data is not UNSET:
            field_dict["platform_data"] = platform_data
        if platforms is not UNSET:
            field_dict["platforms"] = platforms
        if scheduled_at is not UNSET:
            field_dict["scheduled_at"] = scheduled_at
        if segments is not UNSET:
            field_dict["segments"] = segments
        if targets is not UNSET:
            field_dict["targets"] = targets
        if text is not UNSET:
            field_dict["text"] = text

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.media_input import MediaInput  # noqa: PLC0415
        from ..models.segment_request import SegmentRequest  # noqa: PLC0415
        from ..models.target_request import TargetRequest  # noqa: PLC0415
        from ..models.validate_post_request_platform_data import ValidatePostRequestPlatformData  # noqa: PLC0415

        d = dict(src_dict)
        account_ids = cast(list[str], d.pop("account_ids", UNSET))

        _media = d.pop("media", UNSET)
        media: list[MediaInput] | Unset = UNSET
        if _media is not UNSET:
            media = []
            for media_item_data in _media:
                media_item = MediaInput.from_dict(media_item_data)

                media.append(media_item)

        media_ids = cast(list[str], d.pop("media_ids", UNSET))

        _platform_data = d.pop("platform_data", UNSET)
        platform_data: ValidatePostRequestPlatformData | Unset
        if isinstance(_platform_data, Unset):
            platform_data = UNSET
        else:
            platform_data = ValidatePostRequestPlatformData.from_dict(_platform_data)

        _platforms = d.pop("platforms", UNSET)
        platforms: list[Platform] | Unset = UNSET
        if _platforms is not UNSET:
            platforms = []
            for platforms_item_data in _platforms:
                platforms_item = Platform(platforms_item_data)

                platforms.append(platforms_item)

        _scheduled_at = d.pop("scheduled_at", UNSET)
        scheduled_at: datetime.datetime | Unset
        if isinstance(_scheduled_at, Unset):
            scheduled_at = UNSET
        else:
            scheduled_at = datetime.datetime.fromisoformat(_scheduled_at)

        _segments = d.pop("segments", UNSET)
        segments: list[SegmentRequest] | Unset = UNSET
        if _segments is not UNSET:
            segments = []
            for segments_item_data in _segments:
                segments_item = SegmentRequest.from_dict(segments_item_data)

                segments.append(segments_item)

        _targets = d.pop("targets", UNSET)
        targets: list[TargetRequest] | Unset = UNSET
        if _targets is not UNSET:
            targets = []
            for targets_item_data in _targets:
                targets_item = TargetRequest.from_dict(targets_item_data)

                targets.append(targets_item)

        text = d.pop("text", UNSET)

        validate_post_request = cls(
            account_ids=account_ids,
            media=media,
            media_ids=media_ids,
            platform_data=platform_data,
            platforms=platforms,
            scheduled_at=scheduled_at,
            segments=segments,
            targets=targets,
            text=text,
        )

        validate_post_request.additional_properties = d
        return validate_post_request

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
