from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.social_api_ai_core_api_service_webhook_stats import SocialApiAiCoreApiServiceWebhookStats


T = TypeVar("T", bound="ApiEndpointsWebhookDetailResponse")


@_attrs_define
class ApiEndpointsWebhookDetailResponse:
    """
    Attributes:
        created_at (str | Unset):
        events (list[str] | Unset):
        id (str | Unset):
        is_active (bool | Unset):
        secret_hint (str | Unset):
        stats (SocialApiAiCoreApiServiceWebhookStats | Unset):
        url (str | Unset):
    """

    created_at: str | Unset = UNSET
    events: list[str] | Unset = UNSET
    id: str | Unset = UNSET
    is_active: bool | Unset = UNSET
    secret_hint: str | Unset = UNSET
    stats: SocialApiAiCoreApiServiceWebhookStats | Unset = UNSET
    url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        events: list[str] | Unset = UNSET
        if not isinstance(self.events, Unset):
            events = self.events

        id = self.id

        is_active = self.is_active

        secret_hint = self.secret_hint

        stats: dict[str, Any] | Unset = UNSET
        if not isinstance(self.stats, Unset):
            stats = self.stats.to_dict()

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if events is not UNSET:
            field_dict["events"] = events
        if id is not UNSET:
            field_dict["id"] = id
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if secret_hint is not UNSET:
            field_dict["secret_hint"] = secret_hint
        if stats is not UNSET:
            field_dict["stats"] = stats
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.social_api_ai_core_api_service_webhook_stats import (
            SocialApiAiCoreApiServiceWebhookStats,  # noqa: PLC0415
        )

        d = dict(src_dict)
        created_at = d.pop("created_at", UNSET)

        events = cast(list[str], d.pop("events", UNSET))

        id = d.pop("id", UNSET)

        is_active = d.pop("is_active", UNSET)

        secret_hint = d.pop("secret_hint", UNSET)

        _stats = d.pop("stats", UNSET)
        stats: SocialApiAiCoreApiServiceWebhookStats | Unset
        if isinstance(_stats, Unset):
            stats = UNSET
        else:
            stats = SocialApiAiCoreApiServiceWebhookStats.from_dict(_stats)

        url = d.pop("url", UNSET)

        api_endpoints_webhook_detail_response = cls(
            created_at=created_at,
            events=events,
            id=id,
            is_active=is_active,
            secret_hint=secret_hint,
            stats=stats,
            url=url,
        )

        api_endpoints_webhook_detail_response.additional_properties = d
        return api_endpoints_webhook_detail_response

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
