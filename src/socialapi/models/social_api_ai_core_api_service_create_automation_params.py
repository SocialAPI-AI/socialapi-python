from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.social_api_ai_core_api_service_create_automation_params_trigger import (
    SocialApiAiCoreApiServiceCreateAutomationParamsTrigger,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.social_api_ai_core_api_service_follow_gate import SocialApiAiCoreApiServiceFollowGate
    from ..models.social_api_ai_core_api_service_step import SocialApiAiCoreApiServiceStep


T = TypeVar("T", bound="SocialApiAiCoreApiServiceCreateAutomationParams")


@_attrs_define
class SocialApiAiCoreApiServiceCreateAutomationParams:
    """
    Attributes:
        account_id (str | Unset):  Example: acc_01HZ9X3Q4R5M6N7P8V2K0W1J.
        follow_gate (SocialApiAiCoreApiServiceFollowGate | Unset):
        name (str | Unset): 1 to 100 characters Example: Send the link.
        once_per_person (bool | Unset): Reach each person at most once. A run in which every action failed does not
            count. Defaults to false
        post_ids (list[str] | Unset): Up to 100 platform post ids, each 1 to 100 characters, a comment must be on.
            Omitted means every post. Comment trigger only
        steps (list[SocialApiAiCoreApiServiceStep] | Unset):
        trigger (SocialApiAiCoreApiServiceCreateAutomationParamsTrigger | Unset):  Example: comment.
    """

    account_id: str | Unset = UNSET
    follow_gate: SocialApiAiCoreApiServiceFollowGate | Unset = UNSET
    name: str | Unset = UNSET
    once_per_person: bool | Unset = UNSET
    post_ids: list[str] | Unset = UNSET
    steps: list[SocialApiAiCoreApiServiceStep] | Unset = UNSET
    trigger: SocialApiAiCoreApiServiceCreateAutomationParamsTrigger | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_id = self.account_id

        follow_gate: dict[str, Any] | Unset = UNSET
        if not isinstance(self.follow_gate, Unset):
            follow_gate = self.follow_gate.to_dict()

        name = self.name

        once_per_person = self.once_per_person

        post_ids: list[str] | Unset = UNSET
        if not isinstance(self.post_ids, Unset):
            post_ids = self.post_ids

        steps: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.steps, Unset):
            steps = []
            for steps_item_data in self.steps:
                steps_item = steps_item_data.to_dict()
                steps.append(steps_item)

        trigger: str | Unset = UNSET
        if not isinstance(self.trigger, Unset):
            trigger = self.trigger.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_id is not UNSET:
            field_dict["account_id"] = account_id
        if follow_gate is not UNSET:
            field_dict["follow_gate"] = follow_gate
        if name is not UNSET:
            field_dict["name"] = name
        if once_per_person is not UNSET:
            field_dict["once_per_person"] = once_per_person
        if post_ids is not UNSET:
            field_dict["post_ids"] = post_ids
        if steps is not UNSET:
            field_dict["steps"] = steps
        if trigger is not UNSET:
            field_dict["trigger"] = trigger

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.social_api_ai_core_api_service_follow_gate import (
            SocialApiAiCoreApiServiceFollowGate,  # noqa: PLC0415
        )
        from ..models.social_api_ai_core_api_service_step import SocialApiAiCoreApiServiceStep  # noqa: PLC0415

        d = dict(src_dict)
        account_id = d.pop("account_id", UNSET)

        _follow_gate = d.pop("follow_gate", UNSET)
        follow_gate: SocialApiAiCoreApiServiceFollowGate | Unset
        if isinstance(_follow_gate, Unset):
            follow_gate = UNSET
        else:
            follow_gate = SocialApiAiCoreApiServiceFollowGate.from_dict(_follow_gate)

        name = d.pop("name", UNSET)

        once_per_person = d.pop("once_per_person", UNSET)

        post_ids = cast(list[str], d.pop("post_ids", UNSET))

        _steps = d.pop("steps", UNSET)
        steps: list[SocialApiAiCoreApiServiceStep] | Unset = UNSET
        if _steps is not UNSET:
            steps = []
            for steps_item_data in _steps:
                steps_item = SocialApiAiCoreApiServiceStep.from_dict(steps_item_data)

                steps.append(steps_item)

        _trigger = d.pop("trigger", UNSET)
        trigger: SocialApiAiCoreApiServiceCreateAutomationParamsTrigger | Unset
        if isinstance(_trigger, Unset):
            trigger = UNSET
        else:
            trigger = SocialApiAiCoreApiServiceCreateAutomationParamsTrigger(_trigger)

        social_api_ai_core_api_service_create_automation_params = cls(
            account_id=account_id,
            follow_gate=follow_gate,
            name=name,
            once_per_person=once_per_person,
            post_ids=post_ids,
            steps=steps,
            trigger=trigger,
        )

        social_api_ai_core_api_service_create_automation_params.additional_properties = d
        return social_api_ai_core_api_service_create_automation_params

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
