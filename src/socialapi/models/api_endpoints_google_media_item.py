from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_endpoints_google_media_attribution import ApiEndpointsGoogleMediaAttribution
    from ..models.api_endpoints_media_ref import ApiEndpointsMediaRef


T = TypeVar("T", bound="ApiEndpointsGoogleMediaItem")


@_attrs_define
class ApiEndpointsGoogleMediaItem:
    """
    Attributes:
        attribution (ApiEndpointsGoogleMediaAttribution | Unset):
        category (str | Unset):  Example: INTERIOR.
        created_at (str | Unset):  Example: 2026-03-01T12:00:00Z.
        description (str | Unset):  Example: Main dining room.
        height_pixels (int | Unset):  Example: 1200.
        id (str | Unset):  Example: accounts/123/locations/456/media/789.
        media (ApiEndpointsMediaRef | Unset):
        thumbnail_url (str | Unset):
        width_pixels (int | Unset):  Example: 1600.
    """

    attribution: ApiEndpointsGoogleMediaAttribution | Unset = UNSET
    category: str | Unset = UNSET
    created_at: str | Unset = UNSET
    description: str | Unset = UNSET
    height_pixels: int | Unset = UNSET
    id: str | Unset = UNSET
    media: ApiEndpointsMediaRef | Unset = UNSET
    thumbnail_url: str | Unset = UNSET
    width_pixels: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        attribution: dict[str, Any] | Unset = UNSET
        if not isinstance(self.attribution, Unset):
            attribution = self.attribution.to_dict()

        category = self.category

        created_at = self.created_at

        description = self.description

        height_pixels = self.height_pixels

        id = self.id

        media: dict[str, Any] | Unset = UNSET
        if not isinstance(self.media, Unset):
            media = self.media.to_dict()

        thumbnail_url = self.thumbnail_url

        width_pixels = self.width_pixels

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
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
        if id is not UNSET:
            field_dict["id"] = id
        if media is not UNSET:
            field_dict["media"] = media
        if thumbnail_url is not UNSET:
            field_dict["thumbnail_url"] = thumbnail_url
        if width_pixels is not UNSET:
            field_dict["width_pixels"] = width_pixels

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_endpoints_google_media_attribution import ApiEndpointsGoogleMediaAttribution  # noqa: PLC0415
        from ..models.api_endpoints_media_ref import ApiEndpointsMediaRef  # noqa: PLC0415

        d = dict(src_dict)
        _attribution = d.pop("attribution", UNSET)
        attribution: ApiEndpointsGoogleMediaAttribution | Unset
        if isinstance(_attribution, Unset):
            attribution = UNSET
        else:
            attribution = ApiEndpointsGoogleMediaAttribution.from_dict(_attribution)

        category = d.pop("category", UNSET)

        created_at = d.pop("created_at", UNSET)

        description = d.pop("description", UNSET)

        height_pixels = d.pop("height_pixels", UNSET)

        id = d.pop("id", UNSET)

        _media = d.pop("media", UNSET)
        media: ApiEndpointsMediaRef | Unset
        if isinstance(_media, Unset):
            media = UNSET
        else:
            media = ApiEndpointsMediaRef.from_dict(_media)

        thumbnail_url = d.pop("thumbnail_url", UNSET)

        width_pixels = d.pop("width_pixels", UNSET)

        api_endpoints_google_media_item = cls(
            attribution=attribution,
            category=category,
            created_at=created_at,
            description=description,
            height_pixels=height_pixels,
            id=id,
            media=media,
            thumbnail_url=thumbnail_url,
            width_pixels=width_pixels,
        )

        api_endpoints_google_media_item.additional_properties = d
        return api_endpoints_google_media_item

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
