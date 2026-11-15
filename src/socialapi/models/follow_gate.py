from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="FollowGate")


@_attrs_define
class FollowGate:
    """
    Attributes:
        button_title (str): Up to 20 characters Example: Get the link.
        keywords (list[str]): Comment keywords that open the gate Example: ['link'].
        link_texts (list[str]): Sent once the person follows Example: ['Here you go: https://example.com'].
        not_following_texts (list[str]): Sent when the person does not follow the account yet Example: ['Follow us first
            and tap again'].
        opening_texts (list[str]): Private reply sent to the commenter Example: ['Tap below to get the link'].
        retry_button_title (str): Up to 20 characters Example: I followed.
    """

    button_title: str
    keywords: list[str]
    link_texts: list[str]
    not_following_texts: list[str]
    opening_texts: list[str]
    retry_button_title: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        button_title = self.button_title

        keywords = self.keywords

        link_texts = self.link_texts

        not_following_texts = self.not_following_texts

        opening_texts = self.opening_texts

        retry_button_title = self.retry_button_title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "button_title": button_title,
                "keywords": keywords,
                "link_texts": link_texts,
                "not_following_texts": not_following_texts,
                "opening_texts": opening_texts,
                "retry_button_title": retry_button_title,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        button_title = d.pop("button_title")

        keywords = cast(list[str], d.pop("keywords"))

        link_texts = cast(list[str], d.pop("link_texts"))

        not_following_texts = cast(list[str], d.pop("not_following_texts"))

        opening_texts = cast(list[str], d.pop("opening_texts"))

        retry_button_title = d.pop("retry_button_title")

        follow_gate = cls(
            button_title=button_title,
            keywords=keywords,
            link_texts=link_texts,
            not_following_texts=not_following_texts,
            opening_texts=opening_texts,
            retry_button_title=retry_button_title,
        )

        follow_gate.additional_properties = d
        return follow_gate

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
