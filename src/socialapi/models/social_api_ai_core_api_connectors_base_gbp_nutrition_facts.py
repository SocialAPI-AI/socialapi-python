from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.social_api_ai_core_api_connectors_base_gbp_calories_fact import (
        SocialApiAiCoreApiConnectorsBaseGBPCaloriesFact,
    )
    from ..models.social_api_ai_core_api_connectors_base_gbp_nutrition_fact import (
        SocialApiAiCoreApiConnectorsBaseGBPNutritionFact,
    )


T = TypeVar("T", bound="SocialApiAiCoreApiConnectorsBaseGBPNutritionFacts")


@_attrs_define
class SocialApiAiCoreApiConnectorsBaseGBPNutritionFacts:
    """
    Attributes:
        calories (SocialApiAiCoreApiConnectorsBaseGBPCaloriesFact | Unset):
        cholesterol (SocialApiAiCoreApiConnectorsBaseGBPNutritionFact | Unset):
        protein (SocialApiAiCoreApiConnectorsBaseGBPNutritionFact | Unset):
        sodium (SocialApiAiCoreApiConnectorsBaseGBPNutritionFact | Unset):
        total_carbohydrate (SocialApiAiCoreApiConnectorsBaseGBPNutritionFact | Unset):
        total_fat (SocialApiAiCoreApiConnectorsBaseGBPNutritionFact | Unset):
    """

    calories: SocialApiAiCoreApiConnectorsBaseGBPCaloriesFact | Unset = UNSET
    cholesterol: SocialApiAiCoreApiConnectorsBaseGBPNutritionFact | Unset = UNSET
    protein: SocialApiAiCoreApiConnectorsBaseGBPNutritionFact | Unset = UNSET
    sodium: SocialApiAiCoreApiConnectorsBaseGBPNutritionFact | Unset = UNSET
    total_carbohydrate: SocialApiAiCoreApiConnectorsBaseGBPNutritionFact | Unset = UNSET
    total_fat: SocialApiAiCoreApiConnectorsBaseGBPNutritionFact | Unset = UNSET
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
        from ..models.social_api_ai_core_api_connectors_base_gbp_calories_fact import (
            SocialApiAiCoreApiConnectorsBaseGBPCaloriesFact,  # noqa: PLC0415
        )
        from ..models.social_api_ai_core_api_connectors_base_gbp_nutrition_fact import (
            SocialApiAiCoreApiConnectorsBaseGBPNutritionFact,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _calories = d.pop("calories", UNSET)
        calories: SocialApiAiCoreApiConnectorsBaseGBPCaloriesFact | Unset
        if isinstance(_calories, Unset):
            calories = UNSET
        else:
            calories = SocialApiAiCoreApiConnectorsBaseGBPCaloriesFact.from_dict(_calories)

        _cholesterol = d.pop("cholesterol", UNSET)
        cholesterol: SocialApiAiCoreApiConnectorsBaseGBPNutritionFact | Unset
        if isinstance(_cholesterol, Unset):
            cholesterol = UNSET
        else:
            cholesterol = SocialApiAiCoreApiConnectorsBaseGBPNutritionFact.from_dict(_cholesterol)

        _protein = d.pop("protein", UNSET)
        protein: SocialApiAiCoreApiConnectorsBaseGBPNutritionFact | Unset
        if isinstance(_protein, Unset):
            protein = UNSET
        else:
            protein = SocialApiAiCoreApiConnectorsBaseGBPNutritionFact.from_dict(_protein)

        _sodium = d.pop("sodium", UNSET)
        sodium: SocialApiAiCoreApiConnectorsBaseGBPNutritionFact | Unset
        if isinstance(_sodium, Unset):
            sodium = UNSET
        else:
            sodium = SocialApiAiCoreApiConnectorsBaseGBPNutritionFact.from_dict(_sodium)

        _total_carbohydrate = d.pop("total_carbohydrate", UNSET)
        total_carbohydrate: SocialApiAiCoreApiConnectorsBaseGBPNutritionFact | Unset
        if isinstance(_total_carbohydrate, Unset):
            total_carbohydrate = UNSET
        else:
            total_carbohydrate = SocialApiAiCoreApiConnectorsBaseGBPNutritionFact.from_dict(_total_carbohydrate)

        _total_fat = d.pop("total_fat", UNSET)
        total_fat: SocialApiAiCoreApiConnectorsBaseGBPNutritionFact | Unset
        if isinstance(_total_fat, Unset):
            total_fat = UNSET
        else:
            total_fat = SocialApiAiCoreApiConnectorsBaseGBPNutritionFact.from_dict(_total_fat)

        social_api_ai_core_api_connectors_base_gbp_nutrition_facts = cls(
            calories=calories,
            cholesterol=cholesterol,
            protein=protein,
            sodium=sodium,
            total_carbohydrate=total_carbohydrate,
            total_fat=total_fat,
        )

        social_api_ai_core_api_connectors_base_gbp_nutrition_facts.additional_properties = d
        return social_api_ai_core_api_connectors_base_gbp_nutrition_facts

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
