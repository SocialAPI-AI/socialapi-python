from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.keyword_match import KeywordMatch

T = TypeVar("T", bound="KeywordFilter")


@_attrs_define
class KeywordFilter:
    """
    Attributes:
        keywords (list[str]): 1 to 50, each 1 to 100 characters Example: ['link', 'price'].
        match (KeywordMatch):
    """

    keywords: list[str]
    match: KeywordMatch
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        keywords = self.keywords

        match = self.match.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "keywords": keywords,
                "match": match,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        keywords = cast(list[str], d.pop("keywords"))

        match = KeywordMatch(d.pop("match"))

        keyword_filter = cls(
            keywords=keywords,
            match=match,
        )

        keyword_filter.additional_properties = d
        return keyword_filter

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
