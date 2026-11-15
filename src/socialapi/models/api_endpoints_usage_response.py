from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiEndpointsUsageResponse")


@_attrs_define
class ApiEndpointsUsageResponse:
    """
    Attributes:
        brands_limit (int | Unset):  Example: 10.
        brands_used (int | Unset):  Example: 3.
        interactions_limit (int | Unset):  Example: 5000.
        interactions_used (int | Unset):  Example: 1200.
        page_allowance (int | Unset):  Example: 5.
        page_billing_exempt (bool | Unset):  Example: False.
        period_end (str | Unset):  Example: 2026-03-15T00:00:00Z.
        period_start (str | Unset):  Example: 2026-02-15T00:00:00Z.
        posts_limit (int | Unset):  Example: 200.
        posts_used (int | Unset):  Example: 42.
        profile_units_limit (int | Unset):  Example: 10.
        profile_units_used (int | Unset):  Example: 4.
    """

    brands_limit: int | Unset = UNSET
    brands_used: int | Unset = UNSET
    interactions_limit: int | Unset = UNSET
    interactions_used: int | Unset = UNSET
    page_allowance: int | Unset = UNSET
    page_billing_exempt: bool | Unset = UNSET
    period_end: str | Unset = UNSET
    period_start: str | Unset = UNSET
    posts_limit: int | Unset = UNSET
    posts_used: int | Unset = UNSET
    profile_units_limit: int | Unset = UNSET
    profile_units_used: int | Unset = UNSET
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
        field_dict.update({})
        if brands_limit is not UNSET:
            field_dict["brands_limit"] = brands_limit
        if brands_used is not UNSET:
            field_dict["brands_used"] = brands_used
        if interactions_limit is not UNSET:
            field_dict["interactions_limit"] = interactions_limit
        if interactions_used is not UNSET:
            field_dict["interactions_used"] = interactions_used
        if page_allowance is not UNSET:
            field_dict["page_allowance"] = page_allowance
        if page_billing_exempt is not UNSET:
            field_dict["page_billing_exempt"] = page_billing_exempt
        if period_end is not UNSET:
            field_dict["period_end"] = period_end
        if period_start is not UNSET:
            field_dict["period_start"] = period_start
        if posts_limit is not UNSET:
            field_dict["posts_limit"] = posts_limit
        if posts_used is not UNSET:
            field_dict["posts_used"] = posts_used
        if profile_units_limit is not UNSET:
            field_dict["profile_units_limit"] = profile_units_limit
        if profile_units_used is not UNSET:
            field_dict["profile_units_used"] = profile_units_used

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        brands_limit = d.pop("brands_limit", UNSET)

        brands_used = d.pop("brands_used", UNSET)

        interactions_limit = d.pop("interactions_limit", UNSET)

        interactions_used = d.pop("interactions_used", UNSET)

        page_allowance = d.pop("page_allowance", UNSET)

        page_billing_exempt = d.pop("page_billing_exempt", UNSET)

        period_end = d.pop("period_end", UNSET)

        period_start = d.pop("period_start", UNSET)

        posts_limit = d.pop("posts_limit", UNSET)

        posts_used = d.pop("posts_used", UNSET)

        profile_units_limit = d.pop("profile_units_limit", UNSET)

        profile_units_used = d.pop("profile_units_used", UNSET)

        api_endpoints_usage_response = cls(
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

        api_endpoints_usage_response.additional_properties = d
        return api_endpoints_usage_response

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
