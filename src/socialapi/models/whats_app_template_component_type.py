from enum import StrEnum


class WhatsAppTemplateComponentType(StrEnum):
    WHATS_APP_TEMPLATE_COMPONENT_TYPE_BODY = "BODY"
    WHATS_APP_TEMPLATE_COMPONENT_TYPE_BUTTONS = "BUTTONS"
    WHATS_APP_TEMPLATE_COMPONENT_TYPE_FOOTER = "FOOTER"
    WHATS_APP_TEMPLATE_COMPONENT_TYPE_HEADER = "HEADER"

    def __str__(self) -> str:
        return str(self.value)

    # Override (templates/str_enum.py.jinja): a value added to the API after this
    # SDK was released decodes as a pseudo-member instead of raising.
    @classmethod
    def _missing_(cls, value: object) -> "WhatsAppTemplateComponentType | None":
        if not isinstance(value, str):
            return None
        member = str.__new__(cls, value)
        member._name_ = "UNKNOWN"
        member._value_ = value
        return member
