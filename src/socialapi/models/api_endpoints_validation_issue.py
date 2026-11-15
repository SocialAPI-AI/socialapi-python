from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiEndpointsValidationIssue")


@_attrs_define
class ApiEndpointsValidationIssue:
    """
    Attributes:
        field (str | Unset):  Example: text.
        message (str | Unset):  Example: exceeds 2200 character limit (2350/2200).
        platform (str | Unset):  Example: instagram.
        segment_index (int | Unset): SegmentIndex pins the issue to a continuation segment (0-based); nil for the main
            post. Example: 0.
        target (str | Unset):  Example: acc_01HZ9X3Q4R5M6N7P8V2K0W1J.
    """

    field: str | Unset = UNSET
    message: str | Unset = UNSET
    platform: str | Unset = UNSET
    segment_index: int | Unset = UNSET
    target: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field = self.field

        message = self.message

        platform = self.platform

        segment_index = self.segment_index

        target = self.target

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field is not UNSET:
            field_dict["field"] = field
        if message is not UNSET:
            field_dict["message"] = message
        if platform is not UNSET:
            field_dict["platform"] = platform
        if segment_index is not UNSET:
            field_dict["segment_index"] = segment_index
        if target is not UNSET:
            field_dict["target"] = target

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        field = d.pop("field", UNSET)

        message = d.pop("message", UNSET)

        platform = d.pop("platform", UNSET)

        segment_index = d.pop("segment_index", UNSET)

        target = d.pop("target", UNSET)

        api_endpoints_validation_issue = cls(
            field=field,
            message=message,
            platform=platform,
            segment_index=segment_index,
            target=target,
        )

        api_endpoints_validation_issue.additional_properties = d
        return api_endpoints_validation_issue

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
