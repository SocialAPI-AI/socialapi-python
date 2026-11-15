from enum import StrEnum


class MediaFileType(StrEnum):
    MEDIA_FILE_TYPE_AUDIO = "audio"
    MEDIA_FILE_TYPE_FILE = "file"
    MEDIA_FILE_TYPE_IMAGE = "image"
    MEDIA_FILE_TYPE_VIDEO = "video"

    def __str__(self) -> str:
        return str(self.value)

    # Override (templates/str_enum.py.jinja): a value added to the API after this
    # SDK was released decodes as a pseudo-member instead of raising.
    @classmethod
    def _missing_(cls, value: object) -> "MediaFileType | None":
        if not isinstance(value, str):
            return None
        member = str.__new__(cls, value)
        member._name_ = "UNKNOWN"
        member._value_ = value
        return member
