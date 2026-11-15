from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.social_api_ai_core_api_service_step_button_type import SocialApiAiCoreApiServiceStepButtonType
from ..types import UNSET, Unset

T = TypeVar("T", bound="SocialApiAiCoreApiServiceStepButton")


@_attrs_define
class SocialApiAiCoreApiServiceStepButton:
    """
    Attributes:
        next_step (str | Unset): Key of the Step to run when this button is tapped. Required when type is postback
            Example: check.
        title (str | Unset): Up to 20 characters Example: Open.
        type_ (SocialApiAiCoreApiServiceStepButtonType | Unset):  Example: url.
        url (str | Unset): An http or https URL. Required when type is url Example: https://example.com.
    """

    next_step: str | Unset = UNSET
    title: str | Unset = UNSET
    type_: SocialApiAiCoreApiServiceStepButtonType | Unset = UNSET
    url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        next_step = self.next_step

        title = self.title

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if next_step is not UNSET:
            field_dict["next_step"] = next_step
        if title is not UNSET:
            field_dict["title"] = title
        if type_ is not UNSET:
            field_dict["type"] = type_
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        next_step = d.pop("next_step", UNSET)

        title = d.pop("title", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: SocialApiAiCoreApiServiceStepButtonType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = SocialApiAiCoreApiServiceStepButtonType(_type_)

        url = d.pop("url", UNSET)

        social_api_ai_core_api_service_step_button = cls(
            next_step=next_step,
            title=title,
            type_=type_,
            url=url,
        )

        social_api_ai_core_api_service_step_button.additional_properties = d
        return social_api_ai_core_api_service_step_button

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
