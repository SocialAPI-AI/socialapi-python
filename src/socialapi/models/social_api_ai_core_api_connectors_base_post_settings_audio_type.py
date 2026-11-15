from enum import StrEnum


class SocialApiAiCoreApiConnectorsBasePostSettingsAudioType(StrEnum):
    MUSIC = "MUSIC"
    ORIGINAL_SOUND = "ORIGINAL_SOUND"

    def __str__(self) -> str:
        return str(self.value)

    # Override (templates/str_enum.py.jinja): a value added to the API after this
    # SDK was released decodes as a pseudo-member instead of raising.
    @classmethod
    def _missing_(cls, value: object) -> "SocialApiAiCoreApiConnectorsBasePostSettingsAudioType | None":
        if not isinstance(value, str):
            return None
        member = str.__new__(cls, value)
        member._name_ = "UNKNOWN"
        member._value_ = value
        return member
