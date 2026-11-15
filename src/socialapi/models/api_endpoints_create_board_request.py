from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.api_endpoints_create_board_request_privacy import ApiEndpointsCreateBoardRequestPrivacy
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiEndpointsCreateBoardRequest")


@_attrs_define
class ApiEndpointsCreateBoardRequest:
    """
    Attributes:
        description (str | Unset):  Example: Weeknight dinners.
        name (str | Unset):  Example: Recipes.
        privacy (ApiEndpointsCreateBoardRequestPrivacy | Unset):  Example: PUBLIC.
    """

    description: str | Unset = UNSET
    name: str | Unset = UNSET
    privacy: ApiEndpointsCreateBoardRequestPrivacy | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        name = self.name

        privacy: str | Unset = UNSET
        if not isinstance(self.privacy, Unset):
            privacy = self.privacy.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if name is not UNSET:
            field_dict["name"] = name
        if privacy is not UNSET:
            field_dict["privacy"] = privacy

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        description = d.pop("description", UNSET)

        name = d.pop("name", UNSET)

        _privacy = d.pop("privacy", UNSET)
        privacy: ApiEndpointsCreateBoardRequestPrivacy | Unset
        if isinstance(_privacy, Unset):
            privacy = UNSET
        else:
            privacy = ApiEndpointsCreateBoardRequestPrivacy(_privacy)

        api_endpoints_create_board_request = cls(
            description=description,
            name=name,
            privacy=privacy,
        )

        api_endpoints_create_board_request.additional_properties = d
        return api_endpoints_create_board_request

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
