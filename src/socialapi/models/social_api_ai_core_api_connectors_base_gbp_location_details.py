from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.social_api_ai_core_api_connectors_base_gbp_category import SocialApiAiCoreApiConnectorsBaseGBPCategory
    from ..models.social_api_ai_core_api_connectors_base_gbp_lat_lng import SocialApiAiCoreApiConnectorsBaseGBPLatLng
    from ..models.social_api_ai_core_api_connectors_base_gbp_more_hours import (
        SocialApiAiCoreApiConnectorsBaseGBPMoreHours,
    )
    from ..models.social_api_ai_core_api_connectors_base_gbp_postal_address import (
        SocialApiAiCoreApiConnectorsBaseGBPPostalAddress,
    )
    from ..models.social_api_ai_core_api_connectors_base_gbp_relationship_data import (
        SocialApiAiCoreApiConnectorsBaseGBPRelationshipData,
    )
    from ..models.social_api_ai_core_api_connectors_base_gbp_service_area import (
        SocialApiAiCoreApiConnectorsBaseGBPServiceArea,
    )
    from ..models.social_api_ai_core_api_connectors_base_gbp_service_item import (
        SocialApiAiCoreApiConnectorsBaseGBPServiceItem,
    )
    from ..models.social_api_ai_core_api_connectors_base_gbp_special_hour_period import (
        SocialApiAiCoreApiConnectorsBaseGBPSpecialHourPeriod,
    )
    from ..models.social_api_ai_core_api_connectors_base_gbp_time_period import (
        SocialApiAiCoreApiConnectorsBaseGBPTimePeriod,
    )


T = TypeVar("T", bound="SocialApiAiCoreApiConnectorsBaseGBPLocationDetails")


