from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.media_item_response import MediaItemResponse


T = TypeVar("T", bound="MediaListResponse")


@_attrs_define
class MediaListResponse:
    """
    Attributes:
        count (int):  Example: 42.
        data (list[MediaItemResponse]):
        next_cursor (str | Unset):
    """

    count: int
    data: list[MediaItemResponse]
    next_cursor: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        count = self.count

        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)

        next_cursor = self.next_cursor

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "count": count,
                "data": data,
            }
        )
        if next_cursor is not UNSET:
            field_dict["next_cursor"] = next_cursor

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.media_item_response import MediaItemResponse  # noqa: PLC0415

        d = dict(src_dict)
        count = d.pop("count")

        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = MediaItemResponse.from_dict(data_item_data)

            data.append(data_item)

        next_cursor = d.pop("next_cursor", UNSET)

        media_list_response = cls(
            count=count,
            data=data,
            next_cursor=next_cursor,
        )

        media_list_response.additional_properties = d
        return media_list_response

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
