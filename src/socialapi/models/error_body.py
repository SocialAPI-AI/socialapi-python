from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.error_body_meta import ErrorBodyMeta


T = TypeVar("T", bound="ErrorBody")


@_attrs_define
class ErrorBody:
    """
    Attributes:
        code (str):  Example: resource.not_found.
        message (str):  Example: Account not found.
        meta (ErrorBodyMeta | Unset):
    """

    code: str
    message: str
    meta: ErrorBodyMeta | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        message = self.message

        meta: dict[str, Any] | Unset = UNSET
        if not isinstance(self.meta, Unset):
            meta = self.meta.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
                "message": message,
            }
        )
        if meta is not UNSET:
            field_dict["meta"] = meta

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.error_body_meta import ErrorBodyMeta  # noqa: PLC0415

        d = dict(src_dict)
        code = d.pop("code")

        message = d.pop("message")

        _meta = d.pop("meta", UNSET)
        meta: ErrorBodyMeta | Unset
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = ErrorBodyMeta.from_dict(_meta)

        error_body = cls(
            code=code,
            message=message,
            meta=meta,
        )

        error_body.additional_properties = d
        return error_body

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