@_attrs_define
class SocialApiAiCoreApiConnectorsBaseGBPLocationDetails:
    """
    Attributes:
        ad_phone (str | Unset): AdPhone is the alternate number shown on Google Ads extensions.
        additional_categories (list[SocialApiAiCoreApiConnectorsBaseGBPCategory] | Unset):
        additional_phones (list[str] | Unset):
        can_delete (bool | Unset): CanDelete reports whether the location can be deleted. Absent when Google
            said nothing.
        can_have_business_calls (bool | Unset):
        can_have_food_menus (bool | Unset):
        can_modify_service_list (bool | Unset):
        can_operate_health_data (bool | Unset):
        can_operate_local_post (bool | Unset):
        can_operate_lodging_data (bool | Unset):
        can_reopen (bool | Unset): CanReopen is set on a temporarily closed location that can be reopened.
        duplicate_location (str | Unset): DuplicateLocation names the location this one was flagged a duplicate of.
        has_google_updated (bool | Unset):
        has_pending_edits (bool | Unset):
        has_voice_of_merchant (bool | Unset): HasVoiceOfMerchant reports whether the merchant controls the profile.
            When false, posting and replying fail until they resolve it in Google
            Business Profile. Absent when Google said nothing.
        is_particularly_personal_place (bool | Unset):
        labels (list[str] | Unset):
        language_code (str | Unset):  Example: en.
        latlng (SocialApiAiCoreApiConnectorsBaseGBPLatLng | Unset):
        maps_uri (str | Unset): MapsURI is the location's Google Maps page. Example: https://maps.google.com/?cid=123.
        more_hours (list[SocialApiAiCoreApiConnectorsBaseGBPMoreHours] | Unset):
        new_review_uri (str | Unset): NewReviewURI is the short link that opens the review form for this
            location, for review-request campaigns. Example: https://g.page/r/abc/review.
        open_status (str | Unset): OpenStatus is OPEN, CLOSED_PERMANENTLY or CLOSED_TEMPORARILY. Example: OPEN.
        opening_date (str | Unset): OpeningDate is set on a location that has not opened yet. Example: 2026-09-01.
        place_id (str | Unset): PlaceID is the standard Google Places identifier, so a location can be
            joined to Places, Maps and Geocoding results. Example: ChIJabc.
        primary_category (SocialApiAiCoreApiConnectorsBaseGBPCategory | Unset):
        primary_phone (str | Unset):  Example: +33 1 23 45 67 89.
        regular_hours (list[SocialApiAiCoreApiConnectorsBaseGBPTimePeriod] | Unset):
        relationship_data (SocialApiAiCoreApiConnectorsBaseGBPRelationshipData | Unset):
        service_area (SocialApiAiCoreApiConnectorsBaseGBPServiceArea | Unset):
        service_items (list[SocialApiAiCoreApiConnectorsBaseGBPServiceItem] | Unset):
        special_hours (list[SocialApiAiCoreApiConnectorsBaseGBPSpecialHourPeriod] | Unset):
        store_code (str | Unset):  Example: JP-01.
        storefront_address (SocialApiAiCoreApiConnectorsBaseGBPPostalAddress | Unset):
        website_uri (str | Unset):  Example: https://joes.example.
    """

    ad_phone: str | Unset = UNSET
    additional_categories: list[SocialApiAiCoreApiConnectorsBaseGBPCategory] | Unset = UNSET
    additional_phones: list[str] | Unset = UNSET
    can_delete: bool | Unset = UNSET
    can_have_business_calls: bool | Unset = UNSET
    can_have_food_menus: bool | Unset = UNSET
    can_modify_service_list: bool | Unset = UNSET
    can_operate_health_data: bool | Unset = UNSET
    can_operate_local_post: bool | Unset = UNSET
    can_operate_lodging_data: bool | Unset = UNSET
    can_reopen: bool | Unset = UNSET
    duplicate_location: str | Unset = UNSET
    has_google_updated: bool | Unset = UNSET
    has_pending_edits: bool | Unset = UNSET
    has_voice_of_merchant: bool | Unset = UNSET
    is_particularly_personal_place: bool | Unset = UNSET
    labels: list[str] | Unset = UNSET
    language_code: str | Unset = UNSET
    latlng: SocialApiAiCoreApiConnectorsBaseGBPLatLng | Unset = UNSET
    maps_uri: str | Unset = UNSET
    more_hours: list[SocialApiAiCoreApiConnectorsBaseGBPMoreHours] | Unset = UNSET
    new_review_uri: str | Unset = UNSET
    open_status: str | Unset = UNSET
    opening_date: str | Unset = UNSET
    place_id: str | Unset = UNSET
    primary_category: SocialApiAiCoreApiConnectorsBaseGBPCategory | Unset = UNSET
    primary_phone: str | Unset = UNSET
    regular_hours: list[SocialApiAiCoreApiConnectorsBaseGBPTimePeriod] | Unset = UNSET
    relationship_data: SocialApiAiCoreApiConnectorsBaseGBPRelationshipData | Unset = UNSET
    service_area: SocialApiAiCoreApiConnectorsBaseGBPServiceArea | Unset = UNSET
    service_items: list[SocialApiAiCoreApiConnectorsBaseGBPServiceItem] | Unset = UNSET
    special_hours: list[SocialApiAiCoreApiConnectorsBaseGBPSpecialHourPeriod] | Unset = UNSET
    store_code: str | Unset = UNSET
    storefront_address: SocialApiAiCoreApiConnectorsBaseGBPPostalAddress | Unset = UNSET
    website_uri: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ad_phone = self.ad_phone

        additional_categories: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.additional_categories, Unset):
            additional_categories = []
            for additional_categories_item_data in self.additional_categories:
                additional_categories_item = additional_categories_item_data.to_dict()
                additional_categories.append(additional_categories_item)

        additional_phones: list[str] | Unset = UNSET
        if not isinstance(self.additional_phones, Unset):
            additional_phones = self.additional_phones

        can_delete = self.can_delete

        can_have_business_calls = self.can_have_business_calls

        can_have_food_menus = self.can_have_food_menus

        can_modify_service_list = self.can_modify_service_list

        can_operate_health_data = self.can_operate_health_data

        can_operate_local_post = self.can_operate_local_post

        can_operate_lodging_data = self.can_operate_lodging_data

        can_reopen = self.can_reopen

        duplicate_location = self.duplicate_location

        has_google_updated = self.has_google_updated

        has_pending_edits = self.has_pending_edits

        has_voice_of_merchant = self.has_voice_of_merchant

        is_particularly_personal_place = self.is_particularly_personal_place

        labels: list[str] | Unset = UNSET
        if not isinstance(self.labels, Unset):
            labels = self.labels

        language_code = self.language_code

        latlng: dict[str, Any] | Unset = UNSET
        if not isinstance(self.latlng, Unset):
            latlng = self.latlng.to_dict()

        maps_uri = self.maps_uri

        more_hours: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.more_hours, Unset):
            more_hours = []
            for more_hours_item_data in self.more_hours:
                more_hours_item = more_hours_item_data.to_dict()
                more_hours.append(more_hours_item)

        new_review_uri = self.new_review_uri

        open_status = self.open_status

        opening_date = self.opening_date

        place_id = self.place_id

        primary_category: dict[str, Any] | Unset = UNSET
        if not isinstance(self.primary_category, Unset):
            primary_category = self.primary_category.to_dict()

        primary_phone = self.primary_phone

        regular_hours: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.regular_hours, Unset):
            regular_hours = []
            for regular_hours_item_data in self.regular_hours:
                regular_hours_item = regular_hours_item_data.to_dict()
                regular_hours.append(regular_hours_item)

        relationship_data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.relationship_data, Unset):
            relationship_data = self.relationship_data.to_dict()

        service_area: dict[str, Any] | Unset = UNSET
        if not isinstance(self.service_area, Unset):
            service_area = self.service_area.to_dict()

        service_items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.service_items, Unset):
            service_items = []
            for service_items_item_data in self.service_items:
                service_items_item = service_items_item_data.to_dict()
                service_items.append(service_items_item)

        special_hours: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.special_hours, Unset):
            special_hours = []
            for special_hours_item_data in self.special_hours:
                special_hours_item = special_hours_item_data.to_dict()
                special_hours.append(special_hours_item)

        store_code = self.store_code

        storefront_address: dict[str, Any] | Unset = UNSET
        if not isinstance(self.storefront_address, Unset):
            storefront_address = self.storefront_address.to_dict()

        website_uri = self.website_uri

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ad_phone is not UNSET:
            field_dict["ad_phone"] = ad_phone
        if additional_categories is not UNSET:
            field_dict["additional_categories"] = additional_categories
        if additional_phones is not UNSET:
            field_dict["additional_phones"] = additional_phones
        if can_delete is not UNSET:
            field_dict["can_delete"] = can_delete
        if can_have_business_calls is not UNSET:
            field_dict["can_have_business_calls"] = can_have_business_calls
        if can_have_food_menus is not UNSET:
            field_dict["can_have_food_menus"] = can_have_food_menus
        if can_modify_service_list is not UNSET:
            field_dict["can_modify_service_list"] = can_modify_service_list
        if can_operate_health_data is not UNSET:
            field_dict["can_operate_health_data"] = can_operate_health_data
        if can_operate_local_post is not UNSET:
            field_dict["can_operate_local_post"] = can_operate_local_post
        if can_operate_lodging_data is not UNSET:
            field_dict["can_operate_lodging_data"] = can_operate_lodging_data
        if can_reopen is not UNSET:
            field_dict["can_reopen"] = can_reopen
        if duplicate_location is not UNSET:
            field_dict["duplicate_location"] = duplicate_location
        if has_google_updated is not UNSET:
            field_dict["has_google_updated"] = has_google_updated
        if has_pending_edits is not UNSET:
            field_dict["has_pending_edits"] = has_pending_edits
        if has_voice_of_merchant is not UNSET:
            field_dict["has_voice_of_merchant"] = has_voice_of_merchant
        if is_particularly_personal_place is not UNSET:
            field_dict["is_particularly_personal_place"] = is_particularly_personal_place
        if labels is not UNSET:
            field_dict["labels"] = labels
        if language_code is not UNSET:
            field_dict["language_code"] = language_code
        if latlng is not UNSET:
            field_dict["latlng"] = latlng
        if maps_uri is not UNSET:
            field_dict["maps_uri"] = maps_uri
        if more_hours is not UNSET:
            field_dict["more_hours"] = more_hours
        if new_review_uri is not UNSET:
            field_dict["new_review_uri"] = new_review_uri
        if open_status is not UNSET:
            field_dict["open_status"] = open_status
        if opening_date is not UNSET:
            field_dict["opening_date"] = opening_date
        if place_id is not UNSET:
            field_dict["place_id"] = place_id
        if primary_category is not UNSET:
            field_dict["primary_category"] = primary_category
        if primary_phone is not UNSET:
            field_dict["primary_phone"] = primary_phone
        if regular_hours is not UNSET:
            field_dict["regular_hours"] = regular_hours
        if relationship_data is not UNSET:
            field_dict["relationship_data"] = relationship_data
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
        if website_uri is not UNSET:
            field_dict["website_uri"] = website_uri

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.social_api_ai_core_api_connectors_base_gbp_category import (
            SocialApiAiCoreApiConnectorsBaseGBPCategory,  # noqa: PLC0415
        )
        from ..models.social_api_ai_core_api_connectors_base_gbp_lat_lng import (
            SocialApiAiCoreApiConnectorsBaseGBPLatLng,  # noqa: PLC0415
        )
        from ..models.social_api_ai_core_api_connectors_base_gbp_more_hours import (
            SocialApiAiCoreApiConnectorsBaseGBPMoreHours,  # noqa: PLC0415
        )
        from ..models.social_api_ai_core_api_connectors_base_gbp_postal_address import (
            SocialApiAiCoreApiConnectorsBaseGBPPostalAddress,  # noqa: PLC0415
        )
        from ..models.social_api_ai_core_api_connectors_base_gbp_relationship_data import (
            SocialApiAiCoreApiConnectorsBaseGBPRelationshipData,  # noqa: PLC0415
        )
        from ..models.social_api_ai_core_api_connectors_base_gbp_service_area import (
            SocialApiAiCoreApiConnectorsBaseGBPServiceArea,  # noqa: PLC0415
        )
        from ..models.social_api_ai_core_api_connectors_base_gbp_service_item import (
            SocialApiAiCoreApiConnectorsBaseGBPServiceItem,  # noqa: PLC0415
        )
        from ..models.social_api_ai_core_api_connectors_base_gbp_special_hour_period import (
            SocialApiAiCoreApiConnectorsBaseGBPSpecialHourPeriod,  # noqa: PLC0415
        )
        from ..models.social_api_ai_core_api_connectors_base_gbp_time_period import (
            SocialApiAiCoreApiConnectorsBaseGBPTimePeriod,  # noqa: PLC0415
        )

        d = dict(src_dict)
        ad_phone = d.pop("ad_phone", UNSET)

        _additional_categories = d.pop("additional_categories", UNSET)
        additional_categories: list[SocialApiAiCoreApiConnectorsBaseGBPCategory] | Unset = UNSET
        if _additional_categories is not UNSET:
            additional_categories = []
            for additional_categories_item_data in _additional_categories:
                additional_categories_item = SocialApiAiCoreApiConnectorsBaseGBPCategory.from_dict(
                    additional_categories_item_data
                )

                additional_categories.append(additional_categories_item)

        additional_phones = cast(list[str], d.pop("additional_phones", UNSET))

        can_delete = d.pop("can_delete", UNSET)

        can_have_business_calls = d.pop("can_have_business_calls", UNSET)

        can_have_food_menus = d.pop("can_have_food_menus", UNSET)

        can_modify_service_list = d.pop("can_modify_service_list", UNSET)

        can_operate_health_data = d.pop("can_operate_health_data", UNSET)

        can_operate_local_post = d.pop("can_operate_local_post", UNSET)

        can_operate_lodging_data = d.pop("can_operate_lodging_data", UNSET)

        can_reopen = d.pop("can_reopen", UNSET)

        duplicate_location = d.pop("duplicate_location", UNSET)

        has_google_updated = d.pop("has_google_updated", UNSET)

        has_pending_edits = d.pop("has_pending_edits", UNSET)

        has_voice_of_merchant = d.pop("has_voice_of_merchant", UNSET)

        is_particularly_personal_place = d.pop("is_particularly_personal_place", UNSET)

        labels = cast(list[str], d.pop("labels", UNSET))

        language_code = d.pop("language_code", UNSET)

        _latlng = d.pop("latlng", UNSET)
        latlng: SocialApiAiCoreApiConnectorsBaseGBPLatLng | Unset
        if isinstance(_latlng, Unset):
            latlng = UNSET
        else:
            latlng = SocialApiAiCoreApiConnectorsBaseGBPLatLng.from_dict(_latlng)

        maps_uri = d.pop("maps_uri", UNSET)

        _more_hours = d.pop("more_hours", UNSET)
        more_hours: list[SocialApiAiCoreApiConnectorsBaseGBPMoreHours] | Unset = UNSET
        if _more_hours is not UNSET:
            more_hours = []
            for more_hours_item_data in _more_hours:
                more_hours_item = SocialApiAiCoreApiConnectorsBaseGBPMoreHours.from_dict(more_hours_item_data)

                more_hours.append(more_hours_item)

        new_review_uri = d.pop("new_review_uri", UNSET)

        open_status = d.pop("open_status", UNSET)

        opening_date = d.pop("opening_date", UNSET)

        place_id = d.pop("place_id", UNSET)

        _primary_category = d.pop("primary_category", UNSET)
        primary_category: SocialApiAiCoreApiConnectorsBaseGBPCategory | Unset
        if isinstance(_primary_category, Unset):
            primary_category = UNSET
        else:
            primary_category = SocialApiAiCoreApiConnectorsBaseGBPCategory.from_dict(_primary_category)

        primary_phone = d.pop("primary_phone", UNSET)

        _regular_hours = d.pop("regular_hours", UNSET)
        regular_hours: list[SocialApiAiCoreApiConnectorsBaseGBPTimePeriod] | Unset = UNSET
        if _regular_hours is not UNSET:
            regular_hours = []
            for regular_hours_item_data in _regular_hours:
                regular_hours_item = SocialApiAiCoreApiConnectorsBaseGBPTimePeriod.from_dict(regular_hours_item_data)

                regular_hours.append(regular_hours_item)

        _relationship_data = d.pop("relationship_data", UNSET)
        relationship_data: SocialApiAiCoreApiConnectorsBaseGBPRelationshipData | Unset
        if isinstance(_relationship_data, Unset):
            relationship_data = UNSET
        else:
            relationship_data = SocialApiAiCoreApiConnectorsBaseGBPRelationshipData.from_dict(_relationship_data)

        _service_area = d.pop("service_area", UNSET)
        service_area: SocialApiAiCoreApiConnectorsBaseGBPServiceArea | Unset
        if isinstance(_service_area, Unset):
            service_area = UNSET
        else:
            service_area = SocialApiAiCoreApiConnectorsBaseGBPServiceArea.from_dict(_service_area)

        _service_items = d.pop("service_items", UNSET)
        service_items: list[SocialApiAiCoreApiConnectorsBaseGBPServiceItem] | Unset = UNSET
        if _service_items is not UNSET:
            service_items = []
            for service_items_item_data in _service_items:
                service_items_item = SocialApiAiCoreApiConnectorsBaseGBPServiceItem.from_dict(service_items_item_data)

                service_items.append(service_items_item)

        _special_hours = d.pop("special_hours", UNSET)
        special_hours: list[SocialApiAiCoreApiConnectorsBaseGBPSpecialHourPeriod] | Unset = UNSET
        if _special_hours is not UNSET:
            special_hours = []
            for special_hours_item_data in _special_hours:
                special_hours_item = SocialApiAiCoreApiConnectorsBaseGBPSpecialHourPeriod.from_dict(
                    special_hours_item_data
                )

                special_hours.append(special_hours_item)

        store_code = d.pop("store_code", UNSET)

        _storefront_address = d.pop("storefront_address", UNSET)
        storefront_address: SocialApiAiCoreApiConnectorsBaseGBPPostalAddress | Unset
        if isinstance(_storefront_address, Unset):
            storefront_address = UNSET
        else:
            storefront_address = SocialApiAiCoreApiConnectorsBaseGBPPostalAddress.from_dict(_storefront_address)

        website_uri = d.pop("website_uri", UNSET)

        social_api_ai_core_api_connectors_base_gbp_location_details = cls(
            ad_phone=ad_phone,
            additional_categories=additional_categories,
            additional_phones=additional_phones,
            can_delete=can_delete,
            can_have_business_calls=can_have_business_calls,
            can_have_food_menus=can_have_food_menus,
            can_modify_service_list=can_modify_service_list,
            can_operate_health_data=can_operate_health_data,
            can_operate_local_post=can_operate_local_post,
            can_operate_lodging_data=can_operate_lodging_data,
            can_reopen=can_reopen,
            duplicate_location=duplicate_location,
            has_google_updated=has_google_updated,
            has_pending_edits=has_pending_edits,
            has_voice_of_merchant=has_voice_of_merchant,
            is_particularly_personal_place=is_particularly_personal_place,
            labels=labels,
            language_code=language_code,
            latlng=latlng,
            maps_uri=maps_uri,
            more_hours=more_hours,
            new_review_uri=new_review_uri,
            open_status=open_status,
            opening_date=opening_date,
            place_id=place_id,
            primary_category=primary_category,
            primary_phone=primary_phone,
            regular_hours=regular_hours,
            relationship_data=relationship_data,
            service_area=service_area,
            service_items=service_items,
            special_hours=special_hours,
            store_code=store_code,
            storefront_address=storefront_address,
            website_uri=website_uri,
        )

        social_api_ai_core_api_connectors_base_gbp_location_details.additional_properties = d
        return social_api_ai_core_api_connectors_base_gbp_location_details

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
