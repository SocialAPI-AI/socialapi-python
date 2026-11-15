from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.social_api_ai_core_api_connectors_base_gbp_label import SocialApiAiCoreApiConnectorsBaseGBPLabel


T = TypeVar("T", bound="SocialApiAiCoreApiConnectorsBaseGBPFreeFormService")


@_attrs_define
class SocialApiAiCoreApiConnectorsBaseGBPFreeFormService:
    """
    Attributes:
        category (str | Unset):
        label (SocialApiAiCoreApiConnectorsBaseGBPLabel | Unset):
    """

    category: str | Unset = UNSET
    label: SocialApiAiCoreApiConnectorsBaseGBPLabel | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        category = self.category

        label: dict[str, Any] | Unset = UNSET
        if not isinstance(self.label, Unset):
            label = self.label.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if category is not UNSET:
            field_dict["category"] = category
        if label is not UNSET:
            field_dict["label"] = label

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.social_api_ai_core_api_connectors_base_gbp_label import (
            SocialApiAiCoreApiConnectorsBaseGBPLabel,  # noqa: PLC0415
        )

        d = dict(src_dict)
        category = d.pop("category", UNSET)

        _label = d.pop("label", UNSET)
        label: SocialApiAiCoreApiConnectorsBaseGBPLabel | Unset
        if isinstance(_label, Unset):
            label = UNSET
        else:
            label = SocialApiAiCoreApiConnectorsBaseGBPLabel.from_dict(_label)

        social_api_ai_core_api_connectors_base_gbp_free_form_service = cls(
            category=category,
            label=label,
        )

        social_api_ai_core_api_connectors_base_gbp_free_form_service.additional_properties = d
        return social_api_ai_core_api_connectors_base_gbp_free_form_service

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
