from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SocialApiAiCoreApiServiceMessageReply")


@_attrs_define
class SocialApiAiCoreApiServiceMessageReply:
    """
    Attributes:
        platform_id (str | Unset):
    """

    platform_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        platform_id = self.platform_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if platform_id is not UNSET:
            field_dict["platform_id"] = platform_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        platform_id = d.pop("platform_id", UNSET)

        social_api_ai_core_api_service_message_reply = cls(
            platform_id=platform_id,
        )

        social_api_ai_core_api_service_message_reply.additional_properties = d
        return social_api_ai_core_api_service_message_reply

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
