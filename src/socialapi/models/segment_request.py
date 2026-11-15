from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.media_input import MediaInput


T = TypeVar("T", bound="SegmentRequest")


@_attrs_define
class SegmentRequest:
    """
    Attributes:
        text (str): Text is the post body for this segment. Required. Example: And here's the second post in the
            thread..
        media (list[MediaInput] | Unset): Media is the ordered, agnostic media list. Each item is a url, a media_id,
            or a platform_attachment_id; order and mixing are preserved. Supersedes media_ids.
            Currently ignored: X drops segment media, and Threads chaining is temporarily unavailable.
        media_ids (list[str] | Unset): MediaIDs attach media to this segment.

            Deprecated: use Media with source_type "media_id". Ignored when media is set.
    """

    text: str
    media: list[MediaInput] | Unset = UNSET
    media_ids: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        text = self.text

        media: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.media, Unset):
            media = []
            for media_item_data in self.media:
                media_item = media_item_data.to_dict()
                media.append(media_item)

        media_ids: list[str] | Unset = UNSET
        if not isinstance(self.media_ids, Unset):
            media_ids = self.media_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "text": text,
            }
        )
        if media is not UNSET:
            field_dict["media"] = media
        if media_ids is not UNSET:
            field_dict["media_ids"] = media_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.media_input import MediaInput  # noqa: PLC0415

        d = dict(src_dict)
        text = d.pop("text")

        _media = d.pop("media", UNSET)
        media: list[MediaInput] | Unset = UNSET
        if _media is not UNSET:
            media = []
            for media_item_data in _media:
                media_item = MediaInput.from_dict(media_item_data)

                media.append(media_item)

        media_ids = cast(list[str], d.pop("media_ids", UNSET))

        segment_request = cls(
            text=text,
            media=media,
            media_ids=media_ids,
        )

        segment_request.additional_properties = d
        return segment_request

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
