from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PinterestPinItem")


@_attrs_define
class PinterestPinItem:
    """
    Attributes:
        id (str):  Example: 813744South.
        permalink (str):  Example: https://www.pinterest.com/pin/813744/.
        title (str): Title carries the pin's description, not Pinterest's separate title field. Example: Roast chicken.
        board_id (str | Unset):  Example: 8828.
        created_at (datetime.datetime | Unset):  Example: 2026-08-01T12:00:00Z.
        media_url (str | Unset):  Example: https://i.pinimg.com/x.jpg.
    """

    id: str
    permalink: str
    title: str
    board_id: str | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    media_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        permalink = self.permalink

        title = self.title

        board_id = self.board_id

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        media_url = self.media_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "permalink": permalink,
                "title": title,
            }
        )
        if board_id is not UNSET:
            field_dict["board_id"] = board_id
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if media_url is not UNSET:
            field_dict["media_url"] = media_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        permalink = d.pop("permalink")

        title = d.pop("title")

        board_id = d.pop("board_id", UNSET)

        _created_at = d.pop("created_at", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)

        media_url = d.pop("media_url", UNSET)

        pinterest_pin_item = cls(
            id=id,
            permalink=permalink,
            title=title,
            board_id=board_id,
            created_at=created_at,
            media_url=media_url,
        )

        pinterest_pin_item.additional_properties = d
        return pinterest_pin_item

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
