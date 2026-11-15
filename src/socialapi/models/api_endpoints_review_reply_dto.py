from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_endpoints_review_reply_dto_policy_violation import ApiEndpointsReviewReplyDTOPolicyViolation


T = TypeVar("T", bound="ApiEndpointsReviewReplyDTO")


@_attrs_define
class ApiEndpointsReviewReplyDTO:
    """
    Attributes:
        policy_violation (ApiEndpointsReviewReplyDTOPolicyViolation | Unset): PolicyViolation explains a REJECTED reply,
            passed through verbatim from
            the platform. Absent otherwise.
        state (str | Unset): State is the moderation outcome: PENDING, APPROVED, or REJECTED.
            Omitted on platforms that report no moderation state (App Store Connect). Example: APPROVED.
        text (str | Unset):  Example: Thanks for the feedback!.
        updated_at (str | Unset):  Example: 2026-06-21T10:00:00Z.
    """

    policy_violation: ApiEndpointsReviewReplyDTOPolicyViolation | Unset = UNSET
    state: str | Unset = UNSET
    text: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        policy_violation: dict[str, Any] | Unset = UNSET
        if not isinstance(self.policy_violation, Unset):
            policy_violation = self.policy_violation.to_dict()

        state = self.state

        text = self.text

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if policy_violation is not UNSET:
            field_dict["policy_violation"] = policy_violation
        if state is not UNSET:
            field_dict["state"] = state
        if text is not UNSET:
            field_dict["text"] = text
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_endpoints_review_reply_dto_policy_violation import (
            ApiEndpointsReviewReplyDTOPolicyViolation,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _policy_violation = d.pop("policy_violation", UNSET)
        policy_violation: ApiEndpointsReviewReplyDTOPolicyViolation | Unset
        if isinstance(_policy_violation, Unset):
            policy_violation = UNSET
        else:
            policy_violation = ApiEndpointsReviewReplyDTOPolicyViolation.from_dict(_policy_violation)

        state = d.pop("state", UNSET)

        text = d.pop("text", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        api_endpoints_review_reply_dto = cls(
            policy_violation=policy_violation,
            state=state,
            text=text,
            updated_at=updated_at,
        )

        api_endpoints_review_reply_dto.additional_properties = d
        return api_endpoints_review_reply_dto

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
