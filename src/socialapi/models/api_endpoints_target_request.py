from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.api_endpoints_target_request_visibility import ApiEndpointsTargetRequestVisibility
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_endpoints_media_input import ApiEndpointsMediaInput
    from ..models.api_endpoints_target_request_platform_data import ApiEndpointsTargetRequestPlatformData


T = TypeVar("T", bound="ApiEndpointsTargetRequest")


@_attrs_define
class ApiEndpointsTargetRequest:
    """
    Attributes:
        account_id (str | Unset): AccountID is the connected account to publish to. Required. Example:
            acc_01HZ9X3Q4R5M6N7P8V2K0W1J.
        board_id (str | Unset): BoardID targets a specific board within a Pinterest account. Pinterest
            targets use board_id; page_id is also accepted as an alias, but supplying
            both is an error. Example: 8828.
        first_comment (str | Unset): FirstComment overrides the post-level first comment for this target.
        media (list[ApiEndpointsMediaInput] | Unset): Media is the ordered, agnostic media list. Each item is a url, a
            media_id,
            or a platform_attachment_id; order and mixing are preserved. Supersedes media_ids.
        media_ids (list[str] | Unset): MediaIDs overrides the post-level media for this target.

            Deprecated: use Media with source_type "media_id". Ignored when media is set.
        page_id (str | Unset): PageID optionally targets a specific page within the account (e.g. Facebook Page).
            Example: sapi_page_01JRQX....
        platform_data (ApiEndpointsTargetRequestPlatformData | Unset): PlatformData passes platform-specific fields
            (e.g. TikTok privacy settings, LinkedIn article metadata).
        scheduled_at (str | Unset): ScheduledAt overrides the post-level schedule time for this target. Example:
            2026-04-01T10:00:00Z.
        text (str | Unset): Text overrides the post-level text for this target. Example: Platform-specific version of
            the post.
        title (str | Unset): Title overrides the post-level title for this target. Example: Custom title for LinkedIn.
        visibility (ApiEndpointsTargetRequestVisibility | Unset): Visibility overrides the post-level visibility for
            this target. Example: public.
    """

    account_id: str | Unset = UNSET
    board_id: str | Unset = UNSET
    first_comment: str | Unset = UNSET
    media: list[ApiEndpointsMediaInput] | Unset = UNSET
    media_ids: list[str] | Unset = UNSET
    page_id: str | Unset = UNSET
    platform_data: ApiEndpointsTargetRequestPlatformData | Unset = UNSET
    scheduled_at: str | Unset = UNSET
    text: str | Unset = UNSET
    title: str | Unset = UNSET
    visibility: ApiEndpointsTargetRequestVisibility | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_id = self.account_id

        board_id = self.board_id

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

        page_id = self.page_id

        platform_data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.platform_data, Unset):
            platform_data = self.platform_data.to_dict()

        scheduled_at = self.scheduled_at

        text = self.text

        title = self.title

        visibility: str | Unset = UNSET
        if not isinstance(self.visibility, Unset):
            visibility = self.visibility.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_id is not UNSET:
            field_dict["account_id"] = account_id
        if board_id is not UNSET:
            field_dict["board_id"] = board_id
        if first_comment is not UNSET:
            field_dict["first_comment"] = first_comment
        if media is not UNSET:
            field_dict["media"] = media
        if media_ids is not UNSET:
            field_dict["media_ids"] = media_ids
        if page_id is not UNSET:
            field_dict["page_id"] = page_id
        if platform_data is not UNSET:
            field_dict["platform_data"] = platform_data
        if scheduled_at is not UNSET:
            field_dict["scheduled_at"] = scheduled_at
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
        from ..models.api_endpoints_target_request_platform_data import (
            ApiEndpointsTargetRequestPlatformData,  # noqa: PLC0415
        )

        d = dict(src_dict)
        account_id = d.pop("account_id", UNSET)

        board_id = d.pop("board_id", UNSET)

        first_comment = d.pop("first_comment", UNSET)

        _media = d.pop("media", UNSET)
        media: list[ApiEndpointsMediaInput] | Unset = UNSET
        if _media is not UNSET:
            media = []
            for media_item_data in _media:
                media_item = ApiEndpointsMediaInput.from_dict(media_item_data)

                media.append(media_item)

        media_ids = cast(list[str], d.pop("media_ids", UNSET))

        page_id = d.pop("page_id", UNSET)

        _platform_data = d.pop("platform_data", UNSET)
        platform_data: ApiEndpointsTargetRequestPlatformData | Unset
        if isinstance(_platform_data, Unset):
            platform_data = UNSET
        else:
            platform_data = ApiEndpointsTargetRequestPlatformData.from_dict(_platform_data)

        scheduled_at = d.pop("scheduled_at", UNSET)

        text = d.pop("text", UNSET)

        title = d.pop("title", UNSET)

        _visibility = d.pop("visibility", UNSET)
        visibility: ApiEndpointsTargetRequestVisibility | Unset
        if isinstance(_visibility, Unset):
            visibility = UNSET
        else:
            visibility = ApiEndpointsTargetRequestVisibility(_visibility)

        api_endpoints_target_request = cls(
            account_id=account_id,
            board_id=board_id,
            first_comment=first_comment,
            media=media,
            media_ids=media_ids,
            page_id=page_id,
            platform_data=platform_data,
            scheduled_at=scheduled_at,
            text=text,
            title=title,
            visibility=visibility,
        )

        api_endpoints_target_request.additional_properties = d
        return api_endpoints_target_request

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
