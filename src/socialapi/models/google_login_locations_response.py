from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.google_location import GoogleLocation


T = TypeVar("T", bound="GoogleLoginLocationsResponse")


@_attrs_define
class GoogleLoginLocationsResponse:
    """
    Attributes:
        count (int):  Example: 3.
        locations (list[GoogleLocation]):
        login_id (str):  Example: cred_01J....
        login_email (str | Unset):  Example: joe@example.com.
        login_name (str | Unset):  Example: joe@example.com.
    """

    count: int
    locations: list[GoogleLocation]
    login_id: str
    login_email: str | Unset = UNSET
    login_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        count = self.count

        locations = []
        for locations_item_data in self.locations:
            locations_item = locations_item_data.to_dict()
            locations.append(locations_item)

        login_id = self.login_id

        login_email = self.login_email

        login_name = self.login_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "count": count,
                "locations": locations,
                "login_id": login_id,
            }
        )
        if login_email is not UNSET:
            field_dict["login_email"] = login_email
        if login_name is not UNSET:
            field_dict["login_name"] = login_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.google_location import GoogleLocation  # noqa: PLC0415

        d = dict(src_dict)
        count = d.pop("count")

        locations = []
        _locations = d.pop("locations")
        for locations_item_data in _locations:
            locations_item = GoogleLocation.from_dict(locations_item_data)

            locations.append(locations_item)

        login_id = d.pop("login_id")

        login_email = d.pop("login_email", UNSET)

        login_name = d.pop("login_name", UNSET)

        google_login_locations_response = cls(
            count=count,
            locations=locations,
            login_id=login_id,
            login_email=login_email,
            login_name=login_name,
        )

        google_login_locations_response.additional_properties = d
        return google_login_locations_response

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
