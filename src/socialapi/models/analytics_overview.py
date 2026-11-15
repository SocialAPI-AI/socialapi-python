from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.metric_series import MetricSeries
    from ..models.overview_best_times import OverviewBestTimes
    from ..models.overview_day import OverviewDay
    from ..models.overview_format import OverviewFormat
    from ..models.overview_platform import OverviewPlatform
    from ..models.overview_top_post import OverviewTopPost
    from ..models.overview_totals import OverviewTotals


T = TypeVar("T", bound="AnalyticsOverview")


@_attrs_define
class AnalyticsOverview:
    """
    Attributes:
        accounts_excluded (int): AccountsExcluded is how many accounts in scope were left out because
            they lack the analytics.read permission. Example: 0.
        activity (list[MetricSeries]): Activity is the daily count of replies, DMs and moderation SocialAPI
            performed for the accounts in scope, the same series shape as the
            history routes.
        best_times (OverviewBestTimes):
        by_day (list[OverviewDay]):
        by_format (list[OverviewFormat]):
        by_platform (list[OverviewPlatform]):
        from_ (str):  Example: 2026-10-07.
        previous (OverviewTotals):
        to (str):  Example: 2026-11-05.
        top_posts (list[OverviewTopPost]):
        totals (OverviewTotals):
        tz (str):  Example: Europe/Paris.
        metrics_synced_at (datetime.datetime | Unset): MetricsSyncedAt is the most recent counter refresh among the
            posts in
            range. Absent when none has been refreshed yet. Example: 2026-11-05T08:00:00Z.
    """

    accounts_excluded: int
    activity: list[MetricSeries]
    best_times: OverviewBestTimes
    by_day: list[OverviewDay]
    by_format: list[OverviewFormat]
    by_platform: list[OverviewPlatform]
    from_: str
    previous: OverviewTotals
    to: str
    top_posts: list[OverviewTopPost]
    totals: OverviewTotals
    tz: str
    metrics_synced_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        accounts_excluded = self.accounts_excluded

        activity = []
        for activity_item_data in self.activity:
            activity_item = activity_item_data.to_dict()
            activity.append(activity_item)

        best_times = self.best_times.to_dict()

        by_day = []
        for by_day_item_data in self.by_day:
            by_day_item = by_day_item_data.to_dict()
            by_day.append(by_day_item)

        by_format = []
        for by_format_item_data in self.by_format:
            by_format_item = by_format_item_data.to_dict()
            by_format.append(by_format_item)

        by_platform = []
        for by_platform_item_data in self.by_platform:
            by_platform_item = by_platform_item_data.to_dict()
            by_platform.append(by_platform_item)

        from_ = self.from_

        previous = self.previous.to_dict()

        to = self.to

        top_posts = []
        for top_posts_item_data in self.top_posts:
            top_posts_item = top_posts_item_data.to_dict()
            top_posts.append(top_posts_item)

        totals = self.totals.to_dict()

        tz = self.tz

        metrics_synced_at: str | Unset = UNSET
        if not isinstance(self.metrics_synced_at, Unset):
            metrics_synced_at = self.metrics_synced_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accounts_excluded": accounts_excluded,
                "activity": activity,
                "best_times": best_times,
                "by_day": by_day,
                "by_format": by_format,
                "by_platform": by_platform,
                "from": from_,
                "previous": previous,
                "to": to,
                "top_posts": top_posts,
                "totals": totals,
                "tz": tz,
            }
        )
        if metrics_synced_at is not UNSET:
            field_dict["metrics_synced_at"] = metrics_synced_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.metric_series import MetricSeries  # noqa: PLC0415
        from ..models.overview_best_times import OverviewBestTimes  # noqa: PLC0415
        from ..models.overview_day import OverviewDay  # noqa: PLC0415
        from ..models.overview_format import OverviewFormat  # noqa: PLC0415
        from ..models.overview_platform import OverviewPlatform  # noqa: PLC0415
        from ..models.overview_top_post import OverviewTopPost  # noqa: PLC0415
        from ..models.overview_totals import OverviewTotals  # noqa: PLC0415

        d = dict(src_dict)
        accounts_excluded = d.pop("accounts_excluded")

        activity = []
        _activity = d.pop("activity")
        for activity_item_data in _activity:
            activity_item = MetricSeries.from_dict(activity_item_data)

            activity.append(activity_item)

        best_times = OverviewBestTimes.from_dict(d.pop("best_times"))

        by_day = []
        _by_day = d.pop("by_day")
        for by_day_item_data in _by_day:
            by_day_item = OverviewDay.from_dict(by_day_item_data)

            by_day.append(by_day_item)

        by_format = []
        _by_format = d.pop("by_format")
        for by_format_item_data in _by_format:
            by_format_item = OverviewFormat.from_dict(by_format_item_data)

            by_format.append(by_format_item)

        by_platform = []
        _by_platform = d.pop("by_platform")
        for by_platform_item_data in _by_platform:
            by_platform_item = OverviewPlatform.from_dict(by_platform_item_data)

            by_platform.append(by_platform_item)

        from_ = d.pop("from")

        previous = OverviewTotals.from_dict(d.pop("previous"))

        to = d.pop("to")

        top_posts = []
        _top_posts = d.pop("top_posts")
        for top_posts_item_data in _top_posts:
            top_posts_item = OverviewTopPost.from_dict(top_posts_item_data)

            top_posts.append(top_posts_item)

        totals = OverviewTotals.from_dict(d.pop("totals"))

        tz = d.pop("tz")

        _metrics_synced_at = d.pop("metrics_synced_at", UNSET)
        metrics_synced_at: datetime.datetime | Unset
        if isinstance(_metrics_synced_at, Unset):
            metrics_synced_at = UNSET
        else:
            metrics_synced_at = datetime.datetime.fromisoformat(_metrics_synced_at)

        analytics_overview = cls(
            accounts_excluded=accounts_excluded,
            activity=activity,
            best_times=best_times,
            by_day=by_day,
            by_format=by_format,
            by_platform=by_platform,
            from_=from_,
            previous=previous,
            to=to,
            top_posts=top_posts,
            totals=totals,
            tz=tz,
            metrics_synced_at=metrics_synced_at,
        )

        analytics_overview.additional_properties = d
        return analytics_overview

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
