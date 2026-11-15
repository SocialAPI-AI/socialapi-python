from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.whats_app_template_component_type import WhatsAppTemplateComponentType
from ..models.whats_app_template_format import WhatsAppTemplateFormat
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.whats_app_template_button_def import WhatsAppTemplateButtonDef
    from ..models.whats_app_template_component_def_example import WhatsAppTemplateComponentDefExample


T = TypeVar("T", bound="WhatsAppTemplateComponentDef")


@_attrs_define
class WhatsAppTemplateComponentDef:
    """
    Attributes:
        type_ (WhatsAppTemplateComponentType):
        buttons (list[WhatsAppTemplateButtonDef] | Unset): Buttons populate a BUTTONS component (one of QUICK_REPLY,
            URL, PHONE_NUMBER, COPY_CODE).
        example (WhatsAppTemplateComponentDefExample | Unset): Example carries WhatsApp's sample values, forwarded
            verbatim. For a TEXT
            BODY/HEADER it is {"body_text":[["v1","v2"]]} / {"header_text":["v1"]}; for
            a media HEADER it is {"header_handle":["<url-or-handle>"]}. Required for
            approval when the component contains variables.
        format_ (WhatsAppTemplateFormat | Unset):
        text (str | Unset): Text is the literal text for HEADER (when Format is TEXT), BODY, or FOOTER components.
            May contain 1-indexed placeholders such as {{1}}, {{2}}. Example: Hello {{1}}, your order {{2}} is confirmed..
    """

    type_: WhatsAppTemplateComponentType
    buttons: list[WhatsAppTemplateButtonDef] | Unset = UNSET
    example: WhatsAppTemplateComponentDefExample | Unset = UNSET
    format_: WhatsAppTemplateFormat | Unset = UNSET
    text: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        buttons: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.buttons, Unset):
            buttons = []
            for buttons_item_data in self.buttons:
                buttons_item = buttons_item_data.to_dict()
                buttons.append(buttons_item)

        example: dict[str, Any] | Unset = UNSET
        if not isinstance(self.example, Unset):
            example = self.example.to_dict()

        format_: str | Unset = UNSET
        if not isinstance(self.format_, Unset):
            format_ = self.format_.value

        text = self.text

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if buttons is not UNSET:
            field_dict["buttons"] = buttons
        if example is not UNSET:
            field_dict["example"] = example
        if format_ is not UNSET:
            field_dict["format"] = format_
        if text is not UNSET:
            field_dict["text"] = text

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.whats_app_template_button_def import WhatsAppTemplateButtonDef  # noqa: PLC0415
        from ..models.whats_app_template_component_def_example import (
            WhatsAppTemplateComponentDefExample,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = WhatsAppTemplateComponentType(d.pop("type"))

        _buttons = d.pop("buttons", UNSET)
        buttons: list[WhatsAppTemplateButtonDef] | Unset = UNSET
        if _buttons is not UNSET:
            buttons = []
            for buttons_item_data in _buttons:
                buttons_item = WhatsAppTemplateButtonDef.from_dict(buttons_item_data)

                buttons.append(buttons_item)

        _example = d.pop("example", UNSET)
        example: WhatsAppTemplateComponentDefExample | Unset
        if isinstance(_example, Unset):
            example = UNSET
        else:
            example = WhatsAppTemplateComponentDefExample.from_dict(_example)

        _format_ = d.pop("format", UNSET)
        format_: WhatsAppTemplateFormat | Unset
        if isinstance(_format_, Unset):
            format_ = UNSET
        else:
            format_ = WhatsAppTemplateFormat(_format_)

        text = d.pop("text", UNSET)

        whats_app_template_component_def = cls(
            type_=type_,
            buttons=buttons,
            example=example,
            format_=format_,
            text=text,
        )

        whats_app_template_component_def.additional_properties = d
        return whats_app_template_component_def

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
