from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.whats_app_cursors import WhatsAppCursors


T = TypeVar("T", bound="WhatsAppTemplateListPaging")


@_attrs_define
class WhatsAppTemplateListPaging:
    """
    Attributes:
        cursors (WhatsAppCursors):
        next_ (str | Unset):  Example: https://graph.facebook.com/....
    """

    cursors: WhatsAppCursors
    next_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cursors = self.cursors.to_dict()

        next_ = self.next_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cursors": cursors,
            }
        )
        if next_ is not UNSET:
            field_dict["next"] = next_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.whats_app_cursors import WhatsAppCursors  # noqa: PLC0415

        d = dict(src_dict)
        cursors = WhatsAppCursors.from_dict(d.pop("cursors"))

        next_ = d.pop("next", UNSET)

        whats_app_template_list_paging = cls(
            cursors=cursors,
            next_=next_,
        )

        whats_app_template_list_paging.additional_properties = d
        return whats_app_template_list_paging

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
