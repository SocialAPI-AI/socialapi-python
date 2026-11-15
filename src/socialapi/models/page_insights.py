from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.page_insights_kind import PageInsightsKind

if TYPE_CHECKING:
    from ..models.post_insight import PostInsight


T = TypeVar("T", bound="PageInsights")


@_attrs_define
class PageInsights:
    """
    Attributes:
        follower_count (int):
        kind (PageInsightsKind):
        posts (list[PostInsight] | None):
    """

    follower_count: int
    kind: PageInsightsKind
    posts: list[PostInsight] | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        follower_count = self.follower_count

        kind = self.kind.value

        posts: list[dict[str, Any]] | None
        if isinstance(self.posts, list):
            posts = []
            for posts_type_0_item_data in self.posts:
                posts_type_0_item = posts_type_0_item_data.to_dict()
                posts.append(posts_type_0_item)

        else:
            posts = self.posts

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "follower_count": follower_count,
                "kind": kind,
                "posts": posts,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_insight import PostInsight  # noqa: PLC0415

        d = dict(src_dict)
        follower_count = d.pop("follower_count")

        kind = PageInsightsKind(d.pop("kind"))

        def _parse_posts(data: object) -> list[PostInsight] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                posts_type_0 = []
                _posts_type_0 = data
                for posts_type_0_item_data in _posts_type_0:
                    posts_type_0_item = PostInsight.from_dict(posts_type_0_item_data)

                    posts_type_0.append(posts_type_0_item)

                return posts_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[PostInsight] | None, data)

        posts = _parse_posts(d.pop("posts"))

        page_insights = cls(
            follower_count=follower_count,
            kind=kind,
            posts=posts,
        )

        page_insights.additional_properties = d
        return page_insights

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
