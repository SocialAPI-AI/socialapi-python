from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InstagramParticipantProfileResponse")


@_attrs_define
class InstagramParticipantProfileResponse:
    """
    Attributes:
        id (str):
        follower_count (int | Unset):
        is_business_follow_user (bool | Unset):
        is_user_follow_business (bool | Unset):
        is_verified_user (bool | Unset):
        name (str | Unset):
        profile_pic (str | Unset): ProfilePic URLs expire after a few days; never persist one as durable.
        username (str | Unset):
    """

    id: str
    follower_count: int | Unset = UNSET
    is_business_follow_user: bool | Unset = UNSET
    is_user_follow_business: bool | Unset = UNSET
    is_verified_user: bool | Unset = UNSET
    name: str | Unset = UNSET
    profile_pic: str | Unset = UNSET
    username: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        follower_count = self.follower_count

        is_business_follow_user = self.is_business_follow_user

        is_user_follow_business = self.is_user_follow_business

        is_verified_user = self.is_verified_user

        name = self.name

        profile_pic = self.profile_pic

        username = self.username

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if follower_count is not UNSET:
            field_dict["follower_count"] = follower_count
        if is_business_follow_user is not UNSET:
            field_dict["is_business_follow_user"] = is_business_follow_user
        if is_user_follow_business is not UNSET:
            field_dict["is_user_follow_business"] = is_user_follow_business
        if is_verified_user is not UNSET:
            field_dict["is_verified_user"] = is_verified_user
        if name is not UNSET:
            field_dict["name"] = name
        if profile_pic is not UNSET:
            field_dict["profile_pic"] = profile_pic
        if username is not UNSET:
            field_dict["username"] = username

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        follower_count = d.pop("follower_count", UNSET)

        is_business_follow_user = d.pop("is_business_follow_user", UNSET)

        is_user_follow_business = d.pop("is_user_follow_business", UNSET)

        is_verified_user = d.pop("is_verified_user", UNSET)

        name = d.pop("name", UNSET)

        profile_pic = d.pop("profile_pic", UNSET)

        username = d.pop("username", UNSET)

        instagram_participant_profile_response = cls(
            id=id,
            follower_count=follower_count,
            is_business_follow_user=is_business_follow_user,
            is_user_follow_business=is_user_follow_business,
            is_verified_user=is_verified_user,
            name=name,
            profile_pic=profile_pic,
            username=username,
        )

        instagram_participant_profile_response.additional_properties = d
        return instagram_participant_profile_response

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
