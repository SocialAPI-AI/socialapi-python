from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiEndpointsModerateYouTubeCommentRequest")


@_attrs_define
class ApiEndpointsModerateYouTubeCommentRequest:
    """
    Attributes:
        account_id (str | Unset):
        ban_author (bool | Unset):
        post_id (str | Unset):
        status (str | Unset):
    """

    account_id: str | Unset = UNSET
    ban_author: bool | Unset = UNSET
    post_id: str | Unset = UNSET
    status: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_id = self.account_id

        ban_author = self.ban_author

        post_id = self.post_id

        status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_id is not UNSET:
            field_dict["account_id"] = account_id
        if ban_author is not UNSET:
            field_dict["ban_author"] = ban_author
        if post_id is not UNSET:
            field_dict["post_id"] = post_id
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_id = d.pop("account_id", UNSET)

        ban_author = d.pop("ban_author", UNSET)

        post_id = d.pop("post_id", UNSET)

        status = d.pop("status", UNSET)

        api_endpoints_moderate_you_tube_comment_request = cls(
            account_id=account_id,
            ban_author=ban_author,
            post_id=post_id,
            status=status,
        )

        api_endpoints_moderate_you_tube_comment_request.additional_properties = d
        return api_endpoints_moderate_you_tube_comment_request

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
