from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_endpoints_migration_assessment import ApiEndpointsMigrationAssessment
    from ..models.api_endpoints_migration_authorisation import ApiEndpointsMigrationAuthorisation


T = TypeVar("T", bound="ApiEndpointsMigrationResponse")


@_attrs_define
class ApiEndpointsMigrationResponse:
    """
    Attributes:
        assessed_at (str | Unset): When the accounts were last read, RFC 3339. Null until the first read succeeds.
        assessment (ApiEndpointsMigrationAssessment | Unset):
        assessment_error (str | Unset): Why `assessment` is null on a started migration: `migration.key_invalid`,
            `migration.key_restricted` or `migration.source_unavailable`.
        authorisation (ApiEndpointsMigrationAuthorisation | Unset):
        authorisation_version (str | Unset): Version of the authorisation text accepted. Null until started.
        authorised_at (str | Unset): When the authorisation was accepted, RFC 3339. Null until started.
        base_url (str | Unset): Base URL to set in your existing client. Null until started. Example: https://z.social-
            api.ai/api.
        created_at (str | Unset): When the migration started, RFC 3339. Null until started.
        cut_over (int | Unset): Accounts already reconnected to SocialAPI.
        forwarded_calls (int | Unset): Requests sent through the base URL since the migration started.
        key_hint (str | Unset): Start and end of the key in use. Null until started.
        started (bool | Unset): True once a migration has started.
    """

    assessed_at: str | Unset = UNSET
    assessment: ApiEndpointsMigrationAssessment | Unset = UNSET
    assessment_error: str | Unset = UNSET
    authorisation: ApiEndpointsMigrationAuthorisation | Unset = UNSET
    authorisation_version: str | Unset = UNSET
    authorised_at: str | Unset = UNSET
    base_url: str | Unset = UNSET
    created_at: str | Unset = UNSET
    cut_over: int | Unset = UNSET
    forwarded_calls: int | Unset = UNSET
    key_hint: str | Unset = UNSET
    started: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        assessed_at = self.assessed_at

        assessment: dict[str, Any] | Unset = UNSET
        if not isinstance(self.assessment, Unset):
            assessment = self.assessment.to_dict()

        assessment_error = self.assessment_error

        authorisation: dict[str, Any] | Unset = UNSET
        if not isinstance(self.authorisation, Unset):
            authorisation = self.authorisation.to_dict()

        authorisation_version = self.authorisation_version

        authorised_at = self.authorised_at

        base_url = self.base_url

        created_at = self.created_at

        cut_over = self.cut_over

        forwarded_calls = self.forwarded_calls

        key_hint = self.key_hint

        started = self.started

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if assessed_at is not UNSET:
            field_dict["assessed_at"] = assessed_at
        if assessment is not UNSET:
            field_dict["assessment"] = assessment
        if assessment_error is not UNSET:
            field_dict["assessment_error"] = assessment_error
        if authorisation is not UNSET:
            field_dict["authorisation"] = authorisation
        if authorisation_version is not UNSET:
            field_dict["authorisation_version"] = authorisation_version
        if authorised_at is not UNSET:
            field_dict["authorised_at"] = authorised_at
        if base_url is not UNSET:
            field_dict["base_url"] = base_url
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if cut_over is not UNSET:
            field_dict["cut_over"] = cut_over
        if forwarded_calls is not UNSET:
            field_dict["forwarded_calls"] = forwarded_calls
        if key_hint is not UNSET:
            field_dict["key_hint"] = key_hint
        if started is not UNSET:
            field_dict["started"] = started

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_endpoints_migration_assessment import ApiEndpointsMigrationAssessment  # noqa: PLC0415
        from ..models.api_endpoints_migration_authorisation import ApiEndpointsMigrationAuthorisation  # noqa: PLC0415

        d = dict(src_dict)
        assessed_at = d.pop("assessed_at", UNSET)

        _assessment = d.pop("assessment", UNSET)
        assessment: ApiEndpointsMigrationAssessment | Unset
        if isinstance(_assessment, Unset):
            assessment = UNSET
        else:
            assessment = ApiEndpointsMigrationAssessment.from_dict(_assessment)

        assessment_error = d.pop("assessment_error", UNSET)

        _authorisation = d.pop("authorisation", UNSET)
        authorisation: ApiEndpointsMigrationAuthorisation | Unset
        if isinstance(_authorisation, Unset):
            authorisation = UNSET
        else:
            authorisation = ApiEndpointsMigrationAuthorisation.from_dict(_authorisation)

        authorisation_version = d.pop("authorisation_version", UNSET)

        authorised_at = d.pop("authorised_at", UNSET)

        base_url = d.pop("base_url", UNSET)

        created_at = d.pop("created_at", UNSET)

        cut_over = d.pop("cut_over", UNSET)

        forwarded_calls = d.pop("forwarded_calls", UNSET)

        key_hint = d.pop("key_hint", UNSET)

        started = d.pop("started", UNSET)

        api_endpoints_migration_response = cls(
            assessed_at=assessed_at,
            assessment=assessment,
            assessment_error=assessment_error,
            authorisation=authorisation,
            authorisation_version=authorisation_version,
            authorised_at=authorised_at,
            base_url=base_url,
            created_at=created_at,
            cut_over=cut_over,
            forwarded_calls=forwarded_calls,
            key_hint=key_hint,
            started=started,
        )

        api_endpoints_migration_response.additional_properties = d
        return api_endpoints_migration_response

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
