from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.message_button import MessageButton
    from ..models.private_reply_attachment_input import PrivateReplyAttachmentInput


T = TypeVar("T", bound="PrivateReplyRequest")


@_attrs_define
class PrivateReplyRequest:
    """
    Attributes:
        account_id (str):
        attachment (PrivateReplyAttachmentInput | Unset):
        buttons (list[MessageButton] | Unset): Buttons renders a button template (1-3 buttons); uses text as the bubble
            body.
        text (str | Unset):
    """

    account_id: str
    attachment: PrivateReplyAttachmentInput | Unset = UNSET
    buttons: list[MessageButton] | Unset = UNSET
    text: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_id = self.account_id

        attachment: dict[str, Any] | Unset = UNSET
        if not isinstance(self.attachment, Unset):
            attachment = self.attachment.to_dict()

        buttons: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.buttons, Unset):
            buttons = []
            for buttons_item_data in self.buttons:
                buttons_item = buttons_item_data.to_dict()
                buttons.append(buttons_item)

        text = self.text

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "account_id": account_id,
            }
        )
        if attachment is not UNSET:
            field_dict["attachment"] = attachment
        if buttons is not UNSET:
            field_dict["buttons"] = buttons
        if text is not UNSET:
            field_dict["text"] = text

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.message_button import MessageButton  # noqa: PLC0415
        from ..models.private_reply_attachment_input import PrivateReplyAttachmentInput  # noqa: PLC0415

        d = dict(src_dict)
        account_id = d.pop("account_id")

        _attachment = d.pop("attachment", UNSET)
        attachment: PrivateReplyAttachmentInput | Unset
        if isinstance(_attachment, Unset):
            attachment = UNSET
        else:
            attachment = PrivateReplyAttachmentInput.from_dict(_attachment)

        _buttons = d.pop("buttons", UNSET)
        buttons: list[MessageButton] | Unset = UNSET
        if _buttons is not UNSET:
            buttons = []
            for buttons_item_data in _buttons:
                buttons_item = MessageButton.from_dict(buttons_item_data)

                buttons.append(buttons_item)

        text = d.pop("text", UNSET)

        private_reply_request = cls(
            account_id=account_id,
            attachment=attachment,
            buttons=buttons,
            text=text,
        )

        private_reply_request.additional_properties = d
        return private_reply_request

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
