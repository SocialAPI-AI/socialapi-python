from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.media_file_type import MediaFileType
from ..models.media_source_type import MediaSourceType
from ..types import UNSET, Unset

T = TypeVar("T", bound="PrivateReplyAttachmentInput")


@_attrs_define
class PrivateReplyAttachmentInput:
    """
    Attributes:
        source (str): Source is the attachment reference; its meaning is given by source_type. Example:
            https://cdn.example.com/guide.pdf.
        source_type (MediaSourceType):
        type_ (MediaFileType | Unset):
    """

    source: str
    source_type: MediaSourceType
    type_: MediaFileType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        source = self.source

        source_type = self.source_type.value

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

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

        _type_ = d.pop("type", UNSET)
        type_: MediaFileType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = MediaFileType(_type_)

        private_reply_attachment_input = cls(
            source=source,
            source_type=source_type,
            type_=type_,
        )

        private_reply_attachment_input.additional_properties = d
        return private_reply_attachment_input

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
