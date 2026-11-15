from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.action import Action
    from ..models.filter_ import Filter
    from ..models.step_button import StepButton


T = TypeVar("T", bound="Step")


@_attrs_define
class Step:
    """
    Attributes:
        actions (list[Action]): At most one of each type
        key (str): Unique within the Automation. The entry step is "start" Example: start.
        buttons (list[StepButton] | Unset): Up to 3, shown under the private_reply or send_dm message. With buttons,
            each of that message's texts is at most 640 characters
        fallthrough_step (str | Unset): Key of the Step to run when this Step's filters fail. Not allowed on start
        filters (list[Filter] | Unset): Up to 10. All must pass. None means every event passes
    """

    actions: list[Action]
    key: str
    buttons: list[StepButton] | Unset = UNSET
    fallthrough_step: str | Unset = UNSET
    filters: list[Filter] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        actions = []
        for actions_item_data in self.actions:
            actions_item = actions_item_data.to_dict()
            actions.append(actions_item)

        key = self.key

        buttons: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.buttons, Unset):
            buttons = []
            for buttons_item_data in self.buttons:
                buttons_item = buttons_item_data.to_dict()
                buttons.append(buttons_item)

        fallthrough_step = self.fallthrough_step

        filters: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.filters, Unset):
            filters = []
            for filters_item_data in self.filters:
                filters_item = filters_item_data.to_dict()
                filters.append(filters_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "actions": actions,
                "key": key,
            }
        )
        if buttons is not UNSET:
            field_dict["buttons"] = buttons
        if fallthrough_step is not UNSET:
            field_dict["fallthrough_step"] = fallthrough_step
        if filters is not UNSET:
            field_dict["filters"] = filters

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.action import Action  # noqa: PLC0415
        from ..models.filter_ import Filter  # noqa: PLC0415
        from ..models.step_button import StepButton  # noqa: PLC0415

        d = dict(src_dict)
        actions = []
        _actions = d.pop("actions")
        for actions_item_data in _actions:
            actions_item = Action.from_dict(actions_item_data)

            actions.append(actions_item)

        key = d.pop("key")

        _buttons = d.pop("buttons", UNSET)
        buttons: list[StepButton] | Unset = UNSET
        if _buttons is not UNSET:
            buttons = []
            for buttons_item_data in _buttons:
                buttons_item = StepButton.from_dict(buttons_item_data)

                buttons.append(buttons_item)

        fallthrough_step = d.pop("fallthrough_step", UNSET)

        _filters = d.pop("filters", UNSET)
        filters: list[Filter] | Unset = UNSET
        if _filters is not UNSET:
            filters = []
            for filters_item_data in _filters:
                filters_item = Filter.from_dict(filters_item_data)

                filters.append(filters_item)

        step = cls(
            actions=actions,
            key=key,
            buttons=buttons,
            fallthrough_step=fallthrough_step,
            filters=filters,
        )

        step.additional_properties = d
        return step

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
