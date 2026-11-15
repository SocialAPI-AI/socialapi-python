from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_endpoints_migration_plan import ApiEndpointsMigrationPlan
    from ..models.api_endpoints_migration_profile import ApiEndpointsMigrationProfile
    from ..models.api_endpoints_migration_unsupported import ApiEndpointsMigrationUnsupported


T = TypeVar("T", bound="ApiEndpointsMigrationAssessment")


@_attrs_define
class ApiEndpointsMigrationAssessment:
    """
    Attributes:
        brands (int | Unset): Brands needed across all profiles.
        pages_per_brand (int | Unset): Most Pages any one Brand needs on a single platform.
        profiles (list[ApiEndpointsMigrationProfile] | Unset): One entry per profile at your provider.
        recommended_plan (ApiEndpointsMigrationPlan | Unset):
        servable_accounts (int | Unset): Accounts SocialAPI can serve.
        stays_with_provider (list[ApiEndpointsMigrationUnsupported] | Unset): Accounts that stay with your provider, by
            platform.
    """

    brands: int | Unset = UNSET
    pages_per_brand: int | Unset = UNSET
    profiles: list[ApiEndpointsMigrationProfile] | Unset = UNSET
    recommended_plan: ApiEndpointsMigrationPlan | Unset = UNSET
    servable_accounts: int | Unset = UNSET
    stays_with_provider: list[ApiEndpointsMigrationUnsupported] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        brands = self.brands

        pages_per_brand = self.pages_per_brand

        profiles: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.profiles, Unset):
            profiles = []
            for profiles_item_data in self.profiles:
                profiles_item = profiles_item_data.to_dict()
                profiles.append(profiles_item)

        recommended_plan: dict[str, Any] | Unset = UNSET
        if not isinstance(self.recommended_plan, Unset):
            recommended_plan = self.recommended_plan.to_dict()

        servable_accounts = self.servable_accounts

        stays_with_provider: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.stays_with_provider, Unset):
            stays_with_provider = []
            for stays_with_provider_item_data in self.stays_with_provider:
                stays_with_provider_item = stays_with_provider_item_data.to_dict()
                stays_with_provider.append(stays_with_provider_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if brands is not UNSET:
            field_dict["brands"] = brands
        if pages_per_brand is not UNSET:
            field_dict["pages_per_brand"] = pages_per_brand
        if profiles is not UNSET:
            field_dict["profiles"] = profiles
        if recommended_plan is not UNSET:
            field_dict["recommended_plan"] = recommended_plan
        if servable_accounts is not UNSET:
            field_dict["servable_accounts"] = servable_accounts
        if stays_with_provider is not UNSET:
            field_dict["stays_with_provider"] = stays_with_provider

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_endpoints_migration_plan import ApiEndpointsMigrationPlan  # noqa: PLC0415
        from ..models.api_endpoints_migration_profile import ApiEndpointsMigrationProfile  # noqa: PLC0415
        from ..models.api_endpoints_migration_unsupported import ApiEndpointsMigrationUnsupported  # noqa: PLC0415

        d = dict(src_dict)
        brands = d.pop("brands", UNSET)

        pages_per_brand = d.pop("pages_per_brand", UNSET)

        _profiles = d.pop("profiles", UNSET)
        profiles: list[ApiEndpointsMigrationProfile] | Unset = UNSET
        if _profiles is not UNSET:
            profiles = []
            for profiles_item_data in _profiles:
                profiles_item = ApiEndpointsMigrationProfile.from_dict(profiles_item_data)

                profiles.append(profiles_item)

        _recommended_plan = d.pop("recommended_plan", UNSET)
        recommended_plan: ApiEndpointsMigrationPlan | Unset
        if isinstance(_recommended_plan, Unset):
            recommended_plan = UNSET
        else:
            recommended_plan = ApiEndpointsMigrationPlan.from_dict(_recommended_plan)

        servable_accounts = d.pop("servable_accounts", UNSET)

        _stays_with_provider = d.pop("stays_with_provider", UNSET)
        stays_with_provider: list[ApiEndpointsMigrationUnsupported] | Unset = UNSET
        if _stays_with_provider is not UNSET:
            stays_with_provider = []
            for stays_with_provider_item_data in _stays_with_provider:
                stays_with_provider_item = ApiEndpointsMigrationUnsupported.from_dict(stays_with_provider_item_data)

                stays_with_provider.append(stays_with_provider_item)

        api_endpoints_migration_assessment = cls(
            brands=brands,
            pages_per_brand=pages_per_brand,
            profiles=profiles,
            recommended_plan=recommended_plan,
            servable_accounts=servable_accounts,
            stays_with_provider=stays_with_provider,
        )

        api_endpoints_migration_assessment.additional_properties = d
        return api_endpoints_migration_assessment

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
