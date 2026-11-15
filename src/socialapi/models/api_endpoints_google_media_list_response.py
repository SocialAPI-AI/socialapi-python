from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_endpoints_google_media_item import ApiEndpointsGoogleMediaItem


T = TypeVar("T", bound="ApiEndpointsGoogleMediaListResponse")


@_attrs_define
class ApiEndpointsGoogleMediaListResponse:
    """
    Attributes:
        count (int | Unset):  Example: 12.
        items (list[ApiEndpointsGoogleMediaItem] | Unset):
        next_cursor (str | Unset):
        total_count (int | Unset): TotalCount is the total number of media items on the location, across all
            pages. Zero means an empty gallery. Example: 42.
    """

    count: int | Unset = UNSET
    items: list[ApiEndpointsGoogleMediaItem] | Unset = UNSET
    next_cursor: str | Unset = UNSET
    total_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        count = self.count

        items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for items_item_data in self.items:
                items_item = items_item_data.to_dict()
                items.append(items_item)

        next_cursor = self.next_cursor

        total_count = self.total_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if count is not UNSET:
            field_dict["count"] = count
        if items is not UNSET:
            field_dict["items"] = items
        if next_cursor is not UNSET:
            field_dict["next_cursor"] = next_cursor
        if total_count is not UNSET:
            field_dict["total_count"] = total_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_endpoints_google_media_item import ApiEndpointsGoogleMediaItem  # noqa: PLC0415

        d = dict(src_dict)
        count = d.pop("count", UNSET)

        _items = d.pop("items", UNSET)
        items: list[ApiEndpointsGoogleMediaItem] | Unset = UNSET
        if _items is not UNSET:
            items = []
            for items_item_data in _items:
                items_item = ApiEndpointsGoogleMediaItem.from_dict(items_item_data)

                items.append(items_item)

        next_cursor = d.pop("next_cursor", UNSET)

        total_count = d.pop("total_count", UNSET)

        api_endpoints_google_media_list_response = cls(
            count=count,
            items=items,
            next_cursor=next_cursor,
            total_count=total_count,
        )

        api_endpoints_google_media_list_response.additional_properties = d
        return api_endpoints_google_media_list_response

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
