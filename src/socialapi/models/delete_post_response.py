from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.target_delete_outcome_response import TargetDeleteOutcomeResponse


T = TypeVar("T", bound="DeletePostResponse")


@_attrs_define
class DeletePostResponse:
    """
    Attributes:
        deleted (bool):  Example: True.
        success (bool):  Example: True.
        results (list[TargetDeleteOutcomeResponse] | Unset):
    """

    deleted: bool
    success: bool
    results: list[TargetDeleteOutcomeResponse] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        deleted = self.deleted

        success = self.success

        results: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.results, Unset):
            results = []
            for results_item_data in self.results:
                results_item = results_item_data.to_dict()
                results.append(results_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "deleted": deleted,
                "success": success,
            }
        )
        if results is not UNSET:
            field_dict["results"] = results

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.target_delete_outcome_response import TargetDeleteOutcomeResponse  # noqa: PLC0415

        d = dict(src_dict)
        deleted = d.pop("deleted")

        success = d.pop("success")

        _results = d.pop("results", UNSET)
        results: list[TargetDeleteOutcomeResponse] | Unset = UNSET
        if _results is not UNSET:
            results = []
            for results_item_data in _results:
                results_item = TargetDeleteOutcomeResponse.from_dict(results_item_data)

                results.append(results_item)

        delete_post_response = cls(
            deleted=deleted,
            success=success,
            results=results,
        )

        delete_post_response.additional_properties = d
        return delete_post_response

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
