from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.social_api_ai_core_api_connectors_base_gbp_free_form_service import (
        SocialApiAiCoreApiConnectorsBaseGBPFreeFormService,
    )
    from ..models.social_api_ai_core_api_connectors_base_gbp_money import SocialApiAiCoreApiConnectorsBaseGBPMoney
    from ..models.social_api_ai_core_api_connectors_base_gbp_structured_service import (
        SocialApiAiCoreApiConnectorsBaseGBPStructuredService,
    )


T = TypeVar("T", bound="SocialApiAiCoreApiConnectorsBaseGBPServiceItem")


@_attrs_define
class SocialApiAiCoreApiConnectorsBaseGBPServiceItem:
    """
    Attributes:
        free_form_service_item (SocialApiAiCoreApiConnectorsBaseGBPFreeFormService | Unset):
        price (SocialApiAiCoreApiConnectorsBaseGBPMoney | Unset):
        structured_service_item (SocialApiAiCoreApiConnectorsBaseGBPStructuredService | Unset):
    """

    free_form_service_item: SocialApiAiCoreApiConnectorsBaseGBPFreeFormService | Unset = UNSET
    price: SocialApiAiCoreApiConnectorsBaseGBPMoney | Unset = UNSET
    structured_service_item: SocialApiAiCoreApiConnectorsBaseGBPStructuredService | Unset = UNSET
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
        from ..models.social_api_ai_core_api_connectors_base_gbp_free_form_service import (
            SocialApiAiCoreApiConnectorsBaseGBPFreeFormService,  # noqa: PLC0415
        )
        from ..models.social_api_ai_core_api_connectors_base_gbp_money import (
            SocialApiAiCoreApiConnectorsBaseGBPMoney,  # noqa: PLC0415
        )
        from ..models.social_api_ai_core_api_connectors_base_gbp_structured_service import (
            SocialApiAiCoreApiConnectorsBaseGBPStructuredService,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _free_form_service_item = d.pop("free_form_service_item", UNSET)
        free_form_service_item: SocialApiAiCoreApiConnectorsBaseGBPFreeFormService | Unset
        if isinstance(_free_form_service_item, Unset):
            free_form_service_item = UNSET
        else:
            free_form_service_item = SocialApiAiCoreApiConnectorsBaseGBPFreeFormService.from_dict(
                _free_form_service_item
            )

        _price = d.pop("price", UNSET)
        price: SocialApiAiCoreApiConnectorsBaseGBPMoney | Unset
        if isinstance(_price, Unset):
            price = UNSET
        else:
            price = SocialApiAiCoreApiConnectorsBaseGBPMoney.from_dict(_price)

        _structured_service_item = d.pop("structured_service_item", UNSET)
        structured_service_item: SocialApiAiCoreApiConnectorsBaseGBPStructuredService | Unset
        if isinstance(_structured_service_item, Unset):
            structured_service_item = UNSET
        else:
            structured_service_item = SocialApiAiCoreApiConnectorsBaseGBPStructuredService.from_dict(
                _structured_service_item
            )

        social_api_ai_core_api_connectors_base_gbp_service_item = cls(
            free_form_service_item=free_form_service_item,
            price=price,
            structured_service_item=structured_service_item,
        )

        social_api_ai_core_api_connectors_base_gbp_service_item.additional_properties = d
        return social_api_ai_core_api_connectors_base_gbp_service_item

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
