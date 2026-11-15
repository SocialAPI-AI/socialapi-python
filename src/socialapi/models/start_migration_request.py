from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="StartMigrationRequest")


@_attrs_define
class StartMigrationRequest:
    """
    Attributes:
        authorisation_version (str): Version of the authorisation text you accepted, as returned in
            `authorisation.version`.
        key (str): API key from your account with that provider. It needs read access to profiles and accounts.
        provider (str): Identifier of the provider you are moving from.
    """

    authorisation_version: str
    key: str
    provider: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        authorisation_version = self.authorisation_version

        key = self.key

        provider = self.provider

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "authorisation_version": authorisation_version,
                "key": key,
                "provider": provider,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        authorisation_version = d.pop("authorisation_version")

        key = d.pop("key")

        provider = d.pop("provider")

        start_migration_request = cls(
            authorisation_version=authorisation_version,
            key=key,
            provider=provider,
        )

        start_migration_request.additional_properties = d
        return start_migration_request

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
