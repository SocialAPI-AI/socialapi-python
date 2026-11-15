from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.carousel_constraints import CarouselConstraints
    from ..models.media_constraints import MediaConstraints
    from ..models.scheduling_constraints import SchedulingConstraints
    from ..models.text_constraints import TextConstraints


T = TypeVar("T", bound="PlatformConstraints")


@_attrs_define
class PlatformConstraints:
    """
    Attributes:
        carousel (CarouselConstraints):
        media (MediaConstraints):
        scheduling (SchedulingConstraints):
        supports_mixed_media (bool): SupportsMixedMedia reports whether a platform_attachment_id item may be
            combined with other media (url/media_id) in the same post. When false
            (instagram, threads) a platform_attachment_id must be the only media item.
            Meaningful only when SupportsPlatformAttachmentID is true.
        supports_platform_attachment_id (bool):
        text (TextConstraints):
    """

    carousel: CarouselConstraints
    media: MediaConstraints
    scheduling: SchedulingConstraints
    supports_mixed_media: bool
    supports_platform_attachment_id: bool
    text: TextConstraints
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        carousel = self.carousel.to_dict()

        media = self.media.to_dict()

        scheduling = self.scheduling.to_dict()

        supports_mixed_media = self.supports_mixed_media

        supports_platform_attachment_id = self.supports_platform_attachment_id

        text = self.text.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "carousel": carousel,
                "media": media,
                "scheduling": scheduling,
                "supports_mixed_media": supports_mixed_media,
                "supports_platform_attachment_id": supports_platform_attachment_id,
                "text": text,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.carousel_constraints import CarouselConstraints  # noqa: PLC0415
        from ..models.media_constraints import MediaConstraints  # noqa: PLC0415
        from ..models.scheduling_constraints import SchedulingConstraints  # noqa: PLC0415
        from ..models.text_constraints import TextConstraints  # noqa: PLC0415

        d = dict(src_dict)
        carousel = CarouselConstraints.from_dict(d.pop("carousel"))

        media = MediaConstraints.from_dict(d.pop("media"))

        scheduling = SchedulingConstraints.from_dict(d.pop("scheduling"))

        supports_mixed_media = d.pop("supports_mixed_media")

        supports_platform_attachment_id = d.pop("supports_platform_attachment_id")

        text = TextConstraints.from_dict(d.pop("text"))

        platform_constraints = cls(
            carousel=carousel,
            media=media,
            scheduling=scheduling,
            supports_mixed_media=supports_mixed_media,
            supports_platform_attachment_id=supports_platform_attachment_id,
            text=text,
        )

        platform_constraints.additional_properties = d
        return platform_constraints

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
