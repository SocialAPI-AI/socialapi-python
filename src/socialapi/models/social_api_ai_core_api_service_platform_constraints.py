from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.social_api_ai_core_api_service_carousel_constraints import (
        SocialApiAiCoreApiServiceCarouselConstraints,
    )
    from ..models.social_api_ai_core_api_service_media_constraints import SocialApiAiCoreApiServiceMediaConstraints
    from ..models.social_api_ai_core_api_service_scheduling_constraints import (
        SocialApiAiCoreApiServiceSchedulingConstraints,
    )
    from ..models.social_api_ai_core_api_service_text_constraints import SocialApiAiCoreApiServiceTextConstraints


T = TypeVar("T", bound="SocialApiAiCoreApiServicePlatformConstraints")


@_attrs_define
class SocialApiAiCoreApiServicePlatformConstraints:
    """
    Attributes:
        carousel (SocialApiAiCoreApiServiceCarouselConstraints | Unset):
        media (SocialApiAiCoreApiServiceMediaConstraints | Unset):
        scheduling (SocialApiAiCoreApiServiceSchedulingConstraints | Unset):
        supports_mixed_media (bool | Unset): SupportsMixedMedia reports whether a platform_attachment_id item may be
            combined with other media (url/media_id) in the same post. When false
            (instagram, threads) a platform_attachment_id must be the only media item.
            Meaningful only when SupportsPlatformAttachmentID is true.
        supports_platform_attachment_id (bool | Unset):
        text (SocialApiAiCoreApiServiceTextConstraints | Unset):
    """

    carousel: SocialApiAiCoreApiServiceCarouselConstraints | Unset = UNSET
    media: SocialApiAiCoreApiServiceMediaConstraints | Unset = UNSET
    scheduling: SocialApiAiCoreApiServiceSchedulingConstraints | Unset = UNSET
    supports_mixed_media: bool | Unset = UNSET
    supports_platform_attachment_id: bool | Unset = UNSET
    text: SocialApiAiCoreApiServiceTextConstraints | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        carousel: dict[str, Any] | Unset = UNSET
        if not isinstance(self.carousel, Unset):
            carousel = self.carousel.to_dict()

        media: dict[str, Any] | Unset = UNSET
        if not isinstance(self.media, Unset):
            media = self.media.to_dict()

        scheduling: dict[str, Any] | Unset = UNSET
        if not isinstance(self.scheduling, Unset):
            scheduling = self.scheduling.to_dict()

        supports_mixed_media = self.supports_mixed_media

        supports_platform_attachment_id = self.supports_platform_attachment_id

        text: dict[str, Any] | Unset = UNSET
        if not isinstance(self.text, Unset):
            text = self.text.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if carousel is not UNSET:
            field_dict["carousel"] = carousel
        if media is not UNSET:
            field_dict["media"] = media
        if scheduling is not UNSET:
            field_dict["scheduling"] = scheduling
        if supports_mixed_media is not UNSET:
            field_dict["supports_mixed_media"] = supports_mixed_media
        if supports_platform_attachment_id is not UNSET:
            field_dict["supports_platform_attachment_id"] = supports_platform_attachment_id
        if text is not UNSET:
            field_dict["text"] = text

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.social_api_ai_core_api_service_carousel_constraints import (
            SocialApiAiCoreApiServiceCarouselConstraints,  # noqa: PLC0415
        )
        from ..models.social_api_ai_core_api_service_media_constraints import (
            SocialApiAiCoreApiServiceMediaConstraints,  # noqa: PLC0415
        )
        from ..models.social_api_ai_core_api_service_scheduling_constraints import (
            SocialApiAiCoreApiServiceSchedulingConstraints,  # noqa: PLC0415
        )
        from ..models.social_api_ai_core_api_service_text_constraints import (
            SocialApiAiCoreApiServiceTextConstraints,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _carousel = d.pop("carousel", UNSET)
        carousel: SocialApiAiCoreApiServiceCarouselConstraints | Unset
        if isinstance(_carousel, Unset):
            carousel = UNSET
        else:
            carousel = SocialApiAiCoreApiServiceCarouselConstraints.from_dict(_carousel)

        _media = d.pop("media", UNSET)
        media: SocialApiAiCoreApiServiceMediaConstraints | Unset
        if isinstance(_media, Unset):
            media = UNSET
        else:
            media = SocialApiAiCoreApiServiceMediaConstraints.from_dict(_media)

        _scheduling = d.pop("scheduling", UNSET)
        scheduling: SocialApiAiCoreApiServiceSchedulingConstraints | Unset
        if isinstance(_scheduling, Unset):
            scheduling = UNSET
        else:
            scheduling = SocialApiAiCoreApiServiceSchedulingConstraints.from_dict(_scheduling)

        supports_mixed_media = d.pop("supports_mixed_media", UNSET)

        supports_platform_attachment_id = d.pop("supports_platform_attachment_id", UNSET)

        _text = d.pop("text", UNSET)
        text: SocialApiAiCoreApiServiceTextConstraints | Unset
        if isinstance(_text, Unset):
            text = UNSET
        else:
            text = SocialApiAiCoreApiServiceTextConstraints.from_dict(_text)

        social_api_ai_core_api_service_platform_constraints = cls(
            carousel=carousel,
            media=media,
            scheduling=scheduling,
            supports_mixed_media=supports_mixed_media,
            supports_platform_attachment_id=supports_platform_attachment_id,
            text=text,
        )

        social_api_ai_core_api_service_platform_constraints.additional_properties = d
        return social_api_ai_core_api_service_platform_constraints

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
