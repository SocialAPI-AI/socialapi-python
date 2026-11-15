from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PinterestSummaryResponse")


@_attrs_define
class PinterestSummaryResponse:
    """
    Attributes:
        board_count (int):  Example: 23.
        follower_count (int):  Example: 12400.
        monthly_views (int):  Example: 1200000.
        pin_count (int):  Example: 847.
        profile_image (str):  Example: https://i.pinimg.com/x.jpg.
        username (str):  Example: boardandco.
    """

    board_count: int
    follower_count: int
    monthly_views: int
    pin_count: int
    profile_image: str
    username: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        board_count = self.board_count

        follower_count = self.follower_count

        monthly_views = self.monthly_views

        pin_count = self.pin_count

        profile_image = self.profile_image

        username = self.username

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "board_count": board_count,
                "follower_count": follower_count,
                "monthly_views": monthly_views,
                "pin_count": pin_count,
                "profile_image": profile_image,
                "username": username,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        board_count = d.pop("board_count")

        follower_count = d.pop("follower_count")

        monthly_views = d.pop("monthly_views")

        pin_count = d.pop("pin_count")

        profile_image = d.pop("profile_image")

        username = d.pop("username")

        pinterest_summary_response = cls(
            board_count=board_count,
            follower_count=follower_count,
            monthly_views=monthly_views,
            pin_count=pin_count,
            profile_image=profile_image,
            username=username,
        )

        pinterest_summary_response.additional_properties = d
        return pinterest_summary_response

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
