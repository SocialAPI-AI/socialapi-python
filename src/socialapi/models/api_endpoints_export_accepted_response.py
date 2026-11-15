from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiEndpointsExportAcceptedResponse")


@_attrs_define
class ApiEndpointsExportAcceptedResponse:
    """
    Attributes:
        account_id (str | Unset):
        created_at (str | Unset):
        id (str | Unset):
        platform (str | Unset):
        status (str | Unset):
    """

    account_id: str | Unset = UNSET
    created_at: str | Unset = UNSET
    id: str | Unset = UNSET
    platform: str | Unset = UNSET
    status: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_id = self.account_id

        created_at = self.created_at

        id = self.id

        platform = self.platform

        status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_id is not UNSET:
            field_dict["account_id"] = account_id
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if id is not UNSET:
            field_dict["id"] = id
        if platform is not UNSET:
            field_dict["platform"] = platform
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_id = d.pop("account_id", UNSET)

        created_at = d.pop("created_at", UNSET)

        id = d.pop("id", UNSET)

        platform = d.pop("platform", UNSET)

        status = d.pop("status", UNSET)

        api_endpoints_export_accepted_response = cls(
            account_id=account_id,
            created_at=created_at,
            id=id,
            platform=platform,
            status=status,
        )

        api_endpoints_export_accepted_response.additional_properties = d
        return api_endpoints_export_accepted_response

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
