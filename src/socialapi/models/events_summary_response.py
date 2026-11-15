from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.events_summary_response_by_category import EventsSummaryResponseByCategory
    from ..models.events_summary_response_by_error_category import EventsSummaryResponseByErrorCategory
    from ..models.events_summary_response_inbox_breakdown import EventsSummaryResponseInboxBreakdown


T = TypeVar("T", bound="EventsSummaryResponse")


@_attrs_define
class EventsSummaryResponse:
    """
    Attributes:
        by_category (EventsSummaryResponseByCategory):
        by_error_category (EventsSummaryResponseByErrorCategory):
        failed (int):
        inbox_breakdown (EventsSummaryResponseInboxBreakdown):
        retention_days (int):
        total (int):
        total_previous (int | Unset):
    """

    by_category: EventsSummaryResponseByCategory
    by_error_category: EventsSummaryResponseByErrorCategory
    failed: int
    inbox_breakdown: EventsSummaryResponseInboxBreakdown
    retention_days: int
    total: int
    total_previous: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        by_category = self.by_category.to_dict()

        by_error_category = self.by_error_category.to_dict()

        failed = self.failed

        inbox_breakdown = self.inbox_breakdown.to_dict()

        retention_days = self.retention_days

        total = self.total

        total_previous = self.total_previous

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "by_category": by_category,
                "by_error_category": by_error_category,
                "failed": failed,
                "inbox_breakdown": inbox_breakdown,
                "retention_days": retention_days,
                "total": total,
            }
        )
        if total_previous is not UNSET:
            field_dict["total_previous"] = total_previous

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.events_summary_response_by_category import EventsSummaryResponseByCategory  # noqa: PLC0415
        from ..models.events_summary_response_by_error_category import (
            EventsSummaryResponseByErrorCategory,  # noqa: PLC0415
        )
        from ..models.events_summary_response_inbox_breakdown import (
            EventsSummaryResponseInboxBreakdown,  # noqa: PLC0415
        )

        d = dict(src_dict)
        by_category = EventsSummaryResponseByCategory.from_dict(d.pop("by_category"))

        by_error_category = EventsSummaryResponseByErrorCategory.from_dict(d.pop("by_error_category"))

        failed = d.pop("failed")

        inbox_breakdown = EventsSummaryResponseInboxBreakdown.from_dict(d.pop("inbox_breakdown"))

        retention_days = d.pop("retention_days")

        total = d.pop("total")

        total_previous = d.pop("total_previous", UNSET)

        events_summary_response = cls(
            by_category=by_category,
            by_error_category=by_error_category,
            failed=failed,
            inbox_breakdown=inbox_breakdown,
            retention_days=retention_days,
            total=total,
            total_previous=total_previous,
        )

        events_summary_response.additional_properties = d
        return events_summary_response

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
