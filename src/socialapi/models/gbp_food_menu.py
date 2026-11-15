from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.gbp_food_menu_section import GBPFoodMenuSection
    from ..models.gbp_menu_label import GBPMenuLabel


T = TypeVar("T", bound="GBPFoodMenu")


@_attrs_define
class GBPFoodMenu:
    """
    Attributes:
        labels (list[GBPMenuLabel] | None):
        sections (list[GBPFoodMenuSection] | None):
        cuisines (list[str] | Unset): Cuisines are Google's Cuisine values, for example ITALIAN or PIZZA.
        source_url (str | Unset):  Example: https://joes.example/menu.
    """

    labels: list[GBPMenuLabel] | None
    sections: list[GBPFoodMenuSection] | None
    cuisines: list[str] | Unset = UNSET
    source_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        labels: list[dict[str, Any]] | None
        if isinstance(self.labels, list):
            labels = []
            for labels_type_0_item_data in self.labels:
                labels_type_0_item = labels_type_0_item_data.to_dict()
                labels.append(labels_type_0_item)

        else:
            labels = self.labels

        sections: list[dict[str, Any]] | None
        if isinstance(self.sections, list):
            sections = []
            for sections_type_0_item_data in self.sections:
                sections_type_0_item = sections_type_0_item_data.to_dict()
                sections.append(sections_type_0_item)

        else:
            sections = self.sections

        cuisines: list[str] | Unset = UNSET
        if not isinstance(self.cuisines, Unset):
            cuisines = self.cuisines

        source_url = self.source_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "labels": labels,
                "sections": sections,
            }
        )
        if cuisines is not UNSET:
            field_dict["cuisines"] = cuisines
        if source_url is not UNSET:
            field_dict["source_url"] = source_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.gbp_food_menu_section import GBPFoodMenuSection  # noqa: PLC0415
        from ..models.gbp_menu_label import GBPMenuLabel  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_labels(data: object) -> list[GBPMenuLabel] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                labels_type_0 = []
                _labels_type_0 = data
                for labels_type_0_item_data in _labels_type_0:
                    labels_type_0_item = GBPMenuLabel.from_dict(labels_type_0_item_data)

                    labels_type_0.append(labels_type_0_item)

                return labels_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[GBPMenuLabel] | None, data)

        labels = _parse_labels(d.pop("labels"))

        def _parse_sections(data: object) -> list[GBPFoodMenuSection] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                sections_type_0 = []
                _sections_type_0 = data
                for sections_type_0_item_data in _sections_type_0:
                    sections_type_0_item = GBPFoodMenuSection.from_dict(sections_type_0_item_data)

                    sections_type_0.append(sections_type_0_item)

                return sections_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[GBPFoodMenuSection] | None, data)

        sections = _parse_sections(d.pop("sections"))

        cuisines = cast(list[str], d.pop("cuisines", UNSET))

        source_url = d.pop("source_url", UNSET)

        gbp_food_menu = cls(
            labels=labels,
            sections=sections,
            cuisines=cuisines,
            source_url=source_url,
        )

        gbp_food_menu.additional_properties = d
        return gbp_food_menu

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
