from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.api_endpoints_whats_app_request_code_request_method import ApiEndpointsWhatsAppRequestCodeRequestMethod
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiEndpointsWhatsAppRequestCodeRequest")


@_attrs_define
class ApiEndpointsWhatsAppRequestCodeRequest:
    """
    Attributes:
        language (str | Unset): Language is the BCP-47 locale used for the verification message (e.g. en_US, fr_FR).
            Example: en_US.
        method (ApiEndpointsWhatsAppRequestCodeRequestMethod | Unset): Method is the verification channel. WhatsApp
            Business API requires SMS or VOICE. Example: SMS.
    """

    language: str | Unset = UNSET
    method: ApiEndpointsWhatsAppRequestCodeRequestMethod | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        language = self.language

        method: str | Unset = UNSET
        if not isinstance(self.method, Unset):
            method = self.method.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if language is not UNSET:
            field_dict["language"] = language
        if method is not UNSET:
            field_dict["method"] = method

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        language = d.pop("language", UNSET)

        _method = d.pop("method", UNSET)
        method: ApiEndpointsWhatsAppRequestCodeRequestMethod | Unset
        if isinstance(_method, Unset):
            method = UNSET
        else:
            method = ApiEndpointsWhatsAppRequestCodeRequestMethod(_method)

        api_endpoints_whats_app_request_code_request = cls(
            language=language,
            method=method,
        )

        api_endpoints_whats_app_request_code_request.additional_properties = d
        return api_endpoints_whats_app_request_code_request

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
