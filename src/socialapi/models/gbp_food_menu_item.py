from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.gbp_food_menu_item_attribute import GBPFoodMenuItemAttribute
    from ..models.gbp_food_menu_item_option import GBPFoodMenuItemOption
    from ..models.gbp_menu_label import GBPMenuLabel


T = TypeVar("T", bound="GBPFoodMenuItem")


@_attrs_define
class GBPFoodMenuItem:
    """
    Attributes:
        attributes (GBPFoodMenuItemAttribute):
        labels (list[GBPMenuLabel] | None):
        options (list[GBPFoodMenuItemOption] | Unset): Options are variants of the dish (sizes, fillings). An option's
            unset
            attributes are taken from the dish.
    """

    attributes: GBPFoodMenuItemAttribute
    labels: list[GBPMenuLabel] | None
    options: list[GBPFoodMenuItemOption] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        attributes = self.attributes.to_dict()

        labels: list[dict[str, Any]] | None
        if isinstance(self.labels, list):
            labels = []
            for labels_type_0_item_data in self.labels:
                labels_type_0_item = labels_type_0_item_data.to_dict()
                labels.append(labels_type_0_item)

        else:
            labels = self.labels

        options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.options, Unset):
            options = []
            for options_item_data in self.options:
                options_item = options_item_data.to_dict()
                options.append(options_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "attributes": attributes,
                "labels": labels,
            }
        )
        if options is not UNSET:
            field_dict["options"] = options

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.gbp_food_menu_item_attribute import GBPFoodMenuItemAttribute  # noqa: PLC0415
        from ..models.gbp_food_menu_item_option import GBPFoodMenuItemOption  # noqa: PLC0415
        from ..models.gbp_menu_label import GBPMenuLabel  # noqa: PLC0415

        d = dict(src_dict)
        attributes = GBPFoodMenuItemAttribute.from_dict(d.pop("attributes"))

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

        _options = d.pop("options", UNSET)
        options: list[GBPFoodMenuItemOption] | Unset = UNSET
        if _options is not UNSET:
            options = []
            for options_item_data in _options:
                options_item = GBPFoodMenuItemOption.from_dict(options_item_data)

                options.append(options_item)

        gbp_food_menu_item = cls(
            attributes=attributes,
            labels=labels,
            options=options,
        )

        gbp_food_menu_item.additional_properties = d
        return gbp_food_menu_item

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
