from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.action_outcome import ActionOutcome


T = TypeVar("T", bound="Firing")


@_attrs_define
class Firing:
    """
    Attributes:
        created_at (datetime.datetime):
        event_id (str): Platform id of the comment or message Example: 17858893269577012.
        id (str):  Example: afr_01J9Z8Y7X6W5V4T3S2R1Q0P9N8.
        outcomes (list[ActionOutcome] | None):
        person_id (str): Platform id of the person who commented or messaged Example: 17841400000000000.
        step_key (str): Key of the step whose actions ran, or the step the event entered at when no step's filters
            passed Example: start.
    """

    created_at: datetime.datetime
    event_id: str
    id: str
    outcomes: list[ActionOutcome] | None
    person_id: str
    step_key: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        event_id = self.event_id

        id = self.id

        outcomes: list[dict[str, Any]] | None
        if isinstance(self.outcomes, list):
            outcomes = []
            for outcomes_type_0_item_data in self.outcomes:
                outcomes_type_0_item = outcomes_type_0_item_data.to_dict()
                outcomes.append(outcomes_type_0_item)

        else:
            outcomes = self.outcomes

        person_id = self.person_id

        step_key = self.step_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_at": created_at,
                "event_id": event_id,
                "id": id,
                "outcomes": outcomes,
                "person_id": person_id,
                "step_key": step_key,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.action_outcome import ActionOutcome  # noqa: PLC0415

        d = dict(src_dict)
        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        event_id = d.pop("event_id")

        id = d.pop("id")

        def _parse_outcomes(data: object) -> list[ActionOutcome] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                outcomes_type_0 = []
                _outcomes_type_0 = data
                for outcomes_type_0_item_data in _outcomes_type_0:
                    outcomes_type_0_item = ActionOutcome.from_dict(outcomes_type_0_item_data)

                    outcomes_type_0.append(outcomes_type_0_item)

                return outcomes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ActionOutcome] | None, data)

        outcomes = _parse_outcomes(d.pop("outcomes"))

        person_id = d.pop("person_id")

        step_key = d.pop("step_key")

        firing = cls(
            created_at=created_at,
            event_id=event_id,
            id=id,
            outcomes=outcomes,
            person_id=person_id,
            step_key=step_key,
        )

        firing.additional_properties = d
        return firing

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
