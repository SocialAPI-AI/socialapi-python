from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.media_file_type import MediaFileType
from ..models.media_source_type import MediaSourceType
from ..types import UNSET, Unset

T = TypeVar("T", bound="DMAttachmentInput")


@_attrs_define
class DMAttachmentInput:
    """
    Attributes:
        source (str): Source is the attachment reference; its meaning is given by source_type. Example:
            550e8400-e29b-41d4-a716-446655440000.
        source_type (MediaSourceType):
        caption (str | Unset): Caption is text shown with this attachment instead of as a separate message.
            Supported on WhatsApp (not on audio) and Telegram; ignored on platforms whose
            Send API has no caption, where an attachment is always a bare bubble. Example: The damaged panel.
        type_ (MediaFileType | Unset):
        voice (bool | Unset): Voice sends an audio attachment as a native voice note (waveform and
            playback-speed controls) instead of a file bubble. WhatsApp only, and only
            for audio whose file is Ogg encoded with the OPUS codec; WhatsApp rejects
            any other container or codec. Ignored on other platforms. Example: True.
    """

    source: str
    source_type: MediaSourceType
    caption: str | Unset = UNSET
    type_: MediaFileType | Unset = UNSET
    voice: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        source = self.source

        source_type = self.source_type.value

        caption = self.caption

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        voice = self.voice

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "source": source,
                "source_type": source_type,
            }
        )
        if caption is not UNSET:
            field_dict["caption"] = caption
        if type_ is not UNSET:
            field_dict["type"] = type_
        if voice is not UNSET:
            field_dict["voice"] = voice

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        source = d.pop("source")

        source_type = MediaSourceType(d.pop("source_type"))

        caption = d.pop("caption", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: MediaFileType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = MediaFileType(_type_)

        voice = d.pop("voice", UNSET)

        dm_attachment_input = cls(
            source=source,
            source_type=source_type,
            caption=caption,
            type_=type_,
            voice=voice,
        )

        dm_attachment_input.additional_properties = d
        return dm_attachment_input

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
