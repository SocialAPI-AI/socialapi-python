from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GoogleMediaAttribution")


@_attrs_define
class GoogleMediaAttribution:
    """
    Attributes:
        profile_name (str | Unset):  Example: Jane S..
        profile_photo_url (str | Unset):
        profile_url (str | Unset):
        takedown_url (str | Unset):
    """

    profile_name: str | Unset = UNSET
    profile_photo_url: str | Unset = UNSET
    profile_url: str | Unset = UNSET
    takedown_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        profile_name = self.profile_name

        profile_photo_url = self.profile_photo_url

        profile_url = self.profile_url

        takedown_url = self.takedown_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if profile_name is not UNSET:
            field_dict["profile_name"] = profile_name
        if profile_photo_url is not UNSET:
            field_dict["profile_photo_url"] = profile_photo_url
        if profile_url is not UNSET:
            field_dict["profile_url"] = profile_url
        if takedown_url is not UNSET:
            field_dict["takedown_url"] = takedown_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        profile_name = d.pop("profile_name", UNSET)

        profile_photo_url = d.pop("profile_photo_url", UNSET)

        profile_url = d.pop("profile_url", UNSET)

        takedown_url = d.pop("takedown_url", UNSET)

        google_media_attribution = cls(
            profile_name=profile_name,
            profile_photo_url=profile_photo_url,
            profile_url=profile_url,
            takedown_url=takedown_url,
        )

        google_media_attribution.additional_properties = d
        return google_media_attribution

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
