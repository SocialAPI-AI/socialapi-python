from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.filter_type import FilterType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.keyword_filter import KeywordFilter


T = TypeVar("T", bound="Filter")


@_attrs_define
class Filter:
    """
    Attributes:
        type_ (FilterType):
        keyword (KeywordFilter | Unset):
    """

    type_: FilterType
    keyword: KeywordFilter | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        keyword: dict[str, Any] | Unset = UNSET
        if not isinstance(self.keyword, Unset):
            keyword = self.keyword.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if keyword is not UNSET:
            field_dict["keyword"] = keyword

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.keyword_filter import KeywordFilter  # noqa: PLC0415

        d = dict(src_dict)
        type_ = FilterType(d.pop("type"))

        _keyword = d.pop("keyword", UNSET)
        keyword: KeywordFilter | Unset
        if isinstance(_keyword, Unset):
            keyword = UNSET
        else:
            keyword = KeywordFilter.from_dict(_keyword)

        filter_ = cls(
            type_=type_,
            keyword=keyword,
        )

        filter_.additional_properties = d
        return filter_

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
