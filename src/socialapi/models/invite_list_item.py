from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.platform import Platform

T = TypeVar("T", bound="InviteListItem")


@_attrs_define
class InviteListItem:
    """
    Attributes:
        created_at (datetime.datetime):  Example: 2026-03-27T12:00:00Z.
        expires_at (datetime.datetime):  Example: 2026-04-03T12:00:00Z.
        id (str):  Example: inv_01HZ9X3Q4R5M6N7P8V2K0W1J.
        is_active (bool):  Example: True.
        permissions (list[str] | None): The permissions chosen when the invite was created. null means the brand's
            current permissions for this platform apply when the invite is used, or every permission if it has none.
            Example: ['comments.read', 'comments.write'].
        platform (Platform):
        token (str):  Example: a55755cf....
        url (str):  Example: https://api.social-api.ai/invite/a55755cf....
    """

    created_at: datetime.datetime
    expires_at: datetime.datetime
    id: str
    is_active: bool
    permissions: list[str] | None
    platform: Platform
    token: str
    url: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        expires_at = self.expires_at.isoformat()

        id = self.id

        is_active = self.is_active

        permissions: list[str] | None
        if isinstance(self.permissions, list):
            permissions = self.permissions

        else:
            permissions = self.permissions

        platform = self.platform.value

        token = self.token

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_at": created_at,
                "expires_at": expires_at,
                "id": id,
                "is_active": is_active,
                "permissions": permissions,
                "platform": platform,
                "token": token,
                "url": url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        expires_at = datetime.datetime.fromisoformat(d.pop("expires_at"))

        id = d.pop("id")

        is_active = d.pop("is_active")

        def _parse_permissions(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                permissions_type_0 = cast(list[str], data)

                return permissions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        permissions = _parse_permissions(d.pop("permissions"))

        platform = Platform(d.pop("platform"))

        token = d.pop("token")

        url = d.pop("url")

        invite_list_item = cls(
            created_at=created_at,
            expires_at=expires_at,
            id=id,
            is_active=is_active,
            permissions=permissions,
            platform=platform,
            token=token,
            url=url,
        )

        invite_list_item.additional_properties = d
        return invite_list_item

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
