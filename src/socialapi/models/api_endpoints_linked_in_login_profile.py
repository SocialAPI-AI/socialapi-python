from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.api_endpoints_linked_in_login_profile_connection_type import (
    ApiEndpointsLinkedInLoginProfileConnectionType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiEndpointsLinkedInLoginProfile")


@_attrs_define
class ApiEndpointsLinkedInLoginProfile:
    """
    Attributes:
        assignable (bool | Unset):
        assigned_account_id (str | Unset):
        assigned_brand_id (str | Unset):
        assigned_brand_name (str | Unset):
        connection_type (ApiEndpointsLinkedInLoginProfileConnectionType | Unset): ConnectionType is "profile" for the
            member, "organization" for a company Page. Example: organization.
        name (str | Unset):  Example: Acme Corp.
        picture_url (str | Unset):
        platform_account_id (str | Unset):  Example: urn:li:organization:123456.
        username (str | Unset):  Example: acme-corp.
    """

    assignable: bool | Unset = UNSET
    assigned_account_id: str | Unset = UNSET
    assigned_brand_id: str | Unset = UNSET
    assigned_brand_name: str | Unset = UNSET
    connection_type: ApiEndpointsLinkedInLoginProfileConnectionType | Unset = UNSET
    name: str | Unset = UNSET
    picture_url: str | Unset = UNSET
    platform_account_id: str | Unset = UNSET
    username: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        assignable = self.assignable

        assigned_account_id = self.assigned_account_id

        assigned_brand_id = self.assigned_brand_id

        assigned_brand_name = self.assigned_brand_name

        connection_type: str | Unset = UNSET
        if not isinstance(self.connection_type, Unset):
            connection_type = self.connection_type.value

        name = self.name

        picture_url = self.picture_url

        platform_account_id = self.platform_account_id

        username = self.username

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if assignable is not UNSET:
            field_dict["assignable"] = assignable
        if assigned_account_id is not UNSET:
            field_dict["assigned_account_id"] = assigned_account_id
        if assigned_brand_id is not UNSET:
            field_dict["assigned_brand_id"] = assigned_brand_id
        if assigned_brand_name is not UNSET:
            field_dict["assigned_brand_name"] = assigned_brand_name
        if connection_type is not UNSET:
            field_dict["connection_type"] = connection_type
        if name is not UNSET:
            field_dict["name"] = name
        if picture_url is not UNSET:
            field_dict["picture_url"] = picture_url
        if platform_account_id is not UNSET:
            field_dict["platform_account_id"] = platform_account_id
        if username is not UNSET:
            field_dict["username"] = username

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        assignable = d.pop("assignable", UNSET)

        assigned_account_id = d.pop("assigned_account_id", UNSET)

        assigned_brand_id = d.pop("assigned_brand_id", UNSET)

        assigned_brand_name = d.pop("assigned_brand_name", UNSET)

        _connection_type = d.pop("connection_type", UNSET)
        connection_type: ApiEndpointsLinkedInLoginProfileConnectionType | Unset
        if isinstance(_connection_type, Unset):
            connection_type = UNSET
        else:
            connection_type = ApiEndpointsLinkedInLoginProfileConnectionType(_connection_type)

        name = d.pop("name", UNSET)

        picture_url = d.pop("picture_url", UNSET)

        platform_account_id = d.pop("platform_account_id", UNSET)

        username = d.pop("username", UNSET)

        api_endpoints_linked_in_login_profile = cls(
            assignable=assignable,
            assigned_account_id=assigned_account_id,
            assigned_brand_id=assigned_brand_id,
            assigned_brand_name=assigned_brand_name,
            connection_type=connection_type,
            name=name,
            picture_url=picture_url,
            platform_account_id=platform_account_id,
            username=username,
        )

        api_endpoints_linked_in_login_profile.additional_properties = d
        return api_endpoints_linked_in_login_profile

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
