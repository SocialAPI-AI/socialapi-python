from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.social_api_ai_core_api_service_delivery_stat_bucket import SocialApiAiCoreApiServiceDeliveryStatBucket


T = TypeVar("T", bound="SocialApiAiCoreApiServiceWebhookStats")


@_attrs_define
class SocialApiAiCoreApiServiceWebhookStats:
    """
    Attributes:
        last_24h (SocialApiAiCoreApiServiceDeliveryStatBucket | Unset):
        last_7d (SocialApiAiCoreApiServiceDeliveryStatBucket | Unset):
    """

    last_24h: SocialApiAiCoreApiServiceDeliveryStatBucket | Unset = UNSET
    last_7d: SocialApiAiCoreApiServiceDeliveryStatBucket | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        last_24h: dict[str, Any] | Unset = UNSET
        if not isinstance(self.last_24h, Unset):
            last_24h = self.last_24h.to_dict()

        last_7d: dict[str, Any] | Unset = UNSET
        if not isinstance(self.last_7d, Unset):
            last_7d = self.last_7d.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if last_24h is not UNSET:
            field_dict["last_24h"] = last_24h
        if last_7d is not UNSET:
            field_dict["last_7d"] = last_7d

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.social_api_ai_core_api_service_delivery_stat_bucket import (
            SocialApiAiCoreApiServiceDeliveryStatBucket,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _last_24h = d.pop("last_24h", UNSET)
        last_24h: SocialApiAiCoreApiServiceDeliveryStatBucket | Unset
        if isinstance(_last_24h, Unset):
            last_24h = UNSET
        else:
            last_24h = SocialApiAiCoreApiServiceDeliveryStatBucket.from_dict(_last_24h)

        _last_7d = d.pop("last_7d", UNSET)
        last_7d: SocialApiAiCoreApiServiceDeliveryStatBucket | Unset
        if isinstance(_last_7d, Unset):
            last_7d = UNSET
        else:
            last_7d = SocialApiAiCoreApiServiceDeliveryStatBucket.from_dict(_last_7d)

        social_api_ai_core_api_service_webhook_stats = cls(
            last_24h=last_24h,
            last_7d=last_7d,
        )

        social_api_ai_core_api_service_webhook_stats.additional_properties = d
        return social_api_ai_core_api_service_webhook_stats

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
