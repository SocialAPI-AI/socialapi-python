from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.social_api_ai_core_api_service_update_automation_params_status import (
    SocialApiAiCoreApiServiceUpdateAutomationParamsStatus,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.social_api_ai_core_api_service_step import SocialApiAiCoreApiServiceStep


T = TypeVar("T", bound="SocialApiAiCoreApiServiceUpdateAutomationParams")


@_attrs_define
class SocialApiAiCoreApiServiceUpdateAutomationParams:
    """
    Attributes:
        name (str | Unset): 1 to 100 characters
        once_per_person (bool | Unset):
        post_ids (list[str] | Unset): Up to 100 platform post ids, each 1 to 100 characters, a comment must be on. An
            empty list means every post. Comment trigger only
        status (SocialApiAiCoreApiServiceUpdateAutomationParamsStatus | Unset):
        steps (list[SocialApiAiCoreApiServiceStep] | Unset):
    """

    name: str | Unset = UNSET
    once_per_person: bool | Unset = UNSET
    post_ids: list[str] | Unset = UNSET
    status: SocialApiAiCoreApiServiceUpdateAutomationParamsStatus | Unset = UNSET
    steps: list[SocialApiAiCoreApiServiceStep] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        once_per_person = self.once_per_person

        post_ids: list[str] | Unset = UNSET
        if not isinstance(self.post_ids, Unset):
            post_ids = self.post_ids

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        steps: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.steps, Unset):
            steps = []
            for steps_item_data in self.steps:
                steps_item = steps_item_data.to_dict()
                steps.append(steps_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if once_per_person is not UNSET:
            field_dict["once_per_person"] = once_per_person
        if post_ids is not UNSET:
            field_dict["post_ids"] = post_ids
        if status is not UNSET:
            field_dict["status"] = status
        if steps is not UNSET:
            field_dict["steps"] = steps

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.social_api_ai_core_api_service_step import SocialApiAiCoreApiServiceStep  # noqa: PLC0415

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        once_per_person = d.pop("once_per_person", UNSET)

        post_ids = cast(list[str], d.pop("post_ids", UNSET))

        _status = d.pop("status", UNSET)
        status: SocialApiAiCoreApiServiceUpdateAutomationParamsStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = SocialApiAiCoreApiServiceUpdateAutomationParamsStatus(_status)

        _steps = d.pop("steps", UNSET)
        steps: list[SocialApiAiCoreApiServiceStep] | Unset = UNSET
        if _steps is not UNSET:
            steps = []
            for steps_item_data in _steps:
                steps_item = SocialApiAiCoreApiServiceStep.from_dict(steps_item_data)

                steps.append(steps_item)

        social_api_ai_core_api_service_update_automation_params = cls(
            name=name,
            once_per_person=once_per_person,
            post_ids=post_ids,
            status=status,
            steps=steps,
        )

        social_api_ai_core_api_service_update_automation_params.additional_properties = d
        return social_api_ai_core_api_service_update_automation_params

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
