from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="InstagramAccountSummaryResponse")


@_attrs_define
class InstagramAccountSummaryResponse:
    """
    Attributes:
        accounts_engaged (int):
        display_name (str):
        follower_count (int):
        following_count (int):
        interactions (int):
        media_count (int):
        net_follows (int):
        period_end (datetime.datetime):
        period_start (datetime.datetime):
        picture_url (str):
        reach (int):
        username (str):
        views (int):
    """

    accounts_engaged: int
    display_name: str
    follower_count: int
    following_count: int
    interactions: int
    media_count: int
    net_follows: int
    period_end: datetime.datetime
    period_start: datetime.datetime
    picture_url: str
    reach: int
    username: str
    views: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        accounts_engaged = self.accounts_engaged

        display_name = self.display_name

        follower_count = self.follower_count

        following_count = self.following_count

        interactions = self.interactions

        media_count = self.media_count

        net_follows = self.net_follows

        period_end = self.period_end.isoformat()

        period_start = self.period_start.isoformat()

        picture_url = self.picture_url

        reach = self.reach

        username = self.username

        views = self.views

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accounts_engaged": accounts_engaged,
                "display_name": display_name,
                "follower_count": follower_count,
                "following_count": following_count,
                "interactions": interactions,
                "media_count": media_count,
                "net_follows": net_follows,
                "period_end": period_end,
                "period_start": period_start,
                "picture_url": picture_url,
                "reach": reach,
                "username": username,
                "views": views,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        accounts_engaged = d.pop("accounts_engaged")

        display_name = d.pop("display_name")

        follower_count = d.pop("follower_count")

        following_count = d.pop("following_count")

        interactions = d.pop("interactions")

        media_count = d.pop("media_count")

        net_follows = d.pop("net_follows")

        period_end = datetime.datetime.fromisoformat(d.pop("period_end"))

        period_start = datetime.datetime.fromisoformat(d.pop("period_start"))

        picture_url = d.pop("picture_url")

        reach = d.pop("reach")

        username = d.pop("username")

        views = d.pop("views")

        instagram_account_summary_response = cls(
            accounts_engaged=accounts_engaged,
            display_name=display_name,
            follower_count=follower_count,
            following_count=following_count,
            interactions=interactions,
            media_count=media_count,
            net_follows=net_follows,
            period_end=period_end,
            period_start=period_start,
            picture_url=picture_url,
            reach=reach,
            username=username,
            views=views,
        )

        instagram_account_summary_response.additional_properties = d
        return instagram_account_summary_response

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
