from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.review_reply_detail_policy_violation import ReviewReplyDetailPolicyViolation


T = TypeVar("T", bound="ReviewReplyDetail")


@_attrs_define
class ReviewReplyDetail:
    """
    Attributes:
        text (str):  Example: Thanks for the feedback!.
        updated_at (datetime.datetime):  Example: 2026-06-21T10:00:00Z.
        policy_violation (ReviewReplyDetailPolicyViolation | Unset): PolicyViolation explains a REJECTED reply, passed
            through verbatim from
            the platform. Absent otherwise.
        state (str | Unset): State is the moderation outcome: PENDING, APPROVED, or REJECTED.
            Omitted on platforms that report no moderation state (App Store Connect). Example: APPROVED.
    """

    text: str
    updated_at: datetime.datetime
    policy_violation: ReviewReplyDetailPolicyViolation | Unset = UNSET
    state: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        text = self.text

        updated_at = self.updated_at.isoformat()

        policy_violation: dict[str, Any] | Unset = UNSET
        if not isinstance(self.policy_violation, Unset):
            policy_violation = self.policy_violation.to_dict()

        state = self.state

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "text": text,
                "updated_at": updated_at,
            }
        )
        if policy_violation is not UNSET:
            field_dict["policy_violation"] = policy_violation
        if state is not UNSET:
            field_dict["state"] = state

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.review_reply_detail_policy_violation import ReviewReplyDetailPolicyViolation  # noqa: PLC0415

        d = dict(src_dict)
        text = d.pop("text")

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        _policy_violation = d.pop("policy_violation", UNSET)
        policy_violation: ReviewReplyDetailPolicyViolation | Unset
        if isinstance(_policy_violation, Unset):
            policy_violation = UNSET
        else:
            policy_violation = ReviewReplyDetailPolicyViolation.from_dict(_policy_violation)

        state = d.pop("state", UNSET)

        review_reply_detail = cls(
            text=text,
            updated_at=updated_at,
            policy_violation=policy_violation,
            state=state,
        )

        review_reply_detail.additional_properties = d
        return review_reply_detail

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
