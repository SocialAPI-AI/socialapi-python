from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.api_endpoints_create_webhook_request_events_item import ApiEndpointsCreateWebhookRequestEventsItem
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiEndpointsCreateWebhookRequest")


@_attrs_define
class ApiEndpointsCreateWebhookRequest:
    """
    Attributes:
        events (list[ApiEndpointsCreateWebhookRequestEventsItem]): Events is the list of event types to subscribe to.
            Example: ['comment.received', 'dm.received'].
        url (str | Unset): URL is the HTTPS endpoint that will receive webhook POST requests. Example:
            https://example.com/webhooks/socialapi.
    """

    events: list[ApiEndpointsCreateWebhookRequestEventsItem]
    url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        events = []
        for events_item_data in self.events:
            events_item = events_item_data.value
            events.append(events_item)

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "events": events,
            }
        )
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        events = []
        _events = d.pop("events")
        for events_item_data in _events:
            events_item = ApiEndpointsCreateWebhookRequestEventsItem(events_item_data)

            events.append(events_item)

        url = d.pop("url", UNSET)

        api_endpoints_create_webhook_request = cls(
            events=events,
            url=url,
        )

        api_endpoints_create_webhook_request.additional_properties = d
        return api_endpoints_create_webhook_request

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
