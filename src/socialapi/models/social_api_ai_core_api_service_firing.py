from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.social_api_ai_core_api_service_action_outcome import SocialApiAiCoreApiServiceActionOutcome


T = TypeVar("T", bound="SocialApiAiCoreApiServiceFiring")


@_attrs_define
class SocialApiAiCoreApiServiceFiring:
    """
    Attributes:
        created_at (str | Unset):
        event_id (str | Unset): Platform id of the comment or message Example: 17858893269577012.
        id (str | Unset):  Example: afr_01J9Z8Y7X6W5V4T3S2R1Q0P9N8.
        outcomes (list[SocialApiAiCoreApiServiceActionOutcome] | Unset):
        person_id (str | Unset): Platform id of the person who commented or messaged Example: 17841400000000000.
        step_key (str | Unset): Key of the step whose actions ran, or the step the event entered at when no step's
            filters passed Example: start.
    """

    created_at: str | Unset = UNSET
    event_id: str | Unset = UNSET
    id: str | Unset = UNSET
    outcomes: list[SocialApiAiCoreApiServiceActionOutcome] | Unset = UNSET
    person_id: str | Unset = UNSET
    step_key: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        event_id = self.event_id

        id = self.id

        outcomes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.outcomes, Unset):
            outcomes = []
            for outcomes_item_data in self.outcomes:
                outcomes_item = outcomes_item_data.to_dict()
                outcomes.append(outcomes_item)

        person_id = self.person_id

        step_key = self.step_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if event_id is not UNSET:
            field_dict["event_id"] = event_id
        if id is not UNSET:
            field_dict["id"] = id
        if outcomes is not UNSET:
            field_dict["outcomes"] = outcomes
        if person_id is not UNSET:
            field_dict["person_id"] = person_id
        if step_key is not UNSET:
            field_dict["step_key"] = step_key

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.social_api_ai_core_api_service_action_outcome import (
            SocialApiAiCoreApiServiceActionOutcome,  # noqa: PLC0415
        )

        d = dict(src_dict)
        created_at = d.pop("created_at", UNSET)

        event_id = d.pop("event_id", UNSET)

        id = d.pop("id", UNSET)

        _outcomes = d.pop("outcomes", UNSET)
        outcomes: list[SocialApiAiCoreApiServiceActionOutcome] | Unset = UNSET
        if _outcomes is not UNSET:
            outcomes = []
            for outcomes_item_data in _outcomes:
                outcomes_item = SocialApiAiCoreApiServiceActionOutcome.from_dict(outcomes_item_data)

                outcomes.append(outcomes_item)

        person_id = d.pop("person_id", UNSET)

        step_key = d.pop("step_key", UNSET)

        social_api_ai_core_api_service_firing = cls(
            created_at=created_at,
            event_id=event_id,
            id=id,
            outcomes=outcomes,
            person_id=person_id,
            step_key=step_key,
        )

        social_api_ai_core_api_service_firing.additional_properties = d
        return social_api_ai_core_api_service_firing

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
