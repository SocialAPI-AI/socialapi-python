from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SocialApiAiCoreApiConnectorsBaseGBPSearchKeyword")


@_attrs_define
class SocialApiAiCoreApiConnectorsBaseGBPSearchKeyword:
    """
    Attributes:
        is_threshold (bool | Unset):
        keyword (str | Unset):
        threshold (int | Unset):
        value (int | Unset):
    """

    is_threshold: bool | Unset = UNSET
    keyword: str | Unset = UNSET
    threshold: int | Unset = UNSET
    value: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_threshold = self.is_threshold

        keyword = self.keyword

        threshold = self.threshold

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_threshold is not UNSET:
            field_dict["is_threshold"] = is_threshold
        if keyword is not UNSET:
            field_dict["keyword"] = keyword
        if threshold is not UNSET:
            field_dict["threshold"] = threshold
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_threshold = d.pop("is_threshold", UNSET)

        keyword = d.pop("keyword", UNSET)

        threshold = d.pop("threshold", UNSET)

        value = d.pop("value", UNSET)

        social_api_ai_core_api_connectors_base_gbp_search_keyword = cls(
            is_threshold=is_threshold,
            keyword=keyword,
            threshold=threshold,
            value=value,
        )

        social_api_ai_core_api_connectors_base_gbp_search_keyword.additional_properties = d
        return social_api_ai_core_api_connectors_base_gbp_search_keyword

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
