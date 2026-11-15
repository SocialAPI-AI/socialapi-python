from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.platform import Platform
from ..models.review_account_status import ReviewAccountStatus

T = TypeVar("T", bound="ReviewAccount")


@_attrs_define
class ReviewAccount:
    """
    Attributes:
        account_id (str):  Example: acc_01HZ....
        average_rating (float | None):  Example: 4.2.
        last_review_at (datetime.datetime | None):  Example: 2026-06-22T02:24:05Z.
        name (str):  Example: SocialAPI Profile.
        platform (Platform):
        status (ReviewAccountStatus):
        total_count (int | None):  Example: 87.
    """

    account_id: str
    average_rating: float | None
    last_review_at: datetime.datetime | None
    name: str
    platform: Platform
    status: ReviewAccountStatus
    total_count: int | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_id = self.account_id

        average_rating: float | None
        average_rating = self.average_rating

        last_review_at: None | str
        if isinstance(self.last_review_at, datetime.datetime):
            last_review_at = self.last_review_at.isoformat()
        else:
            last_review_at = self.last_review_at

        name = self.name

        platform = self.platform.value

        status = self.status.value

        total_count: int | None
        total_count = self.total_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "account_id": account_id,
                "average_rating": average_rating,
                "last_review_at": last_review_at,
                "name": name,
                "platform": platform,
                "status": status,
                "total_count": total_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_id = d.pop("account_id")

        def _parse_average_rating(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        average_rating = _parse_average_rating(d.pop("average_rating"))

        def _parse_last_review_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_review_at_type_0 = datetime.datetime.fromisoformat(data)

                return last_review_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        last_review_at = _parse_last_review_at(d.pop("last_review_at"))

        name = d.pop("name")

        platform = Platform(d.pop("platform"))

        status = ReviewAccountStatus(d.pop("status"))

        def _parse_total_count(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        total_count = _parse_total_count(d.pop("total_count"))

        review_account = cls(
            account_id=account_id,
            average_rating=average_rating,
            last_review_at=last_review_at,
            name=name,
            platform=platform,
            status=status,
            total_count=total_count,
        )

        review_account.additional_properties = d
        return review_account

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
