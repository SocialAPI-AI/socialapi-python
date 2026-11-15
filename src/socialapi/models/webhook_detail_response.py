from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.webhook_stats import WebhookStats


T = TypeVar("T", bound="WebhookDetailResponse")


@_attrs_define
class WebhookDetailResponse:
    """
    Attributes:
        created_at (datetime.datetime):
        events (list[str] | None):
        id (str):
        is_active (bool):
        secret_hint (str):
        stats (WebhookStats):
        url (str):
    """

    created_at: datetime.datetime
    events: list[str] | None
    id: str
    is_active: bool
    secret_hint: str
    stats: WebhookStats
    url: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        events: list[str] | None
        if isinstance(self.events, list):
            events = self.events

        else:
            events = self.events

        id = self.id

        is_active = self.is_active

        secret_hint = self.secret_hint

        stats = self.stats.to_dict()

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_at": created_at,
                "events": events,
                "id": id,
                "is_active": is_active,
                "secret_hint": secret_hint,
                "stats": stats,
                "url": url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.webhook_stats import WebhookStats  # noqa: PLC0415

        d = dict(src_dict)
        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        def _parse_events(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                events_type_0 = cast(list[str], data)

                return events_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        events = _parse_events(d.pop("events"))

        id = d.pop("id")

        is_active = d.pop("is_active")

        secret_hint = d.pop("secret_hint")

        stats = WebhookStats.from_dict(d.pop("stats"))

        url = d.pop("url")

        webhook_detail_response = cls(
            created_at=created_at,
            events=events,
            id=id,
            is_active=is_active,
            secret_hint=secret_hint,
            stats=stats,
            url=url,
        )

        webhook_detail_response.additional_properties = d
        return webhook_detail_response

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
