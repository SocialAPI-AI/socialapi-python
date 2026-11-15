from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.whats_app_template_component_def import WhatsAppTemplateComponentDef


T = TypeVar("T", bound="WhatsAppEditTemplateRequest")


@_attrs_define
class WhatsAppEditTemplateRequest:
    """
    Attributes:
        components (list[WhatsAppTemplateComponentDef]): Components replaces the template's components.
    """

    components: list[WhatsAppTemplateComponentDef]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        components = []
        for components_item_data in self.components:
            components_item = components_item_data.to_dict()
            components.append(components_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "components": components,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.whats_app_template_component_def import WhatsAppTemplateComponentDef  # noqa: PLC0415

        d = dict(src_dict)
        components = []
        _components = d.pop("components")
        for components_item_data in _components:
            components_item = WhatsAppTemplateComponentDef.from_dict(components_item_data)

            components.append(components_item)

        whats_app_edit_template_request = cls(
            components=components,
        )

        whats_app_edit_template_request.additional_properties = d
        return whats_app_edit_template_request

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
