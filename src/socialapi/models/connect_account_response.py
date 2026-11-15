from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.platform import Platform

T = TypeVar("T", bound="ConnectAccountResponse")


@_attrs_define
class ConnectAccountResponse:
    """
    Attributes:
        account_id (str):  Example: acc_01HZ9X3Q4R5M6N7P8V2K0W1J.
        brand_id (str): BrandID is the brand the account was connected to. When the connect request named no brand, this
            is the brand created for it. Example: b7e3c1a2-4f5d-4e8a-9b1c-2d3e4f5a6b7c.
        display_name (str):  Example: Acme Corp.
        platform (Platform):
        username (str):  Example: acmecorp.
    """

    account_id: str
    brand_id: str
    display_name: str
    platform: Platform
    username: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_id = self.account_id

        brand_id = self.brand_id

        display_name = self.display_name

        platform = self.platform.value

        username = self.username

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "account_id": account_id,
                "brand_id": brand_id,
                "display_name": display_name,
                "platform": platform,
                "username": username,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_id = d.pop("account_id")

        brand_id = d.pop("brand_id")

        display_name = d.pop("display_name")

        platform = Platform(d.pop("platform"))

        username = d.pop("username")

        connect_account_response = cls(
            account_id=account_id,
            brand_id=brand_id,
            display_name=display_name,
            platform=platform,
            username=username,
        )

        connect_account_response.additional_properties = d
        return connect_account_response

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
