from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.action_type import ActionType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.text_action import TextAction


T = TypeVar("T", bound="Action")


@_attrs_define
class Action:
    """
    Attributes:
        type_ (ActionType):
        private_reply (TextAction | Unset):
        reply_comment (TextAction | Unset):
        send_dm (TextAction | Unset):
    """

    type_: ActionType
    private_reply: TextAction | Unset = UNSET
    reply_comment: TextAction | Unset = UNSET
    send_dm: TextAction | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        private_reply: dict[str, Any] | Unset = UNSET
        if not isinstance(self.private_reply, Unset):
            private_reply = self.private_reply.to_dict()

        reply_comment: dict[str, Any] | Unset = UNSET
        if not isinstance(self.reply_comment, Unset):
            reply_comment = self.reply_comment.to_dict()

        send_dm: dict[str, Any] | Unset = UNSET
        if not isinstance(self.send_dm, Unset):
            send_dm = self.send_dm.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if private_reply is not UNSET:
            field_dict["private_reply"] = private_reply
        if reply_comment is not UNSET:
            field_dict["reply_comment"] = reply_comment
        if send_dm is not UNSET:
            field_dict["send_dm"] = send_dm

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.text_action import TextAction  # noqa: PLC0415

        d = dict(src_dict)
        type_ = ActionType(d.pop("type"))

        _private_reply = d.pop("private_reply", UNSET)
        private_reply: TextAction | Unset
        if isinstance(_private_reply, Unset):
            private_reply = UNSET
        else:
            private_reply = TextAction.from_dict(_private_reply)

        _reply_comment = d.pop("reply_comment", UNSET)
        reply_comment: TextAction | Unset
        if isinstance(_reply_comment, Unset):
            reply_comment = UNSET
        else:
            reply_comment = TextAction.from_dict(_reply_comment)

        _send_dm = d.pop("send_dm", UNSET)
        send_dm: TextAction | Unset
        if isinstance(_send_dm, Unset):
            send_dm = UNSET
        else:
            send_dm = TextAction.from_dict(_send_dm)

        action = cls(
            type_=type_,
            private_reply=private_reply,
            reply_comment=reply_comment,
            send_dm=send_dm,
        )

        action.additional_properties = d
        return action

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
