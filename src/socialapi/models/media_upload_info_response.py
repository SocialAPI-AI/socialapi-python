from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="MediaUploadInfoResponse")


@_attrs_define
class MediaUploadInfoResponse:
    """
    Attributes:
        expires_at (datetime.datetime):  Example: 2026-03-14T09:15:00Z.
        media_id (str):
        upload_url (str):
    """

    expires_at: datetime.datetime
    media_id: str
    upload_url: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        expires_at = self.expires_at.isoformat()

        media_id = self.media_id

        upload_url = self.upload_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "expires_at": expires_at,
                "media_id": media_id,
                "upload_url": upload_url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        expires_at = datetime.datetime.fromisoformat(d.pop("expires_at"))

        media_id = d.pop("media_id")

        upload_url = d.pop("upload_url")

        media_upload_info_response = cls(
            expires_at=expires_at,
            media_id=media_id,
            upload_url=upload_url,
        )

        media_upload_info_response.additional_properties = d
        return media_upload_info_response

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
