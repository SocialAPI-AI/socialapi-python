from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.api_endpoints_whats_app_template_component_type import ApiEndpointsWhatsAppTemplateComponentType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_endpoints_whats_app_template_parameter import ApiEndpointsWhatsAppTemplateParameter


T = TypeVar("T", bound="ApiEndpointsWhatsAppTemplateComponent")


@_attrs_define
class ApiEndpointsWhatsAppTemplateComponent:
    """
    Attributes:
        parameters (list[ApiEndpointsWhatsAppTemplateParameter] | Unset): Parameters lists variable substitutions for
            this component.
        type_ (ApiEndpointsWhatsAppTemplateComponentType | Unset): Type is the component slot: header, body, or button.
            Example: body.
    """

    parameters: list[ApiEndpointsWhatsAppTemplateParameter] | Unset = UNSET
    type_: ApiEndpointsWhatsAppTemplateComponentType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        parameters: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.parameters, Unset):
            parameters = []
            for parameters_item_data in self.parameters:
                parameters_item = parameters_item_data.to_dict()
                parameters.append(parameters_item)

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if parameters is not UNSET:
            field_dict["parameters"] = parameters
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_endpoints_whats_app_template_parameter import (
            ApiEndpointsWhatsAppTemplateParameter,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _parameters = d.pop("parameters", UNSET)
        parameters: list[ApiEndpointsWhatsAppTemplateParameter] | Unset = UNSET
        if _parameters is not UNSET:
            parameters = []
            for parameters_item_data in _parameters:
                parameters_item = ApiEndpointsWhatsAppTemplateParameter.from_dict(parameters_item_data)

                parameters.append(parameters_item)

        _type_ = d.pop("type", UNSET)
        type_: ApiEndpointsWhatsAppTemplateComponentType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = ApiEndpointsWhatsAppTemplateComponentType(_type_)

        api_endpoints_whats_app_template_component = cls(
            parameters=parameters,
            type_=type_,
        )

        api_endpoints_whats_app_template_component.additional_properties = d
        return api_endpoints_whats_app_template_component

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
