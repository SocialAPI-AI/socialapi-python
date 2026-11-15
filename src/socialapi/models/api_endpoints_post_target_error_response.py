from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.api_endpoints_post_target_error_response_category import ApiEndpointsPostTargetErrorResponseCategory
from ..models.api_endpoints_post_target_error_response_caused_by import ApiEndpointsPostTargetErrorResponseCausedBy
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiEndpointsPostTargetErrorResponse")


@_attrs_define
class ApiEndpointsPostTargetErrorResponse:
    """
    Attributes:
        category (ApiEndpointsPostTargetErrorResponseCategory | Unset):  Example: validation.
        caused_by (ApiEndpointsPostTargetErrorResponseCausedBy | Unset):  Example: user.
        code (str | Unset):  Example: platform.tiktok.media_required.
        message (str | Unset):  Example: Video posts require at least one media URL.
    """

    category: ApiEndpointsPostTargetErrorResponseCategory | Unset = UNSET
    caused_by: ApiEndpointsPostTargetErrorResponseCausedBy | Unset = UNSET
    code: str | Unset = UNSET
    message: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        category: str | Unset = UNSET
        if not isinstance(self.category, Unset):
            category = self.category.value

        caused_by: str | Unset = UNSET
        if not isinstance(self.caused_by, Unset):
            caused_by = self.caused_by.value

        code = self.code

        message = self.message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if category is not UNSET:
            field_dict["category"] = category
        if caused_by is not UNSET:
            field_dict["caused_by"] = caused_by
        if code is not UNSET:
            field_dict["code"] = code
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _category = d.pop("category", UNSET)
        category: ApiEndpointsPostTargetErrorResponseCategory | Unset
        if isinstance(_category, Unset):
            category = UNSET
        else:
            category = ApiEndpointsPostTargetErrorResponseCategory(_category)

        _caused_by = d.pop("caused_by", UNSET)
        caused_by: ApiEndpointsPostTargetErrorResponseCausedBy | Unset
        if isinstance(_caused_by, Unset):
            caused_by = UNSET
        else:
            caused_by = ApiEndpointsPostTargetErrorResponseCausedBy(_caused_by)

        code = d.pop("code", UNSET)

        message = d.pop("message", UNSET)

        api_endpoints_post_target_error_response = cls(
            category=category,
            caused_by=caused_by,
            code=code,
            message=message,
        )

        api_endpoints_post_target_error_response.additional_properties = d
        return api_endpoints_post_target_error_response

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
