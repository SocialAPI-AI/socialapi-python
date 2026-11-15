from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.social_api_ai_core_api_connectors_base_interaction_settings import (
        SocialApiAiCoreApiConnectorsBaseInteractionSettings,
    )


T = TypeVar("T", bound="ApiEndpointsCreatorInfoResponse")


@_attrs_define
class ApiEndpointsCreatorInfoResponse:
    """
    Attributes:
        avatar_url (str | Unset): [platform: tiktok] Empty on other platforms
        can_post (bool | Unset): [platform: tiktok] Always false on other platforms
        interaction_settings (SocialApiAiCoreApiConnectorsBaseInteractionSettings | Unset):
        max_video_duration_sec (int | Unset): [platform: tiktok] Zero on other platforms
        nickname (str | Unset): [platform: tiktok] Empty on other platforms
        platform (str | Unset): [always]
        privacy_level_options (list[str] | Unset): [platform: tiktok] Nil on other platforms
    """

    avatar_url: str | Unset = UNSET
    can_post: bool | Unset = UNSET
    interaction_settings: SocialApiAiCoreApiConnectorsBaseInteractionSettings | Unset = UNSET
    max_video_duration_sec: int | Unset = UNSET
    nickname: str | Unset = UNSET
    platform: str | Unset = UNSET
    privacy_level_options: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        avatar_url = self.avatar_url

        can_post = self.can_post

        interaction_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.interaction_settings, Unset):
            interaction_settings = self.interaction_settings.to_dict()

        max_video_duration_sec = self.max_video_duration_sec

        nickname = self.nickname

        platform = self.platform

        privacy_level_options: list[str] | Unset = UNSET
        if not isinstance(self.privacy_level_options, Unset):
            privacy_level_options = self.privacy_level_options

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if avatar_url is not UNSET:
            field_dict["avatar_url"] = avatar_url
        if can_post is not UNSET:
            field_dict["can_post"] = can_post
        if interaction_settings is not UNSET:
            field_dict["interaction_settings"] = interaction_settings
        if max_video_duration_sec is not UNSET:
            field_dict["max_video_duration_sec"] = max_video_duration_sec
        if nickname is not UNSET:
            field_dict["nickname"] = nickname
        if platform is not UNSET:
            field_dict["platform"] = platform
        if privacy_level_options is not UNSET:
            field_dict["privacy_level_options"] = privacy_level_options

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.social_api_ai_core_api_connectors_base_interaction_settings import (
            SocialApiAiCoreApiConnectorsBaseInteractionSettings,  # noqa: PLC0415
        )

        d = dict(src_dict)
        avatar_url = d.pop("avatar_url", UNSET)

        can_post = d.pop("can_post", UNSET)

        _interaction_settings = d.pop("interaction_settings", UNSET)
        interaction_settings: SocialApiAiCoreApiConnectorsBaseInteractionSettings | Unset
        if isinstance(_interaction_settings, Unset):
            interaction_settings = UNSET
        else:
            interaction_settings = SocialApiAiCoreApiConnectorsBaseInteractionSettings.from_dict(_interaction_settings)

        max_video_duration_sec = d.pop("max_video_duration_sec", UNSET)

        nickname = d.pop("nickname", UNSET)

        platform = d.pop("platform", UNSET)

        privacy_level_options = cast(list[str], d.pop("privacy_level_options", UNSET))

        api_endpoints_creator_info_response = cls(
            avatar_url=avatar_url,
            can_post=can_post,
            interaction_settings=interaction_settings,
            max_video_duration_sec=max_video_duration_sec,
            nickname=nickname,
            platform=platform,
            privacy_level_options=privacy_level_options,
        )

        api_endpoints_creator_info_response.additional_properties = d
        return api_endpoints_creator_info_response

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
