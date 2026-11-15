from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiEndpointsCreateRedirectURIRequest")


@_attrs_define
class ApiEndpointsCreateRedirectURIRequest:
    """
    Attributes:
        label (str | Unset): Label is an optional human-readable label for this URI. Example: production.
        uri (str | Unset): URI is the redirect URI to whitelist (must be https, or http for localhost). Example:
            https://app.acme.com/oauth/done.
    """

    label: str | Unset = UNSET
    uri: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        label = self.label

        uri = self.uri

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if label is not UNSET:
            field_dict["label"] = label
        if uri is not UNSET:
            field_dict["uri"] = uri

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        label = d.pop("label", UNSET)

        uri = d.pop("uri", UNSET)

        api_endpoints_create_redirect_uri_request = cls(
            label=label,
            uri=uri,
        )

        api_endpoints_create_redirect_uri_request.additional_properties = d
        return api_endpoints_create_redirect_uri_request

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
