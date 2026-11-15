from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiEndpointsConnectAccountResponse")


@_attrs_define
class ApiEndpointsConnectAccountResponse:
    """
    Attributes:
        account_id (str | Unset):  Example: acc_01HZ9X3Q4R5M6N7P8V2K0W1J.
        brand_id (str | Unset): BrandID is the brand the account was connected to. When the connect request named no
            brand, this is the brand created for it. Example: b7e3c1a2-4f5d-4e8a-9b1c-2d3e4f5a6b7c.
        display_name (str | Unset):  Example: Acme Corp.
        platform (str | Unset):  Example: instagram.
        username (str | Unset):  Example: acmecorp.
    """

    account_id: str | Unset = UNSET
    brand_id: str | Unset = UNSET
    display_name: str | Unset = UNSET
    platform: str | Unset = UNSET
    username: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_id = self.account_id

        brand_id = self.brand_id

        display_name = self.display_name

        platform = self.platform

        username = self.username

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_id is not UNSET:
            field_dict["account_id"] = account_id
        if brand_id is not UNSET:
            field_dict["brand_id"] = brand_id
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if platform is not UNSET:
            field_dict["platform"] = platform
        if username is not UNSET:
            field_dict["username"] = username

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_id = d.pop("account_id", UNSET)

        brand_id = d.pop("brand_id", UNSET)

        display_name = d.pop("display_name", UNSET)

        platform = d.pop("platform", UNSET)

        username = d.pop("username", UNSET)

        api_endpoints_connect_account_response = cls(
            account_id=account_id,
            brand_id=brand_id,
            display_name=display_name,
            platform=platform,
            username=username,
        )

        api_endpoints_connect_account_response.additional_properties = d
        return api_endpoints_connect_account_response

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
