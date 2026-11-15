from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.social_api_ai_core_api_connectors_base_gbp_address_update import (
        SocialApiAiCoreApiConnectorsBaseGBPAddressUpdate,
    )
    from ..models.social_api_ai_core_api_connectors_base_gbp_categories_update import (
        SocialApiAiCoreApiConnectorsBaseGBPCategoriesUpdate,
    )
    from ..models.social_api_ai_core_api_connectors_base_gbp_hours_update import (
        SocialApiAiCoreApiConnectorsBaseGBPHoursUpdate,
    )
    from ..models.social_api_ai_core_api_connectors_base_gbp_lat_lng import SocialApiAiCoreApiConnectorsBaseGBPLatLng
    from ..models.social_api_ai_core_api_connectors_base_gbp_more_hours import (
        SocialApiAiCoreApiConnectorsBaseGBPMoreHours,
    )
    from ..models.social_api_ai_core_api_connectors_base_gbp_phone_numbers_update import (
        SocialApiAiCoreApiConnectorsBaseGBPPhoneNumbersUpdate,
    )
    from ..models.social_api_ai_core_api_connectors_base_gbp_service_area_update import (
        SocialApiAiCoreApiConnectorsBaseGBPServiceAreaUpdate,
    )
    from ..models.social_api_ai_core_api_connectors_base_gbp_service_item import (
        SocialApiAiCoreApiConnectorsBaseGBPServiceItem,
    )
    from ..models.social_api_ai_core_api_connectors_base_gbp_special_hours_update import (
        SocialApiAiCoreApiConnectorsBaseGBPSpecialHoursUpdate,
    )


T = TypeVar("T", bound="SocialApiAiCoreApiConnectorsBaseGBPLocationUpdate")


