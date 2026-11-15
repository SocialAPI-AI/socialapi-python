from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.api_endpoints_whats_app_create_template_request_category import (
    ApiEndpointsWhatsAppCreateTemplateRequestCategory,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_endpoints_whats_app_template_component_def import ApiEndpointsWhatsAppTemplateComponentDef


T = TypeVar("T", bound="ApiEndpointsWhatsAppCreateTemplateRequest")


@_attrs_define
class ApiEndpointsWhatsAppCreateTemplateRequest:
    """
    Attributes:
        category (ApiEndpointsWhatsAppCreateTemplateRequestCategory | Unset): Category is the message category.
            Marketing intent in a UTILITY template triggers automatic rejection. Example: UTILITY.
        components (list[ApiEndpointsWhatsAppTemplateComponentDef] | Unset): Components define the template body,
            optional header, optional footer, and optional buttons.
            At minimum one BODY component is required.
        language (str | Unset): Language is the BCP-47 language code (e.g. en_US, fr_FR, pt_BR). Example: en_US.
        name (str | Unset): Name is the template identifier. Lowercase letters, digits, underscores only; no spaces.
            Example: order_confirmation.
    """

    category: ApiEndpointsWhatsAppCreateTemplateRequestCategory | Unset = UNSET
    components: list[ApiEndpointsWhatsAppTemplateComponentDef] | Unset = UNSET
    language: str | Unset = UNSET
    name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        category: str | Unset = UNSET
        if not isinstance(self.category, Unset):
            category = self.category.value

        components: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.components, Unset):
            components = []
            for components_item_data in self.components:
                components_item = components_item_data.to_dict()
                components.append(components_item)

        language = self.language

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if category is not UNSET:
            field_dict["category"] = category
        if components is not UNSET:
            field_dict["components"] = components
        if language is not UNSET:
            field_dict["language"] = language
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_endpoints_whats_app_template_component_def import (
            ApiEndpointsWhatsAppTemplateComponentDef,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _category = d.pop("category", UNSET)
        category: ApiEndpointsWhatsAppCreateTemplateRequestCategory | Unset
        if isinstance(_category, Unset):
            category = UNSET
        else:
            category = ApiEndpointsWhatsAppCreateTemplateRequestCategory(_category)

        _components = d.pop("components", UNSET)
        components: list[ApiEndpointsWhatsAppTemplateComponentDef] | Unset = UNSET
        if _components is not UNSET:
            components = []
            for components_item_data in _components:
                components_item = ApiEndpointsWhatsAppTemplateComponentDef.from_dict(components_item_data)

                components.append(components_item)

        language = d.pop("language", UNSET)

        name = d.pop("name", UNSET)

        api_endpoints_whats_app_create_template_request = cls(
            category=category,
            components=components,
            language=language,
            name=name,
        )

        api_endpoints_whats_app_create_template_request.additional_properties = d
        return api_endpoints_whats_app_create_template_request

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
