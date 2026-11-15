from enum import StrEnum


class PostStatus(StrEnum):
    POST_STATUS_CANCELLED = "cancelled"
    POST_STATUS_DRAFT = "draft"
    POST_STATUS_FAILED = "failed"
    POST_STATUS_PARTIAL = "partial"
    POST_STATUS_PUBLISHED = "published"
    POST_STATUS_PUBLISHING = "publishing"
    POST_STATUS_SCHEDULED = "scheduled"

    def __str__(self) -> str:
        return str(self.value)

    # Override (templates/str_enum.py.jinja): a value added to the API after this
    # SDK was released decodes as a pseudo-member instead of raising.
    @classmethod
    def _missing_(cls, value: object) -> "PostStatus | None":
        if not isinstance(value, str):
            return None
        member = str.__new__(cls, value)
        member._name_ = "UNKNOWN"
        member._value_ = value
        return member