@_attrs_define
class SocialApiAiCoreApiConnectorsBaseGBPLocationUpdate:
    """
    Attributes:
        ad_phone (str | Unset): AdPhone is the alternate number shown on Google Ads extensions.
        categories (SocialApiAiCoreApiConnectorsBaseGBPCategoriesUpdate | Unset):
        description (str | Unset):  Example: Wood-fired pizza since 1998.
        labels (list[str] | Unset):
        latlng (SocialApiAiCoreApiConnectorsBaseGBPLatLng | Unset):
        more_hours (list[SocialApiAiCoreApiConnectorsBaseGBPMoreHours] | Unset):
        open_status (str | Unset): OpenStatus is OPEN, CLOSED_PERMANENTLY or CLOSED_TEMPORARILY. Example: OPEN.
        phone_numbers (SocialApiAiCoreApiConnectorsBaseGBPPhoneNumbersUpdate | Unset):
        regular_hours (SocialApiAiCoreApiConnectorsBaseGBPHoursUpdate | Unset):
        service_area (SocialApiAiCoreApiConnectorsBaseGBPServiceAreaUpdate | Unset):
        service_items (list[SocialApiAiCoreApiConnectorsBaseGBPServiceItem] | Unset): ServiceItems replaces the whole
            list of services the location offers; an
            empty list removes them all. Google refuses it on a location whose
            details report can_modify_service_list=false.
        special_hours (SocialApiAiCoreApiConnectorsBaseGBPSpecialHoursUpdate | Unset):
        store_code (str | Unset):  Example: JP-01.
        storefront_address (SocialApiAiCoreApiConnectorsBaseGBPAddressUpdate | Unset):
        title (str | Unset):  Example: Joe's Pizza (Downtown).
        website_uri (str | Unset):  Example: https://joes.example.
    """

    ad_phone: str | Unset = UNSET
    categories: SocialApiAiCoreApiConnectorsBaseGBPCategoriesUpdate | Unset = UNSET
    description: str | Unset = UNSET
    labels: list[str] | Unset = UNSET
    latlng: SocialApiAiCoreApiConnectorsBaseGBPLatLng | Unset = UNSET
    more_hours: list[SocialApiAiCoreApiConnectorsBaseGBPMoreHours] | Unset = UNSET
    open_status: str | Unset = UNSET
    phone_numbers: SocialApiAiCoreApiConnectorsBaseGBPPhoneNumbersUpdate | Unset = UNSET
    regular_hours: SocialApiAiCoreApiConnectorsBaseGBPHoursUpdate | Unset = UNSET
    service_area: SocialApiAiCoreApiConnectorsBaseGBPServiceAreaUpdate | Unset = UNSET
    service_items: list[SocialApiAiCoreApiConnectorsBaseGBPServiceItem] | Unset = UNSET
    special_hours: SocialApiAiCoreApiConnectorsBaseGBPSpecialHoursUpdate | Unset = UNSET
    store_code: str | Unset = UNSET
    storefront_address: SocialApiAiCoreApiConnectorsBaseGBPAddressUpdate | Unset = UNSET
    title: str | Unset = UNSET
    website_uri: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ad_phone = self.ad_phone

        categories: dict[str, Any] | Unset = UNSET
        if not isinstance(self.categories, Unset):
            categories = self.categories.to_dict()

        description = self.description

        labels: list[str] | Unset = UNSET
        if not isinstance(self.labels, Unset):
            labels = self.labels

        latlng: dict[str, Any] | Unset = UNSET
        if not isinstance(self.latlng, Unset):
            latlng = self.latlng.to_dict()

        more_hours: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.more_hours, Unset):
            more_hours = []
            for more_hours_item_data in self.more_hours:
                more_hours_item = more_hours_item_data.to_dict()
                more_hours.append(more_hours_item)

        open_status = self.open_status

        phone_numbers: dict[str, Any] | Unset = UNSET
        if not isinstance(self.phone_numbers, Unset):
            phone_numbers = self.phone_numbers.to_dict()

        regular_hours: dict[str, Any] | Unset = UNSET
        if not isinstance(self.regular_hours, Unset):
            regular_hours = self.regular_hours.to_dict()

        service_area: dict[str, Any] | Unset = UNSET
        if not isinstance(self.service_area, Unset):
            service_area = self.service_area.to_dict()

        service_items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.service_items, Unset):
            service_items = []
            for service_items_item_data in self.service_items:
                service_items_item = service_items_item_data.to_dict()
                service_items.append(service_items_item)

        special_hours: dict[str, Any] | Unset = UNSET
        if not isinstance(self.special_hours, Unset):
            special_hours = self.special_hours.to_dict()

        store_code = self.store_code

        storefront_address: dict[str, Any] | Unset = UNSET
        if not isinstance(self.storefront_address, Unset):
            storefront_address = self.storefront_address.to_dict()

        title = self.title

        website_uri = self.website_uri

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ad_phone is not UNSET:
            field_dict["ad_phone"] = ad_phone
        if categories is not UNSET:
            field_dict["categories"] = categories
        if description is not UNSET:
            field_dict["description"] = description
        if labels is not UNSET:
            field_dict["labels"] = labels
        if latlng is not UNSET:
            field_dict["latlng"] = latlng
        if more_hours is not UNSET:
            field_dict["more_hours"] = more_hours
        if open_status is not UNSET:
            field_dict["open_status"] = open_status
        if phone_numbers is not UNSET:
            field_dict["phone_numbers"] = phone_numbers
        if regular_hours is not UNSET:
            field_dict["regular_hours"] = regular_hours
        if service_area is not UNSET:
            field_dict["service_area"] = service_area
        if service_items is not UNSET:
            field_dict["service_items"] = service_items
        if special_hours is not UNSET:
            field_dict["special_hours"] = special_hours
        if store_code is not UNSET:
            field_dict["store_code"] = store_code
        if storefront_address is not UNSET:
            field_dict["storefront_address"] = storefront_address
        if title is not UNSET:
            field_dict["title"] = title
        if website_uri is not UNSET:
            field_dict["website_uri"] = website_uri

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.social_api_ai_core_api_connectors_base_gbp_address_update import (
            SocialApiAiCoreApiConnectorsBaseGBPAddressUpdate,  # noqa: PLC0415
        )
        from ..models.social_api_ai_core_api_connectors_base_gbp_categories_update import (
            SocialApiAiCoreApiConnectorsBaseGBPCategoriesUpdate,  # noqa: PLC0415
        )
        from ..models.social_api_ai_core_api_connectors_base_gbp_hours_update import (
            SocialApiAiCoreApiConnectorsBaseGBPHoursUpdate,  # noqa: PLC0415
        )
        from ..models.social_api_ai_core_api_connectors_base_gbp_lat_lng import (
            SocialApiAiCoreApiConnectorsBaseGBPLatLng,  # noqa: PLC0415
        )
        from ..models.social_api_ai_core_api_connectors_base_gbp_more_hours import (
            SocialApiAiCoreApiConnectorsBaseGBPMoreHours,  # noqa: PLC0415
        )
        from ..models.social_api_ai_core_api_connectors_base_gbp_phone_numbers_update import (
            SocialApiAiCoreApiConnectorsBaseGBPPhoneNumbersUpdate,  # noqa: PLC0415
        )
        from ..models.social_api_ai_core_api_connectors_base_gbp_service_area_update import (
            SocialApiAiCoreApiConnectorsBaseGBPServiceAreaUpdate,  # noqa: PLC0415
        )
        from ..models.social_api_ai_core_api_connectors_base_gbp_service_item import (
            SocialApiAiCoreApiConnectorsBaseGBPServiceItem,  # noqa: PLC0415
        )
        from ..models.social_api_ai_core_api_connectors_base_gbp_special_hours_update import (
            SocialApiAiCoreApiConnectorsBaseGBPSpecialHoursUpdate,  # noqa: PLC0415
        )

        d = dict(src_dict)
        ad_phone = d.pop("ad_phone", UNSET)

        _categories = d.pop("categories", UNSET)
        categories: SocialApiAiCoreApiConnectorsBaseGBPCategoriesUpdate | Unset
        if isinstance(_categories, Unset):
            categories = UNSET
        else:
            categories = SocialApiAiCoreApiConnectorsBaseGBPCategoriesUpdate.from_dict(_categories)

        description = d.pop("description", UNSET)

        labels = cast(list[str], d.pop("labels", UNSET))

        _latlng = d.pop("latlng", UNSET)
        latlng: SocialApiAiCoreApiConnectorsBaseGBPLatLng | Unset
        if isinstance(_latlng, Unset):
            latlng = UNSET
        else:
            latlng = SocialApiAiCoreApiConnectorsBaseGBPLatLng.from_dict(_latlng)

        _more_hours = d.pop("more_hours", UNSET)
        more_hours: list[SocialApiAiCoreApiConnectorsBaseGBPMoreHours] | Unset = UNSET
        if _more_hours is not UNSET:
            more_hours = []
            for more_hours_item_data in _more_hours:
                more_hours_item = SocialApiAiCoreApiConnectorsBaseGBPMoreHours.from_dict(more_hours_item_data)

                more_hours.append(more_hours_item)

        open_status = d.pop("open_status", UNSET)

        _phone_numbers = d.pop("phone_numbers", UNSET)
        phone_numbers: SocialApiAiCoreApiConnectorsBaseGBPPhoneNumbersUpdate | Unset
        if isinstance(_phone_numbers, Unset):
            phone_numbers = UNSET
        else:
            phone_numbers = SocialApiAiCoreApiConnectorsBaseGBPPhoneNumbersUpdate.from_dict(_phone_numbers)

        _regular_hours = d.pop("regular_hours", UNSET)
        regular_hours: SocialApiAiCoreApiConnectorsBaseGBPHoursUpdate | Unset
        if isinstance(_regular_hours, Unset):
            regular_hours = UNSET
        else:
            regular_hours = SocialApiAiCoreApiConnectorsBaseGBPHoursUpdate.from_dict(_regular_hours)

        _service_area = d.pop("service_area", UNSET)
        service_area: SocialApiAiCoreApiConnectorsBaseGBPServiceAreaUpdate | Unset
        if isinstance(_service_area, Unset):
            service_area = UNSET
        else:
            service_area = SocialApiAiCoreApiConnectorsBaseGBPServiceAreaUpdate.from_dict(_service_area)

        _service_items = d.pop("service_items", UNSET)
        service_items: list[SocialApiAiCoreApiConnectorsBaseGBPServiceItem] | Unset = UNSET
        if _service_items is not UNSET:
            service_items = []
            for service_items_item_data in _service_items:
                service_items_item = SocialApiAiCoreApiConnectorsBaseGBPServiceItem.from_dict(service_items_item_data)

                service_items.append(service_items_item)

        _special_hours = d.pop("special_hours", UNSET)
        special_hours: SocialApiAiCoreApiConnectorsBaseGBPSpecialHoursUpdate | Unset
        if isinstance(_special_hours, Unset):
            special_hours = UNSET
        else:
            special_hours = SocialApiAiCoreApiConnectorsBaseGBPSpecialHoursUpdate.from_dict(_special_hours)

        store_code = d.pop("store_code", UNSET)

        _storefront_address = d.pop("storefront_address", UNSET)
        storefront_address: SocialApiAiCoreApiConnectorsBaseGBPAddressUpdate | Unset
        if isinstance(_storefront_address, Unset):
            storefront_address = UNSET
        else:
            storefront_address = SocialApiAiCoreApiConnectorsBaseGBPAddressUpdate.from_dict(_storefront_address)

        title = d.pop("title", UNSET)

        website_uri = d.pop("website_uri", UNSET)

        social_api_ai_core_api_connectors_base_gbp_location_update = cls(
            ad_phone=ad_phone,
            categories=categories,
            description=description,
            labels=labels,
            latlng=latlng,
            more_hours=more_hours,
            open_status=open_status,
            phone_numbers=phone_numbers,
            regular_hours=regular_hours,
            service_area=service_area,
            service_items=service_items,
            special_hours=special_hours,
            store_code=store_code,
            storefront_address=storefront_address,
            title=title,
            website_uri=website_uri,
        )

        social_api_ai_core_api_connectors_base_gbp_location_update.additional_properties = d
        return social_api_ai_core_api_connectors_base_gbp_location_update

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
