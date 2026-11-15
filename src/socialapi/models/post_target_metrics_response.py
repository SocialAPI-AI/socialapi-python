from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_target_metrics_response_extra import PostTargetMetricsResponseExtra


T = TypeVar("T", bound="PostTargetMetricsResponse")


@_attrs_define
class PostTargetMetricsResponse:
    """
    Attributes:
        comments (int):  Example: 23.
        likes (int):  Example: 142.
        saves (int):  Example: 31.
        shares (int):  Example: 8.
        avg_watch_time_ms (int | Unset): Average time a viewer spent watching the video, in milliseconds. Example: 7400.
        calls (int | Unset): Taps on the profile's call button. Example: 2.
        crossposted_views (int | Unset): Views of the copy shared to another network, for a post shared there too.
            Example: 310.
        directions (int | Unset): Taps on the profile's directions button. Example: 1.
        emails (int | Unset): Taps on the profile's email button. Example: 2.
        extra (PostTargetMetricsResponseExtra | Unset):
        follows (int | Unset): Accounts that followed after seeing the post. Example: 12.
        interactions (int | Unset): Likes, comments, saves and shares combined, as the platform counts them. Example:
            204.
        profile_actions (int | Unset): Actions taken on the account's profile after visiting it from the post.
            website_clicks, calls, directions, emails and texts break it down. Example: 15.
        profile_visits (int | Unset): Visits to the account's profile from the post. Example: 48.
        reach (int | Unset): Unique accounts that saw the post. Example: 3870.
        reposts (int | Unset): Times other accounts reposted the post. Example: 6.
        skip_rate (float | Unset): Percentage of viewers who skipped the video near its start. Example: 42.5.
        texts (int | Unset): Taps on the profile's text message button. Example: 1.
        total_watch_time_ms (int | Unset): Total time all viewers spent watching the video, in milliseconds. Example:
            37888000.
        views (int | Unset): Times the post was shown or played. Example: 5120.
        website_clicks (int | Unset): Clicks on the profile's website link. Example: 9.
    """

    comments: int
    likes: int
    saves: int
    shares: int
    avg_watch_time_ms: int | Unset = UNSET
    calls: int | Unset = UNSET
    crossposted_views: int | Unset = UNSET
    directions: int | Unset = UNSET
    emails: int | Unset = UNSET
    extra: PostTargetMetricsResponseExtra | Unset = UNSET
    follows: int | Unset = UNSET
    interactions: int | Unset = UNSET
    profile_actions: int | Unset = UNSET
    profile_visits: int | Unset = UNSET
    reach: int | Unset = UNSET
    reposts: int | Unset = UNSET
    skip_rate: float | Unset = UNSET
    texts: int | Unset = UNSET
    total_watch_time_ms: int | Unset = UNSET
    views: int | Unset = UNSET
    website_clicks: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        comments = self.comments

        likes = self.likes

        saves = self.saves

        shares = self.shares

        avg_watch_time_ms = self.avg_watch_time_ms

        calls = self.calls

        crossposted_views = self.crossposted_views

        directions = self.directions

        emails = self.emails

        extra: dict[str, Any] | Unset = UNSET
        if not isinstance(self.extra, Unset):
            extra = self.extra.to_dict()

        follows = self.follows

        interactions = self.interactions

        profile_actions = self.profile_actions

        profile_visits = self.profile_visits

        reach = self.reach

        reposts = self.reposts

        skip_rate = self.skip_rate

        texts = self.texts

        total_watch_time_ms = self.total_watch_time_ms

        views = self.views

        website_clicks = self.website_clicks

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "comments": comments,
                "likes": likes,
                "saves": saves,
                "shares": shares,
            }
        )
        if avg_watch_time_ms is not UNSET:
            field_dict["avg_watch_time_ms"] = avg_watch_time_ms
        if calls is not UNSET:
            field_dict["calls"] = calls
        if crossposted_views is not UNSET:
            field_dict["crossposted_views"] = crossposted_views
        if directions is not UNSET:
            field_dict["directions"] = directions
        if emails is not UNSET:
            field_dict["emails"] = emails
        if extra is not UNSET:
            field_dict["extra"] = extra
        if follows is not UNSET:
            field_dict["follows"] = follows
        if interactions is not UNSET:
            field_dict["interactions"] = interactions
        if profile_actions is not UNSET:
            field_dict["profile_actions"] = profile_actions
        if profile_visits is not UNSET:
            field_dict["profile_visits"] = profile_visits
        if reach is not UNSET:
            field_dict["reach"] = reach
        if reposts is not UNSET:
            field_dict["reposts"] = reposts
        if skip_rate is not UNSET:
            field_dict["skip_rate"] = skip_rate
        if texts is not UNSET:
            field_dict["texts"] = texts
        if total_watch_time_ms is not UNSET:
            field_dict["total_watch_time_ms"] = total_watch_time_ms
        if views is not UNSET:
            field_dict["views"] = views
        if website_clicks is not UNSET:
            field_dict["website_clicks"] = website_clicks

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_target_metrics_response_extra import PostTargetMetricsResponseExtra  # noqa: PLC0415

        d = dict(src_dict)
        comments = d.pop("comments")

        likes = d.pop("likes")

        saves = d.pop("saves")

        shares = d.pop("shares")

        avg_watch_time_ms = d.pop("avg_watch_time_ms", UNSET)

        calls = d.pop("calls", UNSET)

        crossposted_views = d.pop("crossposted_views", UNSET)

        directions = d.pop("directions", UNSET)

        emails = d.pop("emails", UNSET)

        _extra = d.pop("extra", UNSET)
        extra: PostTargetMetricsResponseExtra | Unset
        if isinstance(_extra, Unset):
            extra = UNSET
        else:
            extra = PostTargetMetricsResponseExtra.from_dict(_extra)

        follows = d.pop("follows", UNSET)

        interactions = d.pop("interactions", UNSET)

        profile_actions = d.pop("profile_actions", UNSET)

        profile_visits = d.pop("profile_visits", UNSET)

        reach = d.pop("reach", UNSET)

        reposts = d.pop("reposts", UNSET)

        skip_rate = d.pop("skip_rate", UNSET)

        texts = d.pop("texts", UNSET)

        total_watch_time_ms = d.pop("total_watch_time_ms", UNSET)

        views = d.pop("views", UNSET)

        website_clicks = d.pop("website_clicks", UNSET)

        post_target_metrics_response = cls(
            comments=comments,
            likes=likes,
            saves=saves,
            shares=shares,
            avg_watch_time_ms=avg_watch_time_ms,
            calls=calls,
            crossposted_views=crossposted_views,
            directions=directions,
            emails=emails,
            extra=extra,
            follows=follows,
            interactions=interactions,
            profile_actions=profile_actions,
            profile_visits=profile_visits,
            reach=reach,
            reposts=reposts,
            skip_rate=skip_rate,
            texts=texts,
            total_watch_time_ms=total_watch_time_ms,
            views=views,
            website_clicks=website_clicks,
        )

        post_target_metrics_response.additional_properties = d
        return post_target_metrics_response

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
