from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiEndpointsReviewSummaryResponse")


@_attrs_define
class ApiEndpointsReviewSummaryResponse:
    """
    Attributes:
        average_rating (float | Unset):  Example: 4.2.
        total_count (int | Unset):  Example: 87.
    """

    average_rating: float | Unset = UNSET
    total_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        average_rating = self.average_rating

        total_count = self.total_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if average_rating is not UNSET:
            field_dict["average_rating"] = average_rating
        if total_count is not UNSET:
            field_dict["total_count"] = total_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        average_rating = d.pop("average_rating", UNSET)

        total_count = d.pop("total_count", UNSET)

        api_endpoints_review_summary_response = cls(
            average_rating=average_rating,
            total_count=total_count,
        )

        api_endpoints_review_summary_response.additional_properties = d
        return api_endpoints_review_summary_response

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
