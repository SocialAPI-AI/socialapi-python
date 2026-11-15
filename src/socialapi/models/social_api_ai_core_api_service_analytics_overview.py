from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.social_api_ai_core_api_service_metric_series import SocialApiAiCoreApiServiceMetricSeries
    from ..models.social_api_ai_core_api_service_overview_best_times import SocialApiAiCoreApiServiceOverviewBestTimes
    from ..models.social_api_ai_core_api_service_overview_day import SocialApiAiCoreApiServiceOverviewDay
    from ..models.social_api_ai_core_api_service_overview_format import SocialApiAiCoreApiServiceOverviewFormat
    from ..models.social_api_ai_core_api_service_overview_platform import SocialApiAiCoreApiServiceOverviewPlatform
    from ..models.social_api_ai_core_api_service_overview_top_post import SocialApiAiCoreApiServiceOverviewTopPost
    from ..models.social_api_ai_core_api_service_overview_totals import SocialApiAiCoreApiServiceOverviewTotals


T = TypeVar("T", bound="SocialApiAiCoreApiServiceAnalyticsOverview")


@_attrs_define
class SocialApiAiCoreApiServiceAnalyticsOverview:
    """
    Attributes:
        accounts_excluded (int | Unset): AccountsExcluded is how many accounts in scope were left out because
            they lack the analytics.read permission. Example: 0.
        activity (list[SocialApiAiCoreApiServiceMetricSeries] | Unset): Activity is the daily count of replies, DMs and
            moderation SocialAPI
            performed for the accounts in scope, the same series shape as the
            history routes.
        best_times (SocialApiAiCoreApiServiceOverviewBestTimes | Unset):
        by_day (list[SocialApiAiCoreApiServiceOverviewDay] | Unset):
        by_format (list[SocialApiAiCoreApiServiceOverviewFormat] | Unset):
        by_platform (list[SocialApiAiCoreApiServiceOverviewPlatform] | Unset):
        from_ (str | Unset):  Example: 2026-10-07.
        metrics_synced_at (str | Unset): MetricsSyncedAt is the most recent counter refresh among the posts in
            range. Absent when none has been refreshed yet. Example: 2026-11-05T08:00:00Z.
        previous (SocialApiAiCoreApiServiceOverviewTotals | Unset):
        to (str | Unset):  Example: 2026-11-05.
        top_posts (list[SocialApiAiCoreApiServiceOverviewTopPost] | Unset):
        totals (SocialApiAiCoreApiServiceOverviewTotals | Unset):
        tz (str | Unset):  Example: Europe/Paris.
    """

    accounts_excluded: int | Unset = UNSET
    activity: list[SocialApiAiCoreApiServiceMetricSeries] | Unset = UNSET
    best_times: SocialApiAiCoreApiServiceOverviewBestTimes | Unset = UNSET
    by_day: list[SocialApiAiCoreApiServiceOverviewDay] | Unset = UNSET
    by_format: list[SocialApiAiCoreApiServiceOverviewFormat] | Unset = UNSET
    by_platform: list[SocialApiAiCoreApiServiceOverviewPlatform] | Unset = UNSET
    from_: str | Unset = UNSET
    metrics_synced_at: str | Unset = UNSET
    previous: SocialApiAiCoreApiServiceOverviewTotals | Unset = UNSET
    to: str | Unset = UNSET
    top_posts: list[SocialApiAiCoreApiServiceOverviewTopPost] | Unset = UNSET
    totals: SocialApiAiCoreApiServiceOverviewTotals | Unset = UNSET
    tz: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        accounts_excluded = self.accounts_excluded

        activity: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.activity, Unset):
            activity = []
            for activity_item_data in self.activity:
                activity_item = activity_item_data.to_dict()
                activity.append(activity_item)

        best_times: dict[str, Any] | Unset = UNSET
        if not isinstance(self.best_times, Unset):
            best_times = self.best_times.to_dict()

        by_day: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.by_day, Unset):
            by_day = []
            for by_day_item_data in self.by_day:
                by_day_item = by_day_item_data.to_dict()
                by_day.append(by_day_item)

        by_format: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.by_format, Unset):
            by_format = []
            for by_format_item_data in self.by_format:
                by_format_item = by_format_item_data.to_dict()
                by_format.append(by_format_item)

        by_platform: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.by_platform, Unset):
            by_platform = []
            for by_platform_item_data in self.by_platform:
                by_platform_item = by_platform_item_data.to_dict()
                by_platform.append(by_platform_item)

        from_ = self.from_

        metrics_synced_at = self.metrics_synced_at

        previous: dict[str, Any] | Unset = UNSET
        if not isinstance(self.previous, Unset):
            previous = self.previous.to_dict()

        to = self.to

        top_posts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.top_posts, Unset):
            top_posts = []
            for top_posts_item_data in self.top_posts:
                top_posts_item = top_posts_item_data.to_dict()
                top_posts.append(top_posts_item)

        totals: dict[str, Any] | Unset = UNSET
        if not isinstance(self.totals, Unset):
            totals = self.totals.to_dict()

        tz = self.tz

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if accounts_excluded is not UNSET:
            field_dict["accounts_excluded"] = accounts_excluded
        if activity is not UNSET:
            field_dict["activity"] = activity
        if best_times is not UNSET:
            field_dict["best_times"] = best_times
        if by_day is not UNSET:
            field_dict["by_day"] = by_day
        if by_format is not UNSET:
            field_dict["by_format"] = by_format
        if by_platform is not UNSET:
            field_dict["by_platform"] = by_platform
        if from_ is not UNSET:
            field_dict["from"] = from_
        if metrics_synced_at is not UNSET:
            field_dict["metrics_synced_at"] = metrics_synced_at
        if previous is not UNSET:
            field_dict["previous"] = previous
        if to is not UNSET:
            field_dict["to"] = to
        if top_posts is not UNSET:
            field_dict["top_posts"] = top_posts
        if totals is not UNSET:
            field_dict["totals"] = totals
        if tz is not UNSET:
            field_dict["tz"] = tz

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.social_api_ai_core_api_service_metric_series import (
            SocialApiAiCoreApiServiceMetricSeries,  # noqa: PLC0415
        )
        from ..models.social_api_ai_core_api_service_overview_best_times import (
            SocialApiAiCoreApiServiceOverviewBestTimes,  # noqa: PLC0415
        )
        from ..models.social_api_ai_core_api_service_overview_day import (
            SocialApiAiCoreApiServiceOverviewDay,  # noqa: PLC0415
        )
        from ..models.social_api_ai_core_api_service_overview_format import (
            SocialApiAiCoreApiServiceOverviewFormat,  # noqa: PLC0415
        )
        from ..models.social_api_ai_core_api_service_overview_platform import (
            SocialApiAiCoreApiServiceOverviewPlatform,  # noqa: PLC0415
        )
        from ..models.social_api_ai_core_api_service_overview_top_post import (
            SocialApiAiCoreApiServiceOverviewTopPost,  # noqa: PLC0415
        )
        from ..models.social_api_ai_core_api_service_overview_totals import (
            SocialApiAiCoreApiServiceOverviewTotals,  # noqa: PLC0415
        )

        d = dict(src_dict)
        accounts_excluded = d.pop("accounts_excluded", UNSET)

        _activity = d.pop("activity", UNSET)
        activity: list[SocialApiAiCoreApiServiceMetricSeries] | Unset = UNSET
        if _activity is not UNSET:
            activity = []
            for activity_item_data in _activity:
                activity_item = SocialApiAiCoreApiServiceMetricSeries.from_dict(activity_item_data)

                activity.append(activity_item)

        _best_times = d.pop("best_times", UNSET)
        best_times: SocialApiAiCoreApiServiceOverviewBestTimes | Unset
        if isinstance(_best_times, Unset):
            best_times = UNSET
        else:
            best_times = SocialApiAiCoreApiServiceOverviewBestTimes.from_dict(_best_times)

        _by_day = d.pop("by_day", UNSET)
        by_day: list[SocialApiAiCoreApiServiceOverviewDay] | Unset = UNSET
        if _by_day is not UNSET:
            by_day = []
            for by_day_item_data in _by_day:
                by_day_item = SocialApiAiCoreApiServiceOverviewDay.from_dict(by_day_item_data)

                by_day.append(by_day_item)

        _by_format = d.pop("by_format", UNSET)
        by_format: list[SocialApiAiCoreApiServiceOverviewFormat] | Unset = UNSET
        if _by_format is not UNSET:
            by_format = []
            for by_format_item_data in _by_format:
                by_format_item = SocialApiAiCoreApiServiceOverviewFormat.from_dict(by_format_item_data)

                by_format.append(by_format_item)

        _by_platform = d.pop("by_platform", UNSET)
        by_platform: list[SocialApiAiCoreApiServiceOverviewPlatform] | Unset = UNSET
        if _by_platform is not UNSET:
            by_platform = []
            for by_platform_item_data in _by_platform:
                by_platform_item = SocialApiAiCoreApiServiceOverviewPlatform.from_dict(by_platform_item_data)

                by_platform.append(by_platform_item)

        from_ = d.pop("from", UNSET)

        metrics_synced_at = d.pop("metrics_synced_at", UNSET)

        _previous = d.pop("previous", UNSET)
        previous: SocialApiAiCoreApiServiceOverviewTotals | Unset
        if isinstance(_previous, Unset):
            previous = UNSET
        else:
            previous = SocialApiAiCoreApiServiceOverviewTotals.from_dict(_previous)

        to = d.pop("to", UNSET)

        _top_posts = d.pop("top_posts", UNSET)
        top_posts: list[SocialApiAiCoreApiServiceOverviewTopPost] | Unset = UNSET
        if _top_posts is not UNSET:
            top_posts = []
            for top_posts_item_data in _top_posts:
                top_posts_item = SocialApiAiCoreApiServiceOverviewTopPost.from_dict(top_posts_item_data)

                top_posts.append(top_posts_item)

        _totals = d.pop("totals", UNSET)
        totals: SocialApiAiCoreApiServiceOverviewTotals | Unset
        if isinstance(_totals, Unset):
            totals = UNSET
        else:
            totals = SocialApiAiCoreApiServiceOverviewTotals.from_dict(_totals)

        tz = d.pop("tz", UNSET)

        social_api_ai_core_api_service_analytics_overview = cls(
            accounts_excluded=accounts_excluded,
            activity=activity,
            best_times=best_times,
            by_day=by_day,
            by_format=by_format,
            by_platform=by_platform,
            from_=from_,
            metrics_synced_at=metrics_synced_at,
            previous=previous,
            to=to,
            top_posts=top_posts,
            totals=totals,
            tz=tz,
        )

        social_api_ai_core_api_service_analytics_overview.additional_properties = d
        return social_api_ai_core_api_service_analytics_overview

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
