from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_endpoints_connect_o_auth_response_metadata import ApiEndpointsConnectOAuthResponseMetadata


T = TypeVar("T", bound="ApiEndpointsConnectOAuthResponse")


@_attrs_define
class ApiEndpointsConnectOAuthResponse:
    """
    Attributes:
        auth_url (str | Unset):  Example: https://www.instagram.com/oauth/authorize/?....
        message (str | Unset):  Example: Redirect the user to auth_url.
        metadata (ApiEndpointsConnectOAuthResponseMetadata | Unset):
        state (str | Unset):  Example: 4a8f2c1e9b3d7f06a5c2e8b4d1f3a7e2.
    """

    auth_url: str | Unset = UNSET
    message: str | Unset = UNSET
    metadata: ApiEndpointsConnectOAuthResponseMetadata | Unset = UNSET
    state: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        auth_url = self.auth_url

        message = self.message

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        state = self.state

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if auth_url is not UNSET:
            field_dict["auth_url"] = auth_url
        if message is not UNSET:
            field_dict["message"] = message
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if state is not UNSET:
            field_dict["state"] = state

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_endpoints_connect_o_auth_response_metadata import (
            ApiEndpointsConnectOAuthResponseMetadata,  # noqa: PLC0415
        )

        d = dict(src_dict)
        auth_url = d.pop("auth_url", UNSET)

        message = d.pop("message", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: ApiEndpointsConnectOAuthResponseMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = ApiEndpointsConnectOAuthResponseMetadata.from_dict(_metadata)

        state = d.pop("state", UNSET)

        api_endpoints_connect_o_auth_response = cls(
            auth_url=auth_url,
            message=message,
            metadata=metadata,
            state=state,
        )

        api_endpoints_connect_o_auth_response.additional_properties = d
        return api_endpoints_connect_o_auth_response

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
