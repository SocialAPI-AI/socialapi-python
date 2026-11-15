from enum import StrEnum


class GoogleMediaCategory(StrEnum):
    GOOGLE_MEDIA_CATEGORY_ADDITIONAL = "ADDITIONAL"
    GOOGLE_MEDIA_CATEGORY_AT_WORK = "AT_WORK"
    GOOGLE_MEDIA_CATEGORY_COMMON_AREA = "COMMON_AREA"
    GOOGLE_MEDIA_CATEGORY_COVER = "COVER"
    GOOGLE_MEDIA_CATEGORY_EXTERIOR = "EXTERIOR"
    GOOGLE_MEDIA_CATEGORY_FOOD_AND_DRINK = "FOOD_AND_DRINK"
    GOOGLE_MEDIA_CATEGORY_INTERIOR = "INTERIOR"
    GOOGLE_MEDIA_CATEGORY_LOGO = "LOGO"
    GOOGLE_MEDIA_CATEGORY_MENU = "MENU"
    GOOGLE_MEDIA_CATEGORY_PRODUCT = "PRODUCT"
    GOOGLE_MEDIA_CATEGORY_PROFILE = "PROFILE"
    GOOGLE_MEDIA_CATEGORY_ROOMS = "ROOMS"
    GOOGLE_MEDIA_CATEGORY_TEAMS = "TEAMS"

    def __str__(self) -> str:
        return str(self.value)

    # Override (templates/str_enum.py.jinja): a value added to the API after this
    # SDK was released decodes as a pseudo-member instead of raising.
    @classmethod
    def _missing_(cls, value: object) -> "GoogleMediaCategory | None":
        if not isinstance(value, str):
            return None
        member = str.__new__(cls, value)
        member._name_ = "UNKNOWN"
        member._value_ = value
        return member
