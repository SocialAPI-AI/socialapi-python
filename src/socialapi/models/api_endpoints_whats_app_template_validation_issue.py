from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiEndpointsWhatsAppTemplateValidationIssue")


@_attrs_define
class ApiEndpointsWhatsAppTemplateValidationIssue:
    """
    Attributes:
        component_index (int | Unset): ComponentIndex pins the issue to a components[] entry (0-based); nil for
            top-level fields such as name, category, or language. Example: 0.
        field (str | Unset): Field is the offending request field (e.g. "name", "components.format",
            "components.buttons[0].url"). Example: name.
        message (str | Unset): Message is a developer-facing description of the problem. Example: name must contain only
            lowercase letters, digits, and underscores (no spaces or capitals).
    """

    component_index: int | Unset = UNSET
    field: str | Unset = UNSET
    message: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        component_index = self.component_index

        field = self.field

        message = self.message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if component_index is not UNSET:
            field_dict["component_index"] = component_index
        if field is not UNSET:
            field_dict["field"] = field
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        component_index = d.pop("component_index", UNSET)

        field = d.pop("field", UNSET)

        message = d.pop("message", UNSET)

        api_endpoints_whats_app_template_validation_issue = cls(
            component_index=component_index,
            field=field,
            message=message,
        )

        api_endpoints_whats_app_template_validation_issue.additional_properties = d
        return api_endpoints_whats_app_template_validation_issue

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
