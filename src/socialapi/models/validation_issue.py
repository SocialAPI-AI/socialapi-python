from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ValidationIssue")


@_attrs_define
class ValidationIssue:
    """
    Attributes:
        field (str):  Example: text.
        message (str):  Example: exceeds 2200 character limit (2350/2200).
        platform (str): The platform the issue applies to, such as instagram. Empty when the issue applies to the whole
            post. Example: instagram.
        segment_index (int | Unset): SegmentIndex pins the issue to a continuation segment (0-based); nil for the main
            post. Example: 0.
        target (str | Unset):  Example: acc_01HZ9X3Q4R5M6N7P8V2K0W1J.
    """

    field: str
    message: str
    platform: str
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
        field_dict.update(
            {
                "field": field,
                "message": message,
                "platform": platform,
            }
        )
        if segment_index is not UNSET:
            field_dict["segment_index"] = segment_index
        if target is not UNSET:
            field_dict["target"] = target

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        field = d.pop("field")

        message = d.pop("message")

        platform = d.pop("platform")

        segment_index = d.pop("segment_index", UNSET)

        target = d.pop("target", UNSET)

        validation_issue = cls(
            field=field,
            message=message,
            platform=platform,
            segment_index=segment_index,
            target=target,
        )

        validation_issue.additional_properties = d
        return validation_issue

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
