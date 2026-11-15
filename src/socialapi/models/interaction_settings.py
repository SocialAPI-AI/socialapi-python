from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="InteractionSettings")


@_attrs_define
class InteractionSettings:
    """
    Attributes:
        comment_disabled (bool): [platform: tiktok]
        duet_disabled (bool): [platform: tiktok]
        stitch_disabled (bool): [platform: tiktok]
    """

    comment_disabled: bool
    duet_disabled: bool
    stitch_disabled: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        comment_disabled = self.comment_disabled

        duet_disabled = self.duet_disabled

        stitch_disabled = self.stitch_disabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "comment_disabled": comment_disabled,
                "duet_disabled": duet_disabled,
                "stitch_disabled": stitch_disabled,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        comment_disabled = d.pop("comment_disabled")

        duet_disabled = d.pop("duet_disabled")

        stitch_disabled = d.pop("stitch_disabled")

        interaction_settings = cls(
            comment_disabled=comment_disabled,
            duet_disabled=duet_disabled,
            stitch_disabled=stitch_disabled,
        )

        interaction_settings.additional_properties = d
        return interaction_settings

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
