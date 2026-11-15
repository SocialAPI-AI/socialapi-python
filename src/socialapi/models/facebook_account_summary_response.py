from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="FacebookAccountSummaryResponse")


@_attrs_define
class FacebookAccountSummaryResponse:
    """
    Attributes:
        follower_count (int):
        interactions (int):
        net_follows (int):
        period_end (str):
        period_start (str):
        reach (int):
        views (int):
    """

    follower_count: int
    interactions: int
    net_follows: int
    period_end: str
    period_start: str
    reach: int
    views: int
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
        field_dict.update(
            {
                "follower_count": follower_count,
                "interactions": interactions,
                "net_follows": net_follows,
                "period_end": period_end,
                "period_start": period_start,
                "reach": reach,
                "views": views,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        follower_count = d.pop("follower_count")

        interactions = d.pop("interactions")

        net_follows = d.pop("net_follows")

        period_end = d.pop("period_end")

        period_start = d.pop("period_start")

        reach = d.pop("reach")

        views = d.pop("views")

        facebook_account_summary_response = cls(
            follower_count=follower_count,
            interactions=interactions,
            net_follows=net_follows,
            period_end=period_end,
            period_start=period_start,
            reach=reach,
            views=views,
        )

        facebook_account_summary_response.additional_properties = d
        return facebook_account_summary_response

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
