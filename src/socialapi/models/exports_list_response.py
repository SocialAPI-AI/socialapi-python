from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.export_item import ExportItem


T = TypeVar("T", bound="ExportsListResponse")


@_attrs_define
class ExportsListResponse:
    """
    Attributes:
        exports (list[ExportItem]):
    """

    exports: list[ExportItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        exports = []
        for exports_item_data in self.exports:
            exports_item = exports_item_data.to_dict()
            exports.append(exports_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "exports": exports,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.export_item import ExportItem  # noqa: PLC0415

        d = dict(src_dict)
        exports = []
        _exports = d.pop("exports")
        for exports_item_data in _exports:
            exports_item = ExportItem.from_dict(exports_item_data)

            exports.append(exports_item)

        exports_list_response = cls(
            exports=exports,
        )

        exports_list_response.additional_properties = d
        return exports_list_response

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
