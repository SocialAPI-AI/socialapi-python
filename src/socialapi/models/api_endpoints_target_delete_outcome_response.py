from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.api_endpoints_target_delete_outcome_response_outcome import ApiEndpointsTargetDeleteOutcomeResponseOutcome
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiEndpointsTargetDeleteOutcomeResponse")


@_attrs_define
class ApiEndpointsTargetDeleteOutcomeResponse:
    """
    Attributes:
        account_id (str | Unset):  Example: acc_01HZ9X3Q4R5M6N7P8V2K0W1J.
        message (str | Unset):  Example: Operation not supported for this platform.
        outcome (ApiEndpointsTargetDeleteOutcomeResponseOutcome | Unset):  Example: not_supported.
        platform (str | Unset):  Example: tiktok.
    """

    account_id: str | Unset = UNSET
    message: str | Unset = UNSET
    outcome: ApiEndpointsTargetDeleteOutcomeResponseOutcome | Unset = UNSET
    platform: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_id = self.account_id

        message = self.message

        outcome: str | Unset = UNSET
        if not isinstance(self.outcome, Unset):
            outcome = self.outcome.value

        platform = self.platform

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_id is not UNSET:
            field_dict["account_id"] = account_id
        if message is not UNSET:
            field_dict["message"] = message
        if outcome is not UNSET:
            field_dict["outcome"] = outcome
        if platform is not UNSET:
            field_dict["platform"] = platform

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_id = d.pop("account_id", UNSET)

        message = d.pop("message", UNSET)

        _outcome = d.pop("outcome", UNSET)
        outcome: ApiEndpointsTargetDeleteOutcomeResponseOutcome | Unset
        if isinstance(_outcome, Unset):
            outcome = UNSET
        else:
            outcome = ApiEndpointsTargetDeleteOutcomeResponseOutcome(_outcome)

        platform = d.pop("platform", UNSET)

        api_endpoints_target_delete_outcome_response = cls(
            account_id=account_id,
            message=message,
            outcome=outcome,
            platform=platform,
        )

        api_endpoints_target_delete_outcome_response.additional_properties = d
        return api_endpoints_target_delete_outcome_response

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
