from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ApiEndpointsConnectRequestMetadata")


@_attrs_define
class ApiEndpointsConnectRequestMetadata:
    """Metadata contains platform-specific connection data. For tiktok, connection_type "creator" connects through TikTok's
    Content Posting API instead of the default Business API ("business"). For linkedin, connection_type "profile" or
    "organization" limits the connect to the member profile or to company Pages; without it, one authorization offers
    both, and the user picks one when there are several.

    """

    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        api_endpoints_connect_request_metadata = cls()

        api_endpoints_connect_request_metadata.additional_properties = d
        return api_endpoints_connect_request_metadata

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
