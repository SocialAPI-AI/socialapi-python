from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.social_api_ai_core_api_service_automation_status import SocialApiAiCoreApiServiceAutomationStatus
from ..models.social_api_ai_core_api_service_automation_trigger import SocialApiAiCoreApiServiceAutomationTrigger
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.social_api_ai_core_api_service_step import SocialApiAiCoreApiServiceStep


T = TypeVar("T", bound="SocialApiAiCoreApiServiceAutomation")


@_attrs_define
class SocialApiAiCoreApiServiceAutomation:
    """
    Attributes:
        account_id (str | Unset):  Example: acc_01HZ9X3Q4R5M6N7P8V2K0W1J.
        created_at (str | Unset):
        failed_count (int | Unset): Actions that failed
        fired_count (int | Unset): Events the Automation ran against
        id (str | Unset):  Example: aut_01J9Z8Y7X6W5V4T3S2R1Q0P9N8.
        name (str | Unset):  Example: Send the link.
        once_per_person (bool | Unset): Reach each person at most once. A run in which every action failed does not
            count
        post_ids (list[str] | Unset): Up to 100 platform post ids, each 1 to 100 characters, a comment must be on.
            Omitted means every post. Comment trigger only
        sent_count (int | Unset): Actions carried out successfully
        status (SocialApiAiCoreApiServiceAutomationStatus | Unset):  Example: active.
        steps (list[SocialApiAiCoreApiServiceStep] | Unset): Up to 10 Steps forming a graph. One must have the key
            "start"
        trigger (SocialApiAiCoreApiServiceAutomationTrigger | Unset): The kind of inbound event that fires the
            Automation Example: comment.
        updated_at (str | Unset):
    """

    account_id: str | Unset = UNSET
    created_at: str | Unset = UNSET
    failed_count: int | Unset = UNSET
    fired_count: int | Unset = UNSET
    id: str | Unset = UNSET
    name: str | Unset = UNSET
    once_per_person: bool | Unset = UNSET
    post_ids: list[str] | Unset = UNSET
    sent_count: int | Unset = UNSET
    status: SocialApiAiCoreApiServiceAutomationStatus | Unset = UNSET
    steps: list[SocialApiAiCoreApiServiceStep] | Unset = UNSET
    trigger: SocialApiAiCoreApiServiceAutomationTrigger | Unset = UNSET
    updated_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_id = self.account_id

        created_at = self.created_at

        failed_count = self.failed_count

        fired_count = self.fired_count

        id = self.id

        name = self.name

        once_per_person = self.once_per_person

        post_ids: list[str] | Unset = UNSET
        if not isinstance(self.post_ids, Unset):
            post_ids = self.post_ids

        sent_count = self.sent_count

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        steps: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.steps, Unset):
            steps = []
            for steps_item_data in self.steps:
                steps_item = steps_item_data.to_dict()
                steps.append(steps_item)

        trigger: str | Unset = UNSET
        if not isinstance(self.trigger, Unset):
            trigger = self.trigger.value

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_id is not UNSET:
            field_dict["account_id"] = account_id
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if failed_count is not UNSET:
            field_dict["failed_count"] = failed_count
        if fired_count is not UNSET:
            field_dict["fired_count"] = fired_count
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if once_per_person is not UNSET:
            field_dict["once_per_person"] = once_per_person
        if post_ids is not UNSET:
            field_dict["post_ids"] = post_ids
        if sent_count is not UNSET:
            field_dict["sent_count"] = sent_count
        if status is not UNSET:
            field_dict["status"] = status
        if steps is not UNSET:
            field_dict["steps"] = steps
        if trigger is not UNSET:
            field_dict["trigger"] = trigger
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.social_api_ai_core_api_service_step import SocialApiAiCoreApiServiceStep  # noqa: PLC0415

        d = dict(src_dict)
        account_id = d.pop("account_id", UNSET)

        created_at = d.pop("created_at", UNSET)

        failed_count = d.pop("failed_count", UNSET)

        fired_count = d.pop("fired_count", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        once_per_person = d.pop("once_per_person", UNSET)

        post_ids = cast(list[str], d.pop("post_ids", UNSET))

        sent_count = d.pop("sent_count", UNSET)

        _status = d.pop("status", UNSET)
        status: SocialApiAiCoreApiServiceAutomationStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = SocialApiAiCoreApiServiceAutomationStatus(_status)

        _steps = d.pop("steps", UNSET)
        steps: list[SocialApiAiCoreApiServiceStep] | Unset = UNSET
        if _steps is not UNSET:
            steps = []
            for steps_item_data in _steps:
                steps_item = SocialApiAiCoreApiServiceStep.from_dict(steps_item_data)

                steps.append(steps_item)

        _trigger = d.pop("trigger", UNSET)
        trigger: SocialApiAiCoreApiServiceAutomationTrigger | Unset
        if isinstance(_trigger, Unset):
            trigger = UNSET
        else:
            trigger = SocialApiAiCoreApiServiceAutomationTrigger(_trigger)

        updated_at = d.pop("updated_at", UNSET)

        social_api_ai_core_api_service_automation = cls(
            account_id=account_id,
            created_at=created_at,
            failed_count=failed_count,
            fired_count=fired_count,
            id=id,
            name=name,
            once_per_person=once_per_person,
            post_ids=post_ids,
            sent_count=sent_count,
            status=status,
            steps=steps,
            trigger=trigger,
            updated_at=updated_at,
        )

        social_api_ai_core_api_service_automation.additional_properties = d
        return social_api_ai_core_api_service_automation

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
