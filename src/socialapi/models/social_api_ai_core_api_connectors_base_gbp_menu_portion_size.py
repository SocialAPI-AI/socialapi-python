from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.social_api_ai_core_api_connectors_base_gbp_menu_label import (
        SocialApiAiCoreApiConnectorsBaseGBPMenuLabel,
    )


T = TypeVar("T", bound="SocialApiAiCoreApiConnectorsBaseGBPMenuPortionSize")


@_attrs_define
class SocialApiAiCoreApiConnectorsBaseGBPMenuPortionSize:
    """
    Attributes:
        quantity (int | Unset):
        unit (list[SocialApiAiCoreApiConnectorsBaseGBPMenuLabel] | Unset):
    """

    quantity: int | Unset = UNSET
    unit: list[SocialApiAiCoreApiConnectorsBaseGBPMenuLabel] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        quantity = self.quantity

        unit: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.unit, Unset):
            unit = []
            for unit_item_data in self.unit:
                unit_item = unit_item_data.to_dict()
                unit.append(unit_item)

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
        from ..models.social_api_ai_core_api_connectors_base_gbp_menu_label import (
            SocialApiAiCoreApiConnectorsBaseGBPMenuLabel,  # noqa: PLC0415
        )

        d = dict(src_dict)
        quantity = d.pop("quantity", UNSET)

        _unit = d.pop("unit", UNSET)
        unit: list[SocialApiAiCoreApiConnectorsBaseGBPMenuLabel] | Unset = UNSET
        if _unit is not UNSET:
            unit = []
            for unit_item_data in _unit:
                unit_item = SocialApiAiCoreApiConnectorsBaseGBPMenuLabel.from_dict(unit_item_data)

                unit.append(unit_item)

        social_api_ai_core_api_connectors_base_gbp_menu_portion_size = cls(
            quantity=quantity,
            unit=unit,
        )

        social_api_ai_core_api_connectors_base_gbp_menu_portion_size.additional_properties = d
        return social_api_ai_core_api_connectors_base_gbp_menu_portion_size

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
