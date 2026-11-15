from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiEndpointsKeyListItem")


@_attrs_define
class ApiEndpointsKeyListItem:
    """
    Attributes:
        brand_ids (list[str] | Unset):
        created_at (str | Unset):  Example: 2026-02-28T12:00:00Z.
        id (str | Unset):
        is_active (bool | Unset):
        last_used_at (str | Unset):  Example: 2026-02-28T12:00:00Z.
        name (str | Unset):
        preview (str | Unset):  Example: sapi_key_a1b2c....
        scopes (list[str] | Unset):  Example: ['posts:write', 'inbox:read'].
    """

    brand_ids: list[str] | Unset = UNSET
    created_at: str | Unset = UNSET
    id: str | Unset = UNSET
    is_active: bool | Unset = UNSET
    last_used_at: str | Unset = UNSET
    name: str | Unset = UNSET
    preview: str | Unset = UNSET
    scopes: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        brand_ids: list[str] | Unset = UNSET
        if not isinstance(self.brand_ids, Unset):
            brand_ids = self.brand_ids

        created_at = self.created_at

        id = self.id

        is_active = self.is_active

        last_used_at = self.last_used_at

        name = self.name

        preview = self.preview

        scopes: list[str] | Unset = UNSET
        if not isinstance(self.scopes, Unset):
            scopes = self.scopes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if brand_ids is not UNSET:
            field_dict["brand_ids"] = brand_ids
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if id is not UNSET:
            field_dict["id"] = id
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if last_used_at is not UNSET:
            field_dict["last_used_at"] = last_used_at
        if name is not UNSET:
            field_dict["name"] = name
        if preview is not UNSET:
            field_dict["preview"] = preview
        if scopes is not UNSET:
            field_dict["scopes"] = scopes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        brand_ids = cast(list[str], d.pop("brand_ids", UNSET))

        created_at = d.pop("created_at", UNSET)

        id = d.pop("id", UNSET)

        is_active = d.pop("is_active", UNSET)

        last_used_at = d.pop("last_used_at", UNSET)

        name = d.pop("name", UNSET)

        preview = d.pop("preview", UNSET)

        scopes = cast(list[str], d.pop("scopes", UNSET))

        api_endpoints_key_list_item = cls(
            brand_ids=brand_ids,
            created_at=created_at,
            id=id,
            is_active=is_active,
            last_used_at=last_used_at,
            name=name,
            preview=preview,
            scopes=scopes,
        )

        api_endpoints_key_list_item.additional_properties = d
        return api_endpoints_key_list_item

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
