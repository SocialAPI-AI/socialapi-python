from enum import StrEnum


class Weekday(StrEnum):
    WEEKDAY_FRIDAY = "friday"
    WEEKDAY_MONDAY = "monday"
    WEEKDAY_SATURDAY = "saturday"
    WEEKDAY_SUNDAY = "sunday"
    WEEKDAY_THURSDAY = "thursday"
    WEEKDAY_TUESDAY = "tuesday"
    WEEKDAY_WEDNESDAY = "wednesday"

    def __str__(self) -> str:
        return str(self.value)

    # Override (templates/str_enum.py.jinja): a value added to the API after this
    # SDK was released decodes as a pseudo-member instead of raising.
    @classmethod
    def _missing_(cls, value: object) -> "Weekday | None":
        if not isinstance(value, str):
            return None
        member = str.__new__(cls, value)
        member._name_ = "UNKNOWN"
        member._value_ = value
        return member
