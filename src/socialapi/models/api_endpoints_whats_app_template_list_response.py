from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_endpoints_whats_app_template_info import ApiEndpointsWhatsAppTemplateInfo
    from ..models.api_endpoints_whats_app_template_list_paging import ApiEndpointsWhatsAppTemplateListPaging


T = TypeVar("T", bound="ApiEndpointsWhatsAppTemplateListResponse")


@_attrs_define
class ApiEndpointsWhatsAppTemplateListResponse:
    """
    Attributes:
        data (list[ApiEndpointsWhatsAppTemplateInfo] | Unset):
        paging (ApiEndpointsWhatsAppTemplateListPaging | Unset):
    """

    data: list[ApiEndpointsWhatsAppTemplateInfo] | Unset = UNSET
    paging: ApiEndpointsWhatsAppTemplateListPaging | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item = data_item_data.to_dict()
                data.append(data_item)

        paging: dict[str, Any] | Unset = UNSET
        if not isinstance(self.paging, Unset):
            paging = self.paging.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data
        if paging is not UNSET:
            field_dict["paging"] = paging

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_endpoints_whats_app_template_info import ApiEndpointsWhatsAppTemplateInfo  # noqa: PLC0415
        from ..models.api_endpoints_whats_app_template_list_paging import (
            ApiEndpointsWhatsAppTemplateListPaging,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _data = d.pop("data", UNSET)
        data: list[ApiEndpointsWhatsAppTemplateInfo] | Unset = UNSET
        if _data is not UNSET:
            data = []
            for data_item_data in _data:
                data_item = ApiEndpointsWhatsAppTemplateInfo.from_dict(data_item_data)

                data.append(data_item)

        _paging = d.pop("paging", UNSET)
        paging: ApiEndpointsWhatsAppTemplateListPaging | Unset
        if isinstance(_paging, Unset):
            paging = UNSET
        else:
            paging = ApiEndpointsWhatsAppTemplateListPaging.from_dict(_paging)

        api_endpoints_whats_app_template_list_response = cls(
            data=data,
            paging=paging,
        )

        api_endpoints_whats_app_template_list_response.additional_properties = d
        return api_endpoints_whats_app_template_list_response

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
