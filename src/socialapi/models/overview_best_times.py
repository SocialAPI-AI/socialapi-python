from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.overview_best_time_cell import OverviewBestTimeCell


T = TypeVar("T", bound="OverviewBestTimes")


@_attrs_define
class OverviewBestTimes:
    """
    Attributes:
        cells (list[OverviewBestTimeCell]):
        posts_considered (int):  Example: 42.
    """

    cells: list[OverviewBestTimeCell]
    posts_considered: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cells = []
        for cells_item_data in self.cells:
            cells_item = cells_item_data.to_dict()
            cells.append(cells_item)

        posts_considered = self.posts_considered

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cells": cells,
                "posts_considered": posts_considered,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.overview_best_time_cell import OverviewBestTimeCell  # noqa: PLC0415

        d = dict(src_dict)
        cells = []
        _cells = d.pop("cells")
        for cells_item_data in _cells:
            cells_item = OverviewBestTimeCell.from_dict(cells_item_data)

            cells.append(cells_item)

        posts_considered = d.pop("posts_considered")

        overview_best_times = cls(
            cells=cells,
            posts_considered=posts_considered,
        )

        overview_best_times.additional_properties = d
        return overview_best_times

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
