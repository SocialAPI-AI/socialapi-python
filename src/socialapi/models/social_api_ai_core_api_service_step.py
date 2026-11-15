from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.social_api_ai_core_api_service_action import SocialApiAiCoreApiServiceAction
    from ..models.social_api_ai_core_api_service_filter import SocialApiAiCoreApiServiceFilter
    from ..models.social_api_ai_core_api_service_step_button import SocialApiAiCoreApiServiceStepButton


T = TypeVar("T", bound="SocialApiAiCoreApiServiceStep")


@_attrs_define
class SocialApiAiCoreApiServiceStep:
    """
    Attributes:
        actions (list[SocialApiAiCoreApiServiceAction] | Unset): At most one of each type
        buttons (list[SocialApiAiCoreApiServiceStepButton] | Unset): Up to 3, shown under the private_reply or send_dm
            message. With buttons, each of that message's texts is at most 640 characters
        fallthrough_step (str | Unset): Key of the Step to run when this Step's filters fail. Not allowed on start
        filters (list[SocialApiAiCoreApiServiceFilter] | Unset): Up to 10. All must pass. None means every event passes
        key (str | Unset): Unique within the Automation. The entry step is "start" Example: start.
    """

    actions: list[SocialApiAiCoreApiServiceAction] | Unset = UNSET
    buttons: list[SocialApiAiCoreApiServiceStepButton] | Unset = UNSET
    fallthrough_step: str | Unset = UNSET
    filters: list[SocialApiAiCoreApiServiceFilter] | Unset = UNSET
    key: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        actions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.actions, Unset):
            actions = []
            for actions_item_data in self.actions:
                actions_item = actions_item_data.to_dict()
                actions.append(actions_item)

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

        key = self.key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if actions is not UNSET:
            field_dict["actions"] = actions
        if buttons is not UNSET:
            field_dict["buttons"] = buttons
        if fallthrough_step is not UNSET:
            field_dict["fallthrough_step"] = fallthrough_step
        if filters is not UNSET:
            field_dict["filters"] = filters
        if key is not UNSET:
            field_dict["key"] = key

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.social_api_ai_core_api_service_action import SocialApiAiCoreApiServiceAction  # noqa: PLC0415
        from ..models.social_api_ai_core_api_service_filter import SocialApiAiCoreApiServiceFilter  # noqa: PLC0415
        from ..models.social_api_ai_core_api_service_step_button import (
            SocialApiAiCoreApiServiceStepButton,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _actions = d.pop("actions", UNSET)
        actions: list[SocialApiAiCoreApiServiceAction] | Unset = UNSET
        if _actions is not UNSET:
            actions = []
            for actions_item_data in _actions:
                actions_item = SocialApiAiCoreApiServiceAction.from_dict(actions_item_data)

                actions.append(actions_item)

        _buttons = d.pop("buttons", UNSET)
        buttons: list[SocialApiAiCoreApiServiceStepButton] | Unset = UNSET
        if _buttons is not UNSET:
            buttons = []
            for buttons_item_data in _buttons:
                buttons_item = SocialApiAiCoreApiServiceStepButton.from_dict(buttons_item_data)

                buttons.append(buttons_item)

        fallthrough_step = d.pop("fallthrough_step", UNSET)

        _filters = d.pop("filters", UNSET)
        filters: list[SocialApiAiCoreApiServiceFilter] | Unset = UNSET
        if _filters is not UNSET:
            filters = []
            for filters_item_data in _filters:
                filters_item = SocialApiAiCoreApiServiceFilter.from_dict(filters_item_data)

                filters.append(filters_item)

        key = d.pop("key", UNSET)

        social_api_ai_core_api_service_step = cls(
            actions=actions,
            buttons=buttons,
            fallthrough_step=fallthrough_step,
            filters=filters,
            key=key,
        )

        social_api_ai_core_api_service_step.additional_properties = d
        return social_api_ai_core_api_service_step

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
