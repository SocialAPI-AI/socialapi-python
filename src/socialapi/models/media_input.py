from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.media_source_type import MediaSourceType
from ..types import UNSET, Unset

T = TypeVar("T", bound="MediaInput")


@_attrs_define
class MediaInput:
    """
    Attributes:
        source (str):  Example: 550e8400-e29b-41d4-a716-446655440000.
        source_type (MediaSourceType):
        type_ (str | Unset): The kind of file: image, video, audio or file. Example: image.
    """

    source: str
    source_type: MediaSourceType
    type_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        source = self.source

        source_type = self.source_type.value

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "source": source,
                "source_type": source_type,
            }
        )
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        source = d.pop("source")

        source_type = MediaSourceType(d.pop("source_type"))

        type_ = d.pop("type", UNSET)

        media_input = cls(
            source=source,
            source_type=source_type,
            type_=type_,
        )

        media_input.additional_properties = d
        return media_input

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
