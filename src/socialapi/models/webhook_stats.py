from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.delivery_stat_bucket import DeliveryStatBucket


T = TypeVar("T", bound="WebhookStats")


@_attrs_define
class WebhookStats:
    """
    Attributes:
        last_24h (DeliveryStatBucket):
        last_7d (DeliveryStatBucket):
    """

    last_24h: DeliveryStatBucket
    last_7d: DeliveryStatBucket
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        last_24h = self.last_24h.to_dict()

        last_7d = self.last_7d.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "last_24h": last_24h,
                "last_7d": last_7d,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.delivery_stat_bucket import DeliveryStatBucket  # noqa: PLC0415

        d = dict(src_dict)
        last_24h = DeliveryStatBucket.from_dict(d.pop("last_24h"))

        last_7d = DeliveryStatBucket.from_dict(d.pop("last_7d"))

        webhook_stats = cls(
            last_24h=last_24h,
            last_7d=last_7d,
        )

        webhook_stats.additional_properties = d
        return webhook_stats

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
