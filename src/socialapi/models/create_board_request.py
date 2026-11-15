from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.pinterest_board_privacy import PinterestBoardPrivacy
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateBoardRequest")


@_attrs_define
class CreateBoardRequest:
    """
    Attributes:
        name (str):  Example: Recipes.
        description (str | Unset):  Example: Weeknight dinners.
        privacy (PinterestBoardPrivacy | Unset):
    """

    name: str
    description: str | Unset = UNSET
    privacy: PinterestBoardPrivacy | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description = self.description

        privacy: str | Unset = UNSET
        if not isinstance(self.privacy, Unset):
            privacy = self.privacy.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if privacy is not UNSET:
            field_dict["privacy"] = privacy

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        description = d.pop("description", UNSET)

        _privacy = d.pop("privacy", UNSET)
        privacy: PinterestBoardPrivacy | Unset
        if isinstance(_privacy, Unset):
            privacy = UNSET
        else:
            privacy = PinterestBoardPrivacy(_privacy)

        create_board_request = cls(
            name=name,
            description=description,
            privacy=privacy,
        )

        create_board_request.additional_properties = d
        return create_board_request

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
