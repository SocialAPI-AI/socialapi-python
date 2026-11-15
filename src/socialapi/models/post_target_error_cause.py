from enum import StrEnum


class PostTargetErrorCause(StrEnum):
    POST_TARGET_ERROR_CAUSE_INTERNAL = "internal"
    POST_TARGET_ERROR_CAUSE_NONE = ""
    POST_TARGET_ERROR_CAUSE_PLATFORM = "platform"
    POST_TARGET_ERROR_CAUSE_SYSTEM = "system"
    POST_TARGET_ERROR_CAUSE_USER = "user"

    def __str__(self) -> str:
        return str(self.value)

    # Override (templates/str_enum.py.jinja): a value added to the API after this
    # SDK was released decodes as a pseudo-member instead of raising.
    @classmethod
    def _missing_(cls, value: object) -> "PostTargetErrorCause | None":
        if not isinstance(value, str):
            return None
        member = str.__new__(cls, value)
        member._name_ = "UNKNOWN"
        member._value_ = value
        return member
