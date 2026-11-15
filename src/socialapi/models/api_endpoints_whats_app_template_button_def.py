from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.api_endpoints_whats_app_template_button_def_type import ApiEndpointsWhatsAppTemplateButtonDefType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_endpoints_whats_app_template_button_def_example import (
        ApiEndpointsWhatsAppTemplateButtonDefExample,
    )


T = TypeVar("T", bound="ApiEndpointsWhatsAppTemplateButtonDef")


@_attrs_define
class ApiEndpointsWhatsAppTemplateButtonDef:
    """
    Attributes:
        example (ApiEndpointsWhatsAppTemplateButtonDefExample | Unset): Example carries the button's sample value(s),
            forwarded verbatim: a dynamic
            URL example (["https://..."]) or a COPY_CODE sample ("250FF").
        phone_number (str | Unset): PhoneNumber is required when Type is PHONE_NUMBER. E.164 format with leading "+".
            Example: +15551234567.
        text (str | Unset): Text is the button label. Not required for COPY_CODE (WhatsApp auto-labels it). Example:
            Visit.
        type_ (ApiEndpointsWhatsAppTemplateButtonDefType | Unset): Type is the button kind. Example: URL.
        url (str | Unset): URL is required when Type is URL. May contain a single {{1}} placeholder. Example:
            https://example.com/{{1}}.
    """

    example: ApiEndpointsWhatsAppTemplateButtonDefExample | Unset = UNSET
    phone_number: str | Unset = UNSET
    text: str | Unset = UNSET
    type_: ApiEndpointsWhatsAppTemplateButtonDefType | Unset = UNSET
    url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        example: dict[str, Any] | Unset = UNSET
        if not isinstance(self.example, Unset):
            example = self.example.to_dict()

        phone_number = self.phone_number

        text = self.text

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if example is not UNSET:
            field_dict["example"] = example
        if phone_number is not UNSET:
            field_dict["phone_number"] = phone_number
        if text is not UNSET:
            field_dict["text"] = text
        if type_ is not UNSET:
            field_dict["type"] = type_
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_endpoints_whats_app_template_button_def_example import (
            ApiEndpointsWhatsAppTemplateButtonDefExample,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _example = d.pop("example", UNSET)
        example: ApiEndpointsWhatsAppTemplateButtonDefExample | Unset
        if isinstance(_example, Unset):
            example = UNSET
        else:
            example = ApiEndpointsWhatsAppTemplateButtonDefExample.from_dict(_example)

        phone_number = d.pop("phone_number", UNSET)

        text = d.pop("text", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: ApiEndpointsWhatsAppTemplateButtonDefType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = ApiEndpointsWhatsAppTemplateButtonDefType(_type_)

        url = d.pop("url", UNSET)

        api_endpoints_whats_app_template_button_def = cls(
            example=example,
            phone_number=phone_number,
            text=text,
            type_=type_,
            url=url,
        )

        api_endpoints_whats_app_template_button_def.additional_properties = d
        return api_endpoints_whats_app_template_button_def

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
