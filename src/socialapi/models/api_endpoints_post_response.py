from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.api_endpoints_post_response_status import ApiEndpointsPostResponseStatus
from ..models.api_endpoints_post_response_visibility import ApiEndpointsPostResponseVisibility
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_endpoints_media_input import ApiEndpointsMediaInput
    from ..models.api_endpoints_post_target_response import ApiEndpointsPostTargetResponse


T = TypeVar("T", bound="ApiEndpointsPostResponse")


@_attrs_define
class ApiEndpointsPostResponse:
    """
    Attributes:
        created_at (str | Unset):  Example: 2026-03-14T09:00:00Z.
        hidden (bool | Unset):  Example: False.
        id (str | Unset):  Example: p_01HZ9X3Q4R5M6N7P8V2K0W1J.
        media (list[ApiEndpointsMediaInput] | Unset):
        media_ids (list[str] | Unset): Deprecated: use media.
        published_at (str | Unset):  Example: 2026-04-01T10:00:05Z.
        queue_id (str | Unset): ID of the Queue the post is in. null when the post is not queued. Example:
            que_01J9Z8Y7X6W5V4T3S2R1Q0P9N8.
        retry_count (int | Unset):  Example: 0.
        scheduled_at (str | Unset):  Example: 2026-04-01T10:00:00Z.
        status (ApiEndpointsPostResponseStatus | Unset):  Example: published.
        targets (list[ApiEndpointsPostTargetResponse] | Unset):
        text (str | Unset):  Example: Check out our new product launch!.
        title (str | Unset):  Example: Exciting News.
        updated_at (str | Unset):  Example: 2026-03-14T09:00:00Z.
        visibility (ApiEndpointsPostResponseVisibility | Unset):  Example: public.
    """

    created_at: str | Unset = UNSET
    hidden: bool | Unset = UNSET
    id: str | Unset = UNSET
    media: list[ApiEndpointsMediaInput] | Unset = UNSET
    media_ids: list[str] | Unset = UNSET
    published_at: str | Unset = UNSET
    queue_id: str | Unset = UNSET
    retry_count: int | Unset = UNSET
    scheduled_at: str | Unset = UNSET
    status: ApiEndpointsPostResponseStatus | Unset = UNSET
    targets: list[ApiEndpointsPostTargetResponse] | Unset = UNSET
    text: str | Unset = UNSET
    title: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    visibility: ApiEndpointsPostResponseVisibility | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        hidden = self.hidden

        id = self.id

        media: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.media, Unset):
            media = []
            for media_item_data in self.media:
                media_item = media_item_data.to_dict()
                media.append(media_item)

        media_ids: list[str] | Unset = UNSET
        if not isinstance(self.media_ids, Unset):
            media_ids = self.media_ids

        published_at = self.published_at

        queue_id = self.queue_id

        retry_count = self.retry_count

        scheduled_at = self.scheduled_at

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        targets: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.targets, Unset):
            targets = []
            for targets_item_data in self.targets:
                targets_item = targets_item_data.to_dict()
                targets.append(targets_item)

        text = self.text

        title = self.title

        updated_at = self.updated_at

        visibility: str | Unset = UNSET
        if not isinstance(self.visibility, Unset):
            visibility = self.visibility.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if hidden is not UNSET:
            field_dict["hidden"] = hidden
        if id is not UNSET:
            field_dict["id"] = id
        if media is not UNSET:
            field_dict["media"] = media
        if media_ids is not UNSET:
            field_dict["media_ids"] = media_ids
        if published_at is not UNSET:
            field_dict["published_at"] = published_at
        if queue_id is not UNSET:
            field_dict["queue_id"] = queue_id
        if retry_count is not UNSET:
            field_dict["retry_count"] = retry_count
        if scheduled_at is not UNSET:
            field_dict["scheduled_at"] = scheduled_at
        if status is not UNSET:
            field_dict["status"] = status
        if targets is not UNSET:
            field_dict["targets"] = targets
        if text is not UNSET:
            field_dict["text"] = text
        if title is not UNSET:
            field_dict["title"] = title
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if visibility is not UNSET:
            field_dict["visibility"] = visibility

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_endpoints_media_input import ApiEndpointsMediaInput  # noqa: PLC0415
        from ..models.api_endpoints_post_target_response import ApiEndpointsPostTargetResponse  # noqa: PLC0415

        d = dict(src_dict)
        created_at = d.pop("created_at", UNSET)

        hidden = d.pop("hidden", UNSET)

        id = d.pop("id", UNSET)

        _media = d.pop("media", UNSET)
        media: list[ApiEndpointsMediaInput] | Unset = UNSET
        if _media is not UNSET:
            media = []
            for media_item_data in _media:
                media_item = ApiEndpointsMediaInput.from_dict(media_item_data)

                media.append(media_item)

        media_ids = cast(list[str], d.pop("media_ids", UNSET))

        published_at = d.pop("published_at", UNSET)

        queue_id = d.pop("queue_id", UNSET)

        retry_count = d.pop("retry_count", UNSET)

        scheduled_at = d.pop("scheduled_at", UNSET)

        _status = d.pop("status", UNSET)
        status: ApiEndpointsPostResponseStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ApiEndpointsPostResponseStatus(_status)

        _targets = d.pop("targets", UNSET)
        targets: list[ApiEndpointsPostTargetResponse] | Unset = UNSET
        if _targets is not UNSET:
            targets = []
            for targets_item_data in _targets:
                targets_item = ApiEndpointsPostTargetResponse.from_dict(targets_item_data)

                targets.append(targets_item)

        text = d.pop("text", UNSET)

        title = d.pop("title", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        _visibility = d.pop("visibility", UNSET)
        visibility: ApiEndpointsPostResponseVisibility | Unset
        if isinstance(_visibility, Unset):
            visibility = UNSET
        else:
            visibility = ApiEndpointsPostResponseVisibility(_visibility)

        api_endpoints_post_response = cls(
            created_at=created_at,
            hidden=hidden,
            id=id,
            media=media,
            media_ids=media_ids,
            published_at=published_at,
            queue_id=queue_id,
            retry_count=retry_count,
            scheduled_at=scheduled_at,
            status=status,
            targets=targets,
            text=text,
            title=title,
            updated_at=updated_at,
            visibility=visibility,
        )

        api_endpoints_post_response.additional_properties = d
        return api_endpoints_post_response

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
