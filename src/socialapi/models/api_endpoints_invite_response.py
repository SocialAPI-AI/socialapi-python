from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiEndpointsInviteResponse")


@_attrs_define
class ApiEndpointsInviteResponse:
    """
    Attributes:
        expires_at (str | Unset):  Example: 2026-04-03T12:00:00Z.
        id (str | Unset):  Example: inv_01HZ9X3Q4R5M6N7P8V2K0W1J.
        permissions (list[str] | Unset): The permissions chosen when the invite was created. null means the brand's
            current permissions for this platform apply when the invite is used, or every permission if it has none.
            Example: ['comments.read', 'comments.write'].
        platform (str | Unset):  Example: facebook.
        token (str | Unset):  Example: a55755cf75f73b56deb3dfe0c993fd36fc4c2bfa7.
        url (str | Unset):  Example: https://api.social-api.ai/invite/a55755cf....
    """

    expires_at: str | Unset = UNSET
    id: str | Unset = UNSET
    permissions: list[str] | Unset = UNSET
    platform: str | Unset = UNSET
    token: str | Unset = UNSET
    url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        expires_at = self.expires_at

        id = self.id

        permissions: list[str] | Unset = UNSET
        if not isinstance(self.permissions, Unset):
            permissions = self.permissions

        platform = self.platform

        token = self.token

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at
        if id is not UNSET:
            field_dict["id"] = id
        if permissions is not UNSET:
            field_dict["permissions"] = permissions
        if platform is not UNSET:
            field_dict["platform"] = platform
        if token is not UNSET:
            field_dict["token"] = token
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        expires_at = d.pop("expires_at", UNSET)

        id = d.pop("id", UNSET)

        permissions = cast(list[str], d.pop("permissions", UNSET))

        platform = d.pop("platform", UNSET)

        token = d.pop("token", UNSET)

        url = d.pop("url", UNSET)

        api_endpoints_invite_response = cls(
            expires_at=expires_at,
            id=id,
            permissions=permissions,
            platform=platform,
            token=token,
            url=url,
        )

        api_endpoints_invite_response.additional_properties = d
        return api_endpoints_invite_response

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
