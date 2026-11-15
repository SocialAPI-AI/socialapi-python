from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.social_api_ai_core_api_connectors_base_gbp_search_keyword import (
        SocialApiAiCoreApiConnectorsBaseGBPSearchKeyword,
    )


T = TypeVar("T", bound="SocialApiAiCoreApiConnectorsBaseGBPKeywordsPage")


@_attrs_define
class SocialApiAiCoreApiConnectorsBaseGBPKeywordsPage:
    """
    Attributes:
        keywords (list[SocialApiAiCoreApiConnectorsBaseGBPSearchKeyword] | Unset):
        next_cursor (str | Unset):
    """

    keywords: list[SocialApiAiCoreApiConnectorsBaseGBPSearchKeyword] | Unset = UNSET
    next_cursor: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        keywords: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.keywords, Unset):
            keywords = []
            for keywords_item_data in self.keywords:
                keywords_item = keywords_item_data.to_dict()
                keywords.append(keywords_item)

        next_cursor = self.next_cursor

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if keywords is not UNSET:
            field_dict["keywords"] = keywords
        if next_cursor is not UNSET:
            field_dict["next_cursor"] = next_cursor

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.social_api_ai_core_api_connectors_base_gbp_search_keyword import (
            SocialApiAiCoreApiConnectorsBaseGBPSearchKeyword,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _keywords = d.pop("keywords", UNSET)
        keywords: list[SocialApiAiCoreApiConnectorsBaseGBPSearchKeyword] | Unset = UNSET
        if _keywords is not UNSET:
            keywords = []
            for keywords_item_data in _keywords:
                keywords_item = SocialApiAiCoreApiConnectorsBaseGBPSearchKeyword.from_dict(keywords_item_data)

                keywords.append(keywords_item)

        next_cursor = d.pop("next_cursor", UNSET)

        social_api_ai_core_api_connectors_base_gbp_keywords_page = cls(
            keywords=keywords,
            next_cursor=next_cursor,
        )

        social_api_ai_core_api_connectors_base_gbp_keywords_page.additional_properties = d
        return social_api_ai_core_api_connectors_base_gbp_keywords_page

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
