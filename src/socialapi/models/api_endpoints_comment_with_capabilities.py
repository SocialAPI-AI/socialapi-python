from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_endpoints_comment_capabilities import ApiEndpointsCommentCapabilities


T = TypeVar("T", bound="ApiEndpointsCommentWithCapabilities")


@_attrs_define
class ApiEndpointsCommentWithCapabilities:
    """
    Attributes:
        author_headline (str | Unset):
        author_id (str | Unset):
        author_name (str | Unset):
        author_picture (str | Unset):
        author_profile_url (str | Unset):
        author_username (str | Unset):
        capabilities (ApiEndpointsCommentCapabilities | Unset):
        created_at (str | Unset):
        has_replies (bool | Unset):
        id (str | Unset): ID is the canonical SocialAPI interaction id (sapi_cmt_…). Prefer it over
            platform_id, which is retained for backward compatibility. Example:
            sapi_cmt_TT974YVQH4RAHNN2HY2DJSNY9111D7LMTP1XXPCVQVL.
        is_hidden (bool | Unset):
        is_owner (bool | Unset):
        like_count (int | Unset):
        liked_by_viewer (bool | Unset): LikedByViewer is true when the connected account has liked this comment.
            LinkedIn reports it directly. Instagram and Facebook do not report it on
            the comment read, so there it means "liked through SocialAPI": a like made
            in the platform's own app is not reflected.
        moderation_status (str | Unset): ModerationStatus is the platform's moderation state for this comment, when
            exposed: "published", "held_for_review", "likely_spam", or "rejected".
            Empty when unknown or not applicable. [platform: youtube]
        parent_id (str | Unset):
        platform (str | Unset):
        platform_id (str | Unset):
        reply_count (int | Unset): ReplyCount is kept for backward compatibility but deprecated: prefer
            HasReplies. Not all platforms report an exact count.
        text (str | Unset):
    """

    author_headline: str | Unset = UNSET
    author_id: str | Unset = UNSET
    author_name: str | Unset = UNSET
    author_picture: str | Unset = UNSET
    author_profile_url: str | Unset = UNSET
    author_username: str | Unset = UNSET
    capabilities: ApiEndpointsCommentCapabilities | Unset = UNSET
    created_at: str | Unset = UNSET
    has_replies: bool | Unset = UNSET
    id: str | Unset = UNSET
    is_hidden: bool | Unset = UNSET
    is_owner: bool | Unset = UNSET
    like_count: int | Unset = UNSET
    liked_by_viewer: bool | Unset = UNSET
    moderation_status: str | Unset = UNSET
    parent_id: str | Unset = UNSET
    platform: str | Unset = UNSET
    platform_id: str | Unset = UNSET
    reply_count: int | Unset = UNSET
    text: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        author_headline = self.author_headline

        author_id = self.author_id

        author_name = self.author_name

        author_picture = self.author_picture

        author_profile_url = self.author_profile_url

        author_username = self.author_username

        capabilities: dict[str, Any] | Unset = UNSET
        if not isinstance(self.capabilities, Unset):
            capabilities = self.capabilities.to_dict()

        created_at = self.created_at

        has_replies = self.has_replies

        id = self.id

        is_hidden = self.is_hidden

        is_owner = self.is_owner

        like_count = self.like_count

        liked_by_viewer = self.liked_by_viewer

        moderation_status = self.moderation_status

        parent_id = self.parent_id

        platform = self.platform

        platform_id = self.platform_id

        reply_count = self.reply_count

        text = self.text

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if author_headline is not UNSET:
            field_dict["author_headline"] = author_headline
        if author_id is not UNSET:
            field_dict["author_id"] = author_id
        if author_name is not UNSET:
            field_dict["author_name"] = author_name
        if author_picture is not UNSET:
            field_dict["author_picture"] = author_picture
        if author_profile_url is not UNSET:
            field_dict["author_profile_url"] = author_profile_url
        if author_username is not UNSET:
            field_dict["author_username"] = author_username
        if capabilities is not UNSET:
            field_dict["capabilities"] = capabilities
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if has_replies is not UNSET:
            field_dict["has_replies"] = has_replies
        if id is not UNSET:
            field_dict["id"] = id
        if is_hidden is not UNSET:
            field_dict["is_hidden"] = is_hidden
        if is_owner is not UNSET:
            field_dict["is_owner"] = is_owner
        if like_count is not UNSET:
            field_dict["like_count"] = like_count
        if liked_by_viewer is not UNSET:
            field_dict["liked_by_viewer"] = liked_by_viewer
        if moderation_status is not UNSET:
            field_dict["moderation_status"] = moderation_status
        if parent_id is not UNSET:
            field_dict["parent_id"] = parent_id
        if platform is not UNSET:
            field_dict["platform"] = platform
        if platform_id is not UNSET:
            field_dict["platform_id"] = platform_id
        if reply_count is not UNSET:
            field_dict["reply_count"] = reply_count
        if text is not UNSET:
            field_dict["text"] = text

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_endpoints_comment_capabilities import ApiEndpointsCommentCapabilities  # noqa: PLC0415

        d = dict(src_dict)
        author_headline = d.pop("author_headline", UNSET)

        author_id = d.pop("author_id", UNSET)

        author_name = d.pop("author_name", UNSET)

        author_picture = d.pop("author_picture", UNSET)

        author_profile_url = d.pop("author_profile_url", UNSET)

        author_username = d.pop("author_username", UNSET)

        _capabilities = d.pop("capabilities", UNSET)
        capabilities: ApiEndpointsCommentCapabilities | Unset
        if isinstance(_capabilities, Unset):
            capabilities = UNSET
        else:
            capabilities = ApiEndpointsCommentCapabilities.from_dict(_capabilities)

        created_at = d.pop("created_at", UNSET)

        has_replies = d.pop("has_replies", UNSET)

        id = d.pop("id", UNSET)

        is_hidden = d.pop("is_hidden", UNSET)

        is_owner = d.pop("is_owner", UNSET)

        like_count = d.pop("like_count", UNSET)

        liked_by_viewer = d.pop("liked_by_viewer", UNSET)

        moderation_status = d.pop("moderation_status", UNSET)

        parent_id = d.pop("parent_id", UNSET)

        platform = d.pop("platform", UNSET)

        platform_id = d.pop("platform_id", UNSET)

        reply_count = d.pop("reply_count", UNSET)

        text = d.pop("text", UNSET)

        api_endpoints_comment_with_capabilities = cls(
            author_headline=author_headline,
            author_id=author_id,
            author_name=author_name,
            author_picture=author_picture,
            author_profile_url=author_profile_url,
            author_username=author_username,
            capabilities=capabilities,
            created_at=created_at,
            has_replies=has_replies,
            id=id,
            is_hidden=is_hidden,
            is_owner=is_owner,
            like_count=like_count,
            liked_by_viewer=liked_by_viewer,
            moderation_status=moderation_status,
            parent_id=parent_id,
            platform=platform,
            platform_id=platform_id,
            reply_count=reply_count,
            text=text,
        )

        api_endpoints_comment_with_capabilities.additional_properties = d
        return api_endpoints_comment_with_capabilities

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
