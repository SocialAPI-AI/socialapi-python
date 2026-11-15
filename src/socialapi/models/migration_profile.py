from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="MigrationProfile")


@_attrs_define
class MigrationProfile:
    """
    Attributes:
        brands (int):
        id (str):
        name (str):
        pages_per_brand (int):
        servable_accounts (int):
        splits (list[str] | None): Why the profile needs more than one Brand, one line per reason.
    """

    brands: int
    id: str
    name: str
    pages_per_brand: int
    servable_accounts: int
    splits: list[str] | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        brands = self.brands

        id = self.id

        name = self.name

        pages_per_brand = self.pages_per_brand

        servable_accounts = self.servable_accounts

        splits: list[str] | None
        if isinstance(self.splits, list):
            splits = self.splits

        else:
            splits = self.splits

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "brands": brands,
                "id": id,
                "name": name,
                "pages_per_brand": pages_per_brand,
                "servable_accounts": servable_accounts,
                "splits": splits,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        brands = d.pop("brands")

        id = d.pop("id")

        name = d.pop("name")

        pages_per_brand = d.pop("pages_per_brand")

        servable_accounts = d.pop("servable_accounts")

        def _parse_splits(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                splits_type_0 = cast(list[str], data)

                return splits_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        splits = _parse_splits(d.pop("splits"))

        migration_profile = cls(
            brands=brands,
            id=id,
            name=name,
            pages_per_brand=pages_per_brand,
            servable_accounts=servable_accounts,
            splits=splits,
        )

        migration_profile.additional_properties = d
        return migration_profile

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
