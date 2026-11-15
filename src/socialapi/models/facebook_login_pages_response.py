from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.pending_page import PendingPage


T = TypeVar("T", bound="FacebookLoginPagesResponse")


@_attrs_define
class FacebookLoginPagesResponse:
    """
    Attributes:
        count (int):  Example: 3.
        login_id (str):  Example: cred_01J....
        pages (list[PendingPage]):
    """

    count: int
    login_id: str
    pages: list[PendingPage]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        count = self.count

        login_id = self.login_id

        pages = []
        for pages_item_data in self.pages:
            pages_item = pages_item_data.to_dict()
            pages.append(pages_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "count": count,
                "login_id": login_id,
                "pages": pages,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pending_page import PendingPage  # noqa: PLC0415

        d = dict(src_dict)
        count = d.pop("count")

        login_id = d.pop("login_id")

        pages = []
        _pages = d.pop("pages")
        for pages_item_data in _pages:
            pages_item = PendingPage.from_dict(pages_item_data)

            pages.append(pages_item)

        facebook_login_pages_response = cls(
            count=count,
            login_id=login_id,
            pages=pages,
        )

        facebook_login_pages_response.additional_properties = d
        return facebook_login_pages_response

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
