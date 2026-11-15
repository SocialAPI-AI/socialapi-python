from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CreateWebhookResponse")


@_attrs_define
class CreateWebhookResponse:
    """
    Attributes:
        events (list[str] | None):  Example: ['comment.received', 'dm.received'].
        id (str):  Example: wh_01HZ9X3Q4R5M6N7P8V2K0W1J.
        message (str):  Example: Store the secret securely. It will not be shown again..
        secret (str):  Example: 4f3c2a1b9e8d7c6f5e4d3c2b1a0f9e8d7c6b5a4f3e2d1c0b9a8f7e6d5c4b3a2.
        url (str):  Example: https://example.com/webhooks/socialapi.
    """

    events: list[str] | None
    id: str
    message: str
    secret: str
    url: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        events: list[str] | None
        if isinstance(self.events, list):
            events = self.events

        else:
            events = self.events

        id = self.id

        message = self.message

        secret = self.secret

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "events": events,
                "id": id,
                "message": message,
                "secret": secret,
                "url": url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

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

        message = d.pop("message")

        secret = d.pop("secret")

        url = d.pop("url")

        create_webhook_response = cls(
            events=events,
            id=id,
            message=message,
            secret=secret,
            url=url,
        )

        create_webhook_response.additional_properties = d
        return create_webhook_response

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
