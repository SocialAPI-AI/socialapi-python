from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="UpdateKeyResponse")


@_attrs_define
class UpdateKeyResponse:
    """
    Attributes:
        brand_ids (list[str] | None):
        id (str):
        name (str):
        scopes (list[str] | None):  Example: ['posts:write', 'inbox:read'].
    """

    brand_ids: list[str] | None
    id: str
    name: str
    scopes: list[str] | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        brand_ids: list[str] | None
        if isinstance(self.brand_ids, list):
            brand_ids = self.brand_ids

        else:
            brand_ids = self.brand_ids

        id = self.id

        name = self.name

        scopes: list[str] | None
        if isinstance(self.scopes, list):
            scopes = self.scopes

        else:
            scopes = self.scopes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "brand_ids": brand_ids,
                "id": id,
                "name": name,
                "scopes": scopes,
            }
        )

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

        id = d.pop("id")

        name = d.pop("name")

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

        update_key_response = cls(
            brand_ids=brand_ids,
            id=id,
            name=name,
            scopes=scopes,
        )

        update_key_response.additional_properties = d
        return update_key_response

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
