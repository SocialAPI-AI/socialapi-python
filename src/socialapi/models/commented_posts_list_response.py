from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.inbox_pagination_opt import InboxPaginationOpt
    from ..models.inbox_post import InboxPost


T = TypeVar("T", bound="CommentedPostsListResponse")


@_attrs_define
class CommentedPostsListResponse:
    """
    Attributes:
        data (list[InboxPost] | None):
        pagination (InboxPaginationOpt):
    """

    data: list[InboxPost] | None
    pagination: InboxPaginationOpt
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data: list[dict[str, Any]] | None
        if isinstance(self.data, list):
            data = []
            for data_type_0_item_data in self.data:
                data_type_0_item = data_type_0_item_data.to_dict()
                data.append(data_type_0_item)

        else:
            data = self.data

        pagination = self.pagination.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
                "pagination": pagination,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.inbox_pagination_opt import InboxPaginationOpt  # noqa: PLC0415
        from ..models.inbox_post import InboxPost  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_data(data: object) -> list[InboxPost] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                data_type_0 = []
                _data_type_0 = data
                for data_type_0_item_data in _data_type_0:
                    data_type_0_item = InboxPost.from_dict(data_type_0_item_data)

                    data_type_0.append(data_type_0_item)

                return data_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[InboxPost] | None, data)

        data = _parse_data(d.pop("data"))

        pagination = InboxPaginationOpt.from_dict(d.pop("pagination"))

        commented_posts_list_response = cls(
            data=data,
            pagination=pagination,
        )

        commented_posts_list_response.additional_properties = d
        return commented_posts_list_response

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
