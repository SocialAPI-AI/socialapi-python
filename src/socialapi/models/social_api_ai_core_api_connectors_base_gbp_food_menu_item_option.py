from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.social_api_ai_core_api_connectors_base_gbp_food_menu_item_attribute import (
        SocialApiAiCoreApiConnectorsBaseGBPFoodMenuItemAttribute,
    )
    from ..models.social_api_ai_core_api_connectors_base_gbp_menu_label import (
        SocialApiAiCoreApiConnectorsBaseGBPMenuLabel,
    )


T = TypeVar("T", bound="SocialApiAiCoreApiConnectorsBaseGBPFoodMenuItemOption")


@_attrs_define
class SocialApiAiCoreApiConnectorsBaseGBPFoodMenuItemOption:
    """
    Attributes:
        attributes (SocialApiAiCoreApiConnectorsBaseGBPFoodMenuItemAttribute | Unset):
        labels (list[SocialApiAiCoreApiConnectorsBaseGBPMenuLabel] | Unset):
    """

    attributes: SocialApiAiCoreApiConnectorsBaseGBPFoodMenuItemAttribute | Unset = UNSET
    labels: list[SocialApiAiCoreApiConnectorsBaseGBPMenuLabel] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        attributes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = self.attributes.to_dict()

        labels: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.labels, Unset):
            labels = []
            for labels_item_data in self.labels:
                labels_item = labels_item_data.to_dict()
                labels.append(labels_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if attributes is not UNSET:
            field_dict["attributes"] = attributes
        if labels is not UNSET:
            field_dict["labels"] = labels

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.social_api_ai_core_api_connectors_base_gbp_food_menu_item_attribute import (
            SocialApiAiCoreApiConnectorsBaseGBPFoodMenuItemAttribute,  # noqa: PLC0415
        )
        from ..models.social_api_ai_core_api_connectors_base_gbp_menu_label import (
            SocialApiAiCoreApiConnectorsBaseGBPMenuLabel,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _attributes = d.pop("attributes", UNSET)
        attributes: SocialApiAiCoreApiConnectorsBaseGBPFoodMenuItemAttribute | Unset
        if isinstance(_attributes, Unset):
            attributes = UNSET
        else:
            attributes = SocialApiAiCoreApiConnectorsBaseGBPFoodMenuItemAttribute.from_dict(_attributes)

        _labels = d.pop("labels", UNSET)
        labels: list[SocialApiAiCoreApiConnectorsBaseGBPMenuLabel] | Unset = UNSET
        if _labels is not UNSET:
            labels = []
            for labels_item_data in _labels:
                labels_item = SocialApiAiCoreApiConnectorsBaseGBPMenuLabel.from_dict(labels_item_data)

                labels.append(labels_item)

        social_api_ai_core_api_connectors_base_gbp_food_menu_item_option = cls(
            attributes=attributes,
            labels=labels,
        )

        social_api_ai_core_api_connectors_base_gbp_food_menu_item_option.additional_properties = d
        return social_api_ai_core_api_connectors_base_gbp_food_menu_item_option

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
