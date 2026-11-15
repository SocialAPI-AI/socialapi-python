from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SocialApiAiCoreApiServiceTextAction")


@_attrs_define
class SocialApiAiCoreApiServiceTextAction:
    """
    Attributes:
        texts (list[str] | Unset): 1 to 10 variants, each 1 to 1000 characters, or at most 640 for a private_reply or
            send_dm whose step has buttons; one is picked at random each time Example: ['Here is the link:
            https://example.com'].
    """

    texts: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        texts: list[str] | Unset = UNSET
        if not isinstance(self.texts, Unset):
            texts = self.texts

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if texts is not UNSET:
            field_dict["texts"] = texts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        texts = cast(list[str], d.pop("texts", UNSET))

        social_api_ai_core_api_service_text_action = cls(
            texts=texts,
        )

        social_api_ai_core_api_service_text_action.additional_properties = d
        return social_api_ai_core_api_service_text_action

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
