from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.platform import Platform

if TYPE_CHECKING:
    from ..models.export_video_item import ExportVideoItem


T = TypeVar("T", bound="ExportVideosResponse")


@_attrs_define
class ExportVideosResponse:
    """
    Attributes:
        account_id (str):
        platform (Platform):
        videos (list[ExportVideoItem] | None):
    """

    account_id: str
    platform: Platform
    videos: list[ExportVideoItem] | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_id = self.account_id

        platform = self.platform.value

        videos: list[dict[str, Any]] | None
        if isinstance(self.videos, list):
            videos = []
            for videos_type_0_item_data in self.videos:
                videos_type_0_item = videos_type_0_item_data.to_dict()
                videos.append(videos_type_0_item)

        else:
            videos = self.videos

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "account_id": account_id,
                "platform": platform,
                "videos": videos,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.export_video_item import ExportVideoItem  # noqa: PLC0415

        d = dict(src_dict)
        account_id = d.pop("account_id")

        platform = Platform(d.pop("platform"))

        def _parse_videos(data: object) -> list[ExportVideoItem] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                videos_type_0 = []
                _videos_type_0 = data
                for videos_type_0_item_data in _videos_type_0:
                    videos_type_0_item = ExportVideoItem.from_dict(videos_type_0_item_data)

                    videos_type_0.append(videos_type_0_item)

                return videos_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ExportVideoItem] | None, data)

        videos = _parse_videos(d.pop("videos"))

        export_videos_response = cls(
            account_id=account_id,
            platform=platform,
            videos=videos,
        )

        export_videos_response.additional_properties = d
        return export_videos_response

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
