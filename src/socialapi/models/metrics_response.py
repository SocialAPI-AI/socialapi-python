from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.post_target_response import PostTargetResponse


T = TypeVar("T", bound="MetricsResponse")


@_attrs_define
class MetricsResponse:
    """
    Attributes:
        post_id (str):
        targets (list[PostTargetResponse] | None):
    """

    post_id: str
    targets: list[PostTargetResponse] | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        post_id = self.post_id

        targets: list[dict[str, Any]] | None
        if isinstance(self.targets, list):
            targets = []
            for targets_type_0_item_data in self.targets:
                targets_type_0_item = targets_type_0_item_data.to_dict()
                targets.append(targets_type_0_item)

        else:
            targets = self.targets

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "post_id": post_id,
                "targets": targets,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_target_response import PostTargetResponse  # noqa: PLC0415

        d = dict(src_dict)
        post_id = d.pop("post_id")

        def _parse_targets(data: object) -> list[PostTargetResponse] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                targets_type_0 = []
                _targets_type_0 = data
                for targets_type_0_item_data in _targets_type_0:
                    targets_type_0_item = PostTargetResponse.from_dict(targets_type_0_item_data)

                    targets_type_0.append(targets_type_0_item)

                return targets_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[PostTargetResponse] | None, data)

        targets = _parse_targets(d.pop("targets"))

        metrics_response = cls(
            post_id=post_id,
            targets=targets,
        )

        metrics_response.additional_properties = d
        return metrics_response

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
