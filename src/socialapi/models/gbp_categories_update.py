from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GBPCategoriesUpdate")


@_attrs_define
class GBPCategoriesUpdate:
    """
    Attributes:
        additional_categories (list[str] | Unset): AdditionalCategories replaces the whole list: Google has no way to
            add or
            remove a single category, so a partial list drops the rest.
        primary_category (str | Unset):  Example: categories/gcid:pizza_restaurant.
    """

    additional_categories: list[str] | Unset = UNSET
    primary_category: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        additional_categories: list[str] | Unset = UNSET
        if not isinstance(self.additional_categories, Unset):
            additional_categories = self.additional_categories

        primary_category = self.primary_category

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if additional_categories is not UNSET:
            field_dict["additional_categories"] = additional_categories
        if primary_category is not UNSET:
            field_dict["primary_category"] = primary_category

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        additional_categories = cast(list[str], d.pop("additional_categories", UNSET))

        primary_category = d.pop("primary_category", UNSET)

        gbp_categories_update = cls(
            additional_categories=additional_categories,
            primary_category=primary_category,
        )

        gbp_categories_update.additional_properties = d
        return gbp_categories_update

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
