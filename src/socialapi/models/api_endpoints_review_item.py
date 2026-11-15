from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_endpoints_review_media_dto import ApiEndpointsReviewMediaDTO
    from ..models.api_endpoints_review_reply_dto import ApiEndpointsReviewReplyDTO
    from ..models.social_api_ai_core_api_connectors_base_author import SocialApiAiCoreApiConnectorsBaseAuthor


T = TypeVar("T", bound="ApiEndpointsReviewItem")


@_attrs_define
class ApiEndpointsReviewItem:
    """
    Attributes:
        author (SocialApiAiCoreApiConnectorsBaseAuthor | Unset):
        created_at (str | Unset):  Example: 2026-06-20T18:24:31Z.
        id (str | Unset):  Example: sapi_rev_TXY....
        media (list[ApiEndpointsReviewMediaDTO] | Unset):
        rating (int | Unset):  Example: 3.
        reply (ApiEndpointsReviewReplyDTO | Unset):
        reply_url (str | Unset): ReplyURL is the platform-hosted page for replying to this review, when
            the platform exposes one (Google). Empty elsewhere. Example: https://business.google.com/reviews/reply/abc.
        text (str | Unset):  Example: Great school.
        title (str | Unset): Title is the review's headline, on platforms whose reviews have one (App Store Connect).
            Example: Love it.
        updated_at (str | Unset):  Example: 2026-06-20T18:24:31Z.
    """

    author: SocialApiAiCoreApiConnectorsBaseAuthor | Unset = UNSET
    created_at: str | Unset = UNSET
    id: str | Unset = UNSET
    media: list[ApiEndpointsReviewMediaDTO] | Unset = UNSET
    rating: int | Unset = UNSET
    reply: ApiEndpointsReviewReplyDTO | Unset = UNSET
    reply_url: str | Unset = UNSET
    text: str | Unset = UNSET
    title: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        author: dict[str, Any] | Unset = UNSET
        if not isinstance(self.author, Unset):
            author = self.author.to_dict()

        created_at = self.created_at

        id = self.id

        media: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.media, Unset):
            media = []
            for media_item_data in self.media:
                media_item = media_item_data.to_dict()
                media.append(media_item)

        rating = self.rating

        reply: dict[str, Any] | Unset = UNSET
        if not isinstance(self.reply, Unset):
            reply = self.reply.to_dict()

        reply_url = self.reply_url

        text = self.text

        title = self.title

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if author is not UNSET:
            field_dict["author"] = author
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if id is not UNSET:
            field_dict["id"] = id
        if media is not UNSET:
            field_dict["media"] = media
        if rating is not UNSET:
            field_dict["rating"] = rating
        if reply is not UNSET:
            field_dict["reply"] = reply
        if reply_url is not UNSET:
            field_dict["reply_url"] = reply_url
        if text is not UNSET:
            field_dict["text"] = text
        if title is not UNSET:
            field_dict["title"] = title
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_endpoints_review_media_dto import ApiEndpointsReviewMediaDTO  # noqa: PLC0415
        from ..models.api_endpoints_review_reply_dto import ApiEndpointsReviewReplyDTO  # noqa: PLC0415
        from ..models.social_api_ai_core_api_connectors_base_author import (
            SocialApiAiCoreApiConnectorsBaseAuthor,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _author = d.pop("author", UNSET)
        author: SocialApiAiCoreApiConnectorsBaseAuthor | Unset
        if isinstance(_author, Unset):
            author = UNSET
        else:
            author = SocialApiAiCoreApiConnectorsBaseAuthor.from_dict(_author)

        created_at = d.pop("created_at", UNSET)

        id = d.pop("id", UNSET)

        _media = d.pop("media", UNSET)
        media: list[ApiEndpointsReviewMediaDTO] | Unset = UNSET
        if _media is not UNSET:
            media = []
            for media_item_data in _media:
                media_item = ApiEndpointsReviewMediaDTO.from_dict(media_item_data)

                media.append(media_item)

        rating = d.pop("rating", UNSET)

        _reply = d.pop("reply", UNSET)
        reply: ApiEndpointsReviewReplyDTO | Unset
        if isinstance(_reply, Unset):
            reply = UNSET
        else:
            reply = ApiEndpointsReviewReplyDTO.from_dict(_reply)

        reply_url = d.pop("reply_url", UNSET)

        text = d.pop("text", UNSET)

        title = d.pop("title", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        api_endpoints_review_item = cls(
            author=author,
            created_at=created_at,
            id=id,
            media=media,
            rating=rating,
            reply=reply,
            reply_url=reply_url,
            text=text,
            title=title,
            updated_at=updated_at,
        )

        api_endpoints_review_item.additional_properties = d
        return api_endpoints_review_item

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
