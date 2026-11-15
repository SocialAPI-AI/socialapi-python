from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="WebhookEndpointItem")


@_attrs_define
class WebhookEndpointItem:
    """
    Attributes:
        created_at (datetime.datetime):  Example: 2026-03-14T09:00:00Z.
        events (list[str] | None):  Example: ['comment.received', 'dm.received'].
        id (str):  Example: wh_01HZ9X3Q4R5M6N7P8V2K0W1J.
        is_active (bool):  Example: True.
        url (str):  Example: https://example.com/webhooks/socialapi.
    """

    created_at: datetime.datetime
    events: list[str] | None
    id: str
    is_active: bool
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

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_at": created_at,
                "events": events,
                "id": id,
                "is_active": is_active,
                "url": url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
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

        url = d.pop("url")

        webhook_endpoint_item = cls(
            created_at=created_at,
            events=events,
            id=id,
            is_active=is_active,
            url=url,
        )

        webhook_endpoint_item.additional_properties = d
        return webhook_endpoint_item

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
