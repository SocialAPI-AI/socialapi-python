from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.platform import Platform
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateInviteRequest")


@_attrs_define
class CreateInviteRequest:
    """
    Attributes:
        brand_id (str):  Example: b_01HZ9X3Q4R5M6N7P8V2K0W1J.
        expires_in_days (int):  Example: 7.
        platform (Platform):
        permissions (list[str] | Unset): The permissions the connected account gets, which are the only ones the invited
            person is asked to grant. Omit it to keep the brand's current permissions for this platform, or to give every
            permission if it has none. Valid values: posts.read, posts.write, comments.read, comments.write, messages.read,
            messages.write, reviews.read, reviews.write, analytics.read. Example: ['comments.read', 'comments.write'].
    """

    brand_id: str
    expires_in_days: int
    platform: Platform
    permissions: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        brand_id = self.brand_id

        expires_in_days = self.expires_in_days

        platform = self.platform.value

        permissions: list[str] | Unset = UNSET
        if not isinstance(self.permissions, Unset):
            permissions = self.permissions

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "brand_id": brand_id,
                "expires_in_days": expires_in_days,
                "platform": platform,
            }
        )
        if permissions is not UNSET:
            field_dict["permissions"] = permissions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        brand_id = d.pop("brand_id")

        expires_in_days = d.pop("expires_in_days")

        platform = Platform(d.pop("platform"))

        permissions = cast(list[str], d.pop("permissions", UNSET))

        create_invite_request = cls(
            brand_id=brand_id,
            expires_in_days=expires_in_days,
            platform=platform,
            permissions=permissions,
        )

        create_invite_request.additional_properties = d
        return create_invite_request

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
