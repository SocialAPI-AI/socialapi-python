from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.platform import Platform

T = TypeVar("T", bound="ExportAcceptedResponse")


@_attrs_define
class ExportAcceptedResponse:
    """
    Attributes:
        account_id (str):
        created_at (datetime.datetime):
        id (str):
        platform (Platform):
        status (str):
    """

    account_id: str
    created_at: datetime.datetime
    id: str
    platform: Platform
    status: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_id = self.account_id

        created_at = self.created_at.isoformat()

        id = self.id

        platform = self.platform.value

        status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "account_id": account_id,
                "created_at": created_at,
                "id": id,
                "platform": platform,
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_id = d.pop("account_id")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        id = d.pop("id")

        platform = Platform(d.pop("platform"))

        status = d.pop("status")

        export_accepted_response = cls(
            account_id=account_id,
            created_at=created_at,
            id=id,
            platform=platform,
            status=status,
        )

        export_accepted_response.additional_properties = d
        return export_accepted_response

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
