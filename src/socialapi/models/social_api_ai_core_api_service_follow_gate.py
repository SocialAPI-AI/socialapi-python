from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SocialApiAiCoreApiServiceFollowGate")


@_attrs_define
class SocialApiAiCoreApiServiceFollowGate:
    """
    Attributes:
        button_title (str | Unset): Up to 20 characters Example: Get the link.
        keywords (list[str] | Unset): Comment keywords that open the gate Example: ['link'].
        link_texts (list[str] | Unset): Sent once the person follows Example: ['Here you go: https://example.com'].
        not_following_texts (list[str] | Unset): Sent when the person does not follow the account yet Example: ['Follow
            us first and tap again'].
        opening_texts (list[str] | Unset): Private reply sent to the commenter Example: ['Tap below to get the link'].
        retry_button_title (str | Unset): Up to 20 characters Example: I followed.
    """

    button_title: str | Unset = UNSET
    keywords: list[str] | Unset = UNSET
    link_texts: list[str] | Unset = UNSET
    not_following_texts: list[str] | Unset = UNSET
    opening_texts: list[str] | Unset = UNSET
    retry_button_title: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        button_title = self.button_title

        keywords: list[str] | Unset = UNSET
        if not isinstance(self.keywords, Unset):
            keywords = self.keywords

        link_texts: list[str] | Unset = UNSET
        if not isinstance(self.link_texts, Unset):
            link_texts = self.link_texts

        not_following_texts: list[str] | Unset = UNSET
        if not isinstance(self.not_following_texts, Unset):
            not_following_texts = self.not_following_texts

        opening_texts: list[str] | Unset = UNSET
        if not isinstance(self.opening_texts, Unset):
            opening_texts = self.opening_texts

        retry_button_title = self.retry_button_title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if button_title is not UNSET:
            field_dict["button_title"] = button_title
        if keywords is not UNSET:
            field_dict["keywords"] = keywords
        if link_texts is not UNSET:
            field_dict["link_texts"] = link_texts
        if not_following_texts is not UNSET:
            field_dict["not_following_texts"] = not_following_texts
        if opening_texts is not UNSET:
            field_dict["opening_texts"] = opening_texts
        if retry_button_title is not UNSET:
            field_dict["retry_button_title"] = retry_button_title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        button_title = d.pop("button_title", UNSET)

        keywords = cast(list[str], d.pop("keywords", UNSET))

        link_texts = cast(list[str], d.pop("link_texts", UNSET))

        not_following_texts = cast(list[str], d.pop("not_following_texts", UNSET))

        opening_texts = cast(list[str], d.pop("opening_texts", UNSET))

        retry_button_title = d.pop("retry_button_title", UNSET)

        social_api_ai_core_api_service_follow_gate = cls(
            button_title=button_title,
            keywords=keywords,
            link_texts=link_texts,
            not_following_texts=not_following_texts,
            opening_texts=opening_texts,
            retry_button_title=retry_button_title,
        )

        social_api_ai_core_api_service_follow_gate.additional_properties = d
        return social_api_ai_core_api_service_follow_gate

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
