from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="UsageResponse")


@_attrs_define
class UsageResponse:
    """
    Attributes:
        brands_limit (int):  Example: 10.
        brands_used (int):  Example: 3.
        interactions_limit (int):  Example: 5000.
        interactions_used (int):  Example: 1200.
        page_allowance (int):  Example: 5.
        page_billing_exempt (bool):  Example: False.
        period_end (str):  Example: 2026-03-15T00:00:00Z.
        period_start (str):  Example: 2026-02-15T00:00:00Z.
        posts_limit (int):  Example: 200.
        posts_used (int):  Example: 42.
        profile_units_limit (int):  Example: 10.
        profile_units_used (int):  Example: 4.
    """

    brands_limit: int
    brands_used: int
    interactions_limit: int
    interactions_used: int
    page_allowance: int
    page_billing_exempt: bool
    period_end: str
    period_start: str
    posts_limit: int
    posts_used: int
    profile_units_limit: int
    profile_units_used: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        brands_limit = self.brands_limit

        brands_used = self.brands_used

        interactions_limit = self.interactions_limit

        interactions_used = self.interactions_used

        page_allowance = self.page_allowance

        page_billing_exempt = self.page_billing_exempt

        period_end = self.period_end

        period_start = self.period_start

        posts_limit = self.posts_limit

        posts_used = self.posts_used

        profile_units_limit = self.profile_units_limit

        profile_units_used = self.profile_units_used

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "brands_limit": brands_limit,
                "brands_used": brands_used,
                "interactions_limit": interactions_limit,
                "interactions_used": interactions_used,
                "page_allowance": page_allowance,
                "page_billing_exempt": page_billing_exempt,
                "period_end": period_end,
                "period_start": period_start,
                "posts_limit": posts_limit,
                "posts_used": posts_used,
                "profile_units_limit": profile_units_limit,
                "profile_units_used": profile_units_used,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        brands_limit = d.pop("brands_limit")

        brands_used = d.pop("brands_used")

        interactions_limit = d.pop("interactions_limit")

        interactions_used = d.pop("interactions_used")

        page_allowance = d.pop("page_allowance")

        page_billing_exempt = d.pop("page_billing_exempt")

        period_end = d.pop("period_end")

        period_start = d.pop("period_start")

        posts_limit = d.pop("posts_limit")

        posts_used = d.pop("posts_used")

        profile_units_limit = d.pop("profile_units_limit")

        profile_units_used = d.pop("profile_units_used")

        usage_response = cls(
            brands_limit=brands_limit,
            brands_used=brands_used,
            interactions_limit=interactions_limit,
            interactions_used=interactions_used,
            page_allowance=page_allowance,
            page_billing_exempt=page_billing_exempt,
            period_end=period_end,
            period_start=period_start,
            posts_limit=posts_limit,
            posts_used=posts_used,
            profile_units_limit=profile_units_limit,
            profile_units_used=profile_units_used,
        )

        usage_response.additional_properties = d
        return usage_response

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
