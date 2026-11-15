from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyListItem")


@_attrs_define
class KeyListItem:
    """
    Attributes:
        brand_ids (list[str] | None):
        created_at (datetime.datetime):  Example: 2026-02-28T12:00:00Z.
        id (str):
        is_active (bool):
        name (str):
        preview (str):  Example: sapi_key_a1b2c....
        scopes (list[str] | None):  Example: ['posts:write', 'inbox:read'].
        last_used_at (datetime.datetime | Unset):  Example: 2026-02-28T12:00:00Z.
    """

    brand_ids: list[str] | None
    created_at: datetime.datetime
    id: str
    is_active: bool
    name: str
    preview: str
    scopes: list[str] | None
    last_used_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        brand_ids: list[str] | None
        if isinstance(self.brand_ids, list):
            brand_ids = self.brand_ids

        else:
            brand_ids = self.brand_ids

        created_at = self.created_at.isoformat()

        id = self.id

        is_active = self.is_active

        name = self.name

        preview = self.preview

        scopes: list[str] | None
        if isinstance(self.scopes, list):
            scopes = self.scopes

        else:
            scopes = self.scopes

        last_used_at: str | Unset = UNSET
        if not isinstance(self.last_used_at, Unset):
            last_used_at = self.last_used_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "brand_ids": brand_ids,
                "created_at": created_at,
                "id": id,
                "is_active": is_active,
                "name": name,
                "preview": preview,
                "scopes": scopes,
            }
        )
        if last_used_at is not UNSET:
            field_dict["last_used_at"] = last_used_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_brand_ids(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                brand_ids_type_0 = cast(list[str], data)

                return brand_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        brand_ids = _parse_brand_ids(d.pop("brand_ids"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        id = d.pop("id")

        is_active = d.pop("is_active")

        name = d.pop("name")

        preview = d.pop("preview")

        def _parse_scopes(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                scopes_type_0 = cast(list[str], data)

                return scopes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        scopes = _parse_scopes(d.pop("scopes"))

        _last_used_at = d.pop("last_used_at", UNSET)
        last_used_at: datetime.datetime | Unset
        if isinstance(_last_used_at, Unset):
            last_used_at = UNSET
        else:
            last_used_at = datetime.datetime.fromisoformat(_last_used_at)

        key_list_item = cls(
            brand_ids=brand_ids,
            created_at=created_at,
            id=id,
            is_active=is_active,
            name=name,
            preview=preview,
            scopes=scopes,
            last_used_at=last_used_at,
        )

        key_list_item.additional_properties = d
        return key_list_item

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
