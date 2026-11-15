from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.platform import Platform
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.interaction_settings import InteractionSettings


T = TypeVar("T", bound="CreatorInfoResponse")


@_attrs_define
class CreatorInfoResponse:
    """
    Attributes:
        avatar_url (str): [platform: tiktok] Empty on other platforms
        can_post (bool): [platform: tiktok] Always false on other platforms
        nickname (str): [platform: tiktok] Empty on other platforms
        platform (Platform):
        interaction_settings (InteractionSettings | Unset):
        max_video_duration_sec (int | Unset): [platform: tiktok] Zero on other platforms
        privacy_level_options (list[str] | Unset): [platform: tiktok] Nil on other platforms
    """

    avatar_url: str
    can_post: bool
    nickname: str
    platform: Platform
    interaction_settings: InteractionSettings | Unset = UNSET
    max_video_duration_sec: int | Unset = UNSET
    privacy_level_options: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        avatar_url = self.avatar_url

        can_post = self.can_post

        nickname = self.nickname

        platform = self.platform.value

        interaction_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.interaction_settings, Unset):
            interaction_settings = self.interaction_settings.to_dict()

        max_video_duration_sec = self.max_video_duration_sec

        privacy_level_options: list[str] | Unset = UNSET
        if not isinstance(self.privacy_level_options, Unset):
            privacy_level_options = self.privacy_level_options

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "avatar_url": avatar_url,
                "can_post": can_post,
                "nickname": nickname,
                "platform": platform,
            }
        )
        if interaction_settings is not UNSET:
            field_dict["interaction_settings"] = interaction_settings
        if max_video_duration_sec is not UNSET:
            field_dict["max_video_duration_sec"] = max_video_duration_sec
        if privacy_level_options is not UNSET:
            field_dict["privacy_level_options"] = privacy_level_options

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.interaction_settings import InteractionSettings  # noqa: PLC0415

        d = dict(src_dict)
        avatar_url = d.pop("avatar_url")

        can_post = d.pop("can_post")

        nickname = d.pop("nickname")

        platform = Platform(d.pop("platform"))

        _interaction_settings = d.pop("interaction_settings", UNSET)
        interaction_settings: InteractionSettings | Unset
        if isinstance(_interaction_settings, Unset):
            interaction_settings = UNSET
        else:
            interaction_settings = InteractionSettings.from_dict(_interaction_settings)

        max_video_duration_sec = d.pop("max_video_duration_sec", UNSET)

        privacy_level_options = cast(list[str], d.pop("privacy_level_options", UNSET))

        creator_info_response = cls(
            avatar_url=avatar_url,
            can_post=can_post,
            nickname=nickname,
            platform=platform,
            interaction_settings=interaction_settings,
            max_video_duration_sec=max_video_duration_sec,
            privacy_level_options=privacy_level_options,
        )

        creator_info_response.additional_properties = d
        return creator_info_response

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
