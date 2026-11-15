from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_endpoints_events_summary_response_by_category import ApiEndpointsEventsSummaryResponseByCategory
    from ..models.api_endpoints_events_summary_response_by_error_category import (
        ApiEndpointsEventsSummaryResponseByErrorCategory,
    )
    from ..models.api_endpoints_events_summary_response_inbox_breakdown import (
        ApiEndpointsEventsSummaryResponseInboxBreakdown,
    )


T = TypeVar("T", bound="ApiEndpointsEventsSummaryResponse")


@_attrs_define
class ApiEndpointsEventsSummaryResponse:
    """
    Attributes:
        by_category (ApiEndpointsEventsSummaryResponseByCategory | Unset):
        by_error_category (ApiEndpointsEventsSummaryResponseByErrorCategory | Unset):
        failed (int | Unset):
        inbox_breakdown (ApiEndpointsEventsSummaryResponseInboxBreakdown | Unset):
        retention_days (int | Unset):
        total (int | Unset):
        total_previous (int | Unset):
    """

    by_category: ApiEndpointsEventsSummaryResponseByCategory | Unset = UNSET
    by_error_category: ApiEndpointsEventsSummaryResponseByErrorCategory | Unset = UNSET
    failed: int | Unset = UNSET
    inbox_breakdown: ApiEndpointsEventsSummaryResponseInboxBreakdown | Unset = UNSET
    retention_days: int | Unset = UNSET
    total: int | Unset = UNSET
    total_previous: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        by_category: dict[str, Any] | Unset = UNSET
        if not isinstance(self.by_category, Unset):
            by_category = self.by_category.to_dict()

        by_error_category: dict[str, Any] | Unset = UNSET
        if not isinstance(self.by_error_category, Unset):
            by_error_category = self.by_error_category.to_dict()

        failed = self.failed

        inbox_breakdown: dict[str, Any] | Unset = UNSET
        if not isinstance(self.inbox_breakdown, Unset):
            inbox_breakdown = self.inbox_breakdown.to_dict()

        retention_days = self.retention_days

        total = self.total

        total_previous = self.total_previous

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if by_category is not UNSET:
            field_dict["by_category"] = by_category
        if by_error_category is not UNSET:
            field_dict["by_error_category"] = by_error_category
        if failed is not UNSET:
            field_dict["failed"] = failed
        if inbox_breakdown is not UNSET:
            field_dict["inbox_breakdown"] = inbox_breakdown
        if retention_days is not UNSET:
            field_dict["retention_days"] = retention_days
        if total is not UNSET:
            field_dict["total"] = total
        if total_previous is not UNSET:
            field_dict["total_previous"] = total_previous

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_endpoints_events_summary_response_by_category import (
            ApiEndpointsEventsSummaryResponseByCategory,  # noqa: PLC0415
        )
        from ..models.api_endpoints_events_summary_response_by_error_category import (
            ApiEndpointsEventsSummaryResponseByErrorCategory,  # noqa: PLC0415
        )
        from ..models.api_endpoints_events_summary_response_inbox_breakdown import (
            ApiEndpointsEventsSummaryResponseInboxBreakdown,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _by_category = d.pop("by_category", UNSET)
        by_category: ApiEndpointsEventsSummaryResponseByCategory | Unset
        if isinstance(_by_category, Unset):
            by_category = UNSET
        else:
            by_category = ApiEndpointsEventsSummaryResponseByCategory.from_dict(_by_category)

        _by_error_category = d.pop("by_error_category", UNSET)
        by_error_category: ApiEndpointsEventsSummaryResponseByErrorCategory | Unset
        if isinstance(_by_error_category, Unset):
            by_error_category = UNSET
        else:
            by_error_category = ApiEndpointsEventsSummaryResponseByErrorCategory.from_dict(_by_error_category)

        failed = d.pop("failed", UNSET)

        _inbox_breakdown = d.pop("inbox_breakdown", UNSET)
        inbox_breakdown: ApiEndpointsEventsSummaryResponseInboxBreakdown | Unset
        if isinstance(_inbox_breakdown, Unset):
            inbox_breakdown = UNSET
        else:
            inbox_breakdown = ApiEndpointsEventsSummaryResponseInboxBreakdown.from_dict(_inbox_breakdown)

        retention_days = d.pop("retention_days", UNSET)

        total = d.pop("total", UNSET)

        total_previous = d.pop("total_previous", UNSET)

        api_endpoints_events_summary_response = cls(
            by_category=by_category,
            by_error_category=by_error_category,
            failed=failed,
            inbox_breakdown=inbox_breakdown,
            retention_days=retention_days,
            total=total,
            total_previous=total_previous,
        )

        api_endpoints_events_summary_response.additional_properties = d
        return api_endpoints_events_summary_response

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
