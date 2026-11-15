from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GBPNutritionFact")


@_attrs_define
class GBPNutritionFact:
    """
    Attributes:
        lower_amount (float | Unset):
        unit (str | Unset):  Example: GRAM.
        upper_amount (float | Unset):
    """

    lower_amount: float | Unset = UNSET
    unit: str | Unset = UNSET
    upper_amount: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        lower_amount = self.lower_amount

        unit = self.unit

        upper_amount = self.upper_amount

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if lower_amount is not UNSET:
            field_dict["lower_amount"] = lower_amount
        if unit is not UNSET:
            field_dict["unit"] = unit
        if upper_amount is not UNSET:
            field_dict["upper_amount"] = upper_amount

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        lower_amount = d.pop("lower_amount", UNSET)

        unit = d.pop("unit", UNSET)

        upper_amount = d.pop("upper_amount", UNSET)

        gbp_nutrition_fact = cls(
            lower_amount=lower_amount,
            unit=unit,
            upper_amount=upper_amount,
        )

        gbp_nutrition_fact.additional_properties = d
        return gbp_nutrition_fact

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
