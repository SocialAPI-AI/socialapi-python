from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GBPRepeatedEnumValue")


@_attrs_define
class GBPRepeatedEnumValue:
    """
    Attributes:
        set_values (list[str] | None | Unset):
        unset_values (list[str] | None | Unset):
    """

    set_values: list[str] | None | Unset = UNSET
    unset_values: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        set_values: list[str] | None | Unset
        if isinstance(self.set_values, Unset):
            set_values = UNSET
        elif isinstance(self.set_values, list):
            set_values = self.set_values

        else:
            set_values = self.set_values

        unset_values: list[str] | None | Unset
        if isinstance(self.unset_values, Unset):
            unset_values = UNSET
        elif isinstance(self.unset_values, list):
            unset_values = self.unset_values

        else:
            unset_values = self.unset_values

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if set_values is not UNSET:
            field_dict["set_values"] = set_values
        if unset_values is not UNSET:
            field_dict["unset_values"] = unset_values

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_set_values(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                set_values_type_0 = cast(list[str], data)

                return set_values_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        set_values = _parse_set_values(d.pop("set_values", UNSET))

        def _parse_unset_values(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                unset_values_type_0 = cast(list[str], data)

                return unset_values_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        unset_values = _parse_unset_values(d.pop("unset_values", UNSET))

        gbp_repeated_enum_value = cls(
            set_values=set_values,
            unset_values=unset_values,
        )

        gbp_repeated_enum_value.additional_properties = d
        return gbp_repeated_enum_value

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
