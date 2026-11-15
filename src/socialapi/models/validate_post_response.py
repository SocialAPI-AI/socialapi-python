from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.validation_issue import ValidationIssue


T = TypeVar("T", bound="ValidatePostResponse")


@_attrs_define
class ValidatePostResponse:
    """
    Attributes:
        errors (list[ValidationIssue] | None):
        valid (bool):
        warnings (list[ValidationIssue] | None):
    """

    errors: list[ValidationIssue] | None
    valid: bool
    warnings: list[ValidationIssue] | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        errors: list[dict[str, Any]] | None
        if isinstance(self.errors, list):
            errors = []
            for errors_type_0_item_data in self.errors:
                errors_type_0_item = errors_type_0_item_data.to_dict()
                errors.append(errors_type_0_item)

        else:
            errors = self.errors

        valid = self.valid

        warnings: list[dict[str, Any]] | None
        if isinstance(self.warnings, list):
            warnings = []
            for warnings_type_0_item_data in self.warnings:
                warnings_type_0_item = warnings_type_0_item_data.to_dict()
                warnings.append(warnings_type_0_item)

        else:
            warnings = self.warnings

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "errors": errors,
                "valid": valid,
                "warnings": warnings,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.validation_issue import ValidationIssue  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_errors(data: object) -> list[ValidationIssue] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                errors_type_0 = []
                _errors_type_0 = data
                for errors_type_0_item_data in _errors_type_0:
                    errors_type_0_item = ValidationIssue.from_dict(errors_type_0_item_data)

                    errors_type_0.append(errors_type_0_item)

                return errors_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ValidationIssue] | None, data)

        errors = _parse_errors(d.pop("errors"))

        valid = d.pop("valid")

        def _parse_warnings(data: object) -> list[ValidationIssue] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                warnings_type_0 = []
                _warnings_type_0 = data
                for warnings_type_0_item_data in _warnings_type_0:
                    warnings_type_0_item = ValidationIssue.from_dict(warnings_type_0_item_data)

                    warnings_type_0.append(warnings_type_0_item)

                return warnings_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ValidationIssue] | None, data)

        warnings = _parse_warnings(d.pop("warnings"))

        validate_post_response = cls(
            errors=errors,
            valid=valid,
            warnings=warnings,
        )

        validate_post_response.additional_properties = d
        return validate_post_response

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
