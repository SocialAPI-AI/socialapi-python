from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.gbp_search_keyword import GBPSearchKeyword


T = TypeVar("T", bound="GBPKeywordsPage")


@_attrs_define
class GBPKeywordsPage:
    """
    Attributes:
        keywords (list[GBPSearchKeyword] | None):
        next_cursor (str | Unset):
    """

    keywords: list[GBPSearchKeyword] | None
    next_cursor: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        keywords: list[dict[str, Any]] | None
        if isinstance(self.keywords, list):
            keywords = []
            for keywords_type_0_item_data in self.keywords:
                keywords_type_0_item = keywords_type_0_item_data.to_dict()
                keywords.append(keywords_type_0_item)

        else:
            keywords = self.keywords

        next_cursor = self.next_cursor

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "keywords": keywords,
            }
        )
        if next_cursor is not UNSET:
            field_dict["next_cursor"] = next_cursor

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.gbp_search_keyword import GBPSearchKeyword  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_keywords(data: object) -> list[GBPSearchKeyword] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                keywords_type_0 = []
                _keywords_type_0 = data
                for keywords_type_0_item_data in _keywords_type_0:
                    keywords_type_0_item = GBPSearchKeyword.from_dict(keywords_type_0_item_data)

                    keywords_type_0.append(keywords_type_0_item)

                return keywords_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[GBPSearchKeyword] | None, data)

        keywords = _parse_keywords(d.pop("keywords"))

        next_cursor = d.pop("next_cursor", UNSET)

        gbp_keywords_page = cls(
            keywords=keywords,
            next_cursor=next_cursor,
        )

        gbp_keywords_page.additional_properties = d
        return gbp_keywords_page

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
