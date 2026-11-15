from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiEndpointsDeleteQueueResponse")


@_attrs_define
class ApiEndpointsDeleteQueueResponse:
    """
    Attributes:
        deleted (bool | Unset):
        id (str | Unset):
        released_count (int | Unset): Number of posts that were in the Queue. They keep their scheduled times and are no
            longer queued.
    """

    deleted: bool | Unset = UNSET
    id: str | Unset = UNSET
    released_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        deleted = self.deleted

        id = self.id

        released_count = self.released_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if deleted is not UNSET:
            field_dict["deleted"] = deleted
        if id is not UNSET:
            field_dict["id"] = id
        if released_count is not UNSET:
            field_dict["released_count"] = released_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        deleted = d.pop("deleted", UNSET)

        id = d.pop("id", UNSET)

        released_count = d.pop("released_count", UNSET)

        api_endpoints_delete_queue_response = cls(
            deleted=deleted,
            id=id,
            released_count=released_count,
        )

        api_endpoints_delete_queue_response.additional_properties = d
        return api_endpoints_delete_queue_response

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
