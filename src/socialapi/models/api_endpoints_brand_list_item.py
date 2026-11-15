from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiEndpointsBrandListItem")


@_attrs_define
class ApiEndpointsBrandListItem:
    """
    Attributes:
        accounts_count (int | Unset):  Example: 3.
        created_at (str | Unset):  Example: 2026-03-14T09:00:00Z.
        id (str | Unset):  Example: b_01HZ9X3Q4R5M6N7P8V2K0W1J.
        name (str | Unset):  Example: Acme Corporation.
        updated_at (str | Unset):  Example: 2026-03-14T09:00:00Z.
    """

    accounts_count: int | Unset = UNSET
    created_at: str | Unset = UNSET
    id: str | Unset = UNSET
    name: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        accounts_count = self.accounts_count

        created_at = self.created_at

        id = self.id

        name = self.name

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if accounts_count is not UNSET:
            field_dict["accounts_count"] = accounts_count
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        accounts_count = d.pop("accounts_count", UNSET)

        created_at = d.pop("created_at", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        api_endpoints_brand_list_item = cls(
            accounts_count=accounts_count,
            created_at=created_at,
            id=id,
            name=name,
            updated_at=updated_at,
        )

        api_endpoints_brand_list_item.additional_properties = d
        return api_endpoints_brand_list_item

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
