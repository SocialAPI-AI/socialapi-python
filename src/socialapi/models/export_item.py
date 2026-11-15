from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.platform import Platform
from ..types import UNSET, Unset

T = TypeVar("T", bound="ExportItem")


@_attrs_define
class ExportItem:
    """
    Attributes:
        account_id (str):
        created_at (datetime.datetime):
        expires_at (datetime.datetime):
        id (str):
        platform (Platform):
        processed_videos (int):
        status (str):
        total_videos (int):
        completed_at (datetime.datetime | Unset):
        error (str | Unset):
    """

    account_id: str
    created_at: datetime.datetime
    expires_at: datetime.datetime
    id: str
    platform: Platform
    processed_videos: int
    status: str
    total_videos: int
    completed_at: datetime.datetime | Unset = UNSET
    error: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_id = self.account_id

        created_at = self.created_at.isoformat()

        expires_at = self.expires_at.isoformat()

        id = self.id

        platform = self.platform.value

        processed_videos = self.processed_videos

        status = self.status

        total_videos = self.total_videos

        completed_at: str | Unset = UNSET
        if not isinstance(self.completed_at, Unset):
            completed_at = self.completed_at.isoformat()

        error = self.error

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "account_id": account_id,
                "created_at": created_at,
                "expires_at": expires_at,
                "id": id,
                "platform": platform,
                "processed_videos": processed_videos,
                "status": status,
                "total_videos": total_videos,
            }
        )
        if completed_at is not UNSET:
            field_dict["completed_at"] = completed_at
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_id = d.pop("account_id")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        expires_at = datetime.datetime.fromisoformat(d.pop("expires_at"))

        id = d.pop("id")

        platform = Platform(d.pop("platform"))

        processed_videos = d.pop("processed_videos")

        status = d.pop("status")

        total_videos = d.pop("total_videos")

        _completed_at = d.pop("completed_at", UNSET)
        completed_at: datetime.datetime | Unset
        if isinstance(_completed_at, Unset):
            completed_at = UNSET
        else:
            completed_at = datetime.datetime.fromisoformat(_completed_at)

        error = d.pop("error", UNSET)

        export_item = cls(
            account_id=account_id,
            created_at=created_at,
            expires_at=expires_at,
            id=id,
            platform=platform,
            processed_videos=processed_videos,
            status=status,
            total_videos=total_videos,
            completed_at=completed_at,
            error=error,
        )

        export_item.additional_properties = d
        return export_item

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
