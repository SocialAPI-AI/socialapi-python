from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.social_api_ai_core_api_service_action_type import SocialApiAiCoreApiServiceActionType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.social_api_ai_core_api_service_text_action import SocialApiAiCoreApiServiceTextAction


T = TypeVar("T", bound="SocialApiAiCoreApiServiceAction")


@_attrs_define
class SocialApiAiCoreApiServiceAction:
    """
    Attributes:
        private_reply (SocialApiAiCoreApiServiceTextAction | Unset):
        reply_comment (SocialApiAiCoreApiServiceTextAction | Unset):
        send_dm (SocialApiAiCoreApiServiceTextAction | Unset):
        type_ (SocialApiAiCoreApiServiceActionType | Unset):  Example: private_reply.
    """

    private_reply: SocialApiAiCoreApiServiceTextAction | Unset = UNSET
    reply_comment: SocialApiAiCoreApiServiceTextAction | Unset = UNSET
    send_dm: SocialApiAiCoreApiServiceTextAction | Unset = UNSET
    type_: SocialApiAiCoreApiServiceActionType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        private_reply: dict[str, Any] | Unset = UNSET
        if not isinstance(self.private_reply, Unset):
            private_reply = self.private_reply.to_dict()

        reply_comment: dict[str, Any] | Unset = UNSET
        if not isinstance(self.reply_comment, Unset):
            reply_comment = self.reply_comment.to_dict()

        send_dm: dict[str, Any] | Unset = UNSET
        if not isinstance(self.send_dm, Unset):
            send_dm = self.send_dm.to_dict()

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if private_reply is not UNSET:
            field_dict["private_reply"] = private_reply
        if reply_comment is not UNSET:
            field_dict["reply_comment"] = reply_comment
        if send_dm is not UNSET:
            field_dict["send_dm"] = send_dm
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.social_api_ai_core_api_service_text_action import (
            SocialApiAiCoreApiServiceTextAction,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _private_reply = d.pop("private_reply", UNSET)
        private_reply: SocialApiAiCoreApiServiceTextAction | Unset
        if isinstance(_private_reply, Unset):
            private_reply = UNSET
        else:
            private_reply = SocialApiAiCoreApiServiceTextAction.from_dict(_private_reply)

        _reply_comment = d.pop("reply_comment", UNSET)
        reply_comment: SocialApiAiCoreApiServiceTextAction | Unset
        if isinstance(_reply_comment, Unset):
            reply_comment = UNSET
        else:
            reply_comment = SocialApiAiCoreApiServiceTextAction.from_dict(_reply_comment)

        _send_dm = d.pop("send_dm", UNSET)
        send_dm: SocialApiAiCoreApiServiceTextAction | Unset
        if isinstance(_send_dm, Unset):
            send_dm = UNSET
        else:
            send_dm = SocialApiAiCoreApiServiceTextAction.from_dict(_send_dm)

        _type_ = d.pop("type", UNSET)
        type_: SocialApiAiCoreApiServiceActionType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = SocialApiAiCoreApiServiceActionType(_type_)

        social_api_ai_core_api_service_action = cls(
            private_reply=private_reply,
            reply_comment=reply_comment,
            send_dm=send_dm,
            type_=type_,
        )

        social_api_ai_core_api_service_action.additional_properties = d
        return social_api_ai_core_api_service_action

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
