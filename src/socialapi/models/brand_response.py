from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="BrandResponse")


@_attrs_define
class BrandResponse:
    """
    Attributes:
        accounts_count (int):  Example: 0.
        created_at (datetime.datetime):  Example: 2026-03-14T09:00:00Z.
        id (str):  Example: b_01HZ9X3Q4R5M6N7P8V2K0W1J.
        name (str):  Example: Acme Corporation.
        updated_at (datetime.datetime):  Example: 2026-03-14T09:00:00Z.
    """

    accounts_count: int
    created_at: datetime.datetime
    id: str
    name: str
    updated_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        accounts_count = self.accounts_count

        created_at = self.created_at.isoformat()

        id = self.id

        name = self.name

        updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accounts_count": accounts_count,
                "created_at": created_at,
                "id": id,
                "name": name,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        accounts_count = d.pop("accounts_count")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        id = d.pop("id")

        name = d.pop("name")

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        brand_response = cls(
            accounts_count=accounts_count,
            created_at=created_at,
            id=id,
            name=name,
            updated_at=updated_at,
        )

        brand_response.additional_properties = d
        return brand_response

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
