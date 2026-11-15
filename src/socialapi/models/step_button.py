from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.step_button_type import StepButtonType
from ..types import UNSET, Unset

T = TypeVar("T", bound="StepButton")


@_attrs_define
class StepButton:
    """
    Attributes:
        title (str): Up to 20 characters Example: Open.
        type_ (StepButtonType):
        next_step (str | Unset): Key of the Step to run when this button is tapped. Required when type is postback
            Example: check.
        url (str | Unset): An http or https URL. Required when type is url Example: https://example.com.
    """

    title: str
    type_: StepButtonType
    next_step: str | Unset = UNSET
    url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        type_ = self.type_.value

        next_step = self.next_step

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
                "type": type_,
            }
        )
        if next_step is not UNSET:
            field_dict["next_step"] = next_step
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        title = d.pop("title")

        type_ = StepButtonType(d.pop("type"))

        next_step = d.pop("next_step", UNSET)

        url = d.pop("url", UNSET)

        step_button = cls(
            title=title,
            type_=type_,
            next_step=next_step,
            url=url,
        )

        step_button.additional_properties = d
        return step_button

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
