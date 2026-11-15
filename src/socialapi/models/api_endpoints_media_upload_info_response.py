from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiEndpointsMediaUploadInfoResponse")


@_attrs_define
class ApiEndpointsMediaUploadInfoResponse:
    """
    Attributes:
        expires_at (str | Unset):  Example: 2026-03-14T09:15:00Z.
        media_id (str | Unset):
        upload_url (str | Unset):
    """

    expires_at: str | Unset = UNSET
    media_id: str | Unset = UNSET
    upload_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        expires_at = self.expires_at

        media_id = self.media_id

        upload_url = self.upload_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at
        if media_id is not UNSET:
            field_dict["media_id"] = media_id
        if upload_url is not UNSET:
            field_dict["upload_url"] = upload_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        expires_at = d.pop("expires_at", UNSET)

        media_id = d.pop("media_id", UNSET)

        upload_url = d.pop("upload_url", UNSET)

        api_endpoints_media_upload_info_response = cls(
            expires_at=expires_at,
            media_id=media_id,
            upload_url=upload_url,
        )

        api_endpoints_media_upload_info_response.additional_properties = d
        return api_endpoints_media_upload_info_response

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
