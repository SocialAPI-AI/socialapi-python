from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.gbp_menu_label import GBPMenuLabel


T = TypeVar("T", bound="GBPMenuPortionSize")


@_attrs_define
class GBPMenuPortionSize:
    """
    Attributes:
        quantity (int | Unset):
        unit (list[GBPMenuLabel] | None | Unset):
    """

    quantity: int | Unset = UNSET
    unit: list[GBPMenuLabel] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        quantity = self.quantity

        unit: list[dict[str, Any]] | None | Unset
        if isinstance(self.unit, Unset):
            unit = UNSET
        elif isinstance(self.unit, list):
            unit = []
            for unit_type_0_item_data in self.unit:
                unit_type_0_item = unit_type_0_item_data.to_dict()
                unit.append(unit_type_0_item)

        else:
            unit = self.unit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if unit is not UNSET:
            field_dict["unit"] = unit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.gbp_menu_label import GBPMenuLabel  # noqa: PLC0415

        d = dict(src_dict)
        quantity = d.pop("quantity", UNSET)

        def _parse_unit(data: object) -> list[GBPMenuLabel] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                unit_type_0 = []
                _unit_type_0 = data
                for unit_type_0_item_data in _unit_type_0:
                    unit_type_0_item = GBPMenuLabel.from_dict(unit_type_0_item_data)

                    unit_type_0.append(unit_type_0_item)

                return unit_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[GBPMenuLabel] | None | Unset, data)

        unit = _parse_unit(d.pop("unit", UNSET))

        gbp_menu_portion_size = cls(
            quantity=quantity,
            unit=unit,
        )

        gbp_menu_portion_size.additional_properties = d
        return gbp_menu_portion_size

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
