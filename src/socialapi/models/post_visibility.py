from enum import StrEnum


class PostVisibility(StrEnum):
    POST_VISIBILITY_CONNECTIONS_ONLY = "connections_only"
    POST_VISIBILITY_LOGGED_IN = "logged_in"
    POST_VISIBILITY_PRIVATE = "private"
    POST_VISIBILITY_PUBLIC = "public"

    def __str__(self) -> str:
        return str(self.value)

    # Override (templates/str_enum.py.jinja): a value added to the API after this
    # SDK was released decodes as a pseudo-member instead of raising.
    @classmethod
    def _missing_(cls, value: object) -> "PostVisibility | None":
        if not isinstance(value, str):
            return None
        member = str.__new__(cls, value)
        member._name_ = "UNKNOWN"
        member._value_ = value
        return member
