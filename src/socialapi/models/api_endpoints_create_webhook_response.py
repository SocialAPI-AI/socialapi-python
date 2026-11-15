from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiEndpointsCreateWebhookResponse")


@_attrs_define
class ApiEndpointsCreateWebhookResponse:
    """
    Attributes:
        events (list[str] | Unset):  Example: ['comment.received', 'dm.received'].
        id (str | Unset):  Example: wh_01HZ9X3Q4R5M6N7P8V2K0W1J.
        message (str | Unset):  Example: Store the secret securely. It will not be shown again..
        secret (str | Unset):  Example: 4f3c2a1b9e8d7c6f5e4d3c2b1a0f9e8d7c6b5a4f3e2d1c0b9a8f7e6d5c4b3a2.
        url (str | Unset):  Example: https://example.com/webhooks/socialapi.
    """

    events: list[str] | Unset = UNSET
    id: str | Unset = UNSET
    message: str | Unset = UNSET
    secret: str | Unset = UNSET
    url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        events: list[str] | Unset = UNSET
        if not isinstance(self.events, Unset):
            events = self.events

        id = self.id

        message = self.message

        secret = self.secret

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if events is not UNSET:
            field_dict["events"] = events
        if id is not UNSET:
            field_dict["id"] = id
        if message is not UNSET:
            field_dict["message"] = message
        if secret is not UNSET:
            field_dict["secret"] = secret
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        events = cast(list[str], d.pop("events", UNSET))

        id = d.pop("id", UNSET)

        message = d.pop("message", UNSET)

        secret = d.pop("secret", UNSET)

        url = d.pop("url", UNSET)

        api_endpoints_create_webhook_response = cls(
            events=events,
            id=id,
            message=message,
            secret=secret,
            url=url,
        )

        api_endpoints_create_webhook_response.additional_properties = d
        return api_endpoints_create_webhook_response

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
