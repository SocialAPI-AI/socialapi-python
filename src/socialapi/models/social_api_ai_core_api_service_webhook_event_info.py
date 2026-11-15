from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SocialApiAiCoreApiServiceWebhookEventInfo")


@_attrs_define
class SocialApiAiCoreApiServiceWebhookEventInfo:
    """
    Attributes:
        category (str | Unset): "posts" | "inbox" | "accounts"
        description (str | Unset):
        event (str | Unset):
    """

    category: str | Unset = UNSET
    description: str | Unset = UNSET
    event: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        category = self.category

        description = self.description

        event = self.event

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if category is not UNSET:
            field_dict["category"] = category
        if description is not UNSET:
            field_dict["description"] = description
        if event is not UNSET:
            field_dict["event"] = event

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        category = d.pop("category", UNSET)

        description = d.pop("description", UNSET)

        event = d.pop("event", UNSET)

        social_api_ai_core_api_service_webhook_event_info = cls(
            category=category,
            description=description,
            event=event,
        )

        social_api_ai_core_api_service_webhook_event_info.additional_properties = d
        return social_api_ai_core_api_service_webhook_event_info

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
