from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.gbp_location_details import GBPLocationDetails


T = TypeVar("T", bound="UpdateGoogleLocationResponse")


@_attrs_define
class UpdateGoogleLocationResponse:
    """
    Attributes:
        data (GBPLocationDetails):
        validated (bool | Unset): Validated is true when the request ran with validate_only, meaning Google
            accepted the change as valid and wrote nothing. Data is empty in that case.
    """

    data: GBPLocationDetails
    validated: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = self.data.to_dict()

        validated = self.validated

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
            }
        )
        if validated is not UNSET:
            field_dict["validated"] = validated

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.gbp_location_details import GBPLocationDetails  # noqa: PLC0415

        d = dict(src_dict)
        data = GBPLocationDetails.from_dict(d.pop("data"))

        validated = d.pop("validated", UNSET)

        update_google_location_response = cls(
            data=data,
            validated=validated,
        )

        update_google_location_response.additional_properties = d
        return update_google_location_response

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
