from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiEndpointsFacebookAccountSummaryResponse")


@_attrs_define
class ApiEndpointsFacebookAccountSummaryResponse:
    """
    Attributes:
        follower_count (int | Unset):
        interactions (int | Unset):
        net_follows (int | Unset):
        period_end (str | Unset):
        period_start (str | Unset):
        reach (int | Unset):
        views (int | Unset):
    """

    follower_count: int | Unset = UNSET
    interactions: int | Unset = UNSET
    net_follows: int | Unset = UNSET
    period_end: str | Unset = UNSET
    period_start: str | Unset = UNSET
    reach: int | Unset = UNSET
    views: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        follower_count = self.follower_count

        interactions = self.interactions

        net_follows = self.net_follows

        period_end = self.period_end

        period_start = self.period_start

        reach = self.reach

        views = self.views

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if follower_count is not UNSET:
            field_dict["follower_count"] = follower_count
        if interactions is not UNSET:
            field_dict["interactions"] = interactions
        if net_follows is not UNSET:
            field_dict["net_follows"] = net_follows
        if period_end is not UNSET:
            field_dict["period_end"] = period_end
        if period_start is not UNSET:
            field_dict["period_start"] = period_start
        if reach is not UNSET:
            field_dict["reach"] = reach
        if views is not UNSET:
            field_dict["views"] = views

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        follower_count = d.pop("follower_count", UNSET)

        interactions = d.pop("interactions", UNSET)

        net_follows = d.pop("net_follows", UNSET)

        period_end = d.pop("period_end", UNSET)

        period_start = d.pop("period_start", UNSET)

        reach = d.pop("reach", UNSET)

        views = d.pop("views", UNSET)

        api_endpoints_facebook_account_summary_response = cls(
            follower_count=follower_count,
            interactions=interactions,
            net_follows=net_follows,
            period_end=period_end,
            period_start=period_start,
            reach=reach,
            views=views,
        )

        api_endpoints_facebook_account_summary_response.additional_properties = d
        return api_endpoints_facebook_account_summary_response

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
