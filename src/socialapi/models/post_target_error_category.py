from enum import StrEnum


class PostTargetErrorCategory(StrEnum):
    POST_TARGET_ERROR_CATEGORY_ACCOUNT = "account"
    POST_TARGET_ERROR_CATEGORY_AUTH = "auth"
    POST_TARGET_ERROR_CATEGORY_BILLING = "billing"
    POST_TARGET_ERROR_CATEGORY_CONFLICT = "conflict"
    POST_TARGET_ERROR_CATEGORY_NONE = ""
    POST_TARGET_ERROR_CATEGORY_PLATFORM = "platform"
    POST_TARGET_ERROR_CATEGORY_RATE_LIMIT = "rate_limit"
    POST_TARGET_ERROR_CATEGORY_RESOURCE = "resource"
    POST_TARGET_ERROR_CATEGORY_SYSTEM = "system"
    POST_TARGET_ERROR_CATEGORY_VALIDATION = "validation"

    def __str__(self) -> str:
        return str(self.value)

    # Override (templates/str_enum.py.jinja): a value added to the API after this
    # SDK was released decodes as a pseudo-member instead of raising.
    @classmethod
    def _missing_(cls, value: object) -> "PostTargetErrorCategory | None":
        if not isinstance(value, str):
            return None
        member = str.__new__(cls, value)
        member._name_ = "UNKNOWN"
        member._value_ = value
        return member
