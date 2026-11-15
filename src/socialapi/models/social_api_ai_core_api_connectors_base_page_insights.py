from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.social_api_ai_core_api_connectors_base_page_insights_kind import (
    SocialApiAiCoreApiConnectorsBasePageInsightsKind,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.social_api_ai_core_api_connectors_base_post_insight import SocialApiAiCoreApiConnectorsBasePostInsight


T = TypeVar("T", bound="SocialApiAiCoreApiConnectorsBasePageInsights")


@_attrs_define
class SocialApiAiCoreApiConnectorsBasePageInsights:
    """
    Attributes:
        follower_count (int | Unset):
        kind (SocialApiAiCoreApiConnectorsBasePageInsightsKind | Unset): Kind is "organization" for a LinkedIn Page and
            "member" for a personal profile. Example: organization.
        posts (list[SocialApiAiCoreApiConnectorsBasePostInsight] | Unset):
    """

    follower_count: int | Unset = UNSET
    kind: SocialApiAiCoreApiConnectorsBasePageInsightsKind | Unset = UNSET
    posts: list[SocialApiAiCoreApiConnectorsBasePostInsight] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        follower_count = self.follower_count

        kind: str | Unset = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind.value

        posts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.posts, Unset):
            posts = []
            for posts_item_data in self.posts:
                posts_item = posts_item_data.to_dict()
                posts.append(posts_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if follower_count is not UNSET:
            field_dict["follower_count"] = follower_count
        if kind is not UNSET:
            field_dict["kind"] = kind
        if posts is not UNSET:
            field_dict["posts"] = posts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.social_api_ai_core_api_connectors_base_post_insight import (
            SocialApiAiCoreApiConnectorsBasePostInsight,  # noqa: PLC0415
        )

        d = dict(src_dict)
        follower_count = d.pop("follower_count", UNSET)

        _kind = d.pop("kind", UNSET)
        kind: SocialApiAiCoreApiConnectorsBasePageInsightsKind | Unset
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = SocialApiAiCoreApiConnectorsBasePageInsightsKind(_kind)

        _posts = d.pop("posts", UNSET)
        posts: list[SocialApiAiCoreApiConnectorsBasePostInsight] | Unset = UNSET
        if _posts is not UNSET:
            posts = []
            for posts_item_data in _posts:
                posts_item = SocialApiAiCoreApiConnectorsBasePostInsight.from_dict(posts_item_data)

                posts.append(posts_item)

        social_api_ai_core_api_connectors_base_page_insights = cls(
            follower_count=follower_count,
            kind=kind,
            posts=posts,
        )

        social_api_ai_core_api_connectors_base_page_insights.additional_properties = d
        return social_api_ai_core_api_connectors_base_page_insights

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
