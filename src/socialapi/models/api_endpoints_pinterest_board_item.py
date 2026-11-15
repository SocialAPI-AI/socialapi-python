from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.api_endpoints_pinterest_board_item_privacy import ApiEndpointsPinterestBoardItemPrivacy
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiEndpointsPinterestBoardItem")


@_attrs_define
class ApiEndpointsPinterestBoardItem:
    """
    Attributes:
        board_id (str | Unset):  Example: 8828.
        id (str | Unset):  Example: sapi_board_01HZ9X3Q4R5M6N7P8V2K0W1J.
        name (str | Unset):  Example: Recipes.
        privacy (ApiEndpointsPinterestBoardItemPrivacy | Unset):  Example: PUBLIC.
    """

    board_id: str | Unset = UNSET
    id: str | Unset = UNSET
    name: str | Unset = UNSET
    privacy: ApiEndpointsPinterestBoardItemPrivacy | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        board_id = self.board_id

        id = self.id

        name = self.name

        privacy: str | Unset = UNSET
        if not isinstance(self.privacy, Unset):
            privacy = self.privacy.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if board_id is not UNSET:
            field_dict["board_id"] = board_id
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if privacy is not UNSET:
            field_dict["privacy"] = privacy

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        board_id = d.pop("board_id", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        _privacy = d.pop("privacy", UNSET)
        privacy: ApiEndpointsPinterestBoardItemPrivacy | Unset
        if isinstance(_privacy, Unset):
            privacy = UNSET
        else:
            privacy = ApiEndpointsPinterestBoardItemPrivacy(_privacy)

        api_endpoints_pinterest_board_item = cls(
            board_id=board_id,
            id=id,
            name=name,
            privacy=privacy,
        )

        api_endpoints_pinterest_board_item.additional_properties = d
        return api_endpoints_pinterest_board_item

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
