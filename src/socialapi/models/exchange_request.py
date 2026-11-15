from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.platform import Platform

if TYPE_CHECKING:
    from ..models.exchange_request_metadata import ExchangeRequestMetadata


T = TypeVar("T", bound="ExchangeRequest")


@_attrs_define
class ExchangeRequest:
    """
    Attributes:
        code (str): Code is the authorization code received from the platform callback. Example: AQDtbPB9X....
        metadata (ExchangeRequestMetadata): Metadata must include redirect_uri and state for CSRF validation.
        platform (Platform):
    """

    code: str
    metadata: ExchangeRequestMetadata
    platform: Platform
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        metadata = self.metadata.to_dict()

        platform = self.platform.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
                "metadata": metadata,
                "platform": platform,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.exchange_request_metadata import ExchangeRequestMetadata  # noqa: PLC0415

        d = dict(src_dict)
        code = d.pop("code")

        metadata = ExchangeRequestMetadata.from_dict(d.pop("metadata"))

        platform = Platform(d.pop("platform"))

        exchange_request = cls(
            code=code,
            metadata=metadata,
            platform=platform,
        )

        exchange_request.additional_properties = d
        return exchange_request

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
