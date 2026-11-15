from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiEndpointsWebhookEndpointItem")


@_attrs_define
class ApiEndpointsWebhookEndpointItem:
    """
    Attributes:
        created_at (str | Unset):  Example: 2026-03-14T09:00:00Z.
        events (list[str] | Unset):  Example: ['comment.received', 'dm.received'].
        id (str | Unset):  Example: wh_01HZ9X3Q4R5M6N7P8V2K0W1J.
        is_active (bool | Unset):  Example: True.
        url (str | Unset):  Example: https://example.com/webhooks/socialapi.
    """

    created_at: str | Unset = UNSET
    events: list[str] | Unset = UNSET
    id: str | Unset = UNSET
    is_active: bool | Unset = UNSET
    url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        events: list[str] | Unset = UNSET
        if not isinstance(self.events, Unset):
            events = self.events

        id = self.id

        is_active = self.is_active

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
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created_at = d.pop("created_at", UNSET)

        events = cast(list[str], d.pop("events", UNSET))

        id = d.pop("id", UNSET)

        is_active = d.pop("is_active", UNSET)

        url = d.pop("url", UNSET)

        api_endpoints_webhook_endpoint_item = cls(
            created_at=created_at,
            events=events,
            id=id,
            is_active=is_active,
            url=url,
        )

        api_endpoints_webhook_endpoint_item.additional_properties = d
        return api_endpoints_webhook_endpoint_item

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
