from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.webhook_event_type import WebhookEventType
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateWebhookRequest")


@_attrs_define
class UpdateWebhookRequest:
    """
    Attributes:
        events (list[WebhookEventType] | Unset): Events replaces the subscribed event types.
        is_active (bool | Unset): IsActive enables or disables delivery to this endpoint. Example: True.
        url (str | Unset): URL changes the webhook delivery endpoint. Must be HTTPS. Example:
            https://example.com/webhooks/socialapi.
    """

    events: list[WebhookEventType] | Unset = UNSET
    is_active: bool | Unset = UNSET
    url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        events: list[str] | Unset = UNSET
        if not isinstance(self.events, Unset):
            events = []
            for events_item_data in self.events:
                events_item = events_item_data.value
                events.append(events_item)

        is_active = self.is_active

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if events is not UNSET:
            field_dict["events"] = events
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _events = d.pop("events", UNSET)
        events: list[WebhookEventType] | Unset = UNSET
        if _events is not UNSET:
            events = []
            for events_item_data in _events:
                events_item = WebhookEventType(events_item_data)

                events.append(events_item)

        is_active = d.pop("is_active", UNSET)

        url = d.pop("url", UNSET)

        update_webhook_request = cls(
            events=events,
            is_active=is_active,
            url=url,
        )

        update_webhook_request.additional_properties = d
        return update_webhook_request

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
