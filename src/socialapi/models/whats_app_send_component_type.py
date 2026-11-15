from enum import StrEnum


class WhatsAppSendComponentType(StrEnum):
    WHATS_APP_SEND_COMPONENT_TYPE_BODY = "body"
    WHATS_APP_SEND_COMPONENT_TYPE_BUTTON = "button"
    WHATS_APP_SEND_COMPONENT_TYPE_HEADER = "header"

    def __str__(self) -> str:
        return str(self.value)

    # Override (templates/str_enum.py.jinja): a value added to the API after this
    # SDK was released decodes as a pseudo-member instead of raising.
    @classmethod
    def _missing_(cls, value: object) -> "WhatsAppSendComponentType | None":
        if not isinstance(value, str):
            return None
        member = str.__new__(cls, value)
        member._name_ = "UNKNOWN"
        member._value_ = value
        return member
