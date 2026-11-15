from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_endpoints_event_response import ApiEndpointsEventResponse
    from ..models.api_endpoints_pagination_info import ApiEndpointsPaginationInfo


T = TypeVar("T", bound="ApiEndpointsEventsListResponse")


@_attrs_define
class ApiEndpointsEventsListResponse:
    """
    Attributes:
        events (list[ApiEndpointsEventResponse] | Unset):
        pagination (ApiEndpointsPaginationInfo | Unset):
        retention_days (int | Unset):  Example: 30.
    """

    events: list[ApiEndpointsEventResponse] | Unset = UNSET
    pagination: ApiEndpointsPaginationInfo | Unset = UNSET
    retention_days: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        events: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.events, Unset):
            events = []
            for events_item_data in self.events:
                events_item = events_item_data.to_dict()
                events.append(events_item)

        pagination: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pagination, Unset):
            pagination = self.pagination.to_dict()

        retention_days = self.retention_days

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if events is not UNSET:
            field_dict["events"] = events
        if pagination is not UNSET:
            field_dict["pagination"] = pagination
        if retention_days is not UNSET:
            field_dict["retention_days"] = retention_days

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_endpoints_event_response import ApiEndpointsEventResponse  # noqa: PLC0415
        from ..models.api_endpoints_pagination_info import ApiEndpointsPaginationInfo  # noqa: PLC0415

        d = dict(src_dict)
        _events = d.pop("events", UNSET)
        events: list[ApiEndpointsEventResponse] | Unset = UNSET
        if _events is not UNSET:
            events = []
            for events_item_data in _events:
                events_item = ApiEndpointsEventResponse.from_dict(events_item_data)

                events.append(events_item)

        _pagination = d.pop("pagination", UNSET)
        pagination: ApiEndpointsPaginationInfo | Unset
        if isinstance(_pagination, Unset):
            pagination = UNSET
        else:
            pagination = ApiEndpointsPaginationInfo.from_dict(_pagination)

        retention_days = d.pop("retention_days", UNSET)

        api_endpoints_events_list_response = cls(
            events=events,
            pagination=pagination,
            retention_days=retention_days,
        )

        api_endpoints_events_list_response.additional_properties = d
        return api_endpoints_events_list_response

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
