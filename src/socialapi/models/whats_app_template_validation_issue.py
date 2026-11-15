from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WhatsAppTemplateValidationIssue")


@_attrs_define
class WhatsAppTemplateValidationIssue:
    """
    Attributes:
        field (str): Field is the offending request field (e.g. "name", "components.format",
            "components.buttons[0].url"). Example: name.
        message (str): Message is a developer-facing description of the problem. Example: name must contain only
            lowercase letters, digits, and underscores (no spaces or capitals).
        component_index (int | Unset): ComponentIndex pins the issue to a components[] entry (0-based); nil for
            top-level fields such as name, category, or language. Example: 0.
    """

    field: str
    message: str
    component_index: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field = self.field

        message = self.message

        component_index = self.component_index

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "field": field,
                "message": message,
            }
        )
        if component_index is not UNSET:
            field_dict["component_index"] = component_index

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        field = d.pop("field")

        message = d.pop("message")

        component_index = d.pop("component_index", UNSET)

        whats_app_template_validation_issue = cls(
            field=field,
            message=message,
            component_index=component_index,
        )

        whats_app_template_validation_issue.additional_properties = d
        return whats_app_template_validation_issue

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
