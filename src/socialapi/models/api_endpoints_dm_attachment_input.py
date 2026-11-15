from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.api_endpoints_dm_attachment_input_source_type import ApiEndpointsDMAttachmentInputSourceType
from ..models.api_endpoints_dm_attachment_input_type import ApiEndpointsDMAttachmentInputType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiEndpointsDMAttachmentInput")


@_attrs_define
class ApiEndpointsDMAttachmentInput:
    """
    Attributes:
        caption (str | Unset): Caption is text shown with this attachment instead of as a separate message.
            Supported on WhatsApp (not on audio) and Telegram; ignored on platforms whose
            Send API has no caption, where an attachment is always a bare bubble. Example: The damaged panel.
        source (str | Unset): Source is the attachment reference; its meaning is given by source_type. Example:
            550e8400-e29b-41d4-a716-446655440000.
        source_type (ApiEndpointsDMAttachmentInputSourceType | Unset): SourceType selects how Source is interpreted:
              - "url": Source is a publicly reachable media URL the platform fetches directly.
              - "media_id": Source is a file id in your SocialAPI media library
                (GET /v1/media).
              - "platform_attachment_id": Source is an id of media already uploaded to the
                target platform (for example a Meta attachment_id) to reuse without re-upload. Example: media_id.
        type_ (ApiEndpointsDMAttachmentInputType | Unset): Type is the media kind. Optional for url and media_id sources
            (inferred from
            the file), required for platform_attachment_id (the platform exposes no URL
            to infer from). Example: image.
        voice (bool | Unset): Voice sends an audio attachment as a native voice note (waveform and
            playback-speed controls) instead of a file bubble. WhatsApp only, and only
            for audio whose file is Ogg encoded with the OPUS codec; WhatsApp rejects
            any other container or codec. Ignored on other platforms. Example: True.
    """

    caption: str | Unset = UNSET
    source: str | Unset = UNSET
    source_type: ApiEndpointsDMAttachmentInputSourceType | Unset = UNSET
    type_: ApiEndpointsDMAttachmentInputType | Unset = UNSET
    voice: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        caption = self.caption

        source = self.source

        source_type: str | Unset = UNSET
        if not isinstance(self.source_type, Unset):
            source_type = self.source_type.value

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        voice = self.voice

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if caption is not UNSET:
            field_dict["caption"] = caption
        if source is not UNSET:
            field_dict["source"] = source
        if source_type is not UNSET:
            field_dict["source_type"] = source_type
        if type_ is not UNSET:
            field_dict["type"] = type_
        if voice is not UNSET:
            field_dict["voice"] = voice

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        caption = d.pop("caption", UNSET)

        source = d.pop("source", UNSET)

        _source_type = d.pop("source_type", UNSET)
        source_type: ApiEndpointsDMAttachmentInputSourceType | Unset
        if isinstance(_source_type, Unset):
            source_type = UNSET
        else:
            source_type = ApiEndpointsDMAttachmentInputSourceType(_source_type)

        _type_ = d.pop("type", UNSET)
        type_: ApiEndpointsDMAttachmentInputType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = ApiEndpointsDMAttachmentInputType(_type_)

        voice = d.pop("voice", UNSET)

        api_endpoints_dm_attachment_input = cls(
            caption=caption,
            source=source,
            source_type=source_type,
            type_=type_,
            voice=voice,
        )

        api_endpoints_dm_attachment_input.additional_properties = d
        return api_endpoints_dm_attachment_input

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
