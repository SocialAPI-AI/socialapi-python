from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SchedulingConstraints")


@_attrs_define
class SchedulingConstraints:
    """
    Attributes:
        supported (bool): whether scheduled_at is accepted for this platform
        mode (str | Unset): Mode reflects the platform's native scheduling support: "native" when the
            platform can schedule the post itself, "server_side" when the platform has
            no native scheduling and SocialAPI holds the post and publishes it at the
            scheduled time. Regardless of mode, scheduled_at is accepted whenever
            Supported is true. Empty when Supported is false.
    """

    supported: bool
    mode: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        supported = self.supported

        mode = self.mode

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "supported": supported,
            }
        )
        if mode is not UNSET:
            field_dict["mode"] = mode

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        supported = d.pop("supported")

        mode = d.pop("mode", UNSET)

        scheduling_constraints = cls(
            supported=supported,
            mode=mode,
        )

        scheduling_constraints.additional_properties = d
        return scheduling_constraints

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
