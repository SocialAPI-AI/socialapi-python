from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="UpdateAccountPermissionsRequest")


@_attrs_define
class UpdateAccountPermissionsRequest:
    """
    Attributes:
        permissions (list[str] | None): Permissions replaces the account's permissions and is required. Send null to
            give the account every permission, including ones added later. An empty list is rejected. Removing a permission
            immediately deletes the comments, messages, analytics and posts not published through SocialAPI that it covers;
            posts published through SocialAPI are kept. Valid values: posts.read, posts.write, comments.read,
            comments.write, messages.read, messages.write, reviews.read, reviews.write, analytics.read. Example:
            ['comments.read', 'comments.write'].
    """

    permissions: list[str] | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        permissions: list[str] | None
        if isinstance(self.permissions, list):
            permissions = self.permissions

        else:
            permissions = self.permissions

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "permissions": permissions,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

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

        update_account_permissions_request = cls(
            permissions=permissions,
        )

        update_account_permissions_request.additional_properties = d
        return update_account_permissions_request

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
