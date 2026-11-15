from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.social_api_ai_core_api_connectors_base_gbp_location_details import (
        SocialApiAiCoreApiConnectorsBaseGBPLocationDetails,
    )


T = TypeVar("T", bound="ApiEndpointsGoogleLocation")


@_attrs_define
class ApiEndpointsGoogleLocation:
    """
    Attributes:
        assignable (bool | Unset):
        assigned_account_id (str | Unset):
        assigned_brand_id (str | Unset):
        assigned_brand_name (str | Unset):
        bio (str | Unset):  Example: Wood-fired pizza since 1998.
        category (str | Unset): Category is the location's primary Google category, localized. Example: Pizza
            restaurant.
        details (SocialApiAiCoreApiConnectorsBaseGBPLocationDetails | Unset):
        maps_uri (str | Unset): MapsURI is the location's page on Google Maps. Example:
            https://maps.google.com/?cid=123.
        name (str | Unset):  Example: Joe's Pizza (Downtown).
        platform_account_id (str | Unset):  Example: accounts/123/locations/456.
    """

    assignable: bool | Unset = UNSET
    assigned_account_id: str | Unset = UNSET
    assigned_brand_id: str | Unset = UNSET
    assigned_brand_name: str | Unset = UNSET
    bio: str | Unset = UNSET
    category: str | Unset = UNSET
    details: SocialApiAiCoreApiConnectorsBaseGBPLocationDetails | Unset = UNSET
    maps_uri: str | Unset = UNSET
    name: str | Unset = UNSET
    platform_account_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        assignable = self.assignable

        assigned_account_id = self.assigned_account_id

        assigned_brand_id = self.assigned_brand_id

        assigned_brand_name = self.assigned_brand_name

        bio = self.bio

        category = self.category

        details: dict[str, Any] | Unset = UNSET
        if not isinstance(self.details, Unset):
            details = self.details.to_dict()

        maps_uri = self.maps_uri

        name = self.name

        platform_account_id = self.platform_account_id

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
        if bio is not UNSET:
            field_dict["bio"] = bio
        if category is not UNSET:
            field_dict["category"] = category
        if details is not UNSET:
            field_dict["details"] = details
        if maps_uri is not UNSET:
            field_dict["maps_uri"] = maps_uri
        if name is not UNSET:
            field_dict["name"] = name
        if platform_account_id is not UNSET:
            field_dict["platform_account_id"] = platform_account_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.social_api_ai_core_api_connectors_base_gbp_location_details import (
            SocialApiAiCoreApiConnectorsBaseGBPLocationDetails,  # noqa: PLC0415
        )

        d = dict(src_dict)
        assignable = d.pop("assignable", UNSET)

        assigned_account_id = d.pop("assigned_account_id", UNSET)

        assigned_brand_id = d.pop("assigned_brand_id", UNSET)

        assigned_brand_name = d.pop("assigned_brand_name", UNSET)

        bio = d.pop("bio", UNSET)

        category = d.pop("category", UNSET)

        _details = d.pop("details", UNSET)
        details: SocialApiAiCoreApiConnectorsBaseGBPLocationDetails | Unset
        if isinstance(_details, Unset):
            details = UNSET
        else:
            details = SocialApiAiCoreApiConnectorsBaseGBPLocationDetails.from_dict(_details)

        maps_uri = d.pop("maps_uri", UNSET)

        name = d.pop("name", UNSET)

        platform_account_id = d.pop("platform_account_id", UNSET)

        api_endpoints_google_location = cls(
            assignable=assignable,
            assigned_account_id=assigned_account_id,
            assigned_brand_id=assigned_brand_id,
            assigned_brand_name=assigned_brand_name,
            bio=bio,
            category=category,
            details=details,
            maps_uri=maps_uri,
            name=name,
            platform_account_id=platform_account_id,
        )

        api_endpoints_google_location.additional_properties = d
        return api_endpoints_google_location

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
