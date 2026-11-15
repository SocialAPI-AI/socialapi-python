from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GBPMoney")


@_attrs_define
class GBPMoney:
    """
    Attributes:
        currency_code (str | Unset):  Example: EUR.
        nanos (int | Unset): Nanos is the fractional part of the price, in billionths. Zero is a real
            value, not an absent one.
        units (str | Unset):  Example: 80.
    """

    currency_code: str | Unset = UNSET
    nanos: int | Unset = UNSET
    units: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        currency_code = self.currency_code

        nanos = self.nanos

        units = self.units

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if currency_code is not UNSET:
            field_dict["currency_code"] = currency_code
        if nanos is not UNSET:
            field_dict["nanos"] = nanos
        if units is not UNSET:
            field_dict["units"] = units

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        currency_code = d.pop("currency_code", UNSET)

        nanos = d.pop("nanos", UNSET)

        units = d.pop("units", UNSET)

        gbp_money = cls(
            currency_code=currency_code,
            nanos=nanos,
            units=units,
        )

        gbp_money.additional_properties = d
        return gbp_money

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
