from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiEndpointsKeyScopeItem")


@_attrs_define
class ApiEndpointsKeyScopeItem:
    """
    Attributes:
        description (str | Unset):  Example: Create, edit, publish, and delete posts.
        group (str | Unset):  Example: Posts.
        name (str | Unset):  Example: posts:write.
    """

    description: str | Unset = UNSET
    group: str | Unset = UNSET
    name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        group = self.group

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if group is not UNSET:
            field_dict["group"] = group
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        description = d.pop("description", UNSET)

        group = d.pop("group", UNSET)

        name = d.pop("name", UNSET)

        api_endpoints_key_scope_item = cls(
            description=description,
            group=group,
            name=name,
        )

        api_endpoints_key_scope_item.additional_properties = d
        return api_endpoints_key_scope_item

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
