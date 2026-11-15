from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.social_api_ai_core_api_connectors_base_gbp_food_menu_section import (
        SocialApiAiCoreApiConnectorsBaseGBPFoodMenuSection,
    )
    from ..models.social_api_ai_core_api_connectors_base_gbp_menu_label import (
        SocialApiAiCoreApiConnectorsBaseGBPMenuLabel,
    )


T = TypeVar("T", bound="SocialApiAiCoreApiConnectorsBaseGBPFoodMenu")


@_attrs_define
class SocialApiAiCoreApiConnectorsBaseGBPFoodMenu:
    """
    Attributes:
        cuisines (list[str] | Unset): Cuisines are Google's Cuisine values, for example ITALIAN or PIZZA.
        labels (list[SocialApiAiCoreApiConnectorsBaseGBPMenuLabel] | Unset):
        sections (list[SocialApiAiCoreApiConnectorsBaseGBPFoodMenuSection] | Unset):
        source_url (str | Unset):  Example: https://joes.example/menu.
    """

    cuisines: list[str] | Unset = UNSET
    labels: list[SocialApiAiCoreApiConnectorsBaseGBPMenuLabel] | Unset = UNSET
    sections: list[SocialApiAiCoreApiConnectorsBaseGBPFoodMenuSection] | Unset = UNSET
    source_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cuisines: list[str] | Unset = UNSET
        if not isinstance(self.cuisines, Unset):
            cuisines = self.cuisines

        labels: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.labels, Unset):
            labels = []
            for labels_item_data in self.labels:
                labels_item = labels_item_data.to_dict()
                labels.append(labels_item)

        sections: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.sections, Unset):
            sections = []
            for sections_item_data in self.sections:
                sections_item = sections_item_data.to_dict()
                sections.append(sections_item)

        source_url = self.source_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cuisines is not UNSET:
            field_dict["cuisines"] = cuisines
        if labels is not UNSET:
            field_dict["labels"] = labels
        if sections is not UNSET:
            field_dict["sections"] = sections
        if source_url is not UNSET:
            field_dict["source_url"] = source_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.social_api_ai_core_api_connectors_base_gbp_food_menu_section import (
            SocialApiAiCoreApiConnectorsBaseGBPFoodMenuSection,  # noqa: PLC0415
        )
        from ..models.social_api_ai_core_api_connectors_base_gbp_menu_label import (
            SocialApiAiCoreApiConnectorsBaseGBPMenuLabel,  # noqa: PLC0415
        )

        d = dict(src_dict)
        cuisines = cast(list[str], d.pop("cuisines", UNSET))

        _labels = d.pop("labels", UNSET)
        labels: list[SocialApiAiCoreApiConnectorsBaseGBPMenuLabel] | Unset = UNSET
        if _labels is not UNSET:
            labels = []
            for labels_item_data in _labels:
                labels_item = SocialApiAiCoreApiConnectorsBaseGBPMenuLabel.from_dict(labels_item_data)

                labels.append(labels_item)

        _sections = d.pop("sections", UNSET)
        sections: list[SocialApiAiCoreApiConnectorsBaseGBPFoodMenuSection] | Unset = UNSET
        if _sections is not UNSET:
            sections = []
            for sections_item_data in _sections:
                sections_item = SocialApiAiCoreApiConnectorsBaseGBPFoodMenuSection.from_dict(sections_item_data)

                sections.append(sections_item)

        source_url = d.pop("source_url", UNSET)

        social_api_ai_core_api_connectors_base_gbp_food_menu = cls(
            cuisines=cuisines,
            labels=labels,
            sections=sections,
            source_url=source_url,
        )

        social_api_ai_core_api_connectors_base_gbp_food_menu.additional_properties = d
        return social_api_ai_core_api_connectors_base_gbp_food_menu

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
