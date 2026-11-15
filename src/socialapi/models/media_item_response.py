from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="MediaItemResponse")


@_attrs_define
class MediaItemResponse:
    """
    Attributes:
        content_type (str):  Example: image/jpeg.
        created_at (datetime.datetime):  Example: 2026-03-20T09:00:00Z.
        filename (str):  Example: photo.jpg.
        id (str):  Example: 550e8400-e29b-41d4-a716-446655440000.
        size_bytes (int):  Example: 2048576.
        status (str):  Example: ready.
        url (str):  Example: https://s3.example.com/media/....
    """

    content_type: str
    created_at: datetime.datetime
    filename: str
    id: str
    size_bytes: int
    status: str
    url: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        content_type = self.content_type

        created_at = self.created_at.isoformat()

        filename = self.filename

        id = self.id

        size_bytes = self.size_bytes

        status = self.status

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "content_type": content_type,
                "created_at": created_at,
                "filename": filename,
                "id": id,
                "size_bytes": size_bytes,
                "status": status,
                "url": url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        content_type = d.pop("content_type")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        filename = d.pop("filename")

        id = d.pop("id")

        size_bytes = d.pop("size_bytes")

        status = d.pop("status")

        url = d.pop("url")

        media_item_response = cls(
            content_type=content_type,
            created_at=created_at,
            filename=filename,
            id=id,
            size_bytes=size_bytes,
            status=status,
            url=url,
        )

        media_item_response.additional_properties = d
        return media_item_response

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
