from enum import StrEnum


class SenderAction(StrEnum):
    SENDER_ACTION_MARK_SEEN = "mark_seen"
    SENDER_ACTION_TYPING_OFF = "typing_off"
    SENDER_ACTION_TYPING_ON = "typing_on"

    def __str__(self) -> str:
        return str(self.value)

    # Override (templates/str_enum.py.jinja): a value added to the API after this
    # SDK was released decodes as a pseudo-member instead of raising.
    @classmethod
    def _missing_(cls, value: object) -> "SenderAction | None":
        if not isinstance(value, str):
            return None
        member = str.__new__(cls, value)
        member._name_ = "UNKNOWN"
        member._value_ = value
        return member
