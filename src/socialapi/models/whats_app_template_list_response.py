from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.whats_app_template_info import WhatsAppTemplateInfo
    from ..models.whats_app_template_list_paging import WhatsAppTemplateListPaging


T = TypeVar("T", bound="WhatsAppTemplateListResponse")


@_attrs_define
class WhatsAppTemplateListResponse:
    """
    Attributes:
        data (list[WhatsAppTemplateInfo] | None):
        paging (WhatsAppTemplateListPaging | Unset):
    """

    data: list[WhatsAppTemplateInfo] | None
    paging: WhatsAppTemplateListPaging | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data: list[dict[str, Any]] | None
        if isinstance(self.data, list):
            data = []
            for data_type_0_item_data in self.data:
                data_type_0_item = data_type_0_item_data.to_dict()
                data.append(data_type_0_item)

        else:
            data = self.data

        paging: dict[str, Any] | Unset = UNSET
        if not isinstance(self.paging, Unset):
            paging = self.paging.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
            }
        )
        if paging is not UNSET:
            field_dict["paging"] = paging

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.whats_app_template_info import WhatsAppTemplateInfo  # noqa: PLC0415
        from ..models.whats_app_template_list_paging import WhatsAppTemplateListPaging  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_data(data: object) -> list[WhatsAppTemplateInfo] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                data_type_0 = []
                _data_type_0 = data
                for data_type_0_item_data in _data_type_0:
                    data_type_0_item = WhatsAppTemplateInfo.from_dict(data_type_0_item_data)

                    data_type_0.append(data_type_0_item)

                return data_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[WhatsAppTemplateInfo] | None, data)

        data = _parse_data(d.pop("data"))

        _paging = d.pop("paging", UNSET)
        paging: WhatsAppTemplateListPaging | Unset
        if isinstance(_paging, Unset):
            paging = UNSET
        else:
            paging = WhatsAppTemplateListPaging.from_dict(_paging)

        whats_app_template_list_response = cls(
            data=data,
            paging=paging,
        )

        whats_app_template_list_response.additional_properties = d
        return whats_app_template_list_response

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
