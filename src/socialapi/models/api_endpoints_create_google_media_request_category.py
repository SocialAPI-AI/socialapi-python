from enum import StrEnum


class ApiEndpointsCreateGoogleMediaRequestCategory(StrEnum):
    ADDITIONAL = "ADDITIONAL"
    AT_WORK = "AT_WORK"
    COMMON_AREA = "COMMON_AREA"
    COVER = "COVER"
    EXTERIOR = "EXTERIOR"
    FOOD_AND_DRINK = "FOOD_AND_DRINK"
    INTERIOR = "INTERIOR"
    LOGO = "LOGO"
    MENU = "MENU"
    PRODUCT = "PRODUCT"
    PROFILE = "PROFILE"
    ROOMS = "ROOMS"
    TEAMS = "TEAMS"

    def __str__(self) -> str:
        return str(self.value)

    # Override (templates/str_enum.py.jinja): a value added to the API after this
    # SDK was released decodes as a pseudo-member instead of raising.
    @classmethod
    def _missing_(cls, value: object) -> "ApiEndpointsCreateGoogleMediaRequestCategory | None":
        if not isinstance(value, str):
            return None
        member = str.__new__(cls, value)
        member._name_ = "UNKNOWN"
        member._value_ = value
        return member
