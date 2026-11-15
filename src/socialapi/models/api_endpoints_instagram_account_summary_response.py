from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiEndpointsInstagramAccountSummaryResponse")


@_attrs_define
class ApiEndpointsInstagramAccountSummaryResponse:
    """
    Attributes:
        accounts_engaged (int | Unset):
        display_name (str | Unset):
        follower_count (int | Unset):
        following_count (int | Unset):
        interactions (int | Unset):
        media_count (int | Unset):
        net_follows (int | Unset):
        period_end (str | Unset):
        period_start (str | Unset):
        picture_url (str | Unset):
        reach (int | Unset):
        username (str | Unset):
        views (int | Unset):
    """

    accounts_engaged: int | Unset = UNSET
    display_name: str | Unset = UNSET
    follower_count: int | Unset = UNSET
    following_count: int | Unset = UNSET
    interactions: int | Unset = UNSET
    media_count: int | Unset = UNSET
    net_follows: int | Unset = UNSET
    period_end: str | Unset = UNSET
    period_start: str | Unset = UNSET
    picture_url: str | Unset = UNSET
    reach: int | Unset = UNSET
    username: str | Unset = UNSET
    views: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        accounts_engaged = self.accounts_engaged

        display_name = self.display_name

        follower_count = self.follower_count

        following_count = self.following_count

        interactions = self.interactions

        media_count = self.media_count

        net_follows = self.net_follows

        period_end = self.period_end

        period_start = self.period_start

        picture_url = self.picture_url

        reach = self.reach

        username = self.username

        views = self.views

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if accounts_engaged is not UNSET:
            field_dict["accounts_engaged"] = accounts_engaged
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if follower_count is not UNSET:
            field_dict["follower_count"] = follower_count
        if following_count is not UNSET:
            field_dict["following_count"] = following_count
        if interactions is not UNSET:
            field_dict["interactions"] = interactions
        if media_count is not UNSET:
            field_dict["media_count"] = media_count
        if net_follows is not UNSET:
            field_dict["net_follows"] = net_follows
        if period_end is not UNSET:
            field_dict["period_end"] = period_end
        if period_start is not UNSET:
            field_dict["period_start"] = period_start
        if picture_url is not UNSET:
            field_dict["picture_url"] = picture_url
        if reach is not UNSET:
            field_dict["reach"] = reach
        if username is not UNSET:
            field_dict["username"] = username
        if views is not UNSET:
            field_dict["views"] = views

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        accounts_engaged = d.pop("accounts_engaged", UNSET)

        display_name = d.pop("display_name", UNSET)

        follower_count = d.pop("follower_count", UNSET)

        following_count = d.pop("following_count", UNSET)

        interactions = d.pop("interactions", UNSET)

        media_count = d.pop("media_count", UNSET)

        net_follows = d.pop("net_follows", UNSET)

        period_end = d.pop("period_end", UNSET)

        period_start = d.pop("period_start", UNSET)

        picture_url = d.pop("picture_url", UNSET)

        reach = d.pop("reach", UNSET)

        username = d.pop("username", UNSET)

        views = d.pop("views", UNSET)

        api_endpoints_instagram_account_summary_response = cls(
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

        api_endpoints_instagram_account_summary_response.additional_properties = d
        return api_endpoints_instagram_account_summary_response

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
