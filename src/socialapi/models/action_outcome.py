from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.action_outcome_status import ActionOutcomeStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="ActionOutcome")


@_attrs_define
class ActionOutcome:
    """
    Attributes:
        action (str):  Example: private_reply.
        status (ActionOutcomeStatus):
        error_code (str | Unset): The error code the same API call would have returned Example:
            platform.instagram.private_reply_ineligible.
    """

    action: str
    status: ActionOutcomeStatus
    error_code: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action = self.action

        status = self.status.value

        error_code = self.error_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "action": action,
                "status": status,
            }
        )
        if error_code is not UNSET:
            field_dict["error_code"] = error_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        action = d.pop("action")

        status = ActionOutcomeStatus(d.pop("status"))

        error_code = d.pop("error_code", UNSET)

        action_outcome = cls(
            action=action,
            status=status,
            error_code=error_code,
        )

        action_outcome.additional_properties = d
        return action_outcome

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
