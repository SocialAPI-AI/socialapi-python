from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GBPMenuLabel")


@_attrs_define
class GBPMenuLabel:
    """
    Attributes:
        display_name (str):  Example: Margherita.
        description (str | Unset):  Example: Tomato, mozzarella, basil.
        language_code (str | Unset): LanguageCode is a BCP 47 code. English is assumed when absent. Example: en.
    """

    display_name: str
    description: str | Unset = UNSET
    language_code: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        display_name = self.display_name

        description = self.description

        language_code = self.language_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "display_name": display_name,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if language_code is not UNSET:
            field_dict["language_code"] = language_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        display_name = d.pop("display_name")

        description = d.pop("description", UNSET)

        language_code = d.pop("language_code", UNSET)

        gbp_menu_label = cls(
            display_name=display_name,
            description=description,
            language_code=language_code,
        )

        gbp_menu_label.additional_properties = d
        return gbp_menu_label

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
