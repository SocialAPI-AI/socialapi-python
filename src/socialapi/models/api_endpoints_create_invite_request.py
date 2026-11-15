from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiEndpointsCreateInviteRequest")


@_attrs_define
class ApiEndpointsCreateInviteRequest:
    """
    Attributes:
        brand_id (str | Unset):  Example: b_01HZ9X3Q4R5M6N7P8V2K0W1J.
        expires_in_days (int | Unset):  Example: 7.
        permissions (list[str] | Unset): The permissions the connected account gets, which are the only ones the invited
            person is asked to grant. Omit it to keep the brand's current permissions for this platform, or to give every
            permission if it has none. Valid values: posts.read, posts.write, comments.read, comments.write, messages.read,
            messages.write, reviews.read, reviews.write, analytics.read. Example: ['comments.read', 'comments.write'].
        platform (str | Unset):  Example: facebook.
    """

    brand_id: str | Unset = UNSET
    expires_in_days: int | Unset = UNSET
    permissions: list[str] | Unset = UNSET
    platform: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        brand_id = self.brand_id

        expires_in_days = self.expires_in_days

        permissions: list[str] | Unset = UNSET
        if not isinstance(self.permissions, Unset):
            permissions = self.permissions

        platform = self.platform

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if brand_id is not UNSET:
            field_dict["brand_id"] = brand_id
        if expires_in_days is not UNSET:
            field_dict["expires_in_days"] = expires_in_days
        if permissions is not UNSET:
            field_dict["permissions"] = permissions
        if platform is not UNSET:
            field_dict["platform"] = platform

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        brand_id = d.pop("brand_id", UNSET)

        expires_in_days = d.pop("expires_in_days", UNSET)

        permissions = cast(list[str], d.pop("permissions", UNSET))

        platform = d.pop("platform", UNSET)

        api_endpoints_create_invite_request = cls(
            brand_id=brand_id,
            expires_in_days=expires_in_days,
            permissions=permissions,
            platform=platform,
        )

        api_endpoints_create_invite_request.additional_properties = d
        return api_endpoints_create_invite_request

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
