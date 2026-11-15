from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.overview_post_metrics import OverviewPostMetrics


T = TypeVar("T", bound="OverviewTopPost")


@_attrs_define
class OverviewTopPost:
    """
    Attributes:
        account_id (str):  Example: acc_01HZ9X3Q4R5M6N7P8V2K0W1J.
        media_type (str):  Example: reel.
        metrics (OverviewPostMetrics):
        platform (str):  Example: instagram.
        post_id (str):  Example: 7c9e6679-7425-40de-944b-e07fc1f90ae7.
        published_at (str):  Example: 2026-10-14T09:30:00Z.
        permalink (str | Unset):  Example: https://www.instagram.com/p/C1a2b3c4d5/.
        text (str | Unset):  Example: Our autumn menu is here.
        thumbnail (str | Unset):  Example: https://scontent.cdninstagram.com/v/t51.29350-15/456_n.jpg.
    """

    account_id: str
    media_type: str
    metrics: OverviewPostMetrics
    platform: str
    post_id: str
    published_at: str
    permalink: str | Unset = UNSET
    text: str | Unset = UNSET
    thumbnail: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_id = self.account_id

        media_type = self.media_type

        metrics = self.metrics.to_dict()

        platform = self.platform

        post_id = self.post_id

        published_at = self.published_at

        permalink = self.permalink

        text = self.text

        thumbnail = self.thumbnail

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "account_id": account_id,
                "media_type": media_type,
                "metrics": metrics,
                "platform": platform,
                "post_id": post_id,
                "published_at": published_at,
            }
        )
        if permalink is not UNSET:
            field_dict["permalink"] = permalink
        if text is not UNSET:
            field_dict["text"] = text
        if thumbnail is not UNSET:
            field_dict["thumbnail"] = thumbnail

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.overview_post_metrics import OverviewPostMetrics  # noqa: PLC0415

        d = dict(src_dict)
        account_id = d.pop("account_id")

        media_type = d.pop("media_type")

        metrics = OverviewPostMetrics.from_dict(d.pop("metrics"))

        platform = d.pop("platform")

        post_id = d.pop("post_id")

        published_at = d.pop("published_at")

        permalink = d.pop("permalink", UNSET)

        text = d.pop("text", UNSET)

        thumbnail = d.pop("thumbnail", UNSET)

        overview_top_post = cls(
            account_id=account_id,
            media_type=media_type,
            metrics=metrics,
            platform=platform,
            post_id=post_id,
            published_at=published_at,
            permalink=permalink,
            text=text,
            thumbnail=thumbnail,
        )

        overview_top_post.additional_properties = d
        return overview_top_post

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
