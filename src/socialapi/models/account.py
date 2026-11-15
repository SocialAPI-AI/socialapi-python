from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.connection_type import ConnectionType
from ..models.platform import Platform
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.account_metadata import AccountMetadata


T = TypeVar("T", bound="Account")


@_attrs_define
class Account:
    """
    Attributes:
        brand_id (str): [always] SocialAPI brand ID this account belongs to
        effective_permissions (list[str] | None): [always] The permissions this account can use right now: the requested
            permissions the platform supports, minus any the platform did not grant or has since refused. Uses the same
            names as permissions. An empty list when none apply
        id (str): [always] Example: acc_01HZ9X3Q4R5M6N7P8V2K0W1J.
        name (str): [always] Display name of the account or page Example: Acme Corp.
        permissions (list[str] | None): [always] The permissions requested for this account: one or more of posts.read,
            posts.write, comments.read, comments.write, messages.read, messages.write, reviews.read, reviews.write,
            analytics.read. null means every permission, including ones added later
        platform (Platform):
        status (str): [always] One of: active, reconnect_required Example: active.
        username (str): [always] May equal Name on platforms without a distinct handle Example: acmecorp.
        bio (str | Unset): [optional] Profile biography or description
        connection_type (ConnectionType | Unset):
        login_id (str | Unset): [optional] Login id shared by accounts connected in the same authorization (facebook,
            google, linkedin)
        metadata (AccountMetadata | Unset): [optional] Platform-specific keys for this account
        page_name (str | Unset): [optional] Name of the single active page bound to this account; set only when exactly
            one page is active (e.g. facebook), so clients can label the tile with the page instead of the login identity
        profile_picture_url (str | Unset): [optional] Profile picture URL
        reconnect_reason (str | Unset): [optional] Human-readable reason; only set when Status == "reconnect_required"
    """

    brand_id: str
    effective_permissions: list[str] | None
    id: str
    name: str
    permissions: list[str] | None
    platform: Platform
    status: str
    username: str
    bio: str | Unset = UNSET
    connection_type: ConnectionType | Unset = UNSET
    login_id: str | Unset = UNSET
    metadata: AccountMetadata | Unset = UNSET
    page_name: str | Unset = UNSET
    profile_picture_url: str | Unset = UNSET
    reconnect_reason: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        brand_id = self.brand_id

        effective_permissions: list[str] | None
        if isinstance(self.effective_permissions, list):
            effective_permissions = self.effective_permissions

        else:
            effective_permissions = self.effective_permissions

        id = self.id

        name = self.name

        permissions: list[str] | None
        if isinstance(self.permissions, list):
            permissions = self.permissions

        else:
            permissions = self.permissions

        platform = self.platform.value

        status = self.status

        username = self.username

        bio = self.bio

        connection_type: str | Unset = UNSET
        if not isinstance(self.connection_type, Unset):
            connection_type = self.connection_type.value

        login_id = self.login_id

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        page_name = self.page_name

        profile_picture_url = self.profile_picture_url

        reconnect_reason = self.reconnect_reason

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "brand_id": brand_id,
                "effective_permissions": effective_permissions,
                "id": id,
                "name": name,
                "permissions": permissions,
                "platform": platform,
                "status": status,
                "username": username,
            }
        )
        if bio is not UNSET:
            field_dict["bio"] = bio
        if connection_type is not UNSET:
            field_dict["connection_type"] = connection_type
        if login_id is not UNSET:
            field_dict["login_id"] = login_id
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if page_name is not UNSET:
            field_dict["page_name"] = page_name
        if profile_picture_url is not UNSET:
            field_dict["profile_picture_url"] = profile_picture_url
        if reconnect_reason is not UNSET:
            field_dict["reconnect_reason"] = reconnect_reason

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.account_metadata import AccountMetadata  # noqa: PLC0415

        d = dict(src_dict)
        brand_id = d.pop("brand_id")

        def _parse_effective_permissions(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                effective_permissions_type_0 = cast(list[str], data)

                return effective_permissions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        effective_permissions = _parse_effective_permissions(d.pop("effective_permissions"))

        id = d.pop("id")

        name = d.pop("name")

        def _parse_permissions(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                permissions_type_0 = cast(list[str], data)

                return permissions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        permissions = _parse_permissions(d.pop("permissions"))

        platform = Platform(d.pop("platform"))

        status = d.pop("status")

        username = d.pop("username")

        bio = d.pop("bio", UNSET)

        _connection_type = d.pop("connection_type", UNSET)
        connection_type: ConnectionType | Unset
        if isinstance(_connection_type, Unset):
            connection_type = UNSET
        else:
            connection_type = ConnectionType(_connection_type)

        login_id = d.pop("login_id", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: AccountMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = AccountMetadata.from_dict(_metadata)

        page_name = d.pop("page_name", UNSET)

        profile_picture_url = d.pop("profile_picture_url", UNSET)

        reconnect_reason = d.pop("reconnect_reason", UNSET)

        account = cls(
            brand_id=brand_id,
            effective_permissions=effective_permissions,
            id=id,
            name=name,
            permissions=permissions,
            platform=platform,
            status=status,
            username=username,
            bio=bio,
            connection_type=connection_type,
            login_id=login_id,
            metadata=metadata,
            page_name=page_name,
            profile_picture_url=profile_picture_url,
            reconnect_reason=reconnect_reason,
        )

        account.additional_properties = d
        return account

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
