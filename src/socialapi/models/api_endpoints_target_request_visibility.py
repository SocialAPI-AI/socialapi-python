from enum import StrEnum


class ApiEndpointsTargetRequestVisibility(StrEnum):
    CONNECTIONS_ONLY = "connections_only"
    LOGGED_IN = "logged_in"
    PRIVATE = "private"
    PUBLIC = "public"

    def __str__(self) -> str:
        return str(self.value)

    # Override (templates/str_enum.py.jinja): a value added to the API after this
    # SDK was released decodes as a pseudo-member instead of raising.
    @classmethod
    def _missing_(cls, value: object) -> "ApiEndpointsTargetRequestVisibility | None":
        if not isinstance(value, str):
            return None
        member = str.__new__(cls, value)
        member._name_ = "UNKNOWN"
        member._value_ = value
        return member
