from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.automation_status import AutomationStatus
from ..models.automation_trigger import AutomationTrigger
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.step import Step


T = TypeVar("T", bound="Automation")


@_attrs_define
class Automation:
    """
    Attributes:
        account_id (str):  Example: acc_01HZ9X3Q4R5M6N7P8V2K0W1J.
        created_at (str):
        failed_count (int): Actions that failed
        fired_count (int): Events the Automation ran against
        id (str):  Example: aut_01J9Z8Y7X6W5V4T3S2R1Q0P9N8.
        name (str):  Example: Send the link.
        once_per_person (bool): Reach each person at most once. A run in which every action failed does not count
        sent_count (int): Actions carried out successfully
        status (AutomationStatus):
        steps (list[Step]): Up to 10 Steps forming a graph. One must have the key "start"
        trigger (AutomationTrigger):
        updated_at (str):
        post_ids (list[str] | Unset): Up to 100 platform post ids, each 1 to 100 characters, a comment must be on.
            Omitted means every post. Comment trigger only
    """

    account_id: str
    created_at: str
    failed_count: int
    fired_count: int
    id: str
    name: str
    once_per_person: bool
    sent_count: int
    status: AutomationStatus
    steps: list[Step]
    trigger: AutomationTrigger
    updated_at: str
    post_ids: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_id = self.account_id

        created_at = self.created_at

        failed_count = self.failed_count

        fired_count = self.fired_count

        id = self.id

        name = self.name

        once_per_person = self.once_per_person

        sent_count = self.sent_count

        status = self.status.value

        steps = []
        for steps_item_data in self.steps:
            steps_item = steps_item_data.to_dict()
            steps.append(steps_item)

        trigger = self.trigger.value

        updated_at = self.updated_at

        post_ids: list[str] | Unset = UNSET
        if not isinstance(self.post_ids, Unset):
            post_ids = self.post_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "account_id": account_id,
                "created_at": created_at,
                "failed_count": failed_count,
                "fired_count": fired_count,
                "id": id,
                "name": name,
                "once_per_person": once_per_person,
                "sent_count": sent_count,
                "status": status,
                "steps": steps,
                "trigger": trigger,
                "updated_at": updated_at,
            }
        )
        if post_ids is not UNSET:
            field_dict["post_ids"] = post_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.step import Step  # noqa: PLC0415

        d = dict(src_dict)
        account_id = d.pop("account_id")

        created_at = d.pop("created_at")

        failed_count = d.pop("failed_count")

        fired_count = d.pop("fired_count")

        id = d.pop("id")

        name = d.pop("name")

        once_per_person = d.pop("once_per_person")

        sent_count = d.pop("sent_count")

        status = AutomationStatus(d.pop("status"))

        steps = []
        _steps = d.pop("steps")
        for steps_item_data in _steps:
            steps_item = Step.from_dict(steps_item_data)

            steps.append(steps_item)

        trigger = AutomationTrigger(d.pop("trigger"))

        updated_at = d.pop("updated_at")

        post_ids = cast(list[str], d.pop("post_ids", UNSET))

        automation = cls(
            account_id=account_id,
            created_at=created_at,
            failed_count=failed_count,
            fired_count=fired_count,
            id=id,
            name=name,
            once_per_person=once_per_person,
            sent_count=sent_count,
            status=status,
            steps=steps,
            trigger=trigger,
            updated_at=updated_at,
            post_ids=post_ids,
        )

        automation.additional_properties = d
        return automation

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
