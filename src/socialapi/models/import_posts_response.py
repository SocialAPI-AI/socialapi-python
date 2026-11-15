from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.import_row_error import ImportRowError
    from ..models.post_response import PostResponse


T = TypeVar("T", bound="ImportPostsResponse")


@_attrs_define
class ImportPostsResponse:
    """
    Attributes:
        created (int):  Example: 8.
        failed (int):  Example: 2.
        total_rows (int):  Example: 10.
        errors (list[ImportRowError] | Unset):
        posts (list[PostResponse] | Unset):
    """

    created: int
    failed: int
    total_rows: int
    errors: list[ImportRowError] | Unset = UNSET
    posts: list[PostResponse] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created = self.created

        failed = self.failed

        total_rows = self.total_rows

        errors: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.errors, Unset):
            errors = []
            for errors_item_data in self.errors:
                errors_item = errors_item_data.to_dict()
                errors.append(errors_item)

        posts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.posts, Unset):
            posts = []
            for posts_item_data in self.posts:
                posts_item = posts_item_data.to_dict()
                posts.append(posts_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created": created,
                "failed": failed,
                "total_rows": total_rows,
            }
        )
        if errors is not UNSET:
            field_dict["errors"] = errors
        if posts is not UNSET:
            field_dict["posts"] = posts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.import_row_error import ImportRowError  # noqa: PLC0415
        from ..models.post_response import PostResponse  # noqa: PLC0415

        d = dict(src_dict)
        created = d.pop("created")

        failed = d.pop("failed")

        total_rows = d.pop("total_rows")

        _errors = d.pop("errors", UNSET)
        errors: list[ImportRowError] | Unset = UNSET
        if _errors is not UNSET:
            errors = []
            for errors_item_data in _errors:
                errors_item = ImportRowError.from_dict(errors_item_data)

                errors.append(errors_item)

        _posts = d.pop("posts", UNSET)
        posts: list[PostResponse] | Unset = UNSET
        if _posts is not UNSET:
            posts = []
            for posts_item_data in _posts:
                posts_item = PostResponse.from_dict(posts_item_data)

                posts.append(posts_item)

        import_posts_response = cls(
            created=created,
            failed=failed,
            total_rows=total_rows,
            errors=errors,
            posts=posts,
        )

        import_posts_response.additional_properties = d
        return import_posts_response

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
