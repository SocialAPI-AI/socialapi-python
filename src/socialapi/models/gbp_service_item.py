from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.gbp_free_form_service import GBPFreeFormService
    from ..models.gbp_money import GBPMoney
    from ..models.gbp_structured_service import GBPStructuredService


T = TypeVar("T", bound="GBPServiceItem")


@_attrs_define
class GBPServiceItem:
    """
    Attributes:
        free_form_service_item (GBPFreeFormService | Unset):
        price (GBPMoney | Unset):
        structured_service_item (GBPStructuredService | Unset):
    """

    free_form_service_item: GBPFreeFormService | Unset = UNSET
    price: GBPMoney | Unset = UNSET
    structured_service_item: GBPStructuredService | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        free_form_service_item: dict[str, Any] | Unset = UNSET
        if not isinstance(self.free_form_service_item, Unset):
            free_form_service_item = self.free_form_service_item.to_dict()

        price: dict[str, Any] | Unset = UNSET
        if not isinstance(self.price, Unset):
            price = self.price.to_dict()

        structured_service_item: dict[str, Any] | Unset = UNSET
        if not isinstance(self.structured_service_item, Unset):
            structured_service_item = self.structured_service_item.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if free_form_service_item is not UNSET:
            field_dict["free_form_service_item"] = free_form_service_item
        if price is not UNSET:
            field_dict["price"] = price
        if structured_service_item is not UNSET:
            field_dict["structured_service_item"] = structured_service_item

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.gbp_free_form_service import GBPFreeFormService  # noqa: PLC0415
        from ..models.gbp_money import GBPMoney  # noqa: PLC0415
        from ..models.gbp_structured_service import GBPStructuredService  # noqa: PLC0415

        d = dict(src_dict)
        _free_form_service_item = d.pop("free_form_service_item", UNSET)
        free_form_service_item: GBPFreeFormService | Unset
        if isinstance(_free_form_service_item, Unset):
            free_form_service_item = UNSET
        else:
            free_form_service_item = GBPFreeFormService.from_dict(_free_form_service_item)

        _price = d.pop("price", UNSET)
        price: GBPMoney | Unset
        if isinstance(_price, Unset):
            price = UNSET
        else:
            price = GBPMoney.from_dict(_price)

        _structured_service_item = d.pop("structured_service_item", UNSET)
        structured_service_item: GBPStructuredService | Unset
        if isinstance(_structured_service_item, Unset):
            structured_service_item = UNSET
        else:
            structured_service_item = GBPStructuredService.from_dict(_structured_service_item)

        gbp_service_item = cls(
            free_form_service_item=free_form_service_item,
            price=price,
            structured_service_item=structured_service_item,
        )

        gbp_service_item.additional_properties = d
        return gbp_service_item

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
