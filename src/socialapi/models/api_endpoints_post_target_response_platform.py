from enum import StrEnum


class ApiEndpointsPostTargetResponsePlatform(StrEnum):
    BLUESKY = "bluesky"
    FACEBOOK = "facebook"
    GOOGLE = "google"
    INSTAGRAM = "instagram"
    LINKEDIN = "linkedin"
    PINTEREST = "pinterest"
    THREADS = "threads"
    TIKTOK = "tiktok"
    TWITTER = "twitter"
    WHATSAPP = "whatsapp"
    YOUTUBE = "youtube"
    ZALO = "zalo"

    def __str__(self) -> str:
        return str(self.value)

    # Override (templates/str_enum.py.jinja): a value added to the API after this
    # SDK was released decodes as a pseudo-member instead of raising.
    @classmethod
    def _missing_(cls, value: object) -> "ApiEndpointsPostTargetResponsePlatform | None":
        if not isinstance(value, str):
            return None
        member = str.__new__(cls, value)
        member._name_ = "UNKNOWN"
        member._value_ = value
        return member
