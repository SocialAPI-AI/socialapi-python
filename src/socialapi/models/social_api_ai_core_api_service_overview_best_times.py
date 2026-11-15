from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.social_api_ai_core_api_service_overview_best_time_cell import (
        SocialApiAiCoreApiServiceOverviewBestTimeCell,
    )


T = TypeVar("T", bound="SocialApiAiCoreApiServiceOverviewBestTimes")


@_attrs_define
class SocialApiAiCoreApiServiceOverviewBestTimes:
    """
    Attributes:
        cells (list[SocialApiAiCoreApiServiceOverviewBestTimeCell] | Unset):
        posts_considered (int | Unset):  Example: 42.
    """

    cells: list[SocialApiAiCoreApiServiceOverviewBestTimeCell] | Unset = UNSET
    posts_considered: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cells: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.cells, Unset):
            cells = []
            for cells_item_data in self.cells:
                cells_item = cells_item_data.to_dict()
                cells.append(cells_item)

        posts_considered = self.posts_considered

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cells is not UNSET:
            field_dict["cells"] = cells
        if posts_considered is not UNSET:
            field_dict["posts_considered"] = posts_considered

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.social_api_ai_core_api_service_overview_best_time_cell import (
            SocialApiAiCoreApiServiceOverviewBestTimeCell,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _cells = d.pop("cells", UNSET)
        cells: list[SocialApiAiCoreApiServiceOverviewBestTimeCell] | Unset = UNSET
        if _cells is not UNSET:
            cells = []
            for cells_item_data in _cells:
                cells_item = SocialApiAiCoreApiServiceOverviewBestTimeCell.from_dict(cells_item_data)

                cells.append(cells_item)

        posts_considered = d.pop("posts_considered", UNSET)

        social_api_ai_core_api_service_overview_best_times = cls(
            cells=cells,
            posts_considered=posts_considered,
        )

        social_api_ai_core_api_service_overview_best_times.additional_properties = d
        return social_api_ai_core_api_service_overview_best_times

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
