from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.platform import Platform
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.comment_capabilities import CommentCapabilities


T = TypeVar("T", bound="CommentWithCapabilities")


@_attrs_define
class CommentWithCapabilities:
    """
    Attributes:
        author_id (str):
        author_name (str):
        author_picture (str):
        author_username (str):
        capabilities (CommentCapabilities):
        created_at (datetime.datetime):
        has_replies (bool):
        id (str): ID is the canonical SocialAPI interaction id (sapi_cmt_…). Prefer it over
            platform_id, which is retained for backward compatibility. Example:
            sapi_cmt_TT974YVQH4RAHNN2HY2DJSNY9111D7LMTP1XXPCVQVL.
        is_hidden (bool):
        is_owner (bool):
        like_count (int):
        liked_by_viewer (bool): LikedByViewer is true when the connected account has liked this comment.
            LinkedIn reports it directly. Instagram and Facebook do not report it on
            the comment read, so there it means "liked through SocialAPI": a like made
            in the platform's own app is not reflected.
        parent_id (None | str):
        platform (Platform):
        platform_id (str):
        reply_count (int): ReplyCount is kept for backward compatibility but deprecated: prefer
            HasReplies. Not all platforms report an exact count.
        text (str):
        author_headline (str | Unset):
        author_profile_url (str | Unset):
        moderation_status (str | Unset): ModerationStatus is the platform's moderation state for this comment, when
            exposed: "published", "held_for_review", "likely_spam", or "rejected".
            Empty when unknown or not applicable. [platform: youtube]
    """

    author_id: str
    author_name: str
    author_picture: str
    author_username: str
    capabilities: CommentCapabilities
    created_at: datetime.datetime
    has_replies: bool
    id: str
    is_hidden: bool
    is_owner: bool
    like_count: int
    liked_by_viewer: bool
    parent_id: None | str
    platform: Platform
    platform_id: str
    reply_count: int
    text: str
    author_headline: str | Unset = UNSET
    author_profile_url: str | Unset = UNSET
    moderation_status: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        author_id = self.author_id

        author_name = self.author_name

        author_picture = self.author_picture

        author_username = self.author_username

        capabilities = self.capabilities.to_dict()

        created_at = self.created_at.isoformat()

        has_replies = self.has_replies

        id = self.id

        is_hidden = self.is_hidden

        is_owner = self.is_owner

        like_count = self.like_count

        liked_by_viewer = self.liked_by_viewer

        parent_id: None | str
        parent_id = self.parent_id

        platform = self.platform.value

        platform_id = self.platform_id

        reply_count = self.reply_count

        text = self.text

        author_headline = self.author_headline

        author_profile_url = self.author_profile_url

        moderation_status = self.moderation_status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "author_id": author_id,
                "author_name": author_name,
                "author_picture": author_picture,
                "author_username": author_username,
                "capabilities": capabilities,
                "created_at": created_at,
                "has_replies": has_replies,
                "id": id,
                "is_hidden": is_hidden,
                "is_owner": is_owner,
                "like_count": like_count,
                "liked_by_viewer": liked_by_viewer,
                "parent_id": parent_id,
                "platform": platform,
                "platform_id": platform_id,
                "reply_count": reply_count,
                "text": text,
            }
        )
        if author_headline is not UNSET:
            field_dict["author_headline"] = author_headline
        if author_profile_url is not UNSET:
            field_dict["author_profile_url"] = author_profile_url
        if moderation_status is not UNSET:
            field_dict["moderation_status"] = moderation_status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.comment_capabilities import CommentCapabilities  # noqa: PLC0415

        d = dict(src_dict)
        author_id = d.pop("author_id")

        author_name = d.pop("author_name")

        author_picture = d.pop("author_picture")

        author_username = d.pop("author_username")

        capabilities = CommentCapabilities.from_dict(d.pop("capabilities"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        has_replies = d.pop("has_replies")

        id = d.pop("id")

        is_hidden = d.pop("is_hidden")

        is_owner = d.pop("is_owner")

        like_count = d.pop("like_count")

        liked_by_viewer = d.pop("liked_by_viewer")

        def _parse_parent_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        parent_id = _parse_parent_id(d.pop("parent_id"))

        platform = Platform(d.pop("platform"))

        platform_id = d.pop("platform_id")

        reply_count = d.pop("reply_count")

        text = d.pop("text")

        author_headline = d.pop("author_headline", UNSET)

        author_profile_url = d.pop("author_profile_url", UNSET)

        moderation_status = d.pop("moderation_status", UNSET)

        comment_with_capabilities = cls(
            author_id=author_id,
            author_name=author_name,
            author_picture=author_picture,
            author_username=author_username,
            capabilities=capabilities,
            created_at=created_at,
            has_replies=has_replies,
            id=id,
            is_hidden=is_hidden,
            is_owner=is_owner,
            like_count=like_count,
            liked_by_viewer=liked_by_viewer,
            parent_id=parent_id,
            platform=platform,
            platform_id=platform_id,
            reply_count=reply_count,
            text=text,
            author_headline=author_headline,
            author_profile_url=author_profile_url,
            moderation_status=moderation_status,
        )

        comment_with_capabilities.additional_properties = d
        return comment_with_capabilities

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
