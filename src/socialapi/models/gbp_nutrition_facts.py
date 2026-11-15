from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.gbp_calories_fact import GBPCaloriesFact
    from ..models.gbp_nutrition_fact import GBPNutritionFact


T = TypeVar("T", bound="GBPNutritionFacts")


@_attrs_define
class GBPNutritionFacts:
    """
    Attributes:
        calories (GBPCaloriesFact | Unset):
        cholesterol (GBPNutritionFact | Unset):
        protein (GBPNutritionFact | Unset):
        sodium (GBPNutritionFact | Unset):
        total_carbohydrate (GBPNutritionFact | Unset):
        total_fat (GBPNutritionFact | Unset):
    """

    calories: GBPCaloriesFact | Unset = UNSET
    cholesterol: GBPNutritionFact | Unset = UNSET
    protein: GBPNutritionFact | Unset = UNSET
    sodium: GBPNutritionFact | Unset = UNSET
    total_carbohydrate: GBPNutritionFact | Unset = UNSET
    total_fat: GBPNutritionFact | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        calories: dict[str, Any] | Unset = UNSET
        if not isinstance(self.calories, Unset):
            calories = self.calories.to_dict()

        cholesterol: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cholesterol, Unset):
            cholesterol = self.cholesterol.to_dict()

        protein: dict[str, Any] | Unset = UNSET
        if not isinstance(self.protein, Unset):
            protein = self.protein.to_dict()

        sodium: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sodium, Unset):
            sodium = self.sodium.to_dict()

        total_carbohydrate: dict[str, Any] | Unset = UNSET
        if not isinstance(self.total_carbohydrate, Unset):
            total_carbohydrate = self.total_carbohydrate.to_dict()

        total_fat: dict[str, Any] | Unset = UNSET
        if not isinstance(self.total_fat, Unset):
            total_fat = self.total_fat.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if calories is not UNSET:
            field_dict["calories"] = calories
        if cholesterol is not UNSET:
            field_dict["cholesterol"] = cholesterol
        if protein is not UNSET:
            field_dict["protein"] = protein
        if sodium is not UNSET:
            field_dict["sodium"] = sodium
        if total_carbohydrate is not UNSET:
            field_dict["total_carbohydrate"] = total_carbohydrate
        if total_fat is not UNSET:
            field_dict["total_fat"] = total_fat

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.gbp_calories_fact import GBPCaloriesFact  # noqa: PLC0415
        from ..models.gbp_nutrition_fact import GBPNutritionFact  # noqa: PLC0415

        d = dict(src_dict)
        _calories = d.pop("calories", UNSET)
        calories: GBPCaloriesFact | Unset
        if isinstance(_calories, Unset):
            calories = UNSET
        else:
            calories = GBPCaloriesFact.from_dict(_calories)

        _cholesterol = d.pop("cholesterol", UNSET)
        cholesterol: GBPNutritionFact | Unset
        if isinstance(_cholesterol, Unset):
            cholesterol = UNSET
        else:
            cholesterol = GBPNutritionFact.from_dict(_cholesterol)

        _protein = d.pop("protein", UNSET)
        protein: GBPNutritionFact | Unset
        if isinstance(_protein, Unset):
            protein = UNSET
        else:
            protein = GBPNutritionFact.from_dict(_protein)

        _sodium = d.pop("sodium", UNSET)
        sodium: GBPNutritionFact | Unset
        if isinstance(_sodium, Unset):
            sodium = UNSET
        else:
            sodium = GBPNutritionFact.from_dict(_sodium)

        _total_carbohydrate = d.pop("total_carbohydrate", UNSET)
        total_carbohydrate: GBPNutritionFact | Unset
        if isinstance(_total_carbohydrate, Unset):
            total_carbohydrate = UNSET
        else:
            total_carbohydrate = GBPNutritionFact.from_dict(_total_carbohydrate)

        _total_fat = d.pop("total_fat", UNSET)
        total_fat: GBPNutritionFact | Unset
        if isinstance(_total_fat, Unset):
            total_fat = UNSET
        else:
            total_fat = GBPNutritionFact.from_dict(_total_fat)

        gbp_nutrition_facts = cls(
            calories=calories,
            cholesterol=cholesterol,
            protein=protein,
            sodium=sodium,
            total_carbohydrate=total_carbohydrate,
            total_fat=total_fat,
        )

        gbp_nutrition_facts.additional_properties = d
        return gbp_nutrition_facts

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
