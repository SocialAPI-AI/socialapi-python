from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.platform import Platform
from ..models.target_delete_outcome import TargetDeleteOutcome
from ..types import UNSET, Unset

T = TypeVar("T", bound="TargetDeleteOutcomeResponse")


@_attrs_define
class TargetDeleteOutcomeResponse:
    """
    Attributes:
        outcome (TargetDeleteOutcome):
        platform (Platform):
        account_id (str | Unset):  Example: acc_01HZ9X3Q4R5M6N7P8V2K0W1J.
        message (str | Unset):  Example: Operation not supported for this platform.
    """

    outcome: TargetDeleteOutcome
    platform: Platform
    account_id: str | Unset = UNSET
    message: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        outcome = self.outcome.value

        platform = self.platform.value

        account_id = self.account_id

        message = self.message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "outcome": outcome,
                "platform": platform,
            }
        )
        if account_id is not UNSET:
            field_dict["account_id"] = account_id
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        outcome = TargetDeleteOutcome(d.pop("outcome"))

        platform = Platform(d.pop("platform"))

        account_id = d.pop("account_id", UNSET)

        message = d.pop("message", UNSET)

        target_delete_outcome_response = cls(
            outcome=outcome,
            platform=platform,
            account_id=account_id,
            message=message,
        )

        target_delete_outcome_response.additional_properties = d
        return target_delete_outcome_response

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
