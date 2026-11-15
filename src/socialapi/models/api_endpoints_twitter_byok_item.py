from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiEndpointsTwitterByokItem")


@_attrs_define
class ApiEndpointsTwitterByokItem:
    """
    Attributes:
        brand_id (None | str | Unset): Brand these credentials apply to. null for the default credentials, which apply
            to every brand without its own entry.
        client_id_hint (str | Unset):
        created_at (str | Unset):
        updated_at (str | Unset):
    """

    brand_id: None | str | Unset = UNSET
    client_id_hint: str | Unset = UNSET
    created_at: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        brand_id: None | str | Unset
        if isinstance(self.brand_id, Unset):
            brand_id = UNSET
        else:
            brand_id = self.brand_id

        client_id_hint = self.client_id_hint

        created_at = self.created_at

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if brand_id is not UNSET:
            field_dict["brand_id"] = brand_id
        if client_id_hint is not UNSET:
            field_dict["client_id_hint"] = client_id_hint
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_brand_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        brand_id = _parse_brand_id(d.pop("brand_id", UNSET))

        client_id_hint = d.pop("client_id_hint", UNSET)

        created_at = d.pop("created_at", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        api_endpoints_twitter_byok_item = cls(
            brand_id=brand_id,
            client_id_hint=client_id_hint,
            created_at=created_at,
            updated_at=updated_at,
        )

        api_endpoints_twitter_byok_item.additional_properties = d
        return api_endpoints_twitter_byok_item

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
