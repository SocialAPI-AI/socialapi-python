from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.api_endpoints_whats_app_template_create_response_category import (
    ApiEndpointsWhatsAppTemplateCreateResponseCategory,
)
from ..models.api_endpoints_whats_app_template_create_response_status import (
    ApiEndpointsWhatsAppTemplateCreateResponseStatus,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiEndpointsWhatsAppTemplateCreateResponse")


@_attrs_define
class ApiEndpointsWhatsAppTemplateCreateResponse:
    """
    Attributes:
        category (ApiEndpointsWhatsAppTemplateCreateResponseCategory | Unset):  Example: UTILITY.
        id (str | Unset):  Example: 1234567890123456.
        status (ApiEndpointsWhatsAppTemplateCreateResponseStatus | Unset):  Example: PENDING.
    """

    category: ApiEndpointsWhatsAppTemplateCreateResponseCategory | Unset = UNSET
    id: str | Unset = UNSET
    status: ApiEndpointsWhatsAppTemplateCreateResponseStatus | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        category: str | Unset = UNSET
        if not isinstance(self.category, Unset):
            category = self.category.value

        id = self.id

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if category is not UNSET:
            field_dict["category"] = category
        if id is not UNSET:
            field_dict["id"] = id
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _category = d.pop("category", UNSET)
        category: ApiEndpointsWhatsAppTemplateCreateResponseCategory | Unset
        if isinstance(_category, Unset):
            category = UNSET
        else:
            category = ApiEndpointsWhatsAppTemplateCreateResponseCategory(_category)

        id = d.pop("id", UNSET)

        _status = d.pop("status", UNSET)
        status: ApiEndpointsWhatsAppTemplateCreateResponseStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ApiEndpointsWhatsAppTemplateCreateResponseStatus(_status)

        api_endpoints_whats_app_template_create_response = cls(
            category=category,
            id=id,
            status=status,
        )

        api_endpoints_whats_app_template_create_response.additional_properties = d
        return api_endpoints_whats_app_template_create_response

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
