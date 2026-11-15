from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_endpoints_export_result_ur_ls import ApiEndpointsExportResultURLs


T = TypeVar("T", bound="ApiEndpointsExportStatusResponse")


@_attrs_define
class ApiEndpointsExportStatusResponse:
    """
    Attributes:
        account_id (str | Unset):
        completed_at (str | Unset):
        created_at (str | Unset):
        error (str | Unset):
        expires_at (str | Unset):
        id (str | Unset):
        platform (str | Unset):
        processed_videos (int | Unset):
        result (ApiEndpointsExportResultURLs | Unset):
        status (str | Unset):
        total_videos (int | Unset):
    """

    account_id: str | Unset = UNSET
    completed_at: str | Unset = UNSET
    created_at: str | Unset = UNSET
    error: str | Unset = UNSET
    expires_at: str | Unset = UNSET
    id: str | Unset = UNSET
    platform: str | Unset = UNSET
    processed_videos: int | Unset = UNSET
    result: ApiEndpointsExportResultURLs | Unset = UNSET
    status: str | Unset = UNSET
    total_videos: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_id = self.account_id

        completed_at = self.completed_at

        created_at = self.created_at

        error = self.error

        expires_at = self.expires_at

        id = self.id

        platform = self.platform

        processed_videos = self.processed_videos

        result: dict[str, Any] | Unset = UNSET
        if not isinstance(self.result, Unset):
            result = self.result.to_dict()

        status = self.status

        total_videos = self.total_videos

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_id is not UNSET:
            field_dict["account_id"] = account_id
        if completed_at is not UNSET:
            field_dict["completed_at"] = completed_at
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if error is not UNSET:
            field_dict["error"] = error
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at
        if id is not UNSET:
            field_dict["id"] = id
        if platform is not UNSET:
            field_dict["platform"] = platform
        if processed_videos is not UNSET:
            field_dict["processed_videos"] = processed_videos
        if result is not UNSET:
            field_dict["result"] = result
        if status is not UNSET:
            field_dict["status"] = status
        if total_videos is not UNSET:
            field_dict["total_videos"] = total_videos

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_endpoints_export_result_ur_ls import ApiEndpointsExportResultURLs  # noqa: PLC0415

        d = dict(src_dict)
        account_id = d.pop("account_id", UNSET)

        completed_at = d.pop("completed_at", UNSET)

        created_at = d.pop("created_at", UNSET)

        error = d.pop("error", UNSET)

        expires_at = d.pop("expires_at", UNSET)

        id = d.pop("id", UNSET)

        platform = d.pop("platform", UNSET)

        processed_videos = d.pop("processed_videos", UNSET)

        _result = d.pop("result", UNSET)
        result: ApiEndpointsExportResultURLs | Unset
        if isinstance(_result, Unset):
            result = UNSET
        else:
            result = ApiEndpointsExportResultURLs.from_dict(_result)

        status = d.pop("status", UNSET)

        total_videos = d.pop("total_videos", UNSET)

        api_endpoints_export_status_response = cls(
            account_id=account_id,
            completed_at=completed_at,
            created_at=created_at,
            error=error,
            expires_at=expires_at,
            id=id,
            platform=platform,
            processed_videos=processed_videos,
            result=result,
            status=status,
            total_videos=total_videos,
        )

        api_endpoints_export_status_response.additional_properties = d
        return api_endpoints_export_status_response

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
