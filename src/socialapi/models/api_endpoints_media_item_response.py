from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiEndpointsMediaItemResponse")


@_attrs_define
class ApiEndpointsMediaItemResponse:
    """
    Attributes:
        content_type (str | Unset):  Example: image/jpeg.
        created_at (str | Unset):  Example: 2026-03-20T09:00:00Z.
        filename (str | Unset):  Example: photo.jpg.
        id (str | Unset):  Example: 550e8400-e29b-41d4-a716-446655440000.
        size_bytes (int | Unset):  Example: 2048576.
        status (str | Unset):  Example: ready.
        url (str | Unset):  Example: https://s3.example.com/media/....
    """

    content_type: str | Unset = UNSET
    created_at: str | Unset = UNSET
    filename: str | Unset = UNSET
    id: str | Unset = UNSET
    size_bytes: int | Unset = UNSET
    status: str | Unset = UNSET
    url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        content_type = self.content_type

        created_at = self.created_at

        filename = self.filename

        id = self.id

        size_bytes = self.size_bytes

        status = self.status

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if content_type is not UNSET:
            field_dict["content_type"] = content_type
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if filename is not UNSET:
            field_dict["filename"] = filename
        if id is not UNSET:
            field_dict["id"] = id
        if size_bytes is not UNSET:
            field_dict["size_bytes"] = size_bytes
        if status is not UNSET:
            field_dict["status"] = status
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        content_type = d.pop("content_type", UNSET)

        created_at = d.pop("created_at", UNSET)

        filename = d.pop("filename", UNSET)

        id = d.pop("id", UNSET)

        size_bytes = d.pop("size_bytes", UNSET)

        status = d.pop("status", UNSET)

        url = d.pop("url", UNSET)

        api_endpoints_media_item_response = cls(
            content_type=content_type,
            created_at=created_at,
            filename=filename,
            id=id,
            size_bytes=size_bytes,
            status=status,
            url=url,
        )

        api_endpoints_media_item_response.additional_properties = d
        return api_endpoints_media_item_response

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
