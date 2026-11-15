from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.post_target_error_category import PostTargetErrorCategory
from ..models.post_target_error_cause import PostTargetErrorCause

T = TypeVar("T", bound="PostTargetErrorResponse")


@_attrs_define
class PostTargetErrorResponse:
    """
    Attributes:
        category (PostTargetErrorCategory):
        caused_by (PostTargetErrorCause):
        code (str):  Example: platform.tiktok.media_required.
        message (str):  Example: Video posts require at least one media URL.
    """

    category: PostTargetErrorCategory
    caused_by: PostTargetErrorCause
    code: str
    message: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        category = self.category.value

        caused_by = self.caused_by.value

        code = self.code

        message = self.message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "category": category,
                "caused_by": caused_by,
                "code": code,
                "message": message,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        category = PostTargetErrorCategory(d.pop("category"))

        caused_by = PostTargetErrorCause(d.pop("caused_by"))

        code = d.pop("code")

        message = d.pop("message")

        post_target_error_response = cls(
            category=category,
            caused_by=caused_by,
            code=code,
            message=message,
        )

        post_target_error_response.additional_properties = d
        return post_target_error_response

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
