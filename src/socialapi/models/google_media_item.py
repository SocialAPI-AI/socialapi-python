from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.google_media_attribution import GoogleMediaAttribution
    from ..models.media_ref import MediaRef


T = TypeVar("T", bound="GoogleMediaItem")


@_attrs_define
class GoogleMediaItem:
    """
    Attributes:
        id (str):  Example: accounts/123/locations/456/media/789.
        media (MediaRef):
        attribution (GoogleMediaAttribution | Unset):
        category (str | Unset):  Example: INTERIOR.
        created_at (datetime.datetime | Unset):  Example: 2026-03-01T12:00:00Z.
        description (str | Unset):  Example: Main dining room.
        height_pixels (int | Unset):  Example: 1200.
        thumbnail_url (str | Unset):
        width_pixels (int | Unset):  Example: 1600.
    """

    id: str
    media: MediaRef
    attribution: GoogleMediaAttribution | Unset = UNSET
    category: str | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    description: str | Unset = UNSET
    height_pixels: int | Unset = UNSET
    thumbnail_url: str | Unset = UNSET
    width_pixels: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        media = self.media.to_dict()

        attribution: dict[str, Any] | Unset = UNSET
        if not isinstance(self.attribution, Unset):
            attribution = self.attribution.to_dict()

        category = self.category

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        description = self.description

        height_pixels = self.height_pixels

        thumbnail_url = self.thumbnail_url

        width_pixels = self.width_pixels

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "media": media,
            }
        )
        if attribution is not UNSET:
            field_dict["attribution"] = attribution
        if category is not UNSET:
            field_dict["category"] = category
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if description is not UNSET:
            field_dict["description"] = description
        if height_pixels is not UNSET:
            field_dict["height_pixels"] = height_pixels
        if thumbnail_url is not UNSET:
            field_dict["thumbnail_url"] = thumbnail_url
        if width_pixels is not UNSET:
            field_dict["width_pixels"] = width_pixels

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.google_media_attribution import GoogleMediaAttribution  # noqa: PLC0415
        from ..models.media_ref import MediaRef  # noqa: PLC0415

        d = dict(src_dict)
        id = d.pop("id")

        media = MediaRef.from_dict(d.pop("media"))

        _attribution = d.pop("attribution", UNSET)
        attribution: GoogleMediaAttribution | Unset
        if isinstance(_attribution, Unset):
            attribution = UNSET
        else:
            attribution = GoogleMediaAttribution.from_dict(_attribution)

        category = d.pop("category", UNSET)

        _created_at = d.pop("created_at", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)

        description = d.pop("description", UNSET)

        height_pixels = d.pop("height_pixels", UNSET)

        thumbnail_url = d.pop("thumbnail_url", UNSET)

        width_pixels = d.pop("width_pixels", UNSET)

        google_media_item = cls(
            id=id,
            media=media,
            attribution=attribution,
            category=category,
            created_at=created_at,
            description=description,
            height_pixels=height_pixels,
            thumbnail_url=thumbnail_url,
            width_pixels=width_pixels,
        )

        google_media_item.additional_properties = d
        return google_media_item

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
