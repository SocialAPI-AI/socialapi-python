from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.author import Author
    from ..models.review_media import ReviewMedia
    from ..models.review_reply_detail import ReviewReplyDetail


T = TypeVar("T", bound="ReviewItem")


@_attrs_define
class ReviewItem:
    """
    Attributes:
        author (Author):
        created_at (datetime.datetime):  Example: 2026-06-20T18:24:31Z.
        id (str):  Example: sapi_rev_TXY....
        rating (int):  Example: 3.
        reply (None | ReviewReplyDetail):
        text (str):  Example: Great school.
        updated_at (datetime.datetime):  Example: 2026-06-20T18:24:31Z.
        media (list[ReviewMedia] | Unset):
        reply_url (str | Unset): ReplyURL is the platform-hosted page for replying to this review, when
            the platform exposes one (Google). Empty elsewhere. Example: https://business.google.com/reviews/reply/abc.
        title (str | Unset): Title is the review's headline, on platforms whose reviews have one (App Store Connect).
            Example: Love it.
    """

    author: Author
    created_at: datetime.datetime
    id: str
    rating: int
    reply: None | ReviewReplyDetail
    text: str
    updated_at: datetime.datetime
    media: list[ReviewMedia] | Unset = UNSET
    reply_url: str | Unset = UNSET
    title: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.review_reply_detail import ReviewReplyDetail  # noqa: PLC0415

        author = self.author.to_dict()

        created_at = self.created_at.isoformat()

        id = self.id

        rating = self.rating

        reply: dict[str, Any] | None
        if isinstance(self.reply, ReviewReplyDetail):
            reply = self.reply.to_dict()
        else:
            reply = self.reply

        text = self.text

        updated_at = self.updated_at.isoformat()

        media: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.media, Unset):
            media = []
            for media_item_data in self.media:
                media_item = media_item_data.to_dict()
                media.append(media_item)

        reply_url = self.reply_url

        title = self.title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "author": author,
                "created_at": created_at,
                "id": id,
                "rating": rating,
                "reply": reply,
                "text": text,
                "updated_at": updated_at,
            }
        )
        if media is not UNSET:
            field_dict["media"] = media
        if reply_url is not UNSET:
            field_dict["reply_url"] = reply_url
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.author import Author  # noqa: PLC0415
        from ..models.review_media import ReviewMedia  # noqa: PLC0415
        from ..models.review_reply_detail import ReviewReplyDetail  # noqa: PLC0415

        d = dict(src_dict)
        author = Author.from_dict(d.pop("author"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        id = d.pop("id")

        rating = d.pop("rating")

        def _parse_reply(data: object) -> None | ReviewReplyDetail:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                reply_type_1 = ReviewReplyDetail.from_dict(data)

                return reply_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ReviewReplyDetail, data)

        reply = _parse_reply(d.pop("reply"))

        text = d.pop("text")

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        _media = d.pop("media", UNSET)
        media: list[ReviewMedia] | Unset = UNSET
        if _media is not UNSET:
            media = []
            for media_item_data in _media:
                media_item = ReviewMedia.from_dict(media_item_data)

                media.append(media_item)

        reply_url = d.pop("reply_url", UNSET)

        title = d.pop("title", UNSET)

        review_item = cls(
            author=author,
            created_at=created_at,
            id=id,
            rating=rating,
            reply=reply,
            text=text,
            updated_at=updated_at,
            media=media,
            reply_url=reply_url,
            title=title,
        )

        review_item.additional_properties = d
        return review_item

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
