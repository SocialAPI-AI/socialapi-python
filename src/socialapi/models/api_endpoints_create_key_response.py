from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiEndpointsCreateKeyResponse")


@_attrs_define
class ApiEndpointsCreateKeyResponse:
    """
    Attributes:
        brand_ids (list[str] | Unset):
        id (str | Unset):
        message (str | Unset):  Example: Store this key securely. It will not be shown again..
        name (str | Unset):
        raw_key (str | Unset):  Example: sapi_key_....
        scopes (list[str] | Unset):  Example: ['posts:write', 'inbox:read'].
    """

    brand_ids: list[str] | Unset = UNSET
    id: str | Unset = UNSET
    message: str | Unset = UNSET
    name: str | Unset = UNSET
    raw_key: str | Unset = UNSET
    scopes: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        brand_ids: list[str] | Unset = UNSET
        if not isinstance(self.brand_ids, Unset):
            brand_ids = self.brand_ids

        id = self.id

        message = self.message

        name = self.name

        raw_key = self.raw_key

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
        if message is not UNSET:
            field_dict["message"] = message
        if name is not UNSET:
            field_dict["name"] = name
        if raw_key is not UNSET:
            field_dict["raw_key"] = raw_key
        if scopes is not UNSET:
            field_dict["scopes"] = scopes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        brand_ids = cast(list[str], d.pop("brand_ids", UNSET))

        id = d.pop("id", UNSET)

        message = d.pop("message", UNSET)

        name = d.pop("name", UNSET)

        raw_key = d.pop("raw_key", UNSET)

        scopes = cast(list[str], d.pop("scopes", UNSET))

        api_endpoints_create_key_response = cls(
            brand_ids=brand_ids,
            id=id,
            message=message,
            name=name,
            raw_key=raw_key,
            scopes=scopes,
        )

        api_endpoints_create_key_response.additional_properties = d
        return api_endpoints_create_key_response

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
