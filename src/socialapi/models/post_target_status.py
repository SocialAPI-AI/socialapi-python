from enum import StrEnum


class PostTargetStatus(StrEnum):
    POST_TARGET_STATUS_CANCELLED = "cancelled"
    POST_TARGET_STATUS_FAILED = "failed"
    POST_TARGET_STATUS_PENDING = "pending"
    POST_TARGET_STATUS_PUBLISHED = "published"
    POST_TARGET_STATUS_PUBLISHING = "publishing"
    POST_TARGET_STATUS_UNPUBLISHED = "unpublished"

    def __str__(self) -> str:
        return str(self.value)

    # Override (templates/str_enum.py.jinja): a value added to the API after this
    # SDK was released decodes as a pseudo-member instead of raising.
    @classmethod
    def _missing_(cls, value: object) -> "PostTargetStatus | None":
        if not isinstance(value, str):
            return None
        member = str.__new__(cls, value)
        member._name_ = "UNKNOWN"
        member._value_ = value
        return member
