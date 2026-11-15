from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_target_error_response import PostTargetErrorResponse
    from ..models.post_target_response import PostTargetResponse


T = TypeVar("T", bound="PostsMetricsItem")


@_attrs_define
class PostsMetricsItem:
    """
    Attributes:
        post_id (str): The post ID as given in post_ids. Example: 9b2f1c34-5e6a-4d7b-8c9d-0e1f2a3b4c5d.
        targets (list[PostTargetResponse]): Same targets as GET /v1/posts/{post_id}/metrics. Empty when error is set.
        error (PostTargetErrorResponse | Unset):
    """

    post_id: str
    targets: list[PostTargetResponse]
    error: PostTargetErrorResponse | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        post_id = self.post_id

        targets = []
        for targets_item_data in self.targets:
            targets_item = targets_item_data.to_dict()
            targets.append(targets_item)

        error: dict[str, Any] | Unset = UNSET
        if not isinstance(self.error, Unset):
            error = self.error.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "post_id": post_id,
                "targets": targets,
            }
        )
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_target_error_response import PostTargetErrorResponse  # noqa: PLC0415
        from ..models.post_target_response import PostTargetResponse  # noqa: PLC0415

        d = dict(src_dict)
        post_id = d.pop("post_id")

        targets = []
        _targets = d.pop("targets")
        for targets_item_data in _targets:
            targets_item = PostTargetResponse.from_dict(targets_item_data)

            targets.append(targets_item)

        _error = d.pop("error", UNSET)
        error: PostTargetErrorResponse | Unset
        if isinstance(_error, Unset):
            error = UNSET
        else:
            error = PostTargetErrorResponse.from_dict(_error)

        posts_metrics_item = cls(
            post_id=post_id,
            targets=targets,
            error=error,
        )

        posts_metrics_item.additional_properties = d
        return posts_metrics_item

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
