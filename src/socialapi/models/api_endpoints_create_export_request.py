from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiEndpointsCreateExportRequest")


@_attrs_define
class ApiEndpointsCreateExportRequest:
    """
    Attributes:
        include_transcript (bool | Unset):  Example: True.
        include_vision (bool | Unset):  Example: False.
    """

    include_transcript: bool | Unset = UNSET
    include_vision: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        include_transcript = self.include_transcript

        include_vision = self.include_vision

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if include_transcript is not UNSET:
            field_dict["include_transcript"] = include_transcript
        if include_vision is not UNSET:
            field_dict["include_vision"] = include_vision

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        include_transcript = d.pop("include_transcript", UNSET)

        include_vision = d.pop("include_vision", UNSET)

        api_endpoints_create_export_request = cls(
            include_transcript=include_transcript,
            include_vision=include_vision,
        )

        api_endpoints_create_export_request.additional_properties = d
        return api_endpoints_create_export_request

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
