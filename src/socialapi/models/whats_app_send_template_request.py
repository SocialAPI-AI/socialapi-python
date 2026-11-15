from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.whats_app_template_component import WhatsAppTemplateComponent


T = TypeVar("T", bound="WhatsAppSendTemplateRequest")


@_attrs_define
class WhatsAppSendTemplateRequest:
    """
    Attributes:
        language (str): Language is the BCP-47 code matching the template's approved language (e.g. en_US, fr_FR).
            Example: en_US.
        template_name (str): TemplateName is the approved template name to send. Example: order_confirmation.
        to (str): To is the recipient phone number in E.164 format without the leading "+". Example: 15551234567.
        components (list[WhatsAppTemplateComponent] | Unset): Components carries header/body/button variable
            substitutions.
            Each component matches WhatsApp's template component schema (type + parameters).
    """

    language: str
    template_name: str
    to: str
    components: list[WhatsAppTemplateComponent] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        language = self.language

        template_name = self.template_name

        to = self.to

        components: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.components, Unset):
            components = []
            for components_item_data in self.components:
                components_item = components_item_data.to_dict()
                components.append(components_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "language": language,
                "template_name": template_name,
                "to": to,
            }
        )
        if components is not UNSET:
            field_dict["components"] = components

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.whats_app_template_component import WhatsAppTemplateComponent  # noqa: PLC0415

        d = dict(src_dict)
        language = d.pop("language")

        template_name = d.pop("template_name")

        to = d.pop("to")

        _components = d.pop("components", UNSET)
        components: list[WhatsAppTemplateComponent] | Unset = UNSET
        if _components is not UNSET:
            components = []
            for components_item_data in _components:
                components_item = WhatsAppTemplateComponent.from_dict(components_item_data)

                components.append(components_item)

        whats_app_send_template_request = cls(
            language=language,
            template_name=template_name,
            to=to,
            components=components,
        )

        whats_app_send_template_request.additional_properties = d
        return whats_app_send_template_request

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
