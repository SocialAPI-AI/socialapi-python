from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiEndpointsExportResultURLs")


@_attrs_define
class ApiEndpointsExportResultURLs:
    """
    Attributes:
        excel_url (str | Unset):
        report_url (str | Unset):
    """

    excel_url: str | Unset = UNSET
    report_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        excel_url = self.excel_url

        report_url = self.report_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if excel_url is not UNSET:
            field_dict["excel_url"] = excel_url
        if report_url is not UNSET:
            field_dict["report_url"] = report_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        excel_url = d.pop("excel_url", UNSET)

        report_url = d.pop("report_url", UNSET)

        api_endpoints_export_result_ur_ls = cls(
            excel_url=excel_url,
            report_url=report_url,
        )

        api_endpoints_export_result_ur_ls.additional_properties = d
        return api_endpoints_export_result_ur_ls

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
