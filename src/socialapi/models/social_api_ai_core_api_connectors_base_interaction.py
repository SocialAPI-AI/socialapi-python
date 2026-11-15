from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.social_api_ai_core_api_connectors_base_author import SocialApiAiCoreApiConnectorsBaseAuthor
    from ..models.social_api_ai_core_api_connectors_base_content import SocialApiAiCoreApiConnectorsBaseContent
    from ..models.social_api_ai_core_api_connectors_base_interaction_metadata import (
        SocialApiAiCoreApiConnectorsBaseInteractionMetadata,
    )
    from ..models.social_api_ai_core_api_connectors_base_message_ref import SocialApiAiCoreApiConnectorsBaseMessageRef
    from ..models.social_api_ai_core_api_connectors_base_story import SocialApiAiCoreApiConnectorsBaseStory


T = TypeVar("T", bound="SocialApiAiCoreApiConnectorsBaseInteraction")


@_attrs_define
class SocialApiAiCoreApiConnectorsBaseInteraction:
    """
    Attributes:
        account_id (str | Unset): [always] Example: acc_01HZ9X3Q4R5M6N7P8V2K0W1J.
        author (SocialApiAiCoreApiConnectorsBaseAuthor | Unset):
        content (SocialApiAiCoreApiConnectorsBaseContent | Unset):
        conversation_id (str | Unset): [optional] SocialAPI conversation ID; set on Facebook, Instagram, WhatsApp and
            Telegram DMs that belong to a conversation Example: 550e8400-e29b-41d4-a716-446655440000.
        id (str | Unset): [always] SocialAPI interaction ID (sapi_cmt_/sapi_rev_/sapi_dm_/sapi_mnt_ prefix) Example:
            sapi_cmt_TT974YVQH4RAHNN2HY2DJSNY9111D7LMTP1XXPCVQVL.
        metadata (SocialApiAiCoreApiConnectorsBaseInteractionMetadata | Unset): [optional] Platform-specific keys:
            google sets "star_rating"; facebook mentions set "permalink_url"; instagram sets "media_id" or "referral"
        page_id (str | Unset): [platform: facebook] SocialAPI page ID identifying which Page received the event. Set for
            Facebook Page-scoped events; empty for platforms without a multi-page account model (e.g. Instagram), where
            account_id already identifies the account. Example: 550e8400-e29b-41d4-a716-446655440000.
        permalink (str | Unset): [optional] Public URL of the post this interaction belongs to; set for instagram
            comments Example: https://www.instagram.com/p/C8xY2AbC/.
        platform (str | Unset): [always] Example: instagram.
        platform_id (str | Unset): [optional] Platform-native message id, byte-identical to the platform_id of the
            matching row from GET /v1/inbox/conversations/{id}/messages. Set on Instagram, Facebook and WhatsApp dm.received
            and dm.sent, on Telegram dm.received, and on Instagram and Facebook dm.postback, so a delivered event can be
            joined to a message from that endpoint: id is a SocialAPI interaction id, which the messages endpoint does not
            return, so without this the two carry no field in common. Empty for dm.referral, which has no platform message
            id. Example: m_AbCdEf123.
        platform_post_id (str | Unset): [optional] Platform-native post ID; empty when not available Example:
            17895695668004550.
        post_id (str | Unset): [optional] SocialAPI post ID; empty when the interaction is not linked to a post Example:
            01HZ9X3Q4R5M6N7P8V2K0W1J42.
        received_at (str | Unset): [always] Example: 2026-02-15T14:30:00Z.
        recipient (SocialApiAiCoreApiConnectorsBaseAuthor | Unset):
        reply_to (SocialApiAiCoreApiConnectorsBaseMessageRef | Unset):
        story (SocialApiAiCoreApiConnectorsBaseStory | Unset):
        type_ (str | Unset): [always] One of: comment, review, dm, mention (or dm.sent/dm.received/dm.referral for
            webhook events) Example: comment.
    """

    account_id: str | Unset = UNSET
    author: SocialApiAiCoreApiConnectorsBaseAuthor | Unset = UNSET
    content: SocialApiAiCoreApiConnectorsBaseContent | Unset = UNSET
    conversation_id: str | Unset = UNSET
    id: str | Unset = UNSET
    metadata: SocialApiAiCoreApiConnectorsBaseInteractionMetadata | Unset = UNSET
    page_id: str | Unset = UNSET
    permalink: str | Unset = UNSET
    platform: str | Unset = UNSET
    platform_id: str | Unset = UNSET
    platform_post_id: str | Unset = UNSET
    post_id: str | Unset = UNSET
    received_at: str | Unset = UNSET
    recipient: SocialApiAiCoreApiConnectorsBaseAuthor | Unset = UNSET
    reply_to: SocialApiAiCoreApiConnectorsBaseMessageRef | Unset = UNSET
    story: SocialApiAiCoreApiConnectorsBaseStory | Unset = UNSET
    type_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_id = self.account_id

        author: dict[str, Any] | Unset = UNSET
        if not isinstance(self.author, Unset):
            author = self.author.to_dict()

        content: dict[str, Any] | Unset = UNSET
        if not isinstance(self.content, Unset):
            content = self.content.to_dict()

        conversation_id = self.conversation_id

        id = self.id

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        page_id = self.page_id

        permalink = self.permalink

        platform = self.platform

        platform_id = self.platform_id

        platform_post_id = self.platform_post_id

        post_id = self.post_id

        received_at = self.received_at

        recipient: dict[str, Any] | Unset = UNSET
        if not isinstance(self.recipient, Unset):
            recipient = self.recipient.to_dict()

        reply_to: dict[str, Any] | Unset = UNSET
        if not isinstance(self.reply_to, Unset):
            reply_to = self.reply_to.to_dict()

        story: dict[str, Any] | Unset = UNSET
        if not isinstance(self.story, Unset):
            story = self.story.to_dict()

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_id is not UNSET:
            field_dict["account_id"] = account_id
        if author is not UNSET:
            field_dict["author"] = author
        if content is not UNSET:
            field_dict["content"] = content
        if conversation_id is not UNSET:
            field_dict["conversation_id"] = conversation_id
        if id is not UNSET:
            field_dict["id"] = id
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if page_id is not UNSET:
            field_dict["page_id"] = page_id
        if permalink is not UNSET:
            field_dict["permalink"] = permalink
        if platform is not UNSET:
            field_dict["platform"] = platform
        if platform_id is not UNSET:
            field_dict["platform_id"] = platform_id
        if platform_post_id is not UNSET:
            field_dict["platform_post_id"] = platform_post_id
        if post_id is not UNSET:
            field_dict["post_id"] = post_id
        if received_at is not UNSET:
            field_dict["received_at"] = received_at
        if recipient is not UNSET:
            field_dict["recipient"] = recipient
        if reply_to is not UNSET:
            field_dict["reply_to"] = reply_to
        if story is not UNSET:
            field_dict["story"] = story
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.social_api_ai_core_api_connectors_base_author import (
            SocialApiAiCoreApiConnectorsBaseAuthor,  # noqa: PLC0415
        )
        from ..models.social_api_ai_core_api_connectors_base_content import (
            SocialApiAiCoreApiConnectorsBaseContent,  # noqa: PLC0415
        )
        from ..models.social_api_ai_core_api_connectors_base_interaction_metadata import (
            SocialApiAiCoreApiConnectorsBaseInteractionMetadata,  # noqa: PLC0415
        )
        from ..models.social_api_ai_core_api_connectors_base_message_ref import (
            SocialApiAiCoreApiConnectorsBaseMessageRef,  # noqa: PLC0415
        )
        from ..models.social_api_ai_core_api_connectors_base_story import (
            SocialApiAiCoreApiConnectorsBaseStory,  # noqa: PLC0415
        )

        d = dict(src_dict)
        account_id = d.pop("account_id", UNSET)

        _author = d.pop("author", UNSET)
        author: SocialApiAiCoreApiConnectorsBaseAuthor | Unset
        if isinstance(_author, Unset):
            author = UNSET
        else:
            author = SocialApiAiCoreApiConnectorsBaseAuthor.from_dict(_author)

        _content = d.pop("content", UNSET)
        content: SocialApiAiCoreApiConnectorsBaseContent | Unset
        if isinstance(_content, Unset):
            content = UNSET
        else:
            content = SocialApiAiCoreApiConnectorsBaseContent.from_dict(_content)

        conversation_id = d.pop("conversation_id", UNSET)

        id = d.pop("id", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: SocialApiAiCoreApiConnectorsBaseInteractionMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = SocialApiAiCoreApiConnectorsBaseInteractionMetadata.from_dict(_metadata)

        page_id = d.pop("page_id", UNSET)

        permalink = d.pop("permalink", UNSET)

        platform = d.pop("platform", UNSET)

        platform_id = d.pop("platform_id", UNSET)

        platform_post_id = d.pop("platform_post_id", UNSET)

        post_id = d.pop("post_id", UNSET)

        received_at = d.pop("received_at", UNSET)

        _recipient = d.pop("recipient", UNSET)
        recipient: SocialApiAiCoreApiConnectorsBaseAuthor | Unset
        if isinstance(_recipient, Unset):
            recipient = UNSET
        else:
            recipient = SocialApiAiCoreApiConnectorsBaseAuthor.from_dict(_recipient)

        _reply_to = d.pop("reply_to", UNSET)
        reply_to: SocialApiAiCoreApiConnectorsBaseMessageRef | Unset
        if isinstance(_reply_to, Unset):
            reply_to = UNSET
        else:
            reply_to = SocialApiAiCoreApiConnectorsBaseMessageRef.from_dict(_reply_to)

        _story = d.pop("story", UNSET)
        story: SocialApiAiCoreApiConnectorsBaseStory | Unset
        if isinstance(_story, Unset):
            story = UNSET
        else:
            story = SocialApiAiCoreApiConnectorsBaseStory.from_dict(_story)

        type_ = d.pop("type", UNSET)

        social_api_ai_core_api_connectors_base_interaction = cls(
            account_id=account_id,
            author=author,
            content=content,
            conversation_id=conversation_id,
            id=id,
            metadata=metadata,
            page_id=page_id,
            permalink=permalink,
            platform=platform,
            platform_id=platform_id,
            platform_post_id=platform_post_id,
            post_id=post_id,
            received_at=received_at,
            recipient=recipient,
            reply_to=reply_to,
            story=story,
            type_=type_,
        )

        social_api_ai_core_api_connectors_base_interaction.additional_properties = d
        return social_api_ai_core_api_connectors_base_interaction

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
