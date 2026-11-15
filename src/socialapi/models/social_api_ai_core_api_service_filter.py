from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.social_api_ai_core_api_service_filter_type import SocialApiAiCoreApiServiceFilterType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.social_api_ai_core_api_service_keyword_filter import SocialApiAiCoreApiServiceKeywordFilter


T = TypeVar("T", bound="SocialApiAiCoreApiServiceFilter")


@_attrs_define
class SocialApiAiCoreApiServiceFilter:
    """
    Attributes:
        keyword (SocialApiAiCoreApiServiceKeywordFilter | Unset):
        type_ (SocialApiAiCoreApiServiceFilterType | Unset): follows_account is available on Instagram only and not on
            the start step Example: keyword.
    """

    keyword: SocialApiAiCoreApiServiceKeywordFilter | Unset = UNSET
    type_: SocialApiAiCoreApiServiceFilterType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        keyword: dict[str, Any] | Unset = UNSET
        if not isinstance(self.keyword, Unset):
            keyword = self.keyword.to_dict()

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if keyword is not UNSET:
            field_dict["keyword"] = keyword
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.social_api_ai_core_api_service_keyword_filter import (
            SocialApiAiCoreApiServiceKeywordFilter,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _keyword = d.pop("keyword", UNSET)
        keyword: SocialApiAiCoreApiServiceKeywordFilter | Unset
        if isinstance(_keyword, Unset):
            keyword = UNSET
        else:
            keyword = SocialApiAiCoreApiServiceKeywordFilter.from_dict(_keyword)

        _type_ = d.pop("type", UNSET)
        type_: SocialApiAiCoreApiServiceFilterType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = SocialApiAiCoreApiServiceFilterType(_type_)

        social_api_ai_core_api_service_filter = cls(
            keyword=keyword,
            type_=type_,
        )

        social_api_ai_core_api_service_filter.additional_properties = d
        return social_api_ai_core_api_service_filter

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
