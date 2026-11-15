from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SocialApiAiCoreApiServiceConversationRow")


@_attrs_define
class SocialApiAiCoreApiServiceConversationRow:
    """
    Attributes:
        account_id (str | Unset):
        created_at (str | Unset):
        id (str | Unset):
        last_message (str | Unset):
        last_message_at (str | Unset):
        page_id (str | Unset):
        participant_id (str | Unset):
        participant_name (str | Unset):
        participant_picture (str | Unset):
        platform (str | Unset):
        platform_id (str | Unset):
        status (str | Unset):
        unread_count (int | Unset):
        updated_at (str | Unset):
        user_id (str | Unset):
    """

    account_id: str | Unset = UNSET
    created_at: str | Unset = UNSET
    id: str | Unset = UNSET
    last_message: str | Unset = UNSET
    last_message_at: str | Unset = UNSET
    page_id: str | Unset = UNSET
    participant_id: str | Unset = UNSET
    participant_name: str | Unset = UNSET
    participant_picture: str | Unset = UNSET
    platform: str | Unset = UNSET
    platform_id: str | Unset = UNSET
    status: str | Unset = UNSET
    unread_count: int | Unset = UNSET
    updated_at: str | Unset = UNSET
    user_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_id = self.account_id

        created_at = self.created_at

        id = self.id

        last_message = self.last_message

        last_message_at = self.last_message_at

        page_id = self.page_id

        participant_id = self.participant_id

        participant_name = self.participant_name

        participant_picture = self.participant_picture

        platform = self.platform

        platform_id = self.platform_id

        status = self.status

        unread_count = self.unread_count

        updated_at = self.updated_at

        user_id = self.user_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_id is not UNSET:
            field_dict["account_id"] = account_id
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if id is not UNSET:
            field_dict["id"] = id
        if last_message is not UNSET:
            field_dict["last_message"] = last_message
        if last_message_at is not UNSET:
            field_dict["last_message_at"] = last_message_at
        if page_id is not UNSET:
            field_dict["page_id"] = page_id
        if participant_id is not UNSET:
            field_dict["participant_id"] = participant_id
        if participant_name is not UNSET:
            field_dict["participant_name"] = participant_name
        if participant_picture is not UNSET:
            field_dict["participant_picture"] = participant_picture
        if platform is not UNSET:
            field_dict["platform"] = platform
        if platform_id is not UNSET:
            field_dict["platform_id"] = platform_id
        if status is not UNSET:
            field_dict["status"] = status
        if unread_count is not UNSET:
            field_dict["unread_count"] = unread_count
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if user_id is not UNSET:
            field_dict["user_id"] = user_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_id = d.pop("account_id", UNSET)

        created_at = d.pop("created_at", UNSET)

        id = d.pop("id", UNSET)

        last_message = d.pop("last_message", UNSET)

        last_message_at = d.pop("last_message_at", UNSET)

        page_id = d.pop("page_id", UNSET)

        participant_id = d.pop("participant_id", UNSET)

        participant_name = d.pop("participant_name", UNSET)

        participant_picture = d.pop("participant_picture", UNSET)

        platform = d.pop("platform", UNSET)

        platform_id = d.pop("platform_id", UNSET)

        status = d.pop("status", UNSET)

        unread_count = d.pop("unread_count", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        user_id = d.pop("user_id", UNSET)

        social_api_ai_core_api_service_conversation_row = cls(
            account_id=account_id,
            created_at=created_at,
            id=id,
            last_message=last_message,
            last_message_at=last_message_at,
            page_id=page_id,
            participant_id=participant_id,
            participant_name=participant_name,
            participant_picture=participant_picture,
            platform=platform,
            platform_id=platform_id,
            status=status,
            unread_count=unread_count,
            updated_at=updated_at,
            user_id=user_id,
        )

        social_api_ai_core_api_service_conversation_row.additional_properties = d
        return social_api_ai_core_api_service_conversation_row

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
