from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReplyToReviewResponse")


@_attrs_define
class ReplyToReviewResponse:
    """
    Attributes:
        reply_id (str):  Example: r_abc123.
        success (bool):  Example: True.
        state (str | Unset):  Example: PENDING.
    """

    reply_id: str
    success: bool
    state: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        reply_id = self.reply_id

        success = self.success

        state = self.state

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "reply_id": reply_id,
                "success": success,
            }
        )
        if state is not UNSET:
            field_dict["state"] = state

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        reply_id = d.pop("reply_id")

        success = d.pop("success")

        state = d.pop("state", UNSET)

        reply_to_review_response = cls(
            reply_id=reply_id,
            success=success,
            state=state,
        )

        reply_to_review_response.additional_properties = d
        return reply_to_review_response

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
