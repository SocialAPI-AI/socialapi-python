from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiEndpointsPendingPage")


@_attrs_define
class ApiEndpointsPendingPage:
    """
    Attributes:
        assignable (bool | Unset):
        assigned_account_id (str | Unset):
        assigned_brand_id (str | Unset):
        assigned_brand_name (str | Unset):
        category (str | Unset):
        name (str | Unset):  Example: Acme Bakery.
        picture_url (str | Unset):
        platform_page_id (str | Unset):  Example: 17841400000000000.
    """

    assignable: bool | Unset = UNSET
    assigned_account_id: str | Unset = UNSET
    assigned_brand_id: str | Unset = UNSET
    assigned_brand_name: str | Unset = UNSET
    category: str | Unset = UNSET
    name: str | Unset = UNSET
    picture_url: str | Unset = UNSET
    platform_page_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        assignable = self.assignable

        assigned_account_id = self.assigned_account_id

        assigned_brand_id = self.assigned_brand_id

        assigned_brand_name = self.assigned_brand_name

        category = self.category

        name = self.name

        picture_url = self.picture_url

        platform_page_id = self.platform_page_id

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
        if category is not UNSET:
            field_dict["category"] = category
        if name is not UNSET:
            field_dict["name"] = name
        if picture_url is not UNSET:
            field_dict["picture_url"] = picture_url
        if platform_page_id is not UNSET:
            field_dict["platform_page_id"] = platform_page_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        assignable = d.pop("assignable", UNSET)

        assigned_account_id = d.pop("assigned_account_id", UNSET)

        assigned_brand_id = d.pop("assigned_brand_id", UNSET)

        assigned_brand_name = d.pop("assigned_brand_name", UNSET)

        category = d.pop("category", UNSET)

        name = d.pop("name", UNSET)

        picture_url = d.pop("picture_url", UNSET)

        platform_page_id = d.pop("platform_page_id", UNSET)

        api_endpoints_pending_page = cls(
            assignable=assignable,
            assigned_account_id=assigned_account_id,
            assigned_brand_id=assigned_brand_id,
            assigned_brand_name=assigned_brand_name,
            category=category,
            name=name,
            picture_url=picture_url,
            platform_page_id=platform_page_id,
        )

        api_endpoints_pending_page.additional_properties = d
        return api_endpoints_pending_page

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
