from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_endpoints_target_delete_outcome_response import ApiEndpointsTargetDeleteOutcomeResponse


T = TypeVar("T", bound="ApiEndpointsDeletePostResponse")


@_attrs_define
class ApiEndpointsDeletePostResponse:
    """
    Attributes:
        deleted (bool | Unset):  Example: True.
        results (list[ApiEndpointsTargetDeleteOutcomeResponse] | Unset):
        success (bool | Unset):  Example: True.
    """

    deleted: bool | Unset = UNSET
    results: list[ApiEndpointsTargetDeleteOutcomeResponse] | Unset = UNSET
    success: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        deleted = self.deleted

        results: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.results, Unset):
            results = []
            for results_item_data in self.results:
                results_item = results_item_data.to_dict()
                results.append(results_item)

        success = self.success

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if deleted is not UNSET:
            field_dict["deleted"] = deleted
        if results is not UNSET:
            field_dict["results"] = results
        if success is not UNSET:
            field_dict["success"] = success

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_endpoints_target_delete_outcome_response import (
            ApiEndpointsTargetDeleteOutcomeResponse,  # noqa: PLC0415
        )

        d = dict(src_dict)
        deleted = d.pop("deleted", UNSET)

        _results = d.pop("results", UNSET)
        results: list[ApiEndpointsTargetDeleteOutcomeResponse] | Unset = UNSET
        if _results is not UNSET:
            results = []
            for results_item_data in _results:
                results_item = ApiEndpointsTargetDeleteOutcomeResponse.from_dict(results_item_data)

                results.append(results_item)

        success = d.pop("success", UNSET)

        api_endpoints_delete_post_response = cls(
            deleted=deleted,
            results=results,
            success=success,
        )

        api_endpoints_delete_post_response.additional_properties = d
        return api_endpoints_delete_post_response

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
