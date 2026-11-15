from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.connection_type import ConnectionType
from ..types import UNSET, Unset

T = TypeVar("T", bound="LinkedInLoginProfile")


@_attrs_define
class LinkedInLoginProfile:
    """
    Attributes:
        assignable (bool):
        connection_type (ConnectionType):
        name (str):  Example: Acme Corp.
        platform_account_id (str):  Example: urn:li:organization:123456.
        assigned_account_id (str | Unset):
        assigned_brand_id (str | Unset):
        assigned_brand_name (str | Unset):
        picture_url (str | Unset):
        username (str | Unset):  Example: acme-corp.
    """

    assignable: bool
    connection_type: ConnectionType
    name: str
    platform_account_id: str
    assigned_account_id: str | Unset = UNSET
    assigned_brand_id: str | Unset = UNSET
    assigned_brand_name: str | Unset = UNSET
    picture_url: str | Unset = UNSET
    username: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        assignable = self.assignable

        connection_type = self.connection_type.value

        name = self.name

        platform_account_id = self.platform_account_id

        assigned_account_id = self.assigned_account_id

        assigned_brand_id = self.assigned_brand_id

        assigned_brand_name = self.assigned_brand_name

        picture_url = self.picture_url

        username = self.username

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "assignable": assignable,
                "connection_type": connection_type,
                "name": name,
                "platform_account_id": platform_account_id,
            }
        )
        if assigned_account_id is not UNSET:
            field_dict["assigned_account_id"] = assigned_account_id
        if assigned_brand_id is not UNSET:
            field_dict["assigned_brand_id"] = assigned_brand_id
        if assigned_brand_name is not UNSET:
            field_dict["assigned_brand_name"] = assigned_brand_name
        if picture_url is not UNSET:
            field_dict["picture_url"] = picture_url
        if username is not UNSET:
            field_dict["username"] = username

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        assignable = d.pop("assignable")

        connection_type = ConnectionType(d.pop("connection_type"))

        name = d.pop("name")

        platform_account_id = d.pop("platform_account_id")

        assigned_account_id = d.pop("assigned_account_id", UNSET)

        assigned_brand_id = d.pop("assigned_brand_id", UNSET)

        assigned_brand_name = d.pop("assigned_brand_name", UNSET)

        picture_url = d.pop("picture_url", UNSET)

        username = d.pop("username", UNSET)

        linked_in_login_profile = cls(
            assignable=assignable,
            connection_type=connection_type,
            name=name,
            platform_account_id=platform_account_id,
            assigned_account_id=assigned_account_id,
            assigned_brand_id=assigned_brand_id,
            assigned_brand_name=assigned_brand_name,
            picture_url=picture_url,
            username=username,
        )

        linked_in_login_profile.additional_properties = d
        return linked_in_login_profile

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
