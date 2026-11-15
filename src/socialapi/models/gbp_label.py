from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GBPLabel")


@_attrs_define
class GBPLabel:
    """
    Attributes:
        description (str | Unset):
        display_name (str | Unset):  Example: Emergency unlock.
        language_code (str | Unset):  Example: en.
    """

    description: str | Unset = UNSET
    display_name: str | Unset = UNSET
    language_code: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        display_name = self.display_name

        language_code = self.language_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if language_code is not UNSET:
            field_dict["language_code"] = language_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        description = d.pop("description", UNSET)

        display_name = d.pop("display_name", UNSET)

        language_code = d.pop("language_code", UNSET)

        gbp_label = cls(
            description=description,
            display_name=display_name,
            language_code=language_code,
        )

        gbp_label.additional_properties = d
        return gbp_label

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
