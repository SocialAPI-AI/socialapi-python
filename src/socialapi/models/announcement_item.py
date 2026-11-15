from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AnnouncementItem")


@_attrs_define
class AnnouncementItem:
    """
    Attributes:
        body (str):  Example: We are upgrading our database infrastructure..
        id (str):  Example: 9c1e7f2a-3b4d-4e5f-8a9b-0c1d2e3f4a5b.
        kind (str):  Example: maintenance.
        seen (bool):  Example: False.
        title (str):  Example: Scheduled maintenance.
        link_label (str | Unset):  Example: Status page.
        link_url (str | Unset):  Example: https://status.social-api.ai.
        window_end (str | Unset):  Example: 2026-08-02T04:00:00Z.
        window_start (str | Unset):  Example: 2026-08-02T02:00:00Z.
    """

    body: str
    id: str
    kind: str
    seen: bool
    title: str
    link_label: str | Unset = UNSET
    link_url: str | Unset = UNSET
    window_end: str | Unset = UNSET
    window_start: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        body = self.body

        id = self.id

        kind = self.kind

        seen = self.seen

        title = self.title

        link_label = self.link_label

        link_url = self.link_url

        window_end = self.window_end

        window_start = self.window_start

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "body": body,
                "id": id,
                "kind": kind,
                "seen": seen,
                "title": title,
            }
        )
        if link_label is not UNSET:
            field_dict["link_label"] = link_label
        if link_url is not UNSET:
            field_dict["link_url"] = link_url
        if window_end is not UNSET:
            field_dict["window_end"] = window_end
        if window_start is not UNSET:
            field_dict["window_start"] = window_start

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        body = d.pop("body")

        id = d.pop("id")

        kind = d.pop("kind")

        seen = d.pop("seen")

        title = d.pop("title")

        link_label = d.pop("link_label", UNSET)

        link_url = d.pop("link_url", UNSET)

        window_end = d.pop("window_end", UNSET)

        window_start = d.pop("window_start", UNSET)

        announcement_item = cls(
            body=body,
            id=id,
            kind=kind,
            seen=seen,
            title=title,
            link_label=link_label,
            link_url=link_url,
            window_end=window_end,
            window_start=window_start,
        )

        announcement_item.additional_properties = d
        return announcement_item

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
