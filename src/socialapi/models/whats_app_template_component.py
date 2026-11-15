from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.whats_app_send_component_type import WhatsAppSendComponentType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.whats_app_template_parameter import WhatsAppTemplateParameter


T = TypeVar("T", bound="WhatsAppTemplateComponent")


@_attrs_define
class WhatsAppTemplateComponent:
    """
    Attributes:
        type_ (WhatsAppSendComponentType):
        parameters (list[WhatsAppTemplateParameter] | Unset): Parameters lists variable substitutions for this
            component.
    """

    type_: WhatsAppSendComponentType
    parameters: list[WhatsAppTemplateParameter] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        parameters: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.parameters, Unset):
            parameters = []
            for parameters_item_data in self.parameters:
                parameters_item = parameters_item_data.to_dict()
                parameters.append(parameters_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if parameters is not UNSET:
            field_dict["parameters"] = parameters

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.whats_app_template_parameter import WhatsAppTemplateParameter  # noqa: PLC0415

        d = dict(src_dict)
        type_ = WhatsAppSendComponentType(d.pop("type"))

        _parameters = d.pop("parameters", UNSET)
        parameters: list[WhatsAppTemplateParameter] | Unset = UNSET
        if _parameters is not UNSET:
            parameters = []
            for parameters_item_data in _parameters:
                parameters_item = WhatsAppTemplateParameter.from_dict(parameters_item_data)

                parameters.append(parameters_item)

        whats_app_template_component = cls(
            type_=type_,
            parameters=parameters,
        )

        whats_app_template_component.additional_properties = d
        return whats_app_template_component

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
