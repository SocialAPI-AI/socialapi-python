from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SocialApiAiCoreApiServiceOverviewDay")


@_attrs_define
class SocialApiAiCoreApiServiceOverviewDay:
    """
    Attributes:
        day (str | Unset):  Example: 2026-10-14.
        engagements (int | Unset):  Example: 290.
        posts (int | Unset):  Example: 3.
    """

    day: str | Unset = UNSET
    engagements: int | Unset = UNSET
    posts: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        day = self.day

        engagements = self.engagements

        posts = self.posts

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if day is not UNSET:
            field_dict["day"] = day
        if engagements is not UNSET:
            field_dict["engagements"] = engagements
        if posts is not UNSET:
            field_dict["posts"] = posts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        day = d.pop("day", UNSET)

        engagements = d.pop("engagements", UNSET)

        posts = d.pop("posts", UNSET)

        social_api_ai_core_api_service_overview_day = cls(
            day=day,
            engagements=engagements,
            posts=posts,
        )

        social_api_ai_core_api_service_overview_day.additional_properties = d
        return social_api_ai_core_api_service_overview_day

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
