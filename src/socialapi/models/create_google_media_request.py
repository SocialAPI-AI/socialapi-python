from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.google_media_category import GoogleMediaCategory
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.media_input import MediaInput


T = TypeVar("T", bound="CreateGoogleMediaRequest")


@_attrs_define
class CreateGoogleMediaRequest:
    """
    Attributes:
        category (GoogleMediaCategory):
        media (list[MediaInput]):
        description (str | Unset):  Example: Main dining room.
    """

    category: GoogleMediaCategory
    media: list[MediaInput]
    description: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        category = self.category.value

        media = []
        for media_item_data in self.media:
            media_item = media_item_data.to_dict()
            media.append(media_item)

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "category": category,
                "media": media,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.media_input import MediaInput  # noqa: PLC0415

        d = dict(src_dict)
        category = GoogleMediaCategory(d.pop("category"))

        media = []
        _media = d.pop("media")
        for media_item_data in _media:
            media_item = MediaInput.from_dict(media_item_data)

            media.append(media_item)

        description = d.pop("description", UNSET)

        create_google_media_request = cls(
            category=category,
            media=media,
            description=description,
        )

        create_google_media_request.additional_properties = d
        return create_google_media_request

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
