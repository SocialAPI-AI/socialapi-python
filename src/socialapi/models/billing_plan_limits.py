from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="BillingPlanLimits")


@_attrs_define
class BillingPlanLimits:
    """
    Attributes:
        event_retention_days (int):  Example: 30.
        exports_per_month (int):  Example: 20.
        interactions_per_month (int):  Example: -1.
        posts_per_month (int):  Example: -1.
        profiles (int):  Example: 50.
        storage_bytes (int):  Example: -1.
    """

    event_retention_days: int
    exports_per_month: int
    interactions_per_month: int
    posts_per_month: int
    profiles: int
    storage_bytes: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        event_retention_days = self.event_retention_days

        exports_per_month = self.exports_per_month

        interactions_per_month = self.interactions_per_month

        posts_per_month = self.posts_per_month

        profiles = self.profiles

        storage_bytes = self.storage_bytes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "event_retention_days": event_retention_days,
                "exports_per_month": exports_per_month,
                "interactions_per_month": interactions_per_month,
                "posts_per_month": posts_per_month,
                "profiles": profiles,
                "storage_bytes": storage_bytes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        event_retention_days = d.pop("event_retention_days")

        exports_per_month = d.pop("exports_per_month")

        interactions_per_month = d.pop("interactions_per_month")

        posts_per_month = d.pop("posts_per_month")

        profiles = d.pop("profiles")

        storage_bytes = d.pop("storage_bytes")

        billing_plan_limits = cls(
            event_retention_days=event_retention_days,
            exports_per_month=exports_per_month,
            interactions_per_month=interactions_per_month,
            posts_per_month=posts_per_month,
            profiles=profiles,
            storage_bytes=storage_bytes,
        )

        billing_plan_limits.additional_properties = d
        return billing_plan_limits

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
