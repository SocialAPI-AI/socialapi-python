from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.message_reply import MessageReply


T = TypeVar("T", bound="InboxMessage")


@_attrs_define
class InboxMessage:
    """
    Attributes:
        attachment_type (None | str):
        attachment_url (None | str):
        conversation_id (str):
        created_at (str):
        direction (str):
        id (str):
        platform_id (str):
        reply_to (MessageReply | None): ReplyTo is the message this one replies to, or null when it is not a reply.
        sender_id (str):
        sender_name (str):
        text (None | str):
        status (str | Unset):
        status_updated_at (str | Unset):
    """

    attachment_type: None | str
    attachment_url: None | str
    conversation_id: str
    created_at: str
    direction: str
    id: str
    platform_id: str
    reply_to: MessageReply | None
    sender_id: str
    sender_name: str
    text: None | str
    status: str | Unset = UNSET
    status_updated_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.message_reply import MessageReply  # noqa: PLC0415

        attachment_type: None | str
        attachment_type = self.attachment_type

        attachment_url: None | str
        attachment_url = self.attachment_url

        conversation_id = self.conversation_id

        created_at = self.created_at

        direction = self.direction

        id = self.id

        platform_id = self.platform_id

        reply_to: dict[str, Any] | None
        if isinstance(self.reply_to, MessageReply):
            reply_to = self.reply_to.to_dict()
        else:
            reply_to = self.reply_to

        sender_id = self.sender_id

        sender_name = self.sender_name

        text: None | str
        text = self.text

        status = self.status

        status_updated_at = self.status_updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "attachment_type": attachment_type,
                "attachment_url": attachment_url,
                "conversation_id": conversation_id,
                "created_at": created_at,
                "direction": direction,
                "id": id,
                "platform_id": platform_id,
                "reply_to": reply_to,
                "sender_id": sender_id,
                "sender_name": sender_name,
                "text": text,
            }
        )
        if status is not UNSET:
            field_dict["status"] = status
        if status_updated_at is not UNSET:
            field_dict["status_updated_at"] = status_updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.message_reply import MessageReply  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_attachment_type(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        attachment_type = _parse_attachment_type(d.pop("attachment_type"))

        def _parse_attachment_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        attachment_url = _parse_attachment_url(d.pop("attachment_url"))

        conversation_id = d.pop("conversation_id")

        created_at = d.pop("created_at")

        direction = d.pop("direction")

        id = d.pop("id")

        platform_id = d.pop("platform_id")

        def _parse_reply_to(data: object) -> MessageReply | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                reply_to_type_1 = MessageReply.from_dict(data)

                return reply_to_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MessageReply | None, data)

        reply_to = _parse_reply_to(d.pop("reply_to"))

        sender_id = d.pop("sender_id")

        sender_name = d.pop("sender_name")

        def _parse_text(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        text = _parse_text(d.pop("text"))

        status = d.pop("status", UNSET)

        status_updated_at = d.pop("status_updated_at", UNSET)

        inbox_message = cls(
            attachment_type=attachment_type,
            attachment_url=attachment_url,
            conversation_id=conversation_id,
            created_at=created_at,
            direction=direction,
            id=id,
            platform_id=platform_id,
            reply_to=reply_to,
            sender_id=sender_id,
            sender_name=sender_name,
            text=text,
            status=status,
            status_updated_at=status_updated_at,
        )

        inbox_message.additional_properties = d
        return inbox_message

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
