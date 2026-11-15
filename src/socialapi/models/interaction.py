from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.platform import Platform
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.author import Author
    from ..models.content import Content
    from ..models.interaction_metadata_type_0 import InteractionMetadataType0
    from ..models.message_ref import MessageRef
    from ..models.story import Story


T = TypeVar("T", bound="Interaction")


@_attrs_define
class Interaction:
    """
    Attributes:
        account_id (str): [always] Example: acc_01HZ9X3Q4R5M6N7P8V2K0W1J.
        author (Author):
        content (Content):
        id (str): [always] SocialAPI interaction ID (sapi_cmt_/sapi_rev_/sapi_dm_/sapi_mnt_ prefix) Example:
            sapi_cmt_TT974YVQH4RAHNN2HY2DJSNY9111D7LMTP1XXPCVQVL.
        metadata (InteractionMetadataType0 | None): [optional] Platform-specific keys: google sets "star_rating";
            facebook mentions set "permalink_url"; instagram sets "media_id" or "referral"
        platform (Platform):
        received_at (str): [always] Example: 2026-02-15T14:30:00Z.
        type_ (str): [always] One of: comment, review, dm, mention (or dm.sent/dm.received/dm.referral for webhook
            events) Example: comment.
        conversation_id (str | Unset): [optional] SocialAPI conversation ID; set on Facebook, Instagram, WhatsApp and
            Telegram DMs that belong to a conversation Example: 550e8400-e29b-41d4-a716-446655440000.
        page_id (str | Unset): [platform: facebook] SocialAPI page ID identifying which Page received the event. Set for
            Facebook Page-scoped events; empty for platforms without a multi-page account model (e.g. Instagram), where
            account_id already identifies the account. Example: 550e8400-e29b-41d4-a716-446655440000.
        permalink (str | Unset): [optional] Public URL of the post this interaction belongs to; set for instagram
            comments Example: https://www.instagram.com/p/C8xY2AbC/.
        platform_id (str | Unset): [optional] Platform-native message id, byte-identical to the platform_id of the
            matching row from GET /v1/inbox/conversations/{conversation_id}/messages. Set on Instagram, Facebook and
            WhatsApp dm.received and dm.sent, on Telegram dm.received, and on Instagram and Facebook dm.postback, so a
            delivered event can be joined to a message from that endpoint: id is a SocialAPI interaction id, which the
            messages endpoint does not return, so without this the two carry no field in common. Empty for dm.referral,
            which has no platform message id. Example: m_AbCdEf123.
        platform_post_id (str | Unset): [optional] Platform-native post ID; empty when not available Example:
            17895695668004550.
        post_id (str | Unset): [optional] SocialAPI post ID; empty when the interaction is not linked to a post Example:
            01HZ9X3Q4R5M6N7P8V2K0W1J42.
        recipient (Author | Unset):
        reply_to (MessageRef | Unset):
        story (Story | Unset):
    """

    account_id: str
    author: Author
    content: Content
    id: str
    metadata: InteractionMetadataType0 | None
    platform: Platform
    received_at: str
    type_: str
    conversation_id: str | Unset = UNSET
    page_id: str | Unset = UNSET
    permalink: str | Unset = UNSET
    platform_id: str | Unset = UNSET
    platform_post_id: str | Unset = UNSET
    post_id: str | Unset = UNSET
    recipient: Author | Unset = UNSET
    reply_to: MessageRef | Unset = UNSET
    story: Story | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.interaction_metadata_type_0 import InteractionMetadataType0  # noqa: PLC0415

        account_id = self.account_id

        author = self.author.to_dict()

        content = self.content.to_dict()

        id = self.id

        metadata: dict[str, Any] | None
        if isinstance(self.metadata, InteractionMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        platform = self.platform.value

        received_at = self.received_at

        type_ = self.type_

        conversation_id = self.conversation_id

        page_id = self.page_id

        permalink = self.permalink

        platform_id = self.platform_id

        platform_post_id = self.platform_post_id

        post_id = self.post_id

        recipient: dict[str, Any] | Unset = UNSET
        if not isinstance(self.recipient, Unset):
            recipient = self.recipient.to_dict()

        reply_to: dict[str, Any] | Unset = UNSET
        if not isinstance(self.reply_to, Unset):
            reply_to = self.reply_to.to_dict()

        story: dict[str, Any] | Unset = UNSET
        if not isinstance(self.story, Unset):
            story = self.story.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "account_id": account_id,
                "author": author,
                "content": content,
                "id": id,
                "metadata": metadata,
                "platform": platform,
                "received_at": received_at,
                "type": type_,
            }
        )
        if conversation_id is not UNSET:
            field_dict["conversation_id"] = conversation_id
        if page_id is not UNSET:
            field_dict["page_id"] = page_id
        if permalink is not UNSET:
            field_dict["permalink"] = permalink
        if platform_id is not UNSET:
            field_dict["platform_id"] = platform_id
        if platform_post_id is not UNSET:
            field_dict["platform_post_id"] = platform_post_id
        if post_id is not UNSET:
            field_dict["post_id"] = post_id
        if recipient is not UNSET:
            field_dict["recipient"] = recipient
        if reply_to is not UNSET:
            field_dict["reply_to"] = reply_to
        if story is not UNSET:
            field_dict["story"] = story

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.author import Author  # noqa: PLC0415
        from ..models.content import Content  # noqa: PLC0415
        from ..models.interaction_metadata_type_0 import InteractionMetadataType0  # noqa: PLC0415
        from ..models.message_ref import MessageRef  # noqa: PLC0415
        from ..models.story import Story  # noqa: PLC0415

        d = dict(src_dict)
        account_id = d.pop("account_id")

        author = Author.from_dict(d.pop("author"))

        content = Content.from_dict(d.pop("content"))

        id = d.pop("id")

        def _parse_metadata(data: object) -> InteractionMetadataType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = InteractionMetadataType0.from_dict(data)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(InteractionMetadataType0 | None, data)

        metadata = _parse_metadata(d.pop("metadata"))

        platform = Platform(d.pop("platform"))

        received_at = d.pop("received_at")

        type_ = d.pop("type")

        conversation_id = d.pop("conversation_id", UNSET)

        page_id = d.pop("page_id", UNSET)

        permalink = d.pop("permalink", UNSET)

        platform_id = d.pop("platform_id", UNSET)

        platform_post_id = d.pop("platform_post_id", UNSET)

        post_id = d.pop("post_id", UNSET)

        _recipient = d.pop("recipient", UNSET)
        recipient: Author | Unset
        if isinstance(_recipient, Unset):
            recipient = UNSET
        else:
            recipient = Author.from_dict(_recipient)

        _reply_to = d.pop("reply_to", UNSET)
        reply_to: MessageRef | Unset
        if isinstance(_reply_to, Unset):
            reply_to = UNSET
        else:
            reply_to = MessageRef.from_dict(_reply_to)

        _story = d.pop("story", UNSET)
        story: Story | Unset
        if isinstance(_story, Unset):
            story = UNSET
        else:
            story = Story.from_dict(_story)

        interaction = cls(
            account_id=account_id,
            author=author,
            content=content,
            id=id,
            metadata=metadata,
            platform=platform,
            received_at=received_at,
            type_=type_,
            conversation_id=conversation_id,
            page_id=page_id,
            permalink=permalink,
            platform_id=platform_id,
            platform_post_id=platform_post_id,
            post_id=post_id,
            recipient=recipient,
            reply_to=reply_to,
            story=story,
        )

        interaction.additional_properties = d
        return interaction

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
