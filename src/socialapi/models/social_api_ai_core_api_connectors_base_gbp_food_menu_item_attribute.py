from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.social_api_ai_core_api_connectors_base_gbp_menu_ingredient import (
        SocialApiAiCoreApiConnectorsBaseGBPMenuIngredient,
    )
    from ..models.social_api_ai_core_api_connectors_base_gbp_menu_portion_size import (
        SocialApiAiCoreApiConnectorsBaseGBPMenuPortionSize,
    )
    from ..models.social_api_ai_core_api_connectors_base_gbp_money import SocialApiAiCoreApiConnectorsBaseGBPMoney
    from ..models.social_api_ai_core_api_connectors_base_gbp_nutrition_facts import (
        SocialApiAiCoreApiConnectorsBaseGBPNutritionFacts,
    )


T = TypeVar("T", bound="SocialApiAiCoreApiConnectorsBaseGBPFoodMenuItemAttribute")


@_attrs_define
class SocialApiAiCoreApiConnectorsBaseGBPFoodMenuItemAttribute:
    """
    Attributes:
        allergen (list[str] | Unset): Allergen lists Google's Allergen values, for example DAIRY or PEANUT.
        dietary_restriction (list[str] | Unset): DietaryRestriction lists Google's values, for example VEGAN or HALAL.
        ingredients (list[SocialApiAiCoreApiConnectorsBaseGBPMenuIngredient] | Unset):
        media_keys (list[str] | Unset): MediaKeys reference photos of the dish from the location's photo gallery.
        nutrition_facts (SocialApiAiCoreApiConnectorsBaseGBPNutritionFacts | Unset):
        portion_size (SocialApiAiCoreApiConnectorsBaseGBPMenuPortionSize | Unset):
        preparation_methods (list[str] | Unset):
        price (SocialApiAiCoreApiConnectorsBaseGBPMoney | Unset):
        serves_num_people (int | Unset):
        spiciness (str | Unset): Spiciness is MILD, MEDIUM or HOT.
    """

    allergen: list[str] | Unset = UNSET
    dietary_restriction: list[str] | Unset = UNSET
    ingredients: list[SocialApiAiCoreApiConnectorsBaseGBPMenuIngredient] | Unset = UNSET
    media_keys: list[str] | Unset = UNSET
    nutrition_facts: SocialApiAiCoreApiConnectorsBaseGBPNutritionFacts | Unset = UNSET
    portion_size: SocialApiAiCoreApiConnectorsBaseGBPMenuPortionSize | Unset = UNSET
    preparation_methods: list[str] | Unset = UNSET
    price: SocialApiAiCoreApiConnectorsBaseGBPMoney | Unset = UNSET
    serves_num_people: int | Unset = UNSET
    spiciness: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        allergen: list[str] | Unset = UNSET
        if not isinstance(self.allergen, Unset):
            allergen = self.allergen

        dietary_restriction: list[str] | Unset = UNSET
        if not isinstance(self.dietary_restriction, Unset):
            dietary_restriction = self.dietary_restriction

        ingredients: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.ingredients, Unset):
            ingredients = []
            for ingredients_item_data in self.ingredients:
                ingredients_item = ingredients_item_data.to_dict()
                ingredients.append(ingredients_item)

        media_keys: list[str] | Unset = UNSET
        if not isinstance(self.media_keys, Unset):
            media_keys = self.media_keys

        nutrition_facts: dict[str, Any] | Unset = UNSET
        if not isinstance(self.nutrition_facts, Unset):
            nutrition_facts = self.nutrition_facts.to_dict()

        portion_size: dict[str, Any] | Unset = UNSET
        if not isinstance(self.portion_size, Unset):
            portion_size = self.portion_size.to_dict()

        preparation_methods: list[str] | Unset = UNSET
        if not isinstance(self.preparation_methods, Unset):
            preparation_methods = self.preparation_methods

        price: dict[str, Any] | Unset = UNSET
        if not isinstance(self.price, Unset):
            price = self.price.to_dict()

        serves_num_people = self.serves_num_people

        spiciness = self.spiciness

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if allergen is not UNSET:
            field_dict["allergen"] = allergen
        if dietary_restriction is not UNSET:
            field_dict["dietary_restriction"] = dietary_restriction
        if ingredients is not UNSET:
            field_dict["ingredients"] = ingredients
        if media_keys is not UNSET:
            field_dict["media_keys"] = media_keys
        if nutrition_facts is not UNSET:
            field_dict["nutrition_facts"] = nutrition_facts
        if portion_size is not UNSET:
            field_dict["portion_size"] = portion_size
        if preparation_methods is not UNSET:
            field_dict["preparation_methods"] = preparation_methods
        if price is not UNSET:
            field_dict["price"] = price
        if serves_num_people is not UNSET:
            field_dict["serves_num_people"] = serves_num_people
        if spiciness is not UNSET:
            field_dict["spiciness"] = spiciness

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.social_api_ai_core_api_connectors_base_gbp_menu_ingredient import (
            SocialApiAiCoreApiConnectorsBaseGBPMenuIngredient,  # noqa: PLC0415
        )
        from ..models.social_api_ai_core_api_connectors_base_gbp_menu_portion_size import (
            SocialApiAiCoreApiConnectorsBaseGBPMenuPortionSize,  # noqa: PLC0415
        )
        from ..models.social_api_ai_core_api_connectors_base_gbp_money import (
            SocialApiAiCoreApiConnectorsBaseGBPMoney,  # noqa: PLC0415
        )
        from ..models.social_api_ai_core_api_connectors_base_gbp_nutrition_facts import (
            SocialApiAiCoreApiConnectorsBaseGBPNutritionFacts,  # noqa: PLC0415
        )

        d = dict(src_dict)
        allergen = cast(list[str], d.pop("allergen", UNSET))

        dietary_restriction = cast(list[str], d.pop("dietary_restriction", UNSET))

        _ingredients = d.pop("ingredients", UNSET)
        ingredients: list[SocialApiAiCoreApiConnectorsBaseGBPMenuIngredient] | Unset = UNSET
        if _ingredients is not UNSET:
            ingredients = []
            for ingredients_item_data in _ingredients:
                ingredients_item = SocialApiAiCoreApiConnectorsBaseGBPMenuIngredient.from_dict(ingredients_item_data)

                ingredients.append(ingredients_item)

        media_keys = cast(list[str], d.pop("media_keys", UNSET))

        _nutrition_facts = d.pop("nutrition_facts", UNSET)
        nutrition_facts: SocialApiAiCoreApiConnectorsBaseGBPNutritionFacts | Unset
        if isinstance(_nutrition_facts, Unset):
            nutrition_facts = UNSET
        else:
            nutrition_facts = SocialApiAiCoreApiConnectorsBaseGBPNutritionFacts.from_dict(_nutrition_facts)

        _portion_size = d.pop("portion_size", UNSET)
        portion_size: SocialApiAiCoreApiConnectorsBaseGBPMenuPortionSize | Unset
        if isinstance(_portion_size, Unset):
            portion_size = UNSET
        else:
            portion_size = SocialApiAiCoreApiConnectorsBaseGBPMenuPortionSize.from_dict(_portion_size)

        preparation_methods = cast(list[str], d.pop("preparation_methods", UNSET))

        _price = d.pop("price", UNSET)
        price: SocialApiAiCoreApiConnectorsBaseGBPMoney | Unset
        if isinstance(_price, Unset):
            price = UNSET
        else:
            price = SocialApiAiCoreApiConnectorsBaseGBPMoney.from_dict(_price)

        serves_num_people = d.pop("serves_num_people", UNSET)

        spiciness = d.pop("spiciness", UNSET)

        social_api_ai_core_api_connectors_base_gbp_food_menu_item_attribute = cls(
            allergen=allergen,
            dietary_restriction=dietary_restriction,
            ingredients=ingredients,
            media_keys=media_keys,
            nutrition_facts=nutrition_facts,
            portion_size=portion_size,
            preparation_methods=preparation_methods,
            price=price,
            serves_num_people=serves_num_people,
            spiciness=spiciness,
        )

        social_api_ai_core_api_connectors_base_gbp_food_menu_item_attribute.additional_properties = d
        return social_api_ai_core_api_connectors_base_gbp_food_menu_item_attribute

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
