from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_endpoints_linked_in_login_profile import ApiEndpointsLinkedInLoginProfile


T = TypeVar("T", bound="ApiEndpointsLinkedInLoginProfilesResponse")


@_attrs_define
class ApiEndpointsLinkedInLoginProfilesResponse:
    """
    Attributes:
        count (int | Unset):  Example: 2.
        login_id (str | Unset):  Example: cred_01J....
        login_name (str | Unset): LoginName is the name of the LinkedIn member who authorized the login. Example: Jane
            Doe.
        profiles (list[ApiEndpointsLinkedInLoginProfile] | Unset):
    """

    count: int | Unset = UNSET
    login_id: str | Unset = UNSET
    login_name: str | Unset = UNSET
    profiles: list[ApiEndpointsLinkedInLoginProfile] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        count = self.count

        login_id = self.login_id

        login_name = self.login_name

        profiles: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.profiles, Unset):
            profiles = []
            for profiles_item_data in self.profiles:
                profiles_item = profiles_item_data.to_dict()
                profiles.append(profiles_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if count is not UNSET:
            field_dict["count"] = count
        if login_id is not UNSET:
            field_dict["login_id"] = login_id
        if login_name is not UNSET:
            field_dict["login_name"] = login_name
        if profiles is not UNSET:
            field_dict["profiles"] = profiles

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_endpoints_linked_in_login_profile import ApiEndpointsLinkedInLoginProfile  # noqa: PLC0415

        d = dict(src_dict)
        count = d.pop("count", UNSET)

        login_id = d.pop("login_id", UNSET)

        login_name = d.pop("login_name", UNSET)

        _profiles = d.pop("profiles", UNSET)
        profiles: list[ApiEndpointsLinkedInLoginProfile] | Unset = UNSET
        if _profiles is not UNSET:
            profiles = []
            for profiles_item_data in _profiles:
                profiles_item = ApiEndpointsLinkedInLoginProfile.from_dict(profiles_item_data)

                profiles.append(profiles_item)

        api_endpoints_linked_in_login_profiles_response = cls(
            count=count,
            login_id=login_id,
            login_name=login_name,
            profiles=profiles,
        )

        api_endpoints_linked_in_login_profiles_response.additional_properties = d
        return api_endpoints_linked_in_login_profiles_response

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
