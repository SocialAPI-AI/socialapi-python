from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AssignLocationResponse")


@_attrs_define
class AssignLocationResponse:
    """
    Attributes:
        account_id (str):  Example: acc_01J....
        brand_id (str):
        platform_account_id (str):
    """

    account_id: str
    brand_id: str
    platform_account_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_id = self.account_id

        brand_id = self.brand_id

        platform_account_id = self.platform_account_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "account_id": account_id,
                "brand_id": brand_id,
                "platform_account_id": platform_account_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_id = d.pop("account_id")

        brand_id = d.pop("brand_id")

        platform_account_id = d.pop("platform_account_id")

        assign_location_response = cls(
            account_id=account_id,
            brand_id=brand_id,
            platform_account_id=platform_account_id,
        )

        assign_location_response.additional_properties = d
        return assign_location_response

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
