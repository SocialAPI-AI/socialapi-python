from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiEndpointsReplyToReviewResponse")


@_attrs_define
class ApiEndpointsReplyToReviewResponse:
    """
    Attributes:
        reply_id (str | Unset):  Example: r_abc123.
        state (str | Unset):  Example: PENDING.
        success (bool | Unset):  Example: True.
    """

    reply_id: str | Unset = UNSET
    state: str | Unset = UNSET
    success: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        reply_id = self.reply_id

        state = self.state

        success = self.success

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if reply_id is not UNSET:
            field_dict["reply_id"] = reply_id
        if state is not UNSET:
            field_dict["state"] = state
        if success is not UNSET:
            field_dict["success"] = success

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        reply_id = d.pop("reply_id", UNSET)

        state = d.pop("state", UNSET)

        success = d.pop("success", UNSET)

        api_endpoints_reply_to_review_response = cls(
            reply_id=reply_id,
            state=state,
            success=success,
        )

        api_endpoints_reply_to_review_response.additional_properties = d
        return api_endpoints_reply_to_review_response

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
