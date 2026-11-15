from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.social_api_ai_core_api_connectors_base_account_connection_type import (
    SocialApiAiCoreApiConnectorsBaseAccountConnectionType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.social_api_ai_core_api_connectors_base_account_metadata import (
        SocialApiAiCoreApiConnectorsBaseAccountMetadata,
    )


T = TypeVar("T", bound="SocialApiAiCoreApiConnectorsBaseAccount")


@_attrs_define
class SocialApiAiCoreApiConnectorsBaseAccount:
    """
    Attributes:
        bio (str | Unset): [optional] Profile biography or description
        brand_id (str | Unset): [always] SocialAPI brand ID this account belongs to
        connection_type (SocialApiAiCoreApiConnectorsBaseAccountConnectionType | Unset): [optional] LinkedIn only:
            "profile" for a member profile, "organization" for a company Page. Absent for every other account Example:
            profile.
        effective_permissions (list[str] | Unset): [always] The permissions this account can use right now: the
            requested permissions the platform supports, minus any the platform did not grant or has since refused. Uses the
            same names as permissions. An empty list when none apply
        id (str | Unset): [always] Example: acc_01HZ9X3Q4R5M6N7P8V2K0W1J.
        login_id (str | Unset): [optional] Login id shared by accounts connected in the same authorization (facebook,
            google, linkedin)
        metadata (SocialApiAiCoreApiConnectorsBaseAccountMetadata | Unset): [optional] Platform-specific keys for this
            account
        name (str | Unset): [always] Display name of the account or page Example: Acme Corp.
        page_name (str | Unset): [optional] Name of the single active page bound to this account; set only when exactly
            one page is active (e.g. facebook), so clients can label the tile with the page instead of the login identity
        permissions (list[str] | Unset): [always] The permissions requested for this account: one or more of posts.read,
            posts.write, comments.read, comments.write, messages.read, messages.write, reviews.read, reviews.write,
            analytics.read. null means every permission, including ones added later
        platform (str | Unset): [always] Example: instagram.
        profile_picture_url (str | Unset): [optional] Profile picture URL
        reconnect_reason (str | Unset): [optional] Human-readable reason; only set when Status == "reconnect_required"
        status (str | Unset): [always] One of: active, reconnect_required Example: active.
        username (str | Unset): [always] May equal Name on platforms without a distinct handle Example: acmecorp.
    """

    bio: str | Unset = UNSET
    brand_id: str | Unset = UNSET
    connection_type: SocialApiAiCoreApiConnectorsBaseAccountConnectionType | Unset = UNSET
    effective_permissions: list[str] | Unset = UNSET
    id: str | Unset = UNSET
    login_id: str | Unset = UNSET
    metadata: SocialApiAiCoreApiConnectorsBaseAccountMetadata | Unset = UNSET
    name: str | Unset = UNSET
    page_name: str | Unset = UNSET
    permissions: list[str] | Unset = UNSET
    platform: str | Unset = UNSET
    profile_picture_url: str | Unset = UNSET
    reconnect_reason: str | Unset = UNSET
    status: str | Unset = UNSET
    username: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bio = self.bio

        brand_id = self.brand_id

        connection_type: str | Unset = UNSET
        if not isinstance(self.connection_type, Unset):
            connection_type = self.connection_type.value

        effective_permissions: list[str] | Unset = UNSET
        if not isinstance(self.effective_permissions, Unset):
            effective_permissions = self.effective_permissions

        id = self.id

        login_id = self.login_id

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        name = self.name

        page_name = self.page_name

        permissions: list[str] | Unset = UNSET
        if not isinstance(self.permissions, Unset):
            permissions = self.permissions

        platform = self.platform

        profile_picture_url = self.profile_picture_url

        reconnect_reason = self.reconnect_reason

        status = self.status

        username = self.username

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bio is not UNSET:
            field_dict["bio"] = bio
        if brand_id is not UNSET:
            field_dict["brand_id"] = brand_id
        if connection_type is not UNSET:
            field_dict["connection_type"] = connection_type
        if effective_permissions is not UNSET:
            field_dict["effective_permissions"] = effective_permissions
        if id is not UNSET:
            field_dict["id"] = id
        if login_id is not UNSET:
            field_dict["login_id"] = login_id
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if name is not UNSET:
            field_dict["name"] = name
        if page_name is not UNSET:
            field_dict["page_name"] = page_name
        if permissions is not UNSET:
            field_dict["permissions"] = permissions
        if platform is not UNSET:
            field_dict["platform"] = platform
        if profile_picture_url is not UNSET:
            field_dict["profile_picture_url"] = profile_picture_url
        if reconnect_reason is not UNSET:
            field_dict["reconnect_reason"] = reconnect_reason
        if status is not UNSET:
            field_dict["status"] = status
        if username is not UNSET:
            field_dict["username"] = username

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.social_api_ai_core_api_connectors_base_account_metadata import (
            SocialApiAiCoreApiConnectorsBaseAccountMetadata,  # noqa: PLC0415
        )

        d = dict(src_dict)
        bio = d.pop("bio", UNSET)

        brand_id = d.pop("brand_id", UNSET)

        _connection_type = d.pop("connection_type", UNSET)
        connection_type: SocialApiAiCoreApiConnectorsBaseAccountConnectionType | Unset
        if isinstance(_connection_type, Unset):
            connection_type = UNSET
        else:
            connection_type = SocialApiAiCoreApiConnectorsBaseAccountConnectionType(_connection_type)

        effective_permissions = cast(list[str], d.pop("effective_permissions", UNSET))

        id = d.pop("id", UNSET)

        login_id = d.pop("login_id", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: SocialApiAiCoreApiConnectorsBaseAccountMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = SocialApiAiCoreApiConnectorsBaseAccountMetadata.from_dict(_metadata)

        name = d.pop("name", UNSET)

        page_name = d.pop("page_name", UNSET)

        permissions = cast(list[str], d.pop("permissions", UNSET))

        platform = d.pop("platform", UNSET)

        profile_picture_url = d.pop("profile_picture_url", UNSET)

        reconnect_reason = d.pop("reconnect_reason", UNSET)

        status = d.pop("status", UNSET)

        username = d.pop("username", UNSET)

        social_api_ai_core_api_connectors_base_account = cls(
            bio=bio,
            brand_id=brand_id,
            connection_type=connection_type,
            effective_permissions=effective_permissions,
            id=id,
            login_id=login_id,
            metadata=metadata,
            name=name,
            page_name=page_name,
            permissions=permissions,
            platform=platform,
            profile_picture_url=profile_picture_url,
            reconnect_reason=reconnect_reason,
            status=status,
            username=username,
        )

        social_api_ai_core_api_connectors_base_account.additional_properties = d
        return social_api_ai_core_api_connectors_base_account

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
