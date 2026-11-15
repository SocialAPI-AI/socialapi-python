from enum import StrEnum


class WhatsAppTemplateButtonType(StrEnum):
    WHATS_APP_TEMPLATE_BUTTON_TYPE_COPY_CODE = "COPY_CODE"
    WHATS_APP_TEMPLATE_BUTTON_TYPE_PHONE_NUMBER = "PHONE_NUMBER"
    WHATS_APP_TEMPLATE_BUTTON_TYPE_QUICK_REPLY = "QUICK_REPLY"
    WHATS_APP_TEMPLATE_BUTTON_TYPE_URL = "URL"

    def __str__(self) -> str:
        return str(self.value)

    # Override (templates/str_enum.py.jinja): a value added to the API after this
    # SDK was released decodes as a pseudo-member instead of raising.
    @classmethod
    def _missing_(cls, value: object) -> "WhatsAppTemplateButtonType | None":
        if not isinstance(value, str):
            return None
        member = str.__new__(cls, value)
        member._name_ = "UNKNOWN"
        member._value_ = value
        return member
