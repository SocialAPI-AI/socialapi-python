from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.billing_plan_limits import BillingPlanLimits


T = TypeVar("T", bound="BillingPlan")


@_attrs_define
class BillingPlan:
    """
    Attributes:
        annual_price_eur (int):  Example: 929.
        annual_price_usd (int):  Example: 1044.
        limits (BillingPlanLimits):
        monthly_price_eur (int):  Example: 97.
        monthly_price_usd (int):  Example: 109.
        name (str):  Example: Full Send.
        popular (bool):  Example: True.
        tagline (str):  Example: For growing teams and products.
        tier (str):  Example: pro.
    """

    annual_price_eur: int
    annual_price_usd: int
    limits: BillingPlanLimits
    monthly_price_eur: int
    monthly_price_usd: int
    name: str
    popular: bool
    tagline: str
    tier: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        annual_price_eur = self.annual_price_eur

        annual_price_usd = self.annual_price_usd

        limits = self.limits.to_dict()

        monthly_price_eur = self.monthly_price_eur

        monthly_price_usd = self.monthly_price_usd

        name = self.name

        popular = self.popular

        tagline = self.tagline

        tier = self.tier

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "annual_price_eur": annual_price_eur,
                "annual_price_usd": annual_price_usd,
                "limits": limits,
                "monthly_price_eur": monthly_price_eur,
                "monthly_price_usd": monthly_price_usd,
                "name": name,
                "popular": popular,
                "tagline": tagline,
                "tier": tier,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.billing_plan_limits import BillingPlanLimits  # noqa: PLC0415

        d = dict(src_dict)
        annual_price_eur = d.pop("annual_price_eur")

        annual_price_usd = d.pop("annual_price_usd")

        limits = BillingPlanLimits.from_dict(d.pop("limits"))

        monthly_price_eur = d.pop("monthly_price_eur")

        monthly_price_usd = d.pop("monthly_price_usd")

        name = d.pop("name")

        popular = d.pop("popular")

        tagline = d.pop("tagline")

        tier = d.pop("tier")

        billing_plan = cls(
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

        billing_plan.additional_properties = d
        return billing_plan

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
