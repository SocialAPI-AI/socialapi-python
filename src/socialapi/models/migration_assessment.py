from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.migration_plan import MigrationPlan
    from ..models.migration_profile import MigrationProfile
    from ..models.migration_unsupported import MigrationUnsupported


T = TypeVar("T", bound="MigrationAssessment")


@_attrs_define
class MigrationAssessment:
    """
    Attributes:
        brands (int): Brands needed across all profiles.
        pages_per_brand (int): Most Pages any one Brand needs on a single platform.
        profiles (list[MigrationProfile]): One entry per profile at your provider.
        recommended_plan (MigrationPlan):
        servable_accounts (int): Accounts SocialAPI can serve.
        stays_with_provider (list[MigrationUnsupported]): Accounts that stay with your provider, by platform.
    """

    brands: int
    pages_per_brand: int
    profiles: list[MigrationProfile]
    recommended_plan: MigrationPlan
    servable_accounts: int
    stays_with_provider: list[MigrationUnsupported]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        brands = self.brands

        pages_per_brand = self.pages_per_brand

        profiles = []
        for profiles_item_data in self.profiles:
            profiles_item = profiles_item_data.to_dict()
            profiles.append(profiles_item)

        recommended_plan = self.recommended_plan.to_dict()

        servable_accounts = self.servable_accounts

        stays_with_provider = []
        for stays_with_provider_item_data in self.stays_with_provider:
            stays_with_provider_item = stays_with_provider_item_data.to_dict()
            stays_with_provider.append(stays_with_provider_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "brands": brands,
                "pages_per_brand": pages_per_brand,
                "profiles": profiles,
                "recommended_plan": recommended_plan,
                "servable_accounts": servable_accounts,
                "stays_with_provider": stays_with_provider,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.migration_plan import MigrationPlan  # noqa: PLC0415
        from ..models.migration_profile import MigrationProfile  # noqa: PLC0415
        from ..models.migration_unsupported import MigrationUnsupported  # noqa: PLC0415

        d = dict(src_dict)
        brands = d.pop("brands")

        pages_per_brand = d.pop("pages_per_brand")

        profiles = []
        _profiles = d.pop("profiles")
        for profiles_item_data in _profiles:
            profiles_item = MigrationProfile.from_dict(profiles_item_data)

            profiles.append(profiles_item)

        recommended_plan = MigrationPlan.from_dict(d.pop("recommended_plan"))

        servable_accounts = d.pop("servable_accounts")

        stays_with_provider = []
        _stays_with_provider = d.pop("stays_with_provider")
        for stays_with_provider_item_data in _stays_with_provider:
            stays_with_provider_item = MigrationUnsupported.from_dict(stays_with_provider_item_data)

            stays_with_provider.append(stays_with_provider_item)

        migration_assessment = cls(
            brands=brands,
            pages_per_brand=pages_per_brand,
            profiles=profiles,
            recommended_plan=recommended_plan,
            servable_accounts=servable_accounts,
            stays_with_provider=stays_with_provider,
        )

        migration_assessment.additional_properties = d
        return migration_assessment

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
