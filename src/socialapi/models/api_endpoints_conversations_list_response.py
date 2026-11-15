from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.api_endpoints_conversations_list_response_sync_state import ApiEndpointsConversationsListResponseSyncState
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_endpoints_inbox_pagination import ApiEndpointsInboxPagination
    from ..models.social_api_ai_core_api_service_conversation_row import SocialApiAiCoreApiServiceConversationRow


T = TypeVar("T", bound="ApiEndpointsConversationsListResponse")


@_attrs_define
class ApiEndpointsConversationsListResponse:
    """
    Attributes:
        data (list[SocialApiAiCoreApiServiceConversationRow] | Unset):
        last_synced_at (str | Unset):
        pagination (ApiEndpointsInboxPagination | Unset):
        sync_state (ApiEndpointsConversationsListResponseSyncState | Unset): SyncState is "idle", "syncing", or "failed"
            for this account's
            conversation-list sync. Reading it never triggers a sync, and a client
            that ignores it sees exactly the previous response. Example: idle.
    """

    data: list[SocialApiAiCoreApiServiceConversationRow] | Unset = UNSET
    last_synced_at: str | Unset = UNSET
    pagination: ApiEndpointsInboxPagination | Unset = UNSET
    sync_state: ApiEndpointsConversationsListResponseSyncState | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item = data_item_data.to_dict()
                data.append(data_item)

        last_synced_at = self.last_synced_at

        pagination: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pagination, Unset):
            pagination = self.pagination.to_dict()

        sync_state: str | Unset = UNSET
        if not isinstance(self.sync_state, Unset):
            sync_state = self.sync_state.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data
        if last_synced_at is not UNSET:
            field_dict["last_synced_at"] = last_synced_at
        if pagination is not UNSET:
            field_dict["pagination"] = pagination
        if sync_state is not UNSET:
            field_dict["sync_state"] = sync_state

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_endpoints_inbox_pagination import ApiEndpointsInboxPagination  # noqa: PLC0415
        from ..models.social_api_ai_core_api_service_conversation_row import (
            SocialApiAiCoreApiServiceConversationRow,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _data = d.pop("data", UNSET)
        data: list[SocialApiAiCoreApiServiceConversationRow] | Unset = UNSET
        if _data is not UNSET:
            data = []
            for data_item_data in _data:
                data_item = SocialApiAiCoreApiServiceConversationRow.from_dict(data_item_data)

                data.append(data_item)

        last_synced_at = d.pop("last_synced_at", UNSET)

        _pagination = d.pop("pagination", UNSET)
        pagination: ApiEndpointsInboxPagination | Unset
        if isinstance(_pagination, Unset):
            pagination = UNSET
        else:
            pagination = ApiEndpointsInboxPagination.from_dict(_pagination)

        _sync_state = d.pop("sync_state", UNSET)
        sync_state: ApiEndpointsConversationsListResponseSyncState | Unset
        if isinstance(_sync_state, Unset):
            sync_state = UNSET
        else:
            sync_state = ApiEndpointsConversationsListResponseSyncState(_sync_state)

        api_endpoints_conversations_list_response = cls(
            data=data,
            last_synced_at=last_synced_at,
            pagination=pagination,
            sync_state=sync_state,
        )

        api_endpoints_conversations_list_response.additional_properties = d
        return api_endpoints_conversations_list_response

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
