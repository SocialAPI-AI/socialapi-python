from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RedirectURIResponse")


@_attrs_define
class RedirectURIResponse:
    """
    Attributes:
        created_at (str):  Example: 2026-04-10T12:00:00Z.
        id (str):  Example: sapi_ruri_a1b2c3d4e5f6.
        uri (str):  Example: https://app.acme.com/oauth/done.
        label (str | Unset):  Example: production.
    """

    created_at: str
    id: str
    uri: str
    label: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        id = self.id

        uri = self.uri

        label = self.label

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_at": created_at,
                "id": id,
                "uri": uri,
            }
        )
        if label is not UNSET:
            field_dict["label"] = label

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created_at = d.pop("created_at")

        id = d.pop("id")

        uri = d.pop("uri")

        label = d.pop("label", UNSET)

        redirect_uri_response = cls(
            created_at=created_at,
            id=id,
            uri=uri,
            label=label,
        )

        redirect_uri_response.additional_properties = d
        return redirect_uri_response

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
