from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.sync_state import SyncState

if TYPE_CHECKING:
    from ..models.inbox_message import InboxMessage
    from ..models.inbox_pagination import InboxPagination


T = TypeVar("T", bound="MessagesListResponse")


@_attrs_define
class MessagesListResponse:
    """
    Attributes:
        data (list[InboxMessage] | None):
        last_synced_at (datetime.datetime | None):
        pagination (InboxPagination):
        sync_state (SyncState):
    """

    data: list[InboxMessage] | None
    last_synced_at: datetime.datetime | None
    pagination: InboxPagination
    sync_state: SyncState
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data: list[dict[str, Any]] | None
        if isinstance(self.data, list):
            data = []
            for data_type_0_item_data in self.data:
                data_type_0_item = data_type_0_item_data.to_dict()
                data.append(data_type_0_item)

        else:
            data = self.data

        last_synced_at: None | str
        if isinstance(self.last_synced_at, datetime.datetime):
            last_synced_at = self.last_synced_at.isoformat()
        else:
            last_synced_at = self.last_synced_at

        pagination = self.pagination.to_dict()

        sync_state = self.sync_state.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
                "last_synced_at": last_synced_at,
                "pagination": pagination,
                "sync_state": sync_state,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.inbox_message import InboxMessage  # noqa: PLC0415
        from ..models.inbox_pagination import InboxPagination  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_data(data: object) -> list[InboxMessage] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                data_type_0 = []
                _data_type_0 = data
                for data_type_0_item_data in _data_type_0:
                    data_type_0_item = InboxMessage.from_dict(data_type_0_item_data)

                    data_type_0.append(data_type_0_item)

                return data_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[InboxMessage] | None, data)

        data = _parse_data(d.pop("data"))

        def _parse_last_synced_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_synced_at_type_0 = datetime.datetime.fromisoformat(data)

                return last_synced_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        last_synced_at = _parse_last_synced_at(d.pop("last_synced_at"))

        pagination = InboxPagination.from_dict(d.pop("pagination"))

        sync_state = SyncState(d.pop("sync_state"))

        messages_list_response = cls(
            data=data,
            last_synced_at=last_synced_at,
            pagination=pagination,
            sync_state=sync_state,
        )

        messages_list_response.additional_properties = d
        return messages_list_response

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
