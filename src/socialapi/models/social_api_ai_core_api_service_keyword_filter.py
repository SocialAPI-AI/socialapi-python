from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.social_api_ai_core_api_service_keyword_filter_match import SocialApiAiCoreApiServiceKeywordFilterMatch
from ..types import UNSET, Unset

T = TypeVar("T", bound="SocialApiAiCoreApiServiceKeywordFilter")


@_attrs_define
class SocialApiAiCoreApiServiceKeywordFilter:
    """
    Attributes:
        keywords (list[str] | Unset): 1 to 50, each 1 to 100 characters Example: ['link', 'price'].
        match (SocialApiAiCoreApiServiceKeywordFilterMatch | Unset): contains: a keyword appears as a whole word or
            phrase. exact: the whole text equals a keyword Example: contains.
    """

    keywords: list[str] | Unset = UNSET
    match: SocialApiAiCoreApiServiceKeywordFilterMatch | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        keywords: list[str] | Unset = UNSET
        if not isinstance(self.keywords, Unset):
            keywords = self.keywords

        match: str | Unset = UNSET
        if not isinstance(self.match, Unset):
            match = self.match.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if keywords is not UNSET:
            field_dict["keywords"] = keywords
        if match is not UNSET:
            field_dict["match"] = match

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        keywords = cast(list[str], d.pop("keywords", UNSET))

        _match = d.pop("match", UNSET)
        match: SocialApiAiCoreApiServiceKeywordFilterMatch | Unset
        if isinstance(_match, Unset):
            match = UNSET
        else:
            match = SocialApiAiCoreApiServiceKeywordFilterMatch(_match)

        social_api_ai_core_api_service_keyword_filter = cls(
            keywords=keywords,
            match=match,
        )

        social_api_ai_core_api_service_keyword_filter.additional_properties = d
        return social_api_ai_core_api_service_keyword_filter

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
