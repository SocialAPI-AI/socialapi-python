from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.sync_state import SyncState

T = TypeVar("T", bound="AccountPostsSyncStatus")


@_attrs_define
class AccountPostsSyncStatus:
    """
    Attributes:
        error (str): Error says why the last sync failed. Empty unless State is "failed".
        finished_at (None | str):
        last_synced_at (None | str):
        started_at (None | str):
        state (SyncState):
    """

    error: str
    finished_at: None | str
    last_synced_at: None | str
    started_at: None | str
    state: SyncState
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        error = self.error

        finished_at: None | str
        finished_at = self.finished_at

        last_synced_at: None | str
        last_synced_at = self.last_synced_at

        started_at: None | str
        started_at = self.started_at

        state = self.state.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "error": error,
                "finished_at": finished_at,
                "last_synced_at": last_synced_at,
                "started_at": started_at,
                "state": state,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        error = d.pop("error")

        def _parse_finished_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        finished_at = _parse_finished_at(d.pop("finished_at"))

        def _parse_last_synced_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        last_synced_at = _parse_last_synced_at(d.pop("last_synced_at"))

        def _parse_started_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        started_at = _parse_started_at(d.pop("started_at"))

        state = SyncState(d.pop("state"))

        account_posts_sync_status = cls(
            error=error,
            finished_at=finished_at,
            last_synced_at=last_synced_at,
            started_at=started_at,
            state=state,
        )

        account_posts_sync_status.additional_properties = d
        return account_posts_sync_status

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
