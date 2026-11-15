from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.automation_trigger import AutomationTrigger
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.follow_gate import FollowGate
    from ..models.step import Step


T = TypeVar("T", bound="CreateAutomationParams")


@_attrs_define
class CreateAutomationParams:
    """
    Attributes:
        account_id (str):  Example: acc_01HZ9X3Q4R5M6N7P8V2K0W1J.
        name (str): 1 to 100 characters Example: Send the link.
        trigger (AutomationTrigger):
        follow_gate (FollowGate | Unset):
        once_per_person (bool | Unset): Reach each person at most once. A run in which every action failed does not
            count. Defaults to false
        post_ids (list[str] | Unset): Up to 100 platform post ids, each 1 to 100 characters, a comment must be on.
            Omitted means every post. Comment trigger only
        steps (list[Step] | Unset):
    """

    account_id: str
    name: str
    trigger: AutomationTrigger
    follow_gate: FollowGate | Unset = UNSET
    once_per_person: bool | Unset = UNSET
    post_ids: list[str] | Unset = UNSET
    steps: list[Step] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_id = self.account_id

        name = self.name

        trigger = self.trigger.value

        follow_gate: dict[str, Any] | Unset = UNSET
        if not isinstance(self.follow_gate, Unset):
            follow_gate = self.follow_gate.to_dict()

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "account_id": account_id,
                "name": name,
                "trigger": trigger,
            }
        )
        if follow_gate is not UNSET:
            field_dict["follow_gate"] = follow_gate
        if once_per_person is not UNSET:
            field_dict["once_per_person"] = once_per_person
        if post_ids is not UNSET:
            field_dict["post_ids"] = post_ids
        if steps is not UNSET:
            field_dict["steps"] = steps

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.follow_gate import FollowGate  # noqa: PLC0415
        from ..models.step import Step  # noqa: PLC0415

        d = dict(src_dict)
        account_id = d.pop("account_id")

        name = d.pop("name")

        trigger = AutomationTrigger(d.pop("trigger"))

        _follow_gate = d.pop("follow_gate", UNSET)
        follow_gate: FollowGate | Unset
        if isinstance(_follow_gate, Unset):
            follow_gate = UNSET
        else:
            follow_gate = FollowGate.from_dict(_follow_gate)

        once_per_person = d.pop("once_per_person", UNSET)

        post_ids = cast(list[str], d.pop("post_ids", UNSET))

        _steps = d.pop("steps", UNSET)
        steps: list[Step] | Unset = UNSET
        if _steps is not UNSET:
            steps = []
            for steps_item_data in _steps:
                steps_item = Step.from_dict(steps_item_data)

                steps.append(steps_item)

        create_automation_params = cls(
            account_id=account_id,
            name=name,
            trigger=trigger,
            follow_gate=follow_gate,
            once_per_person=once_per_person,
            post_ids=post_ids,
            steps=steps,
        )

        create_automation_params.additional_properties = d
        return create_automation_params

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
