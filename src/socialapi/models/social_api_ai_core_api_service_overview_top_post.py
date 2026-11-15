from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.social_api_ai_core_api_service_overview_post_metrics import (
        SocialApiAiCoreApiServiceOverviewPostMetrics,
    )


T = TypeVar("T", bound="SocialApiAiCoreApiServiceOverviewTopPost")


@_attrs_define
class SocialApiAiCoreApiServiceOverviewTopPost:
    """
    Attributes:
        account_id (str | Unset):  Example: acc_01HZ9X3Q4R5M6N7P8V2K0W1J.
        media_type (str | Unset):  Example: reel.
        metrics (SocialApiAiCoreApiServiceOverviewPostMetrics | Unset):
        permalink (str | Unset):  Example: https://www.instagram.com/p/C1a2b3c4d5/.
        platform (str | Unset):  Example: instagram.
        post_id (str | Unset):  Example: 7c9e6679-7425-40de-944b-e07fc1f90ae7.
        published_at (str | Unset):  Example: 2026-10-14T09:30:00Z.
        text (str | Unset):  Example: Our autumn menu is here.
        thumbnail (str | Unset):  Example: https://scontent.cdninstagram.com/v/t51.29350-15/456_n.jpg.
    """

    account_id: str | Unset = UNSET
    media_type: str | Unset = UNSET
    metrics: SocialApiAiCoreApiServiceOverviewPostMetrics | Unset = UNSET
    permalink: str | Unset = UNSET
    platform: str | Unset = UNSET
    post_id: str | Unset = UNSET
    published_at: str | Unset = UNSET
    text: str | Unset = UNSET
    thumbnail: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_id = self.account_id

        media_type = self.media_type

        metrics: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metrics, Unset):
            metrics = self.metrics.to_dict()

        permalink = self.permalink

        platform = self.platform

        post_id = self.post_id

        published_at = self.published_at

        text = self.text

        thumbnail = self.thumbnail

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_id is not UNSET:
            field_dict["account_id"] = account_id
        if media_type is not UNSET:
            field_dict["media_type"] = media_type
        if metrics is not UNSET:
            field_dict["metrics"] = metrics
        if permalink is not UNSET:
            field_dict["permalink"] = permalink
        if platform is not UNSET:
            field_dict["platform"] = platform
        if post_id is not UNSET:
            field_dict["post_id"] = post_id
        if published_at is not UNSET:
            field_dict["published_at"] = published_at
        if text is not UNSET:
            field_dict["text"] = text
        if thumbnail is not UNSET:
            field_dict["thumbnail"] = thumbnail

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.social_api_ai_core_api_service_overview_post_metrics import (
            SocialApiAiCoreApiServiceOverviewPostMetrics,  # noqa: PLC0415
        )

        d = dict(src_dict)
        account_id = d.pop("account_id", UNSET)

        media_type = d.pop("media_type", UNSET)

        _metrics = d.pop("metrics", UNSET)
        metrics: SocialApiAiCoreApiServiceOverviewPostMetrics | Unset
        if isinstance(_metrics, Unset):
            metrics = UNSET
        else:
            metrics = SocialApiAiCoreApiServiceOverviewPostMetrics.from_dict(_metrics)

        permalink = d.pop("permalink", UNSET)

        platform = d.pop("platform", UNSET)

        post_id = d.pop("post_id", UNSET)

        published_at = d.pop("published_at", UNSET)

        text = d.pop("text", UNSET)

        thumbnail = d.pop("thumbnail", UNSET)

        social_api_ai_core_api_service_overview_top_post = cls(
            account_id=account_id,
            media_type=media_type,
            metrics=metrics,
            permalink=permalink,
            platform=platform,
            post_id=post_id,
            published_at=published_at,
            text=text,
            thumbnail=thumbnail,
        )

        social_api_ai_core_api_service_overview_top_post.additional_properties = d
        return social_api_ai_core_api_service_overview_top_post

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
