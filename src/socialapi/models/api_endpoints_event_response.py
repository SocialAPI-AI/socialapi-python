from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_endpoints_event_response_metadata import ApiEndpointsEventResponseMetadata


T = TypeVar("T", bound="ApiEndpointsEventResponse")


@_attrs_define
class ApiEndpointsEventResponse:
    """
    Attributes:
        account_id (str | Unset):
        action (str | Unset):  Example: publish.
        category (str | Unset):  Example: post.
        created_at (str | Unset):  Example: 2026-03-27T10:00:00Z.
        duration_ms (int | Unset):  Example: 230.
        error_category (str | Unset):  Example: validation.
        error_message (str | Unset):
        id (str | Unset):
        metadata (ApiEndpointsEventResponseMetadata | Unset):
        platform (str | Unset):  Example: instagram.
        resource_id (str | Unset):
        status (str | Unset):  Example: success.
        status_code (int | Unset):  Example: 400.
        summary (str | Unset):  Example: Published to Instagram.
    """

    account_id: str | Unset = UNSET
    action: str | Unset = UNSET
    category: str | Unset = UNSET
    created_at: str | Unset = UNSET
    duration_ms: int | Unset = UNSET
    error_category: str | Unset = UNSET
    error_message: str | Unset = UNSET
    id: str | Unset = UNSET
    metadata: ApiEndpointsEventResponseMetadata | Unset = UNSET
    platform: str | Unset = UNSET
    resource_id: str | Unset = UNSET
    status: str | Unset = UNSET
    status_code: int | Unset = UNSET
    summary: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_id = self.account_id

        action = self.action

        category = self.category

        created_at = self.created_at

        duration_ms = self.duration_ms

        error_category = self.error_category

        error_message = self.error_message

        id = self.id

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        platform = self.platform

        resource_id = self.resource_id

        status = self.status

        status_code = self.status_code

        summary = self.summary

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_id is not UNSET:
            field_dict["account_id"] = account_id
        if action is not UNSET:
            field_dict["action"] = action
        if category is not UNSET:
            field_dict["category"] = category
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if duration_ms is not UNSET:
            field_dict["duration_ms"] = duration_ms
        if error_category is not UNSET:
            field_dict["error_category"] = error_category
        if error_message is not UNSET:
            field_dict["error_message"] = error_message
        if id is not UNSET:
            field_dict["id"] = id
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if platform is not UNSET:
            field_dict["platform"] = platform
        if resource_id is not UNSET:
            field_dict["resource_id"] = resource_id
        if status is not UNSET:
            field_dict["status"] = status
        if status_code is not UNSET:
            field_dict["status_code"] = status_code
        if summary is not UNSET:
            field_dict["summary"] = summary

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_endpoints_event_response_metadata import ApiEndpointsEventResponseMetadata  # noqa: PLC0415

        d = dict(src_dict)
        account_id = d.pop("account_id", UNSET)

        action = d.pop("action", UNSET)

        category = d.pop("category", UNSET)

        created_at = d.pop("created_at", UNSET)

        duration_ms = d.pop("duration_ms", UNSET)

        error_category = d.pop("error_category", UNSET)

        error_message = d.pop("error_message", UNSET)

        id = d.pop("id", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: ApiEndpointsEventResponseMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = ApiEndpointsEventResponseMetadata.from_dict(_metadata)

        platform = d.pop("platform", UNSET)

        resource_id = d.pop("resource_id", UNSET)

        status = d.pop("status", UNSET)

        status_code = d.pop("status_code", UNSET)

        summary = d.pop("summary", UNSET)

        api_endpoints_event_response = cls(
            account_id=account_id,
            action=action,
            category=category,
            created_at=created_at,
            duration_ms=duration_ms,
            error_category=error_category,
            error_message=error_message,
            id=id,
            metadata=metadata,
            platform=platform,
            resource_id=resource_id,
            status=status,
            status_code=status_code,
            summary=summary,
        )

        api_endpoints_event_response.additional_properties = d
        return api_endpoints_event_response

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
