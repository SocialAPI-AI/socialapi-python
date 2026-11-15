from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="OverviewDay")


@_attrs_define
class OverviewDay:
    """
    Attributes:
        day (str):  Example: 2026-10-14.
        engagements (int):  Example: 290.
        posts (int):  Example: 3.
    """

    day: str
    engagements: int
    posts: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        day = self.day

        engagements = self.engagements

        posts = self.posts

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "day": day,
                "engagements": engagements,
                "posts": posts,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        day = d.pop("day")

        engagements = d.pop("engagements")

        posts = d.pop("posts")

        overview_day = cls(
            day=day,
            engagements=engagements,
            posts=posts,
        )

        overview_day.additional_properties = d
        return overview_day

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
