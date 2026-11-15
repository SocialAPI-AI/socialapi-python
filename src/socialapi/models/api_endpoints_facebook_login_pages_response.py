from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_endpoints_pending_page import ApiEndpointsPendingPage


T = TypeVar("T", bound="ApiEndpointsFacebookLoginPagesResponse")


@_attrs_define
class ApiEndpointsFacebookLoginPagesResponse:
    """
    Attributes:
        count (int | Unset):  Example: 3.
        login_id (str | Unset):  Example: cred_01J....
        pages (list[ApiEndpointsPendingPage] | Unset):
    """

    count: int | Unset = UNSET
    login_id: str | Unset = UNSET
    pages: list[ApiEndpointsPendingPage] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        count = self.count

        login_id = self.login_id

        pages: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.pages, Unset):
            pages = []
            for pages_item_data in self.pages:
                pages_item = pages_item_data.to_dict()
                pages.append(pages_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if count is not UNSET:
            field_dict["count"] = count
        if login_id is not UNSET:
            field_dict["login_id"] = login_id
        if pages is not UNSET:
            field_dict["pages"] = pages

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_endpoints_pending_page import ApiEndpointsPendingPage  # noqa: PLC0415

        d = dict(src_dict)
        count = d.pop("count", UNSET)

        login_id = d.pop("login_id", UNSET)

        _pages = d.pop("pages", UNSET)
        pages: list[ApiEndpointsPendingPage] | Unset = UNSET
        if _pages is not UNSET:
            pages = []
            for pages_item_data in _pages:
                pages_item = ApiEndpointsPendingPage.from_dict(pages_item_data)

                pages.append(pages_item)

        api_endpoints_facebook_login_pages_response = cls(
            count=count,
            login_id=login_id,
            pages=pages,
        )

        api_endpoints_facebook_login_pages_response.additional_properties = d
        return api_endpoints_facebook_login_pages_response

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
