from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_endpoints_exchange_request_metadata import ApiEndpointsExchangeRequestMetadata


T = TypeVar("T", bound="ApiEndpointsExchangeRequest")


@_attrs_define
class ApiEndpointsExchangeRequest:
    """
    Attributes:
        code (str | Unset): Code is the authorization code received from the platform callback. Example: AQDtbPB9X....
        metadata (ApiEndpointsExchangeRequestMetadata | Unset): Metadata must include redirect_uri and state for CSRF
            validation.
        platform (str | Unset): Platform identifies the social platform (must match the connect call). Example:
            instagram.
    """

    code: str | Unset = UNSET
    metadata: ApiEndpointsExchangeRequestMetadata | Unset = UNSET
    platform: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        platform = self.platform

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if platform is not UNSET:
            field_dict["platform"] = platform

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_endpoints_exchange_request_metadata import (
            ApiEndpointsExchangeRequestMetadata,  # noqa: PLC0415
        )

        d = dict(src_dict)
        code = d.pop("code", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: ApiEndpointsExchangeRequestMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = ApiEndpointsExchangeRequestMetadata.from_dict(_metadata)

        platform = d.pop("platform", UNSET)

        api_endpoints_exchange_request = cls(
            code=code,
            metadata=metadata,
            platform=platform,
        )

        api_endpoints_exchange_request.additional_properties = d
        return api_endpoints_exchange_request

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
