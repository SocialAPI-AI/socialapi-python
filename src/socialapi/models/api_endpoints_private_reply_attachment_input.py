from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.api_endpoints_private_reply_attachment_input_source_type import (
    ApiEndpointsPrivateReplyAttachmentInputSourceType,
)
from ..models.api_endpoints_private_reply_attachment_input_type import ApiEndpointsPrivateReplyAttachmentInputType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiEndpointsPrivateReplyAttachmentInput")


@_attrs_define
class ApiEndpointsPrivateReplyAttachmentInput:
    """
    Attributes:
        source (str | Unset): Source is the attachment reference; its meaning is given by source_type. Example:
            https://cdn.example.com/guide.pdf.
        source_type (ApiEndpointsPrivateReplyAttachmentInputSourceType | Unset): SourceType selects how Source is
            interpreted:
              - "url": Source is a publicly reachable media URL the platform fetches directly.
              - "media_id": Source is a file id in your SocialAPI media library
                (GET /v1/media).
              - "platform_attachment_id": Source is an id of media already uploaded to the
                target platform (for example a Meta attachment_id). Example: url.
        type_ (ApiEndpointsPrivateReplyAttachmentInputType | Unset): Type is the media kind. Optional for url and
            media_id sources (inferred from
            the file), required for platform_attachment_id. Example: file.
    """

    source: str | Unset = UNSET
    source_type: ApiEndpointsPrivateReplyAttachmentInputSourceType | Unset = UNSET
    type_: ApiEndpointsPrivateReplyAttachmentInputType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        source = self.source

        source_type: str | Unset = UNSET
        if not isinstance(self.source_type, Unset):
            source_type = self.source_type.value

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if source is not UNSET:
            field_dict["source"] = source
        if source_type is not UNSET:
            field_dict["source_type"] = source_type
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        source = d.pop("source", UNSET)

        _source_type = d.pop("source_type", UNSET)
        source_type: ApiEndpointsPrivateReplyAttachmentInputSourceType | Unset
        if isinstance(_source_type, Unset):
            source_type = UNSET
        else:
            source_type = ApiEndpointsPrivateReplyAttachmentInputSourceType(_source_type)

        _type_ = d.pop("type", UNSET)
        type_: ApiEndpointsPrivateReplyAttachmentInputType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = ApiEndpointsPrivateReplyAttachmentInputType(_type_)

        api_endpoints_private_reply_attachment_input = cls(
            source=source,
            source_type=source_type,
            type_=type_,
        )

        api_endpoints_private_reply_attachment_input.additional_properties = d
        return api_endpoints_private_reply_attachment_input

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
