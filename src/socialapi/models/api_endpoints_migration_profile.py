from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiEndpointsMigrationProfile")


@_attrs_define
class ApiEndpointsMigrationProfile:
    """
    Attributes:
        brands (int | Unset):
        id (str | Unset):
        name (str | Unset):
        pages_per_brand (int | Unset):
        servable_accounts (int | Unset):
        splits (list[str] | Unset): Why the profile needs more than one Brand, one line per reason.
    """

    brands: int | Unset = UNSET
    id: str | Unset = UNSET
    name: str | Unset = UNSET
    pages_per_brand: int | Unset = UNSET
    servable_accounts: int | Unset = UNSET
    splits: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        brands = self.brands

        id = self.id

        name = self.name

        pages_per_brand = self.pages_per_brand

        servable_accounts = self.servable_accounts

        splits: list[str] | Unset = UNSET
        if not isinstance(self.splits, Unset):
            splits = self.splits

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if brands is not UNSET:
            field_dict["brands"] = brands
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if pages_per_brand is not UNSET:
            field_dict["pages_per_brand"] = pages_per_brand
        if servable_accounts is not UNSET:
            field_dict["servable_accounts"] = servable_accounts
        if splits is not UNSET:
            field_dict["splits"] = splits

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        brands = d.pop("brands", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        pages_per_brand = d.pop("pages_per_brand", UNSET)

        servable_accounts = d.pop("servable_accounts", UNSET)

        splits = cast(list[str], d.pop("splits", UNSET))

        api_endpoints_migration_profile = cls(
            brands=brands,
            id=id,
            name=name,
            pages_per_brand=pages_per_brand,
            servable_accounts=servable_accounts,
            splits=splits,
        )

        api_endpoints_migration_profile.additional_properties = d
        return api_endpoints_migration_profile

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
