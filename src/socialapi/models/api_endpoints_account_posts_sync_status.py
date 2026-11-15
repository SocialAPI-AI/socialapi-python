from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.api_endpoints_account_posts_sync_status_state import ApiEndpointsAccountPostsSyncStatusState
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiEndpointsAccountPostsSyncStatus")


@_attrs_define
class ApiEndpointsAccountPostsSyncStatus:
    """
    Attributes:
        error (str | Unset): Error says why the last sync failed. Empty unless State is "failed".
        finished_at (str | Unset):
        last_synced_at (str | Unset):
        started_at (str | Unset):
        state (ApiEndpointsAccountPostsSyncStatusState | Unset): State is "idle", "syncing", or "failed". A finished
            sync is idle with a
            newer LastSyncedAt. Example: syncing.
    """

    error: str | Unset = UNSET
    finished_at: str | Unset = UNSET
    last_synced_at: str | Unset = UNSET
    started_at: str | Unset = UNSET
    state: ApiEndpointsAccountPostsSyncStatusState | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        error = self.error

        finished_at = self.finished_at

        last_synced_at = self.last_synced_at

        started_at = self.started_at

        state: str | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if error is not UNSET:
            field_dict["error"] = error
        if finished_at is not UNSET:
            field_dict["finished_at"] = finished_at
        if last_synced_at is not UNSET:
            field_dict["last_synced_at"] = last_synced_at
        if started_at is not UNSET:
            field_dict["started_at"] = started_at
        if state is not UNSET:
            field_dict["state"] = state

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        error = d.pop("error", UNSET)

        finished_at = d.pop("finished_at", UNSET)

        last_synced_at = d.pop("last_synced_at", UNSET)

        started_at = d.pop("started_at", UNSET)

        _state = d.pop("state", UNSET)
        state: ApiEndpointsAccountPostsSyncStatusState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = ApiEndpointsAccountPostsSyncStatusState(_state)

        api_endpoints_account_posts_sync_status = cls(
            error=error,
            finished_at=finished_at,
            last_synced_at=last_synced_at,
            started_at=started_at,
            state=state,
        )

        api_endpoints_account_posts_sync_status.additional_properties = d
        return api_endpoints_account_posts_sync_status

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
