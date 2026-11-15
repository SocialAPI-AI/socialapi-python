from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiEndpointsRedirectURIResponse")


@_attrs_define
class ApiEndpointsRedirectURIResponse:
    """
    Attributes:
        created_at (str | Unset):  Example: 2026-04-10T12:00:00Z.
        id (str | Unset):  Example: sapi_ruri_a1b2c3d4e5f6.
        label (str | Unset):  Example: production.
        uri (str | Unset):  Example: https://app.acme.com/oauth/done.
    """

    created_at: str | Unset = UNSET
    id: str | Unset = UNSET
    label: str | Unset = UNSET
    uri: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        id = self.id

        label = self.label

        uri = self.uri

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if id is not UNSET:
            field_dict["id"] = id
        if label is not UNSET:
            field_dict["label"] = label
        if uri is not UNSET:
            field_dict["uri"] = uri

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created_at = d.pop("created_at", UNSET)

        id = d.pop("id", UNSET)

        label = d.pop("label", UNSET)

        uri = d.pop("uri", UNSET)

        api_endpoints_redirect_uri_response = cls(
            created_at=created_at,
            id=id,
            label=label,
            uri=uri,
        )

        api_endpoints_redirect_uri_response.additional_properties = d
        return api_endpoints_redirect_uri_response

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
