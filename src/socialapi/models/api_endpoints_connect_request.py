from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.api_endpoints_connect_request_onboarding import ApiEndpointsConnectRequestOnboarding
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_endpoints_connect_request_metadata import ApiEndpointsConnectRequestMetadata


T = TypeVar("T", bound="ApiEndpointsConnectRequest")


@_attrs_define
class ApiEndpointsConnectRequest:
    """
    Attributes:
        brand_id (str | Unset): BrandID optionally specifies which brand to attach the account to. If omitted, a new
            brand is auto-created. Example: b_01HZ9X3Q4R5M6N7P8V2K0W1J.
        metadata (ApiEndpointsConnectRequestMetadata | Unset): Metadata contains platform-specific connection data. For
            tiktok, connection_type "creator" connects through TikTok's Content Posting API instead of the default Business
            API ("business"). For linkedin, connection_type "profile" or "organization" limits the connect to the member
            profile or to company Pages; without it, one authorization offers both, and the user picks one when there are
            several.
        onboarding (ApiEndpointsConnectRequestOnboarding | Unset): Onboarding applies to WhatsApp only. cloud_api
            (default) connects the number for use through the API alone. business_app connects a number that stays in use on
            the WhatsApp Business app, and imports its recent chats. Example: cloud_api.
        permissions (list[str] | Unset): Permissions are the permissions to request for this account. If omitted, the
            brand's existing selection for this platform applies, and a brand with none gets every permission. Valid values:
            posts.read, posts.write, comments.read, comments.write, messages.read, messages.write, reviews.read,
            reviews.write, analytics.read. Example: ['comments.read', 'comments.write'].
        platform (str | Unset): Platform identifies the social platform to connect (e.g. instagram, facebook, google,
            threads, tiktok, linkedin). Example: instagram.
        redirect_uri (str | Unset): RedirectURI is the customer's URL to redirect the user to after OAuth completes.
            If you have registered redirect URIs in the dashboard, the value must match one of them.
            If you have none registered, any valid https URI is accepted. If omitted, the default HTML success page is
            shown. Example: https://app.acme.com/oauth/done.
        state (str | Unset): CustomerState is an opaque value echoed back to the customer's redirect URI. Max 512 chars.
            Example: session_abc123.
    """

    brand_id: str | Unset = UNSET
    metadata: ApiEndpointsConnectRequestMetadata | Unset = UNSET
    onboarding: ApiEndpointsConnectRequestOnboarding | Unset = UNSET
    permissions: list[str] | Unset = UNSET
    platform: str | Unset = UNSET
    redirect_uri: str | Unset = UNSET
    state: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        brand_id = self.brand_id

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        onboarding: str | Unset = UNSET
        if not isinstance(self.onboarding, Unset):
            onboarding = self.onboarding.value

        permissions: list[str] | Unset = UNSET
        if not isinstance(self.permissions, Unset):
            permissions = self.permissions

        platform = self.platform

        redirect_uri = self.redirect_uri

        state = self.state

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if brand_id is not UNSET:
            field_dict["brand_id"] = brand_id
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if onboarding is not UNSET:
            field_dict["onboarding"] = onboarding
        if permissions is not UNSET:
            field_dict["permissions"] = permissions
        if platform is not UNSET:
            field_dict["platform"] = platform
        if redirect_uri is not UNSET:
            field_dict["redirect_uri"] = redirect_uri
        if state is not UNSET:
            field_dict["state"] = state

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_endpoints_connect_request_metadata import ApiEndpointsConnectRequestMetadata  # noqa: PLC0415

        d = dict(src_dict)
        brand_id = d.pop("brand_id", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: ApiEndpointsConnectRequestMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = ApiEndpointsConnectRequestMetadata.from_dict(_metadata)

        _onboarding = d.pop("onboarding", UNSET)
        onboarding: ApiEndpointsConnectRequestOnboarding | Unset
        if isinstance(_onboarding, Unset):
            onboarding = UNSET
        else:
            onboarding = ApiEndpointsConnectRequestOnboarding(_onboarding)

        permissions = cast(list[str], d.pop("permissions", UNSET))

        platform = d.pop("platform", UNSET)

        redirect_uri = d.pop("redirect_uri", UNSET)

        state = d.pop("state", UNSET)

        api_endpoints_connect_request = cls(
            brand_id=brand_id,
            metadata=metadata,
            onboarding=onboarding,
            permissions=permissions,
            platform=platform,
            redirect_uri=redirect_uri,
            state=state,
        )

        api_endpoints_connect_request.additional_properties = d
        return api_endpoints_connect_request

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
