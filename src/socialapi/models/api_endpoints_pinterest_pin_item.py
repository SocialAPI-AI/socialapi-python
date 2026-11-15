from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiEndpointsPinterestPinItem")


@_attrs_define
class ApiEndpointsPinterestPinItem:
    """
    Attributes:
        board_id (str | Unset):  Example: 8828.
        created_at (str | Unset):  Example: 2026-08-01T12:00:00Z.
        id (str | Unset):  Example: 813744South.
        media_url (str | Unset):  Example: https://i.pinimg.com/x.jpg.
        permalink (str | Unset):  Example: https://www.pinterest.com/pin/813744/.
        title (str | Unset): Title carries the pin's description, not Pinterest's separate title field. Example: Roast
            chicken.
    """

    board_id: str | Unset = UNSET
    created_at: str | Unset = UNSET
    id: str | Unset = UNSET
    media_url: str | Unset = UNSET
    permalink: str | Unset = UNSET
    title: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        board_id = self.board_id

        created_at = self.created_at

        id = self.id

        media_url = self.media_url

        permalink = self.permalink

        title = self.title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if board_id is not UNSET:
            field_dict["board_id"] = board_id
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if id is not UNSET:
            field_dict["id"] = id
        if media_url is not UNSET:
            field_dict["media_url"] = media_url
        if permalink is not UNSET:
            field_dict["permalink"] = permalink
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        board_id = d.pop("board_id", UNSET)

        created_at = d.pop("created_at", UNSET)

        id = d.pop("id", UNSET)

        media_url = d.pop("media_url", UNSET)

        permalink = d.pop("permalink", UNSET)

        title = d.pop("title", UNSET)

        api_endpoints_pinterest_pin_item = cls(
            board_id=board_id,
            created_at=created_at,
            id=id,
            media_url=media_url,
            permalink=permalink,
            title=title,
        )

        api_endpoints_pinterest_pin_item.additional_properties = d
        return api_endpoints_pinterest_pin_item

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
