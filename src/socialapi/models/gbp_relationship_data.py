from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.gbp_relevant_location import GBPRelevantLocation


T = TypeVar("T", bound="GBPRelationshipData")


@_attrs_define
class GBPRelationshipData:
    """
    Attributes:
        children_locations (list[GBPRelevantLocation] | Unset):
        parent_chain (str | Unset):
        parent_location (GBPRelevantLocation | Unset):
    """

    children_locations: list[GBPRelevantLocation] | Unset = UNSET
    parent_chain: str | Unset = UNSET
    parent_location: GBPRelevantLocation | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        children_locations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.children_locations, Unset):
            children_locations = []
            for children_locations_item_data in self.children_locations:
                children_locations_item = children_locations_item_data.to_dict()
                children_locations.append(children_locations_item)

        parent_chain = self.parent_chain

        parent_location: dict[str, Any] | Unset = UNSET
        if not isinstance(self.parent_location, Unset):
            parent_location = self.parent_location.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if children_locations is not UNSET:
            field_dict["children_locations"] = children_locations
        if parent_chain is not UNSET:
            field_dict["parent_chain"] = parent_chain
        if parent_location is not UNSET:
            field_dict["parent_location"] = parent_location

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.gbp_relevant_location import GBPRelevantLocation  # noqa: PLC0415

        d = dict(src_dict)
        _children_locations = d.pop("children_locations", UNSET)
        children_locations: list[GBPRelevantLocation] | Unset = UNSET
        if _children_locations is not UNSET:
            children_locations = []
            for children_locations_item_data in _children_locations:
                children_locations_item = GBPRelevantLocation.from_dict(children_locations_item_data)

                children_locations.append(children_locations_item)

        parent_chain = d.pop("parent_chain", UNSET)

        _parent_location = d.pop("parent_location", UNSET)
        parent_location: GBPRelevantLocation | Unset
        if isinstance(_parent_location, Unset):
            parent_location = UNSET
        else:
            parent_location = GBPRelevantLocation.from_dict(_parent_location)

        gbp_relationship_data = cls(
            children_locations=children_locations,
            parent_chain=parent_chain,
            parent_location=parent_location,
        )

        gbp_relationship_data.additional_properties = d
        return gbp_relationship_data

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
