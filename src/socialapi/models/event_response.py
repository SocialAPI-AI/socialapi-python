from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.platform import Platform
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.event_response_metadata_type_0 import EventResponseMetadataType0


T = TypeVar("T", bound="EventResponse")


@_attrs_define
class EventResponse:
    """
    Attributes:
        action (str):  Example: publish.
        category (str):  Example: post.
        created_at (datetime.datetime):  Example: 2026-03-27T10:00:00Z.
        id (str):
        metadata (EventResponseMetadataType0 | None):
        status (str):  Example: success.
        summary (str):  Example: Published to Instagram.
        account_id (str | Unset):
        duration_ms (int | Unset):  Example: 230.
        error_category (str | Unset):  Example: validation.
        error_message (str | Unset):
        platform (Platform | Unset):
        resource_id (str | Unset):
        status_code (int | Unset):  Example: 400.
    """

    action: str
    category: str
    created_at: datetime.datetime
    id: str
    metadata: EventResponseMetadataType0 | None
    status: str
    summary: str
    account_id: str | Unset = UNSET
    duration_ms: int | Unset = UNSET
    error_category: str | Unset = UNSET
    error_message: str | Unset = UNSET
    platform: Platform | Unset = UNSET
    resource_id: str | Unset = UNSET
    status_code: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.event_response_metadata_type_0 import EventResponseMetadataType0  # noqa: PLC0415

        action = self.action

        category = self.category

        created_at = self.created_at.isoformat()

        id = self.id

        metadata: dict[str, Any] | None
        if isinstance(self.metadata, EventResponseMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        status = self.status

        summary = self.summary

        account_id = self.account_id

        duration_ms = self.duration_ms

        error_category = self.error_category

        error_message = self.error_message

        platform: str | Unset = UNSET
        if not isinstance(self.platform, Unset):
            platform = self.platform.value

        resource_id = self.resource_id

        status_code = self.status_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "action": action,
                "category": category,
                "created_at": created_at,
                "id": id,
                "metadata": metadata,
                "status": status,
                "summary": summary,
            }
        )
        if account_id is not UNSET:
            field_dict["account_id"] = account_id
        if duration_ms is not UNSET:
            field_dict["duration_ms"] = duration_ms
        if error_category is not UNSET:
            field_dict["error_category"] = error_category
        if error_message is not UNSET:
            field_dict["error_message"] = error_message
        if platform is not UNSET:
            field_dict["platform"] = platform
        if resource_id is not UNSET:
            field_dict["resource_id"] = resource_id
        if status_code is not UNSET:
            field_dict["status_code"] = status_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.event_response_metadata_type_0 import EventResponseMetadataType0  # noqa: PLC0415

        d = dict(src_dict)
        action = d.pop("action")

        category = d.pop("category")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        id = d.pop("id")

        def _parse_metadata(data: object) -> EventResponseMetadataType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = EventResponseMetadataType0.from_dict(data)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EventResponseMetadataType0 | None, data)

        metadata = _parse_metadata(d.pop("metadata"))

        status = d.pop("status")

        summary = d.pop("summary")

        account_id = d.pop("account_id", UNSET)

        duration_ms = d.pop("duration_ms", UNSET)

        error_category = d.pop("error_category", UNSET)

        error_message = d.pop("error_message", UNSET)

        _platform = d.pop("platform", UNSET)
        platform: Platform | Unset
        if isinstance(_platform, Unset):
            platform = UNSET
        else:
            platform = Platform(_platform)

        resource_id = d.pop("resource_id", UNSET)

        status_code = d.pop("status_code", UNSET)

        event_response = cls(
            action=action,
            category=category,
            created_at=created_at,
            id=id,
            metadata=metadata,
            status=status,
            summary=summary,
            account_id=account_id,
            duration_ms=duration_ms,
            error_category=error_category,
            error_message=error_message,
            platform=platform,
            resource_id=resource_id,
            status_code=status_code,
        )

        event_response.additional_properties = d
        return event_response

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
