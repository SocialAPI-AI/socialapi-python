from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SelectProfileRequest")


@_attrs_define
class SelectProfileRequest:
    """
    Attributes:
        page_ids (list[str] | Unset): PageIDs selects the Facebook Pages to assign to the brand (Facebook pending
            connections only).
        platform_account_id (str | Unset): PlatformAccountID selects the Google Business Profile to connect (Google
            pending connections only). Example: accounts/123/locations/456.
    """

    page_ids: list[str] | Unset = UNSET
    platform_account_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        page_ids: list[str] | Unset = UNSET
        if not isinstance(self.page_ids, Unset):
            page_ids = self.page_ids

        platform_account_id = self.platform_account_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if page_ids is not UNSET:
            field_dict["page_ids"] = page_ids
        if platform_account_id is not UNSET:
            field_dict["platform_account_id"] = platform_account_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        page_ids = cast(list[str], d.pop("page_ids", UNSET))

        platform_account_id = d.pop("platform_account_id", UNSET)

        select_profile_request = cls(
            page_ids=page_ids,
            platform_account_id=platform_account_id,
        )

        select_profile_request.additional_properties = d
        return select_profile_request

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
