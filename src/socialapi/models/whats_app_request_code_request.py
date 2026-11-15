from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.whats_app_verification_method import WhatsAppVerificationMethod

T = TypeVar("T", bound="WhatsAppRequestCodeRequest")


@_attrs_define
class WhatsAppRequestCodeRequest:
    """
    Attributes:
        language (str): Language is the BCP-47 locale used for the verification message (e.g. en_US, fr_FR). Example:
            en_US.
        method (WhatsAppVerificationMethod):
    """

    language: str
    method: WhatsAppVerificationMethod
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        language = self.language

        method = self.method.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "language": language,
                "method": method,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        language = d.pop("language")

        method = WhatsAppVerificationMethod(d.pop("method"))

        whats_app_request_code_request = cls(
            language=language,
            method=method,
        )

        whats_app_request_code_request.additional_properties = d
        return whats_app_request_code_request

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
