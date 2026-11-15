from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_endpoints_export_video_item import ApiEndpointsExportVideoItem


T = TypeVar("T", bound="ApiEndpointsExportVideosResponse")


@_attrs_define
class ApiEndpointsExportVideosResponse:
    """
    Attributes:
        account_id (str | Unset):
        platform (str | Unset):
        videos (list[ApiEndpointsExportVideoItem] | Unset):
    """

    account_id: str | Unset = UNSET
    platform: str | Unset = UNSET
    videos: list[ApiEndpointsExportVideoItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_id = self.account_id

        platform = self.platform

        videos: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.videos, Unset):
            videos = []
            for videos_item_data in self.videos:
                videos_item = videos_item_data.to_dict()
                videos.append(videos_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_id is not UNSET:
            field_dict["account_id"] = account_id
        if platform is not UNSET:
            field_dict["platform"] = platform
        if videos is not UNSET:
            field_dict["videos"] = videos

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_endpoints_export_video_item import ApiEndpointsExportVideoItem  # noqa: PLC0415

        d = dict(src_dict)
        account_id = d.pop("account_id", UNSET)

        platform = d.pop("platform", UNSET)

        _videos = d.pop("videos", UNSET)
        videos: list[ApiEndpointsExportVideoItem] | Unset = UNSET
        if _videos is not UNSET:
            videos = []
            for videos_item_data in _videos:
                videos_item = ApiEndpointsExportVideoItem.from_dict(videos_item_data)

                videos.append(videos_item)

        api_endpoints_export_videos_response = cls(
            account_id=account_id,
            platform=platform,
            videos=videos,
        )

        api_endpoints_export_videos_response.additional_properties = d
        return api_endpoints_export_videos_response

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
