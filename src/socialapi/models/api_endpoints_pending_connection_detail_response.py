from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_endpoints_lost_page_access import ApiEndpointsLostPageAccess
    from ..models.api_endpoints_pending_page import ApiEndpointsPendingPage
    from ..models.api_endpoints_pending_profile import ApiEndpointsPendingProfile


T = TypeVar("T", bound="ApiEndpointsPendingConnectionDetailResponse")


@_attrs_define
class ApiEndpointsPendingConnectionDetailResponse:
    """
    Attributes:
        connection_id (str | Unset):
        expires_at (str | Unset):  Example: 2026-07-04T12:30:00Z.
        login_id (str | Unset): login_id identifies the login and is set for Facebook, Google and LinkedIn.
            pages and lost_access are Facebook page-selection only.
        lost_access (list[ApiEndpointsLostPageAccess] | Unset):
        pages (list[ApiEndpointsPendingPage] | Unset):
        platform (str | Unset):  Example: google.
        profiles (list[ApiEndpointsPendingProfile] | Unset):
    """

    connection_id: str | Unset = UNSET
    expires_at: str | Unset = UNSET
    login_id: str | Unset = UNSET
    lost_access: list[ApiEndpointsLostPageAccess] | Unset = UNSET
    pages: list[ApiEndpointsPendingPage] | Unset = UNSET
    platform: str | Unset = UNSET
    profiles: list[ApiEndpointsPendingProfile] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        connection_id = self.connection_id

        expires_at = self.expires_at

        login_id = self.login_id

        lost_access: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.lost_access, Unset):
            lost_access = []
            for lost_access_item_data in self.lost_access:
                lost_access_item = lost_access_item_data.to_dict()
                lost_access.append(lost_access_item)

        pages: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.pages, Unset):
            pages = []
            for pages_item_data in self.pages:
                pages_item = pages_item_data.to_dict()
                pages.append(pages_item)

        platform = self.platform

        profiles: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.profiles, Unset):
            profiles = []
            for profiles_item_data in self.profiles:
                profiles_item = profiles_item_data.to_dict()
                profiles.append(profiles_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if connection_id is not UNSET:
            field_dict["connection_id"] = connection_id
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at
        if login_id is not UNSET:
            field_dict["login_id"] = login_id
        if lost_access is not UNSET:
            field_dict["lost_access"] = lost_access
        if pages is not UNSET:
            field_dict["pages"] = pages
        if platform is not UNSET:
            field_dict["platform"] = platform
        if profiles is not UNSET:
            field_dict["profiles"] = profiles

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_endpoints_lost_page_access import ApiEndpointsLostPageAccess  # noqa: PLC0415
        from ..models.api_endpoints_pending_page import ApiEndpointsPendingPage  # noqa: PLC0415
        from ..models.api_endpoints_pending_profile import ApiEndpointsPendingProfile  # noqa: PLC0415

        d = dict(src_dict)
        connection_id = d.pop("connection_id", UNSET)

        expires_at = d.pop("expires_at", UNSET)

        login_id = d.pop("login_id", UNSET)

        _lost_access = d.pop("lost_access", UNSET)
        lost_access: list[ApiEndpointsLostPageAccess] | Unset = UNSET
        if _lost_access is not UNSET:
            lost_access = []
            for lost_access_item_data in _lost_access:
                lost_access_item = ApiEndpointsLostPageAccess.from_dict(lost_access_item_data)

                lost_access.append(lost_access_item)

        _pages = d.pop("pages", UNSET)
        pages: list[ApiEndpointsPendingPage] | Unset = UNSET
        if _pages is not UNSET:
            pages = []
            for pages_item_data in _pages:
                pages_item = ApiEndpointsPendingPage.from_dict(pages_item_data)

                pages.append(pages_item)

        platform = d.pop("platform", UNSET)

        _profiles = d.pop("profiles", UNSET)
        profiles: list[ApiEndpointsPendingProfile] | Unset = UNSET
        if _profiles is not UNSET:
            profiles = []
            for profiles_item_data in _profiles:
                profiles_item = ApiEndpointsPendingProfile.from_dict(profiles_item_data)

                profiles.append(profiles_item)

        api_endpoints_pending_connection_detail_response = cls(
            connection_id=connection_id,
            expires_at=expires_at,
            login_id=login_id,
            lost_access=lost_access,
            pages=pages,
            platform=platform,
            profiles=profiles,
        )

        api_endpoints_pending_connection_detail_response.additional_properties = d
        return api_endpoints_pending_connection_detail_response

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
