from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SocialApiAiCoreApiConnectorsBaseThreadsBreakdownResult")


@_attrs_define
class SocialApiAiCoreApiConnectorsBaseThreadsBreakdownResult:
    """
    Attributes:
        dimension (str | Unset): Dimension is the breakdown value, such as a country code, a city, an age range or a
            gender.
        value (int | Unset):
    """

    dimension: str | Unset = UNSET
    value: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dimension = self.dimension

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dimension is not UNSET:
            field_dict["dimension"] = dimension
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        dimension = d.pop("dimension", UNSET)

        value = d.pop("value", UNSET)

        social_api_ai_core_api_connectors_base_threads_breakdown_result = cls(
            dimension=dimension,
            value=value,
        )

        social_api_ai_core_api_connectors_base_threads_breakdown_result.additional_properties = d
        return social_api_ai_core_api_connectors_base_threads_breakdown_result

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
