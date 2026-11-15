from enum import StrEnum


class ApiEndpointsPostTargetErrorResponseCategory(StrEnum):
    AUTH = "auth"
    PLATFORM = "platform"
    RATE_LIMIT = "rate_limit"
    SYSTEM = "system"
    VALIDATION = "validation"

    def __str__(self) -> str:
        return str(self.value)

    # Override (templates/str_enum.py.jinja): a value added to the API after this
    # SDK was released decodes as a pseudo-member instead of raising.
    @classmethod
    def _missing_(cls, value: object) -> "ApiEndpointsPostTargetErrorResponseCategory | None":
        if not isinstance(value, str):
            return None
        member = str.__new__(cls, value)
        member._name_ = "UNKNOWN"
        member._value_ = value
        return member
