from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.platform import Platform
from ..types import UNSET, Unset

T = TypeVar("T", bound="InboxConversation")


@_attrs_define
class InboxConversation:
    """
    Attributes:
        account_id (str):
        created_at (datetime.datetime):
        id (str):
        last_message (str):
        last_message_at (datetime.datetime | None):
        participant_id (str):
        participant_name (str):
        participant_picture (str):
        platform (Platform):
        platform_id (str):
        status (str):
        unread_count (int):
        updated_at (datetime.datetime):
        user_id (str):
        page_id (str | Unset):
    """

    account_id: str
    created_at: datetime.datetime
    id: str
    last_message: str
    last_message_at: datetime.datetime | None
    participant_id: str
    participant_name: str
    participant_picture: str
    platform: Platform
    platform_id: str
    status: str
    unread_count: int
    updated_at: datetime.datetime
    user_id: str
    page_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_id = self.account_id

        created_at = self.created_at.isoformat()

        id = self.id

        last_message = self.last_message

        last_message_at: None | str
        if isinstance(self.last_message_at, datetime.datetime):
            last_message_at = self.last_message_at.isoformat()
        else:
            last_message_at = self.last_message_at

        participant_id = self.participant_id

        participant_name = self.participant_name

        participant_picture = self.participant_picture

        platform = self.platform.value

        platform_id = self.platform_id

        status = self.status

        unread_count = self.unread_count

        updated_at = self.updated_at.isoformat()

        user_id = self.user_id

        page_id = self.page_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "account_id": account_id,
                "created_at": created_at,
                "id": id,
                "last_message": last_message,
                "last_message_at": last_message_at,
                "participant_id": participant_id,
                "participant_name": participant_name,
                "participant_picture": participant_picture,
                "platform": platform,
                "platform_id": platform_id,
                "status": status,
                "unread_count": unread_count,
                "updated_at": updated_at,
                "user_id": user_id,
            }
        )
        if page_id is not UNSET:
            field_dict["page_id"] = page_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_id = d.pop("account_id")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        id = d.pop("id")

        last_message = d.pop("last_message")

        def _parse_last_message_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_message_at_type_0 = datetime.datetime.fromisoformat(data)

                return last_message_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        last_message_at = _parse_last_message_at(d.pop("last_message_at"))

        participant_id = d.pop("participant_id")

        participant_name = d.pop("participant_name")

        participant_picture = d.pop("participant_picture")

        platform = Platform(d.pop("platform"))

        platform_id = d.pop("platform_id")

        status = d.pop("status")

        unread_count = d.pop("unread_count")

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        user_id = d.pop("user_id")

        page_id = d.pop("page_id", UNSET)

        inbox_conversation = cls(
            account_id=account_id,
            created_at=created_at,
            id=id,
            last_message=last_message,
            last_message_at=last_message_at,
            participant_id=participant_id,
            participant_name=participant_name,
            participant_picture=participant_picture,
            platform=platform,
            platform_id=platform_id,
            status=status,
            unread_count=unread_count,
            updated_at=updated_at,
            user_id=user_id,
            page_id=page_id,
        )

        inbox_conversation.additional_properties = d
        return inbox_conversation

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
