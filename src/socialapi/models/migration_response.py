from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.migration_assessment import MigrationAssessment
    from ..models.migration_authorisation import MigrationAuthorisation


T = TypeVar("T", bound="MigrationResponse")


@_attrs_define
class MigrationResponse:
    """
    Attributes:
        assessed_at (datetime.datetime | None): When the accounts were last read, RFC 3339. Null until the first read
            succeeds.
        assessment (MigrationAssessment | None): Your accounts and how they map to SocialAPI. Null until started, or
            when your provider could not be read.
        assessment_error (None | str): Why `assessment` is null on a started migration: `migration.key_invalid`,
            `migration.key_restricted` or `migration.source_unavailable`.
        authorisation (MigrationAuthorisation):
        authorisation_version (None | str): Version of the authorisation text accepted. Null until started.
        authorised_at (datetime.datetime | None): When the authorisation was accepted, RFC 3339. Null until started.
        base_url (None | str): Base URL to set in your existing client. Null until started. Example: https://z.social-
            api.ai/api.
        created_at (datetime.datetime | None): When the migration started, RFC 3339. Null until started.
        cut_over (int): Accounts already reconnected to SocialAPI.
        forwarded_calls (int): Requests sent through the base URL since the migration started.
        key_hint (None | str): Start and end of the key in use. Null until started.
        started (bool): True once a migration has started.
    """

    assessed_at: datetime.datetime | None
    assessment: MigrationAssessment | None
    assessment_error: None | str
    authorisation: MigrationAuthorisation
    authorisation_version: None | str
    authorised_at: datetime.datetime | None
    base_url: None | str
    created_at: datetime.datetime | None
    cut_over: int
    forwarded_calls: int
    key_hint: None | str
    started: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.migration_assessment import MigrationAssessment  # noqa: PLC0415

        assessed_at: None | str
        if isinstance(self.assessed_at, datetime.datetime):
            assessed_at = self.assessed_at.isoformat()
        else:
            assessed_at = self.assessed_at

        assessment: dict[str, Any] | None
        if isinstance(self.assessment, MigrationAssessment):
            assessment = self.assessment.to_dict()
        else:
            assessment = self.assessment

        assessment_error: None | str
        assessment_error = self.assessment_error

        authorisation = self.authorisation.to_dict()

        authorisation_version: None | str
        authorisation_version = self.authorisation_version

        authorised_at: None | str
        if isinstance(self.authorised_at, datetime.datetime):
            authorised_at = self.authorised_at.isoformat()
        else:
            authorised_at = self.authorised_at

        base_url: None | str
        base_url = self.base_url

        created_at: None | str
        if isinstance(self.created_at, datetime.datetime):
            created_at = self.created_at.isoformat()
        else:
            created_at = self.created_at

        cut_over = self.cut_over

        forwarded_calls = self.forwarded_calls

        key_hint: None | str
        key_hint = self.key_hint

        started = self.started

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "assessed_at": assessed_at,
                "assessment": assessment,
                "assessment_error": assessment_error,
                "authorisation": authorisation,
                "authorisation_version": authorisation_version,
                "authorised_at": authorised_at,
                "base_url": base_url,
                "created_at": created_at,
                "cut_over": cut_over,
                "forwarded_calls": forwarded_calls,
                "key_hint": key_hint,
                "started": started,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.migration_assessment import MigrationAssessment  # noqa: PLC0415
        from ..models.migration_authorisation import MigrationAuthorisation  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_assessed_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                assessed_at_type_0 = datetime.datetime.fromisoformat(data)

                return assessed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        assessed_at = _parse_assessed_at(d.pop("assessed_at"))

        def _parse_assessment(data: object) -> MigrationAssessment | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                assessment_type_1 = MigrationAssessment.from_dict(data)

                return assessment_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MigrationAssessment | None, data)

        assessment = _parse_assessment(d.pop("assessment"))

        def _parse_assessment_error(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        assessment_error = _parse_assessment_error(d.pop("assessment_error"))

        authorisation = MigrationAuthorisation.from_dict(d.pop("authorisation"))

        def _parse_authorisation_version(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        authorisation_version = _parse_authorisation_version(d.pop("authorisation_version"))

        def _parse_authorised_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                authorised_at_type_0 = datetime.datetime.fromisoformat(data)

                return authorised_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        authorised_at = _parse_authorised_at(d.pop("authorised_at"))

        def _parse_base_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        base_url = _parse_base_url(d.pop("base_url"))

        def _parse_created_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_at_type_0 = datetime.datetime.fromisoformat(data)

                return created_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        created_at = _parse_created_at(d.pop("created_at"))

        cut_over = d.pop("cut_over")

        forwarded_calls = d.pop("forwarded_calls")

        def _parse_key_hint(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        key_hint = _parse_key_hint(d.pop("key_hint"))

        started = d.pop("started")

        migration_response = cls(
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

        migration_response.additional_properties = d
        return migration_response

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
