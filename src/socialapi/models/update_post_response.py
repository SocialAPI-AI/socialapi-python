from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.post_status import PostStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.media_input import MediaInput
    from ..models.post_target_response import PostTargetResponse


T = TypeVar("T", bound="UpdatePostResponse")


@_attrs_define
class UpdatePostResponse:
    """
    Attributes:
        created_at (datetime.datetime):  Example: 2026-03-14T09:00:00Z.
        hidden (bool):  Example: False.
        id (str):  Example: p_01HZ9X3Q4R5M6N7P8V2K0W1J.
        queue_id (None | str): ID of the Queue the post is in. null when the post is not queued. Example:
            que_01J9Z8Y7X6W5V4T3S2R1Q0P9N8.
        retry_count (int):  Example: 0.
        status (PostStatus):
        text (None | str):  Example: Check out our new product launch!.
        updated_at (datetime.datetime):  Example: 2026-03-14T09:00:00Z.
        media (list[MediaInput] | Unset):
        media_ids (list[str] | Unset): Deprecated: use media.
        not_updated_account_ids (list[str] | Unset): Accounts whose live post kept its published text because the
            platform does not allow editing it, for example Instagram captions or Facebook Reels. Absent when every live
            target was edited. Example: ['acc_01HZ9X3Q4R5M6N7P8V2K0W1J'].
        published_at (datetime.datetime | Unset):  Example: 2026-04-01T10:00:05Z.
        scheduled_at (datetime.datetime | Unset):  Example: 2026-04-01T10:00:00Z.
        targets (list[PostTargetResponse] | Unset):
        title (str | Unset):  Example: Exciting News.
        visibility (str | Unset): Who can see the post, as set when it was created or last updated: public, private,
            connections_only or logged_in. Example: public.
    """

    created_at: datetime.datetime
    hidden: bool
    id: str
    queue_id: None | str
    retry_count: int
    status: PostStatus
    text: None | str
    updated_at: datetime.datetime
    media: list[MediaInput] | Unset = UNSET
    media_ids: list[str] | Unset = UNSET
    not_updated_account_ids: list[str] | Unset = UNSET
    published_at: datetime.datetime | Unset = UNSET
    scheduled_at: datetime.datetime | Unset = UNSET
    targets: list[PostTargetResponse] | Unset = UNSET
    title: str | Unset = UNSET
    visibility: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        hidden = self.hidden

        id = self.id

        queue_id: None | str
        queue_id = self.queue_id

        retry_count = self.retry_count

        status = self.status.value

        text: None | str
        text = self.text

        updated_at = self.updated_at.isoformat()

        media: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.media, Unset):
            media = []
            for media_item_data in self.media:
                media_item = media_item_data.to_dict()
                media.append(media_item)

        media_ids: list[str] | Unset = UNSET
        if not isinstance(self.media_ids, Unset):
            media_ids = self.media_ids

        not_updated_account_ids: list[str] | Unset = UNSET
        if not isinstance(self.not_updated_account_ids, Unset):
            not_updated_account_ids = self.not_updated_account_ids

        published_at: str | Unset = UNSET
        if not isinstance(self.published_at, Unset):
            published_at = self.published_at.isoformat()

        scheduled_at: str | Unset = UNSET
        if not isinstance(self.scheduled_at, Unset):
            scheduled_at = self.scheduled_at.isoformat()

        targets: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.targets, Unset):
            targets = []
            for targets_item_data in self.targets:
                targets_item = targets_item_data.to_dict()
                targets.append(targets_item)

        title = self.title

        visibility = self.visibility

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_at": created_at,
                "hidden": hidden,
                "id": id,
                "queue_id": queue_id,
                "retry_count": retry_count,
                "status": status,
                "text": text,
                "updated_at": updated_at,
            }
        )
        if media is not UNSET:
            field_dict["media"] = media
        if media_ids is not UNSET:
            field_dict["media_ids"] = media_ids
        if not_updated_account_ids is not UNSET:
            field_dict["not_updated_account_ids"] = not_updated_account_ids
        if published_at is not UNSET:
            field_dict["published_at"] = published_at
        if scheduled_at is not UNSET:
            field_dict["scheduled_at"] = scheduled_at
        if targets is not UNSET:
            field_dict["targets"] = targets
        if title is not UNSET:
            field_dict["title"] = title
        if visibility is not UNSET:
            field_dict["visibility"] = visibility

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.media_input import MediaInput  # noqa: PLC0415
        from ..models.post_target_response import PostTargetResponse  # noqa: PLC0415

        d = dict(src_dict)
        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        hidden = d.pop("hidden")

        id = d.pop("id")

        def _parse_queue_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        queue_id = _parse_queue_id(d.pop("queue_id"))

        retry_count = d.pop("retry_count")

        status = PostStatus(d.pop("status"))

        def _parse_text(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        text = _parse_text(d.pop("text"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        _media = d.pop("media", UNSET)
        media: list[MediaInput] | Unset = UNSET
        if _media is not UNSET:
            media = []
            for media_item_data in _media:
                media_item = MediaInput.from_dict(media_item_data)

                media.append(media_item)

        media_ids = cast(list[str], d.pop("media_ids", UNSET))

        not_updated_account_ids = cast(list[str], d.pop("not_updated_account_ids", UNSET))

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

        _targets = d.pop("targets", UNSET)
        targets: list[PostTargetResponse] | Unset = UNSET
        if _targets is not UNSET:
            targets = []
            for targets_item_data in _targets:
                targets_item = PostTargetResponse.from_dict(targets_item_data)

                targets.append(targets_item)

        title = d.pop("title", UNSET)

        visibility = d.pop("visibility", UNSET)

        update_post_response = cls(
            created_at=created_at,
            hidden=hidden,
            id=id,
            queue_id=queue_id,
            retry_count=retry_count,
            status=status,
            text=text,
            updated_at=updated_at,
            media=media,
            media_ids=media_ids,
            not_updated_account_ids=not_updated_account_ids,
            published_at=published_at,
            scheduled_at=scheduled_at,
            targets=targets,
            title=title,
            visibility=visibility,
        )

        update_post_response.additional_properties = d
        return update_post_response

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
