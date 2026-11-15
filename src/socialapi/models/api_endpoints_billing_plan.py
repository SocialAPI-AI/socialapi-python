from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_endpoints_billing_plan_limits import ApiEndpointsBillingPlanLimits


T = TypeVar("T", bound="ApiEndpointsBillingPlan")


@_attrs_define
class ApiEndpointsBillingPlan:
    """
    Attributes:
        annual_price_eur (int | Unset):  Example: 929.
        annual_price_usd (int | Unset):  Example: 1044.
        limits (ApiEndpointsBillingPlanLimits | Unset):
        monthly_price_eur (int | Unset):  Example: 97.
        monthly_price_usd (int | Unset):  Example: 109.
        name (str | Unset):  Example: Full Send.
        popular (bool | Unset):  Example: True.
        tagline (str | Unset):  Example: For growing teams and products.
        tier (str | Unset):  Example: pro.
    """

    annual_price_eur: int | Unset = UNSET
    annual_price_usd: int | Unset = UNSET
    limits: ApiEndpointsBillingPlanLimits | Unset = UNSET
    monthly_price_eur: int | Unset = UNSET
    monthly_price_usd: int | Unset = UNSET
    name: str | Unset = UNSET
    popular: bool | Unset = UNSET
    tagline: str | Unset = UNSET
    tier: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        annual_price_eur = self.annual_price_eur

        annual_price_usd = self.annual_price_usd

        limits: dict[str, Any] | Unset = UNSET
        if not isinstance(self.limits, Unset):
            limits = self.limits.to_dict()

        monthly_price_eur = self.monthly_price_eur

        monthly_price_usd = self.monthly_price_usd

        name = self.name

        popular = self.popular

        tagline = self.tagline

        tier = self.tier

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if annual_price_eur is not UNSET:
            field_dict["annual_price_eur"] = annual_price_eur
        if annual_price_usd is not UNSET:
            field_dict["annual_price_usd"] = annual_price_usd
        if limits is not UNSET:
            field_dict["limits"] = limits
        if monthly_price_eur is not UNSET:
            field_dict["monthly_price_eur"] = monthly_price_eur
        if monthly_price_usd is not UNSET:
            field_dict["monthly_price_usd"] = monthly_price_usd
        if name is not UNSET:
            field_dict["name"] = name
        if popular is not UNSET:
            field_dict["popular"] = popular
        if tagline is not UNSET:
            field_dict["tagline"] = tagline
        if tier is not UNSET:
            field_dict["tier"] = tier

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_endpoints_billing_plan_limits import ApiEndpointsBillingPlanLimits  # noqa: PLC0415

        d = dict(src_dict)
        annual_price_eur = d.pop("annual_price_eur", UNSET)

        annual_price_usd = d.pop("annual_price_usd", UNSET)

        _limits = d.pop("limits", UNSET)
        limits: ApiEndpointsBillingPlanLimits | Unset
        if isinstance(_limits, Unset):
            limits = UNSET
        else:
            limits = ApiEndpointsBillingPlanLimits.from_dict(_limits)

        monthly_price_eur = d.pop("monthly_price_eur", UNSET)

        monthly_price_usd = d.pop("monthly_price_usd", UNSET)

        name = d.pop("name", UNSET)

        popular = d.pop("popular", UNSET)

        tagline = d.pop("tagline", UNSET)

        tier = d.pop("tier", UNSET)

        api_endpoints_billing_plan = cls(
            annual_price_eur=annual_price_eur,
            annual_price_usd=annual_price_usd,
            limits=limits,
            monthly_price_eur=monthly_price_eur,
            monthly_price_usd=monthly_price_usd,
            name=name,
            popular=popular,
            tagline=tagline,
            tier=tier,
        )

        api_endpoints_billing_plan.additional_properties = d
        return api_endpoints_billing_plan

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
