from enum import StrEnum


class TargetDeleteOutcome(StrEnum):
    TARGET_DELETE_OUTCOME_DELETED = "deleted"
    TARGET_DELETE_OUTCOME_FAILED = "failed"
    TARGET_DELETE_OUTCOME_NOT_SUPPORTED = "not_supported"

    def __str__(self) -> str:
        return str(self.value)

    # Override (templates/str_enum.py.jinja): a value added to the API after this
    # SDK was released decodes as a pseudo-member instead of raising.
    @classmethod
    def _missing_(cls, value: object) -> "TargetDeleteOutcome | None":
        if not isinstance(value, str):
            return None
        member = str.__new__(cls, value)
        member._name_ = "UNKNOWN"
        member._value_ = value
        return member
