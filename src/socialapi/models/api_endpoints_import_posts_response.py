from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_endpoints_import_row_error import ApiEndpointsImportRowError
    from ..models.api_endpoints_post_response import ApiEndpointsPostResponse


T = TypeVar("T", bound="ApiEndpointsImportPostsResponse")


@_attrs_define
class ApiEndpointsImportPostsResponse:
    """
    Attributes:
        created (int | Unset):  Example: 8.
        errors (list[ApiEndpointsImportRowError] | Unset):
        failed (int | Unset):  Example: 2.
        posts (list[ApiEndpointsPostResponse] | Unset):
        total_rows (int | Unset):  Example: 10.
    """

    created: int | Unset = UNSET
    errors: list[ApiEndpointsImportRowError] | Unset = UNSET
    failed: int | Unset = UNSET
    posts: list[ApiEndpointsPostResponse] | Unset = UNSET
    total_rows: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created = self.created

        errors: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.errors, Unset):
            errors = []
            for errors_item_data in self.errors:
                errors_item = errors_item_data.to_dict()
                errors.append(errors_item)

        failed = self.failed

        posts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.posts, Unset):
            posts = []
            for posts_item_data in self.posts:
                posts_item = posts_item_data.to_dict()
                posts.append(posts_item)

        total_rows = self.total_rows

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created is not UNSET:
            field_dict["created"] = created
        if errors is not UNSET:
            field_dict["errors"] = errors
        if failed is not UNSET:
            field_dict["failed"] = failed
        if posts is not UNSET:
            field_dict["posts"] = posts
        if total_rows is not UNSET:
            field_dict["total_rows"] = total_rows

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_endpoints_import_row_error import ApiEndpointsImportRowError  # noqa: PLC0415
        from ..models.api_endpoints_post_response import ApiEndpointsPostResponse  # noqa: PLC0415

        d = dict(src_dict)
        created = d.pop("created", UNSET)

        _errors = d.pop("errors", UNSET)
        errors: list[ApiEndpointsImportRowError] | Unset = UNSET
        if _errors is not UNSET:
            errors = []
            for errors_item_data in _errors:
                errors_item = ApiEndpointsImportRowError.from_dict(errors_item_data)

                errors.append(errors_item)

        failed = d.pop("failed", UNSET)

        _posts = d.pop("posts", UNSET)
        posts: list[ApiEndpointsPostResponse] | Unset = UNSET
        if _posts is not UNSET:
            posts = []
            for posts_item_data in _posts:
                posts_item = ApiEndpointsPostResponse.from_dict(posts_item_data)

                posts.append(posts_item)

        total_rows = d.pop("total_rows", UNSET)

        api_endpoints_import_posts_response = cls(
            created=created,
            errors=errors,
            failed=failed,
            posts=posts,
            total_rows=total_rows,
        )

        api_endpoints_import_posts_response.additional_properties = d
        return api_endpoints_import_posts_response

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
