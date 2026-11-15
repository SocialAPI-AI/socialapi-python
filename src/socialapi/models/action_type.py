from enum import StrEnum


class ActionType(StrEnum):
    ACTION_HIDE_COMMENT = "hide_comment"
    ACTION_PRIVATE_REPLY = "private_reply"
    ACTION_REPLY_COMMENT = "reply_comment"
    ACTION_SEND_DM = "send_dm"

    def __str__(self) -> str:
        return str(self.value)

    # Override (templates/str_enum.py.jinja): a value added to the API after this
    # SDK was released decodes as a pseudo-member instead of raising.
    @classmethod
    def _missing_(cls, value: object) -> "ActionType | None":
        if not isinstance(value, str):
            return None
        member = str.__new__(cls, value)
        member._name_ = "UNKNOWN"
        member._value_ = value
        return member
