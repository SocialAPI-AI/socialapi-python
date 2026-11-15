from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WhatsAppTemplateInfo")


@_attrs_define
class WhatsAppTemplateInfo:
    """
    Attributes:
        category (str): Template category, for example AUTHENTICATION, MARKETING or UTILITY. Other values can appear.
            Example: UTILITY.
        id (str):  Example: 1234567890123456.
        language (str):  Example: en_US.
        name (str):  Example: order_confirmation.
        status (str): Review status of the template, for example APPROVED, PENDING, REJECTED, PAUSED or DISABLED. Other
            values can appear. Example: APPROVED.
        components (Any | Unset): Components is the raw WhatsApp template component definition.
    """

    category: str
    id: str
    language: str
    name: str
    status: str
    components: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        category = self.category

        id = self.id

        language = self.language

        name = self.name

        status = self.status

        components = self.components

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "category": category,
                "id": id,
                "language": language,
                "name": name,
                "status": status,
            }
        )
        if components is not UNSET:
            field_dict["components"] = components

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        category = d.pop("category")

        id = d.pop("id")

        language = d.pop("language")

        name = d.pop("name")

        status = d.pop("status")

        components = d.pop("components", UNSET)

        whats_app_template_info = cls(
            category=category,
            id=id,
            language=language,
            name=name,
            status=status,
            components=components,
        )

        whats_app_template_info.additional_properties = d
        return whats_app_template_info

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
