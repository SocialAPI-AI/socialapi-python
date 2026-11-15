from enum import StrEnum


class Platform(StrEnum):
    PLATFORM_APP_STORE_CONNECT = "app_store_connect"
    PLATFORM_BLUESKY = "bluesky"
    PLATFORM_FACEBOOK = "facebook"
    PLATFORM_GOOGLE = "google"
    PLATFORM_INSTAGRAM = "instagram"
    PLATFORM_INSTAGRAM_FB = "instagram_fb"
    PLATFORM_LINKED_IN = "linkedin"
    PLATFORM_LINKED_IN_PAGE = "linkedin_page"
    PLATFORM_PINTEREST = "pinterest"
    PLATFORM_TELEGRAM = "telegram"
    PLATFORM_THREADS = "threads"
    PLATFORM_TIK_TOK = "tiktok"
    PLATFORM_TWITTER = "twitter"
    PLATFORM_WHATS_APP = "whatsapp"
    PLATFORM_YOU_TUBE = "youtube"
    PLATFORM_ZALO = "zalo"

    def __str__(self) -> str:
        return str(self.value)

    # Override (templates/str_enum.py.jinja): a value added to the API after this
    # SDK was released decodes as a pseudo-member instead of raising.
    @classmethod
    def _missing_(cls, value: object) -> "Platform | None":
        if not isinstance(value, str):
            return None
        member = str.__new__(cls, value)
        member._name_ = "UNKNOWN"
        member._value_ = value
        return member
