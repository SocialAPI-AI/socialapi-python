from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_endpoints_post_target_response import ApiEndpointsPostTargetResponse


T = TypeVar("T", bound="ApiEndpointsMetricsResponse")


@_attrs_define
class ApiEndpointsMetricsResponse:
    """
    Attributes:
        post_id (str | Unset):
        targets (list[ApiEndpointsPostTargetResponse] | Unset):
    """

    post_id: str | Unset = UNSET
    targets: list[ApiEndpointsPostTargetResponse] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        post_id = self.post_id

        targets: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.targets, Unset):
            targets = []
            for targets_item_data in self.targets:
                targets_item = targets_item_data.to_dict()
                targets.append(targets_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if post_id is not UNSET:
            field_dict["post_id"] = post_id
        if targets is not UNSET:
            field_dict["targets"] = targets

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_endpoints_post_target_response import ApiEndpointsPostTargetResponse  # noqa: PLC0415

        d = dict(src_dict)
        post_id = d.pop("post_id", UNSET)

        _targets = d.pop("targets", UNSET)
        targets: list[ApiEndpointsPostTargetResponse] | Unset = UNSET
        if _targets is not UNSET:
            targets = []
            for targets_item_data in _targets:
                targets_item = ApiEndpointsPostTargetResponse.from_dict(targets_item_data)

                targets.append(targets_item)

        api_endpoints_metrics_response = cls(
            post_id=post_id,
            targets=targets,
        )

        api_endpoints_metrics_response.additional_properties = d
        return api_endpoints_metrics_response

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
