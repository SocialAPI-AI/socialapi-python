from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.connect_o_auth_response_metadata import ConnectOAuthResponseMetadata


T = TypeVar("T", bound="ConnectOAuthResponse")


@_attrs_define
class ConnectOAuthResponse:
    """
    Attributes:
        auth_url (str):  Example: https://www.instagram.com/oauth/authorize/?....
        message (str):  Example: Redirect the user to auth_url.
        state (str):  Example: 4a8f2c1e9b3d7f06a5c2e8b4d1f3a7e2.
        metadata (ConnectOAuthResponseMetadata | Unset):
    """

    auth_url: str
    message: str
    state: str
    metadata: ConnectOAuthResponseMetadata | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        auth_url = self.auth_url

        message = self.message

        state = self.state

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "auth_url": auth_url,
                "message": message,
                "state": state,
            }
        )
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.connect_o_auth_response_metadata import ConnectOAuthResponseMetadata  # noqa: PLC0415

        d = dict(src_dict)
        auth_url = d.pop("auth_url")

        message = d.pop("message")

        state = d.pop("state")

        _metadata = d.pop("metadata", UNSET)
        metadata: ConnectOAuthResponseMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = ConnectOAuthResponseMetadata.from_dict(_metadata)

        connect_o_auth_response = cls(
            auth_url=auth_url,
            message=message,
            state=state,
            metadata=metadata,
        )

        connect_o_auth_response.additional_properties = d
        return connect_o_auth_response

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
