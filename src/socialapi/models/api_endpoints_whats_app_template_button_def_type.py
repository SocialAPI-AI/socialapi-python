from enum import StrEnum


class ApiEndpointsWhatsAppTemplateButtonDefType(StrEnum):
    COPY_CODE = "COPY_CODE"
    PHONE_NUMBER = "PHONE_NUMBER"
    QUICK_REPLY = "QUICK_REPLY"
    URL = "URL"

    def __str__(self) -> str:
        return str(self.value)

    # Override (templates/str_enum.py.jinja): a value added to the API after this
    # SDK was released decodes as a pseudo-member instead of raising.
    @classmethod
    def _missing_(cls, value: object) -> "ApiEndpointsWhatsAppTemplateButtonDefType | None":
        if not isinstance(value, str):
            return None
        member = str.__new__(cls, value)
        member._name_ = "UNKNOWN"
        member._value_ = value
        return member
