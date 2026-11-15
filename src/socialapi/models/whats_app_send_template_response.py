from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.whats_app_contact import WhatsAppContact
    from ..models.whats_app_message_ref import WhatsAppMessageRef


T = TypeVar("T", bound="WhatsAppSendTemplateResponse")


@_attrs_define
class WhatsAppSendTemplateResponse:
    """
    Attributes:
        contacts (list[WhatsAppContact]): Contacts maps the input phone number to its canonical WhatsApp ID.
        messages (list[WhatsAppMessageRef]): Messages contains one entry per delivered message, with its platform ID.
        messaging_product (str): MessagingProduct is always "whatsapp". Example: whatsapp.
        message_id (str | Unset): MessageID is the SocialAPI message ID for the send, matching the "id"
            field on the dm.status.* webhooks for this message. Empty when WhatsApp
            returned no wamid or no canonical wa_id, since an ID built from half the
            pair would collide across conversations. Example: sapi_dm_TT974YVQH4RAHNN2HY2DJSNY9111D7LMTP1XXPCVQVL.
    """

    contacts: list[WhatsAppContact]
    messages: list[WhatsAppMessageRef]
    messaging_product: str
    message_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        contacts = []
        for contacts_item_data in self.contacts:
            contacts_item = contacts_item_data.to_dict()
            contacts.append(contacts_item)

        messages = []
        for messages_item_data in self.messages:
            messages_item = messages_item_data.to_dict()
            messages.append(messages_item)

        messaging_product = self.messaging_product

        message_id = self.message_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "contacts": contacts,
                "messages": messages,
                "messaging_product": messaging_product,
            }
        )
        if message_id is not UNSET:
            field_dict["message_id"] = message_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.whats_app_contact import WhatsAppContact  # noqa: PLC0415
        from ..models.whats_app_message_ref import WhatsAppMessageRef  # noqa: PLC0415

        d = dict(src_dict)
        contacts = []
        _contacts = d.pop("contacts")
        for contacts_item_data in _contacts:
            contacts_item = WhatsAppContact.from_dict(contacts_item_data)

            contacts.append(contacts_item)

        messages = []
        _messages = d.pop("messages")
        for messages_item_data in _messages:
            messages_item = WhatsAppMessageRef.from_dict(messages_item_data)

            messages.append(messages_item)

        messaging_product = d.pop("messaging_product")

        message_id = d.pop("message_id", UNSET)

        whats_app_send_template_response = cls(
            contacts=contacts,
            messages=messages,
            messaging_product=messaging_product,
            message_id=message_id,
        )

        whats_app_send_template_response.additional_properties = d
        return whats_app_send_template_response

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
