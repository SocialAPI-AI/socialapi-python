from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.api_endpoints_whats_app_template_info_category import ApiEndpointsWhatsAppTemplateInfoCategory
from ..models.api_endpoints_whats_app_template_info_status import ApiEndpointsWhatsAppTemplateInfoStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiEndpointsWhatsAppTemplateInfo")


@_attrs_define
class ApiEndpointsWhatsAppTemplateInfo:
    """
    Attributes:
        category (ApiEndpointsWhatsAppTemplateInfoCategory | Unset):  Example: UTILITY.
        components (Any | Unset): Components is the raw WhatsApp template component definition.
        id (str | Unset):  Example: 1234567890123456.
        language (str | Unset):  Example: en_US.
        name (str | Unset):  Example: order_confirmation.
        status (ApiEndpointsWhatsAppTemplateInfoStatus | Unset):  Example: APPROVED.
    """

    category: ApiEndpointsWhatsAppTemplateInfoCategory | Unset = UNSET
    components: Any | Unset = UNSET
    id: str | Unset = UNSET
    language: str | Unset = UNSET
    name: str | Unset = UNSET
    status: ApiEndpointsWhatsAppTemplateInfoStatus | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        category: str | Unset = UNSET
        if not isinstance(self.category, Unset):
            category = self.category.value

        components = self.components

        id = self.id

        language = self.language

        name = self.name

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if category is not UNSET:
            field_dict["category"] = category
        if components is not UNSET:
            field_dict["components"] = components
        if id is not UNSET:
            field_dict["id"] = id
        if language is not UNSET:
            field_dict["language"] = language
        if name is not UNSET:
            field_dict["name"] = name
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _category = d.pop("category", UNSET)
        category: ApiEndpointsWhatsAppTemplateInfoCategory | Unset
        if isinstance(_category, Unset):
            category = UNSET
        else:
            category = ApiEndpointsWhatsAppTemplateInfoCategory(_category)

        components = d.pop("components", UNSET)

        id = d.pop("id", UNSET)

        language = d.pop("language", UNSET)

        name = d.pop("name", UNSET)

        _status = d.pop("status", UNSET)
        status: ApiEndpointsWhatsAppTemplateInfoStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ApiEndpointsWhatsAppTemplateInfoStatus(_status)

        api_endpoints_whats_app_template_info = cls(
            category=category,
            components=components,
            id=id,
            language=language,
            name=name,
            status=status,
        )

        api_endpoints_whats_app_template_info.additional_properties = d
        return api_endpoints_whats_app_template_info

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
