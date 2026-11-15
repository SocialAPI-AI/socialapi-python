from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PinterestBoardItem")


@_attrs_define
class PinterestBoardItem:
    """
    Attributes:
        board_id (str):  Example: 8828.
        id (str):  Example: sapi_board_01HZ9X3Q4R5M6N7P8V2K0W1J.
        name (str):  Example: Recipes.
        privacy (str | Unset): Who can see the board, for example PUBLIC, PROTECTED or SECRET. Other values can appear.
            Example: PUBLIC.
    """

    board_id: str
    id: str
    name: str
    privacy: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        board_id = self.board_id

        id = self.id

        name = self.name

        privacy = self.privacy

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "board_id": board_id,
                "id": id,
                "name": name,
            }
        )
        if privacy is not UNSET:
            field_dict["privacy"] = privacy

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        board_id = d.pop("board_id")

        id = d.pop("id")

        name = d.pop("name")

        privacy = d.pop("privacy", UNSET)

        pinterest_board_item = cls(
            board_id=board_id,
            id=id,
            name=name,
            privacy=privacy,
        )

        pinterest_board_item.additional_properties = d
        return pinterest_board_item

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
