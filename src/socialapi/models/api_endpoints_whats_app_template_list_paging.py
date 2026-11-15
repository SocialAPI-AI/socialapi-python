from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_endpoints_whats_app_cursors import ApiEndpointsWhatsAppCursors


T = TypeVar("T", bound="ApiEndpointsWhatsAppTemplateListPaging")


@_attrs_define
class ApiEndpointsWhatsAppTemplateListPaging:
    """
    Attributes:
        cursors (ApiEndpointsWhatsAppCursors | Unset):
        next_ (str | Unset):  Example: https://graph.facebook.com/....
    """

    cursors: ApiEndpointsWhatsAppCursors | Unset = UNSET
    next_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cursors: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cursors, Unset):
            cursors = self.cursors.to_dict()

        next_ = self.next_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cursors is not UNSET:
            field_dict["cursors"] = cursors
        if next_ is not UNSET:
            field_dict["next"] = next_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_endpoints_whats_app_cursors import ApiEndpointsWhatsAppCursors  # noqa: PLC0415

        d = dict(src_dict)
        _cursors = d.pop("cursors", UNSET)
        cursors: ApiEndpointsWhatsAppCursors | Unset
        if isinstance(_cursors, Unset):
            cursors = UNSET
        else:
            cursors = ApiEndpointsWhatsAppCursors.from_dict(_cursors)

        next_ = d.pop("next", UNSET)

        api_endpoints_whats_app_template_list_paging = cls(
            cursors=cursors,
            next_=next_,
        )

        api_endpoints_whats_app_template_list_paging.additional_properties = d
        return api_endpoints_whats_app_template_list_paging

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
