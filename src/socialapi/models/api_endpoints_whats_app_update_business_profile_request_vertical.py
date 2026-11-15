from enum import StrEnum


class ApiEndpointsWhatsAppUpdateBusinessProfileRequestVertical(StrEnum):
    ALCOHOL = "ALCOHOL"
    APPAREL = "APPAREL"
    AUTO = "AUTO"
    BEAUTY = "BEAUTY"
    EDU = "EDU"
    ENTERTAIN = "ENTERTAIN"
    EVENT_PLAN = "EVENT_PLAN"
    FINANCE = "FINANCE"
    GOVT = "GOVT"
    GROCERY = "GROCERY"
    HEALTH = "HEALTH"
    HOTEL = "HOTEL"
    NONPROFIT = "NONPROFIT"
    OTHER = "OTHER"
    PROF_SERVICES = "PROF_SERVICES"
    RESTAURANT = "RESTAURANT"
    RETAIL = "RETAIL"
    TRAVEL = "TRAVEL"

    def __str__(self) -> str:
        return str(self.value)

    # Override (templates/str_enum.py.jinja): a value added to the API after this
    # SDK was released decodes as a pseudo-member instead of raising.
    @classmethod
    def _missing_(cls, value: object) -> "ApiEndpointsWhatsAppUpdateBusinessProfileRequestVertical | None":
        if not isinstance(value, str):
            return None
        member = str.__new__(cls, value)
        member._name_ = "UNKNOWN"
        member._value_ = value
        return member
