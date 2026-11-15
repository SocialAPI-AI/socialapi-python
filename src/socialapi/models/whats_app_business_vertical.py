from enum import StrEnum


class WhatsAppBusinessVertical(StrEnum):
    WHATS_APP_BUSINESS_VERTICAL_ALCOHOL = "ALCOHOL"
    WHATS_APP_BUSINESS_VERTICAL_APPAREL = "APPAREL"
    WHATS_APP_BUSINESS_VERTICAL_AUTO = "AUTO"
    WHATS_APP_BUSINESS_VERTICAL_BEAUTY = "BEAUTY"
    WHATS_APP_BUSINESS_VERTICAL_EDU = "EDU"
    WHATS_APP_BUSINESS_VERTICAL_ENTERTAIN = "ENTERTAIN"
    WHATS_APP_BUSINESS_VERTICAL_EVENT_PLAN = "EVENT_PLAN"
    WHATS_APP_BUSINESS_VERTICAL_FINANCE = "FINANCE"
    WHATS_APP_BUSINESS_VERTICAL_GOVT = "GOVT"
    WHATS_APP_BUSINESS_VERTICAL_GROCERY = "GROCERY"
    WHATS_APP_BUSINESS_VERTICAL_HEALTH = "HEALTH"
    WHATS_APP_BUSINESS_VERTICAL_HOTEL = "HOTEL"
    WHATS_APP_BUSINESS_VERTICAL_NONPROFIT = "NONPROFIT"
    WHATS_APP_BUSINESS_VERTICAL_OTHER = "OTHER"
    WHATS_APP_BUSINESS_VERTICAL_PROF_SERVICES = "PROF_SERVICES"
    WHATS_APP_BUSINESS_VERTICAL_RESTAURANT = "RESTAURANT"
    WHATS_APP_BUSINESS_VERTICAL_RETAIL = "RETAIL"
    WHATS_APP_BUSINESS_VERTICAL_TRAVEL = "TRAVEL"

    def __str__(self) -> str:
        return str(self.value)

    # Override (templates/str_enum.py.jinja): a value added to the API after this
    # SDK was released decodes as a pseudo-member instead of raising.
    @classmethod
    def _missing_(cls, value: object) -> "WhatsAppBusinessVertical | None":
        if not isinstance(value, str):
            return None
        member = str.__new__(cls, value)
        member._name_ = "UNKNOWN"
        member._value_ = value
        return member
