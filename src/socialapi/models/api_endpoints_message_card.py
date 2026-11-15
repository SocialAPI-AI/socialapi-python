from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_endpoints_message_button import ApiEndpointsMessageButton


T = TypeVar("T", bound="ApiEndpointsMessageCard")


@_attrs_define
class ApiEndpointsMessageCard:
    """
    Attributes:
        buttons (list[ApiEndpointsMessageButton] | Unset):
        image_url (str | Unset):  Example: https://cdn.example.com/p.jpg.
        subtitle (str | Unset):  Example: Short description.
        title (str | Unset):  Example: Product name.
    """

    buttons: list[ApiEndpointsMessageButton] | Unset = UNSET
    image_url: str | Unset = UNSET
    subtitle: str | Unset = UNSET
    title: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        buttons: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.buttons, Unset):
            buttons = []
            for buttons_item_data in self.buttons:
                buttons_item = buttons_item_data.to_dict()
                buttons.append(buttons_item)

        image_url = self.image_url

        subtitle = self.subtitle

        title = self.title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if buttons is not UNSET:
            field_dict["buttons"] = buttons
        if image_url is not UNSET:
            field_dict["image_url"] = image_url
        if subtitle is not UNSET:
            field_dict["subtitle"] = subtitle
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_endpoints_message_button import ApiEndpointsMessageButton  # noqa: PLC0415

        d = dict(src_dict)
        _buttons = d.pop("buttons", UNSET)
        buttons: list[ApiEndpointsMessageButton] | Unset = UNSET
        if _buttons is not UNSET:
            buttons = []
            for buttons_item_data in _buttons:
                buttons_item = ApiEndpointsMessageButton.from_dict(buttons_item_data)

                buttons.append(buttons_item)

        image_url = d.pop("image_url", UNSET)

        subtitle = d.pop("subtitle", UNSET)

        title = d.pop("title", UNSET)

        api_endpoints_message_card = cls(
            buttons=buttons,
            image_url=image_url,
            subtitle=subtitle,
            title=title,
        )

        api_endpoints_message_card.additional_properties = d
        return api_endpoints_message_card

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
