from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.social_api_ai_core_api_service_message_reply import SocialApiAiCoreApiServiceMessageReply


T = TypeVar("T", bound="SocialApiAiCoreApiServiceMessageRow")


@_attrs_define
class SocialApiAiCoreApiServiceMessageRow:
    """
    Attributes:
        attachment_type (str | Unset):
        attachment_url (str | Unset):
        conversation_id (str | Unset):
        created_at (str | Unset):
        direction (str | Unset):
        id (str | Unset):
        platform_id (str | Unset):
        reply_to (SocialApiAiCoreApiServiceMessageReply | Unset):
        sender_id (str | Unset):
        sender_name (str | Unset):
        status (str | Unset):
        status_updated_at (str | Unset):
        text (str | Unset):
    """

    attachment_type: str | Unset = UNSET
    attachment_url: str | Unset = UNSET
    conversation_id: str | Unset = UNSET
    created_at: str | Unset = UNSET
    direction: str | Unset = UNSET
    id: str | Unset = UNSET
    platform_id: str | Unset = UNSET
    reply_to: SocialApiAiCoreApiServiceMessageReply | Unset = UNSET
    sender_id: str | Unset = UNSET
    sender_name: str | Unset = UNSET
    status: str | Unset = UNSET
    status_updated_at: str | Unset = UNSET
    text: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        attachment_type = self.attachment_type

        attachment_url = self.attachment_url

        conversation_id = self.conversation_id

        created_at = self.created_at

        direction = self.direction

        id = self.id

        platform_id = self.platform_id

        reply_to: dict[str, Any] | Unset = UNSET
        if not isinstance(self.reply_to, Unset):
            reply_to = self.reply_to.to_dict()

        sender_id = self.sender_id

        sender_name = self.sender_name

        status = self.status

        status_updated_at = self.status_updated_at

        text = self.text

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if attachment_type is not UNSET:
            field_dict["attachment_type"] = attachment_type
        if attachment_url is not UNSET:
            field_dict["attachment_url"] = attachment_url
        if conversation_id is not UNSET:
            field_dict["conversation_id"] = conversation_id
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if direction is not UNSET:
            field_dict["direction"] = direction
        if id is not UNSET:
            field_dict["id"] = id
        if platform_id is not UNSET:
            field_dict["platform_id"] = platform_id
        if reply_to is not UNSET:
            field_dict["reply_to"] = reply_to
        if sender_id is not UNSET:
            field_dict["sender_id"] = sender_id
        if sender_name is not UNSET:
            field_dict["sender_name"] = sender_name
        if status is not UNSET:
            field_dict["status"] = status
        if status_updated_at is not UNSET:
            field_dict["status_updated_at"] = status_updated_at
        if text is not UNSET:
            field_dict["text"] = text

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.social_api_ai_core_api_service_message_reply import (
            SocialApiAiCoreApiServiceMessageReply,  # noqa: PLC0415
        )

        d = dict(src_dict)
        attachment_type = d.pop("attachment_type", UNSET)

        attachment_url = d.pop("attachment_url", UNSET)

        conversation_id = d.pop("conversation_id", UNSET)

        created_at = d.pop("created_at", UNSET)

        direction = d.pop("direction", UNSET)

        id = d.pop("id", UNSET)

        platform_id = d.pop("platform_id", UNSET)

        _reply_to = d.pop("reply_to", UNSET)
        reply_to: SocialApiAiCoreApiServiceMessageReply | Unset
        if isinstance(_reply_to, Unset):
            reply_to = UNSET
        else:
            reply_to = SocialApiAiCoreApiServiceMessageReply.from_dict(_reply_to)

        sender_id = d.pop("sender_id", UNSET)

        sender_name = d.pop("sender_name", UNSET)

        status = d.pop("status", UNSET)

        status_updated_at = d.pop("status_updated_at", UNSET)

        text = d.pop("text", UNSET)

        social_api_ai_core_api_service_message_row = cls(
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
            status=status,
            status_updated_at=status_updated_at,
            text=text,
        )

        social_api_ai_core_api_service_message_row.additional_properties = d
        return social_api_ai_core_api_service_message_row

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
