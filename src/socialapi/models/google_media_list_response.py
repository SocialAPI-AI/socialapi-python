from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.google_media_item import GoogleMediaItem


T = TypeVar("T", bound="GoogleMediaListResponse")


@_attrs_define
class GoogleMediaListResponse:
    """
    Attributes:
        count (int):  Example: 12.
        items (list[GoogleMediaItem]):
        total_count (int): TotalCount is the total number of media items on the location, across all
            pages. Zero means an empty gallery. Example: 42.
        next_cursor (str | Unset):
    """

    count: int
    items: list[GoogleMediaItem]
    total_count: int
    next_cursor: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        count = self.count

        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()
            items.append(items_item)

        total_count = self.total_count

        next_cursor = self.next_cursor

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "count": count,
                "items": items,
                "total_count": total_count,
            }
        )
        if next_cursor is not UNSET:
            field_dict["next_cursor"] = next_cursor

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.google_media_item import GoogleMediaItem  # noqa: PLC0415

        d = dict(src_dict)
        count = d.pop("count")

        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = GoogleMediaItem.from_dict(items_item_data)

            items.append(items_item)

        total_count = d.pop("total_count")

        next_cursor = d.pop("next_cursor", UNSET)

        google_media_list_response = cls(
            count=count,
            items=items,
            total_count=total_count,
            next_cursor=next_cursor,
        )

        google_media_list_response.additional_properties = d
        return google_media_list_response

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
