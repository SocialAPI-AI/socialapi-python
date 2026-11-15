from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.social_api_ai_core_api_connectors_base_post_settings_audio_type import (
    SocialApiAiCoreApiConnectorsBasePostSettingsAudioType,
)
from ..models.social_api_ai_core_api_connectors_base_post_settings_product_type import (
    SocialApiAiCoreApiConnectorsBasePostSettingsProductType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.social_api_ai_core_api_connectors_base_post_child_attachment import (
        SocialApiAiCoreApiConnectorsBasePostChildAttachment,
    )
    from ..models.social_api_ai_core_api_connectors_base_post_place import SocialApiAiCoreApiConnectorsBasePostPlace


T = TypeVar("T", bound="SocialApiAiCoreApiConnectorsBasePostSettings")


@_attrs_define
class SocialApiAiCoreApiConnectorsBasePostSettings:
    """
    Attributes:
        alt_text (str | Unset): Image description set on the Instagram post.
        audio_type (SocialApiAiCoreApiConnectorsBasePostSettingsAudioType | Unset): Kind of audio on an Instagram Reel.
        child_attachments (list[SocialApiAiCoreApiConnectorsBasePostChildAttachment] | Unset): Cards of a Facebook
            multi-link post.
        comments_enabled (bool | Unset): True when comments are open on the Instagram post.
        countries (list[str] | Unset): ISO 3166-1 alpha-2 countries the Facebook post is restricted to. Example: ['FR',
            'BE'].
        cta_link (str | Unset): Call-to-action destination on the Facebook post.
        cta_type (str | Unset): Call-to-action button type on the Facebook post. Example: SHOP_NOW.
        is_ai_generated (bool | Unset): True when Instagram shows the AI info label on the post.
        max_age (int | Unset): Maximum audience age set on the Facebook post. Example: 65.
        min_age (int | Unset): Minimum audience age set on the Facebook post. Example: 18.
        multi_share_end_card (bool | Unset): True when the multi-link post shows an end card.
        multi_share_optimized (bool | Unset): True when Facebook picks the card order.
        place (SocialApiAiCoreApiConnectorsBasePostPlace | Unset):
        product_type (SocialApiAiCoreApiConnectorsBasePostSettingsProductType | Unset): Instagram surface the post lives
            on.
        share_to_feed (bool | Unset): True when an Instagram Reel also appears in the main profile feed.
    """

    alt_text: str | Unset = UNSET
    audio_type: SocialApiAiCoreApiConnectorsBasePostSettingsAudioType | Unset = UNSET
    child_attachments: list[SocialApiAiCoreApiConnectorsBasePostChildAttachment] | Unset = UNSET
    comments_enabled: bool | Unset = UNSET
    countries: list[str] | Unset = UNSET
    cta_link: str | Unset = UNSET
    cta_type: str | Unset = UNSET
    is_ai_generated: bool | Unset = UNSET
    max_age: int | Unset = UNSET
    min_age: int | Unset = UNSET
    multi_share_end_card: bool | Unset = UNSET
    multi_share_optimized: bool | Unset = UNSET
    place: SocialApiAiCoreApiConnectorsBasePostPlace | Unset = UNSET
    product_type: SocialApiAiCoreApiConnectorsBasePostSettingsProductType | Unset = UNSET
    share_to_feed: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        alt_text = self.alt_text

        audio_type: str | Unset = UNSET
        if not isinstance(self.audio_type, Unset):
            audio_type = self.audio_type.value

        child_attachments: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.child_attachments, Unset):
            child_attachments = []
            for child_attachments_item_data in self.child_attachments:
                child_attachments_item = child_attachments_item_data.to_dict()
                child_attachments.append(child_attachments_item)

        comments_enabled = self.comments_enabled

        countries: list[str] | Unset = UNSET
        if not isinstance(self.countries, Unset):
            countries = self.countries

        cta_link = self.cta_link

        cta_type = self.cta_type

        is_ai_generated = self.is_ai_generated

        max_age = self.max_age

        min_age = self.min_age

        multi_share_end_card = self.multi_share_end_card

        multi_share_optimized = self.multi_share_optimized

        place: dict[str, Any] | Unset = UNSET
        if not isinstance(self.place, Unset):
            place = self.place.to_dict()

        product_type: str | Unset = UNSET
        if not isinstance(self.product_type, Unset):
            product_type = self.product_type.value

        share_to_feed = self.share_to_feed

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if alt_text is not UNSET:
            field_dict["alt_text"] = alt_text
        if audio_type is not UNSET:
            field_dict["audio_type"] = audio_type
        if child_attachments is not UNSET:
            field_dict["child_attachments"] = child_attachments
        if comments_enabled is not UNSET:
            field_dict["comments_enabled"] = comments_enabled
        if countries is not UNSET:
            field_dict["countries"] = countries
        if cta_link is not UNSET:
            field_dict["cta_link"] = cta_link
        if cta_type is not UNSET:
            field_dict["cta_type"] = cta_type
        if is_ai_generated is not UNSET:
            field_dict["is_ai_generated"] = is_ai_generated
        if max_age is not UNSET:
            field_dict["max_age"] = max_age
        if min_age is not UNSET:
            field_dict["min_age"] = min_age
        if multi_share_end_card is not UNSET:
            field_dict["multi_share_end_card"] = multi_share_end_card
        if multi_share_optimized is not UNSET:
            field_dict["multi_share_optimized"] = multi_share_optimized
        if place is not UNSET:
            field_dict["place"] = place
        if product_type is not UNSET:
            field_dict["product_type"] = product_type
        if share_to_feed is not UNSET:
            field_dict["share_to_feed"] = share_to_feed

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.social_api_ai_core_api_connectors_base_post_child_attachment import (
            SocialApiAiCoreApiConnectorsBasePostChildAttachment,  # noqa: PLC0415
        )
        from ..models.social_api_ai_core_api_connectors_base_post_place import (
            SocialApiAiCoreApiConnectorsBasePostPlace,  # noqa: PLC0415
        )

        d = dict(src_dict)
        alt_text = d.pop("alt_text", UNSET)

        _audio_type = d.pop("audio_type", UNSET)
        audio_type: SocialApiAiCoreApiConnectorsBasePostSettingsAudioType | Unset
        if isinstance(_audio_type, Unset):
            audio_type = UNSET
        else:
            audio_type = SocialApiAiCoreApiConnectorsBasePostSettingsAudioType(_audio_type)

        _child_attachments = d.pop("child_attachments", UNSET)
        child_attachments: list[SocialApiAiCoreApiConnectorsBasePostChildAttachment] | Unset = UNSET
        if _child_attachments is not UNSET:
            child_attachments = []
            for child_attachments_item_data in _child_attachments:
                child_attachments_item = SocialApiAiCoreApiConnectorsBasePostChildAttachment.from_dict(
                    child_attachments_item_data
                )

                child_attachments.append(child_attachments_item)

        comments_enabled = d.pop("comments_enabled", UNSET)

        countries = cast(list[str], d.pop("countries", UNSET))

        cta_link = d.pop("cta_link", UNSET)

        cta_type = d.pop("cta_type", UNSET)

        is_ai_generated = d.pop("is_ai_generated", UNSET)

        max_age = d.pop("max_age", UNSET)

        min_age = d.pop("min_age", UNSET)

        multi_share_end_card = d.pop("multi_share_end_card", UNSET)

        multi_share_optimized = d.pop("multi_share_optimized", UNSET)

        _place = d.pop("place", UNSET)
        place: SocialApiAiCoreApiConnectorsBasePostPlace | Unset
        if isinstance(_place, Unset):
            place = UNSET
        else:
            place = SocialApiAiCoreApiConnectorsBasePostPlace.from_dict(_place)

        _product_type = d.pop("product_type", UNSET)
        product_type: SocialApiAiCoreApiConnectorsBasePostSettingsProductType | Unset
        if isinstance(_product_type, Unset):
            product_type = UNSET
        else:
            product_type = SocialApiAiCoreApiConnectorsBasePostSettingsProductType(_product_type)

        share_to_feed = d.pop("share_to_feed", UNSET)

        social_api_ai_core_api_connectors_base_post_settings = cls(
            alt_text=alt_text,
            audio_type=audio_type,
            child_attachments=child_attachments,
            comments_enabled=comments_enabled,
            countries=countries,
            cta_link=cta_link,
            cta_type=cta_type,
            is_ai_generated=is_ai_generated,
            max_age=max_age,
            min_age=min_age,
            multi_share_end_card=multi_share_end_card,
            multi_share_optimized=multi_share_optimized,
            place=place,
            product_type=product_type,
            share_to_feed=share_to_feed,
        )

        social_api_ai_core_api_connectors_base_post_settings.additional_properties = d
        return social_api_ai_core_api_connectors_base_post_settings

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
