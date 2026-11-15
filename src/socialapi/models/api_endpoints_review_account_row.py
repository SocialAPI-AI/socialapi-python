from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.api_endpoints_review_account_row_status import ApiEndpointsReviewAccountRowStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiEndpointsReviewAccountRow")


@_attrs_define
class ApiEndpointsReviewAccountRow:
    """
    Attributes:
        account_id (str | Unset):  Example: acc_01HZ....
        average_rating (float | Unset):  Example: 4.2.
        last_review_at (str | Unset):  Example: 2026-06-22T02:24:05Z.
        name (str | Unset):  Example: SocialAPI Profile.
        platform (str | Unset):  Example: google.
        status (ApiEndpointsReviewAccountRowStatus | Unset):  Example: ok.
        total_count (int | Unset):  Example: 87.
    """

    account_id: str | Unset = UNSET
    average_rating: float | Unset = UNSET
    last_review_at: str | Unset = UNSET
    name: str | Unset = UNSET
    platform: str | Unset = UNSET
    status: ApiEndpointsReviewAccountRowStatus | Unset = UNSET
    total_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_id = self.account_id

        average_rating = self.average_rating

        last_review_at = self.last_review_at

        name = self.name

        platform = self.platform

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        total_count = self.total_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_id is not UNSET:
            field_dict["account_id"] = account_id
        if average_rating is not UNSET:
            field_dict["average_rating"] = average_rating
        if last_review_at is not UNSET:
            field_dict["last_review_at"] = last_review_at
        if name is not UNSET:
            field_dict["name"] = name
        if platform is not UNSET:
            field_dict["platform"] = platform
        if status is not UNSET:
            field_dict["status"] = status
        if total_count is not UNSET:
            field_dict["total_count"] = total_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_id = d.pop("account_id", UNSET)

        average_rating = d.pop("average_rating", UNSET)

        last_review_at = d.pop("last_review_at", UNSET)

        name = d.pop("name", UNSET)

        platform = d.pop("platform", UNSET)

        _status = d.pop("status", UNSET)
        status: ApiEndpointsReviewAccountRowStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ApiEndpointsReviewAccountRowStatus(_status)

        total_count = d.pop("total_count", UNSET)

        api_endpoints_review_account_row = cls(
            account_id=account_id,
            average_rating=average_rating,
            last_review_at=last_review_at,
            name=name,
            platform=platform,
            status=status,
            total_count=total_count,
        )

        api_endpoints_review_account_row.additional_properties = d
        return api_endpoints_review_account_row

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
