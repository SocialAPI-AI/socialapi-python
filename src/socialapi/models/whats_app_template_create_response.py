from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="WhatsAppTemplateCreateResponse")


@_attrs_define
class WhatsAppTemplateCreateResponse:
    """
    Attributes:
        category (str): Category WhatsApp gave the template, for example AUTHENTICATION, MARKETING or UTILITY. Other
            values can appear. Example: UTILITY.
        id (str):  Example: 1234567890123456.
        status (str): Review status of the new template, for example APPROVED, PENDING or REJECTED. Other values can
            appear. Example: PENDING.
    """

    category: str
    id: str
    status: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        category = self.category

        id = self.id

        status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "category": category,
                "id": id,
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        category = d.pop("category")

        id = d.pop("id")

        status = d.pop("status")

        whats_app_template_create_response = cls(
            category=category,
            id=id,
            status=status,
        )

        whats_app_template_create_response.additional_properties = d
        return whats_app_template_create_response

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
