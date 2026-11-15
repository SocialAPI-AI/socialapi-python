from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiEndpointsUpdateKeyResponse")


@_attrs_define
class ApiEndpointsUpdateKeyResponse:
    """
    Attributes:
        brand_ids (list[str] | Unset):
        id (str | Unset):
        name (str | Unset):
        scopes (list[str] | Unset):  Example: ['posts:write', 'inbox:read'].
    """

    brand_ids: list[str] | Unset = UNSET
    id: str | Unset = UNSET
    name: str | Unset = UNSET
    scopes: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        brand_ids: list[str] | Unset = UNSET
        if not isinstance(self.brand_ids, Unset):
            brand_ids = self.brand_ids

        id = self.id

        name = self.name

        scopes: list[str] | Unset = UNSET
        if not isinstance(self.scopes, Unset):
            scopes = self.scopes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if brand_ids is not UNSET:
            field_dict["brand_ids"] = brand_ids
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if scopes is not UNSET:
            field_dict["scopes"] = scopes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        brand_ids = cast(list[str], d.pop("brand_ids", UNSET))

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        scopes = cast(list[str], d.pop("scopes", UNSET))

        api_endpoints_update_key_response = cls(
            brand_ids=brand_ids,
            id=id,
            name=name,
            scopes=scopes,
        )

        api_endpoints_update_key_response.additional_properties = d
        return api_endpoints_update_key_response

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
