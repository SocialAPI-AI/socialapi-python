from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.gbp_food_menu import GBPFoodMenu


T = TypeVar("T", bound="GBPFoodMenus")


@_attrs_define
class GBPFoodMenus:
    """
    Attributes:
        menus (list[GBPFoodMenu] | None | Unset):
    """

    menus: list[GBPFoodMenu] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        menus: list[dict[str, Any]] | None | Unset
        if isinstance(self.menus, Unset):
            menus = UNSET
        elif isinstance(self.menus, list):
            menus = []
            for menus_type_0_item_data in self.menus:
                menus_type_0_item = menus_type_0_item_data.to_dict()
                menus.append(menus_type_0_item)

        else:
            menus = self.menus

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if menus is not UNSET:
            field_dict["menus"] = menus

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.gbp_food_menu import GBPFoodMenu  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_menus(data: object) -> list[GBPFoodMenu] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                menus_type_0 = []
                _menus_type_0 = data
                for menus_type_0_item_data in _menus_type_0:
                    menus_type_0_item = GBPFoodMenu.from_dict(menus_type_0_item_data)

                    menus_type_0.append(menus_type_0_item)

                return menus_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[GBPFoodMenu] | None | Unset, data)

        menus = _parse_menus(d.pop("menus", UNSET))

        gbp_food_menus = cls(
            menus=menus,
        )

        gbp_food_menus.additional_properties = d
        return gbp_food_menus

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
