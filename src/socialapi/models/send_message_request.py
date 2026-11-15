from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dm_attachment_input import DMAttachmentInput
    from ..models.message_button import MessageButton
    from ..models.message_card import MessageCard
    from ..models.message_list_section import MessageListSection
    from ..models.message_quick_reply import MessageQuickReply


T = TypeVar("T", bound="SendMessageRequest")


@_attrs_define
class SendMessageRequest:
    """
    Attributes:
        account_id (str):  Example: acc_abc123.
        attachment_url (str | Unset): AttachmentURL is a single-attachment shorthand. Ignored when attachments is
            non-empty; its type is inferred from the URL extension.

            Deprecated: use Attachments instead, which supersedes it and supports one or
            many items. Example: https://cdn.example.com/photo.jpg.
        attachments (list[DMAttachmentInput] | Unset): Attachments sends one or more media items, each as its own
            message bubble.
        buttons (list[MessageButton] | Unset): Buttons renders a button template (1-3 buttons); uses text as the bubble
            body.
            On WhatsApp send up to 3 postback buttons with unique payloads, or a single
            url button that opens its url.
        cards (list[MessageCard] | Unset): Cards renders a generic/carousel template (up to 10 cards).
        list_button (str | Unset): ListButton is the label on the button that opens the list. Required with
            list_sections, max 20 characters. Example: View options.
        list_sections (list[MessageListSection] | Unset): ListSections renders a tappable list behind a single button,
            for menus wider
            than the 3 buttons a reply-button message allows (up to 10 rows in total,
            across up to 10 sections). WhatsApp only; requires text and list_button.
        message_tag (str | Unset): Optional. Only `HUMAN_AGENT` is accepted, on Instagram accounts connected with
            Instagram Login, for replies a member of your team types between 24 hours and 7 days after the person's last
            message. Workflows, automations, bots and AI agents acting on their own send without it, so they reply within 24
            hours of the person's last message. Ask support to enable it for your account. Inside 24 hours the message is
            sent without the tag. Example: HUMAN_AGENT.
        quick_replies (list[MessageQuickReply] | Unset): QuickReplies renders up to 13 tappable chips above the
            keyboard; requires text.
        reply_to_message_id (str | Unset): ReplyToMessageID makes the first sent bubble a reply to a specific prior
            message (Meta reply_to.mid). Instagram/Facebook only. Example: m_1234567890.
        text (str | Unset):  Example: Thanks for your message!.
    """

    account_id: str
    attachment_url: str | Unset = UNSET
    attachments: list[DMAttachmentInput] | Unset = UNSET
    buttons: list[MessageButton] | Unset = UNSET
    cards: list[MessageCard] | Unset = UNSET
    list_button: str | Unset = UNSET
    list_sections: list[MessageListSection] | Unset = UNSET
    message_tag: str | Unset = UNSET
    quick_replies: list[MessageQuickReply] | Unset = UNSET
    reply_to_message_id: str | Unset = UNSET
    text: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_id = self.account_id

        attachment_url = self.attachment_url

        attachments: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.attachments, Unset):
            attachments = []
            for attachments_item_data in self.attachments:
                attachments_item = attachments_item_data.to_dict()
                attachments.append(attachments_item)

        buttons: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.buttons, Unset):
            buttons = []
            for buttons_item_data in self.buttons:
                buttons_item = buttons_item_data.to_dict()
                buttons.append(buttons_item)

        cards: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.cards, Unset):
            cards = []
            for cards_item_data in self.cards:
                cards_item = cards_item_data.to_dict()
                cards.append(cards_item)

        list_button = self.list_button

        list_sections: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.list_sections, Unset):
            list_sections = []
            for list_sections_item_data in self.list_sections:
                list_sections_item = list_sections_item_data.to_dict()
                list_sections.append(list_sections_item)

        message_tag = self.message_tag

        quick_replies: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.quick_replies, Unset):
            quick_replies = []
            for quick_replies_item_data in self.quick_replies:
                quick_replies_item = quick_replies_item_data.to_dict()
                quick_replies.append(quick_replies_item)

        reply_to_message_id = self.reply_to_message_id

        text = self.text

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "account_id": account_id,
            }
        )
        if attachment_url is not UNSET:
            field_dict["attachment_url"] = attachment_url
        if attachments is not UNSET:
            field_dict["attachments"] = attachments
        if buttons is not UNSET:
            field_dict["buttons"] = buttons
        if cards is not UNSET:
            field_dict["cards"] = cards
        if list_button is not UNSET:
            field_dict["list_button"] = list_button
        if list_sections is not UNSET:
            field_dict["list_sections"] = list_sections
        if message_tag is not UNSET:
            field_dict["message_tag"] = message_tag
        if quick_replies is not UNSET:
            field_dict["quick_replies"] = quick_replies
        if reply_to_message_id is not UNSET:
            field_dict["reply_to_message_id"] = reply_to_message_id
        if text is not UNSET:
            field_dict["text"] = text

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dm_attachment_input import DMAttachmentInput  # noqa: PLC0415
        from ..models.message_button import MessageButton  # noqa: PLC0415
        from ..models.message_card import MessageCard  # noqa: PLC0415
        from ..models.message_list_section import MessageListSection  # noqa: PLC0415
        from ..models.message_quick_reply import MessageQuickReply  # noqa: PLC0415

        d = dict(src_dict)
        account_id = d.pop("account_id")

        attachment_url = d.pop("attachment_url", UNSET)

        _attachments = d.pop("attachments", UNSET)
        attachments: list[DMAttachmentInput] | Unset = UNSET
        if _attachments is not UNSET:
            attachments = []
            for attachments_item_data in _attachments:
                attachments_item = DMAttachmentInput.from_dict(attachments_item_data)

                attachments.append(attachments_item)

        _buttons = d.pop("buttons", UNSET)
        buttons: list[MessageButton] | Unset = UNSET
        if _buttons is not UNSET:
            buttons = []
            for buttons_item_data in _buttons:
                buttons_item = MessageButton.from_dict(buttons_item_data)

                buttons.append(buttons_item)

        _cards = d.pop("cards", UNSET)
        cards: list[MessageCard] | Unset = UNSET
        if _cards is not UNSET:
            cards = []
            for cards_item_data in _cards:
                cards_item = MessageCard.from_dict(cards_item_data)

                cards.append(cards_item)

        list_button = d.pop("list_button", UNSET)

        _list_sections = d.pop("list_sections", UNSET)
        list_sections: list[MessageListSection] | Unset = UNSET
        if _list_sections is not UNSET:
            list_sections = []
            for list_sections_item_data in _list_sections:
                list_sections_item = MessageListSection.from_dict(list_sections_item_data)

                list_sections.append(list_sections_item)

        message_tag = d.pop("message_tag", UNSET)

        _quick_replies = d.pop("quick_replies", UNSET)
        quick_replies: list[MessageQuickReply] | Unset = UNSET
        if _quick_replies is not UNSET:
            quick_replies = []
            for quick_replies_item_data in _quick_replies:
                quick_replies_item = MessageQuickReply.from_dict(quick_replies_item_data)

                quick_replies.append(quick_replies_item)

        reply_to_message_id = d.pop("reply_to_message_id", UNSET)

        text = d.pop("text", UNSET)

        send_message_request = cls(
            account_id=account_id,
            attachment_url=attachment_url,
            attachments=attachments,
            buttons=buttons,
            cards=cards,
            list_button=list_button,
            list_sections=list_sections,
            message_tag=message_tag,
            quick_replies=quick_replies,
            reply_to_message_id=reply_to_message_id,
            text=text,
        )

        send_message_request.additional_properties = d
        return send_message_request

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
