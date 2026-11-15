from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SocialApiAiCoreApiConnectorsBaseDailyInsight")


@_attrs_define
class SocialApiAiCoreApiConnectorsBaseDailyInsight:
    """
    Attributes:
        date (str | Unset): Day in YYYY-MM-DD. Example: 2026-09-27.
        followers (int | Unset):
        interactions (int | Unset):
        reach (int | Unset):
        views (int | Unset):
    """

    date: str | Unset = UNSET
    followers: int | Unset = UNSET
    interactions: int | Unset = UNSET
    reach: int | Unset = UNSET
    views: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date = self.date

        followers = self.followers

        interactions = self.interactions

        reach = self.reach

        views = self.views

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if date is not UNSET:
            field_dict["date"] = date
        if followers is not UNSET:
            field_dict["followers"] = followers
        if interactions is not UNSET:
            field_dict["interactions"] = interactions
        if reach is not UNSET:
            field_dict["reach"] = reach
        if views is not UNSET:
            field_dict["views"] = views

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        date = d.pop("date", UNSET)

        followers = d.pop("followers", UNSET)

        interactions = d.pop("interactions", UNSET)

        reach = d.pop("reach", UNSET)

        views = d.pop("views", UNSET)

        social_api_ai_core_api_connectors_base_daily_insight = cls(
            date=date,
            followers=followers,
            interactions=interactions,
            reach=reach,
            views=views,
        )

        social_api_ai_core_api_connectors_base_daily_insight.additional_properties = d
        return social_api_ai_core_api_connectors_base_daily_insight

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
