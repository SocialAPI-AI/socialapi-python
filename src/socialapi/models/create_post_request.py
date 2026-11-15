from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.post_visibility import PostVisibility
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_post_request_platform_data import CreatePostRequestPlatformData
    from ..models.media_input import MediaInput
    from ..models.segment_request import SegmentRequest
    from ..models.stagger_request import StaggerRequest
    from ..models.target_request import TargetRequest


T = TypeVar("T", bound="CreatePostRequest")


@_attrs_define
class CreatePostRequest:
    """
    Attributes:
        first_comment (str | Unset): FirstComment is auto-posted as the first comment after publishing (Instagram,
            Facebook, YouTube). Ignored by every other platform, and by Facebook Page Stories. Example: Follow us for more
            updates!.
        media (list[MediaInput] | Unset): Media is the ordered, agnostic media list. Each item is a url, a media_id,
            or a platform_attachment_id; order and mixing are preserved. Supersedes media_ids.
        media_ids (list[str] | Unset): MediaIDs are previously uploaded media file IDs to attach.

            Deprecated: use Media with source_type "media_id". Ignored when media is set.
        platform_data (CreatePostRequestPlatformData | Unset): PlatformData passes platform-specific fields keyed by
            platform name (e.g. {"instagram": {"content_type": "feed"}}). Folded into each matching target; a target's own
            platform_data wins on conflicts.
        publish_now (bool | Unset): PublishNow publishes immediately when targets are provided (ignores scheduled_at).
            Without this flag (and without scheduled_at) the post is saved as a draft; publish it later with POST
            /posts/{post_id}/publish. Example: False.
        queue_id (str | Unset): QueueID puts the post in a Queue: it takes the Queue's earliest free time and is
            scheduled. Send a Queue ID, or "default" for the default Queue of the targets' Brand. Requires targets, all in
            one Brand. Cannot be combined with scheduled_at, publish_now or a target's scheduled_at. Example:
            que_01J9Z8Y7X6W5V4T3S2R1Q0P9N8.
        scheduled_at (datetime.datetime | Unset): ScheduledAt queues the post for future publication (RFC3339). When
            set, the post is scheduled rather than drafted. Example: 2026-04-01T10:00:00Z.
        segments (list[SegmentRequest] | Unset): Segments are continuation posts that publish as a native thread on X.
            Threads chaining is temporarily unavailable.
        skip_duplicate_check (bool | Unset): SkipDuplicateCheck bypasses the duplicate content detection. Example:
            False.
        skip_validation (bool | Unset): SkipValidation bypasses pre-publish validation. The post is scheduled/published
            as-is and may fail at the platform. Example: False.
        stagger (StaggerRequest | Unset):
        targets (list[TargetRequest] | Unset): Targets specifies which connected accounts to publish to, with optional
            per-target overrides.
        text (str | Unset): Text is the post body content. Required, unless every target supplies a
            body of its own through text or a platform_data field the connector uses
            as the body (e.g. Pinterest's platform_data.description IS the pin body). Example: Check out our new product
            launch! #newproduct.
        title (str | Unset): Title is an optional post title (used by LinkedIn, Google). Example: Exciting News from
            Acme Corp.
        visibility (PostVisibility | Unset):
    """

    first_comment: str | Unset = UNSET
    media: list[MediaInput] | Unset = UNSET
    media_ids: list[str] | Unset = UNSET
    platform_data: CreatePostRequestPlatformData | Unset = UNSET
    publish_now: bool | Unset = UNSET
    queue_id: str | Unset = UNSET
    scheduled_at: datetime.datetime | Unset = UNSET
    segments: list[SegmentRequest] | Unset = UNSET
    skip_duplicate_check: bool | Unset = UNSET
    skip_validation: bool | Unset = UNSET
    stagger: StaggerRequest | Unset = UNSET
    targets: list[TargetRequest] | Unset = UNSET
    text: str | Unset = UNSET
    title: str | Unset = UNSET
    visibility: PostVisibility | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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

        platform_data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.platform_data, Unset):
            platform_data = self.platform_data.to_dict()

        publish_now = self.publish_now

        queue_id = self.queue_id

        scheduled_at: str | Unset = UNSET
        if not isinstance(self.scheduled_at, Unset):
            scheduled_at = self.scheduled_at.isoformat()

        segments: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.segments, Unset):
            segments = []
            for segments_item_data in self.segments:
                segments_item = segments_item_data.to_dict()
                segments.append(segments_item)

        skip_duplicate_check = self.skip_duplicate_check

        skip_validation = self.skip_validation

        stagger: dict[str, Any] | Unset = UNSET
        if not isinstance(self.stagger, Unset):
            stagger = self.stagger.to_dict()

        targets: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.targets, Unset):
            targets = []
            for targets_item_data in self.targets:
                targets_item = targets_item_data.to_dict()
                targets.append(targets_item)

        text = self.text

        title = self.title

        visibility: str | Unset = UNSET
        if not isinstance(self.visibility, Unset):
            visibility = self.visibility.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if first_comment is not UNSET:
            field_dict["first_comment"] = first_comment
        if media is not UNSET:
            field_dict["media"] = media
        if media_ids is not UNSET:
            field_dict["media_ids"] = media_ids
        if platform_data is not UNSET:
            field_dict["platform_data"] = platform_data
        if publish_now is not UNSET:
            field_dict["publish_now"] = publish_now
        if queue_id is not UNSET:
            field_dict["queue_id"] = queue_id
        if scheduled_at is not UNSET:
            field_dict["scheduled_at"] = scheduled_at
        if segments is not UNSET:
            field_dict["segments"] = segments
        if skip_duplicate_check is not UNSET:
            field_dict["skip_duplicate_check"] = skip_duplicate_check
        if skip_validation is not UNSET:
            field_dict["skip_validation"] = skip_validation
        if stagger is not UNSET:
            field_dict["stagger"] = stagger
        if targets is not UNSET:
            field_dict["targets"] = targets
        if text is not UNSET:
            field_dict["text"] = text
        if title is not UNSET:
            field_dict["title"] = title
        if visibility is not UNSET:
            field_dict["visibility"] = visibility

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_post_request_platform_data import CreatePostRequestPlatformData  # noqa: PLC0415
        from ..models.media_input import MediaInput  # noqa: PLC0415
        from ..models.segment_request import SegmentRequest  # noqa: PLC0415
        from ..models.stagger_request import StaggerRequest  # noqa: PLC0415
        from ..models.target_request import TargetRequest  # noqa: PLC0415

        d = dict(src_dict)
        first_comment = d.pop("first_comment", UNSET)

        _media = d.pop("media", UNSET)
        media: list[MediaInput] | Unset = UNSET
        if _media is not UNSET:
            media = []
            for media_item_data in _media:
                media_item = MediaInput.from_dict(media_item_data)

                media.append(media_item)

        media_ids = cast(list[str], d.pop("media_ids", UNSET))

        _platform_data = d.pop("platform_data", UNSET)
        platform_data: CreatePostRequestPlatformData | Unset
        if isinstance(_platform_data, Unset):
            platform_data = UNSET
        else:
            platform_data = CreatePostRequestPlatformData.from_dict(_platform_data)

        publish_now = d.pop("publish_now", UNSET)

        queue_id = d.pop("queue_id", UNSET)

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

        skip_duplicate_check = d.pop("skip_duplicate_check", UNSET)

        skip_validation = d.pop("skip_validation", UNSET)

        _stagger = d.pop("stagger", UNSET)
        stagger: StaggerRequest | Unset
        if isinstance(_stagger, Unset):
            stagger = UNSET
        else:
            stagger = StaggerRequest.from_dict(_stagger)

        _targets = d.pop("targets", UNSET)
        targets: list[TargetRequest] | Unset = UNSET
        if _targets is not UNSET:
            targets = []
            for targets_item_data in _targets:
                targets_item = TargetRequest.from_dict(targets_item_data)

                targets.append(targets_item)

        text = d.pop("text", UNSET)

        title = d.pop("title", UNSET)

        _visibility = d.pop("visibility", UNSET)
        visibility: PostVisibility | Unset
        if isinstance(_visibility, Unset):
            visibility = UNSET
        else:
            visibility = PostVisibility(_visibility)

        create_post_request = cls(
            first_comment=first_comment,
            media=media,
            media_ids=media_ids,
            platform_data=platform_data,
            publish_now=publish_now,
            queue_id=queue_id,
            scheduled_at=scheduled_at,
            segments=segments,
            skip_duplicate_check=skip_duplicate_check,
            skip_validation=skip_validation,
            stagger=stagger,
            targets=targets,
            text=text,
            title=title,
            visibility=visibility,
        )

        create_post_request.additional_properties = d
        return create_post_request

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
