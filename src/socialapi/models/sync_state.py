from enum import StrEnum


class SyncState(StrEnum):
    SYNC_STATE_FAILED = "failed"
    SYNC_STATE_IDLE = "idle"
    SYNC_STATE_SYNCING = "syncing"
    SYNC_STATE_UNSCOPED = ""

    def __str__(self) -> str:
        return str(self.value)

    # Override (templates/str_enum.py.jinja): a value added to the API after this
    # SDK was released decodes as a pseudo-member instead of raising.
    @classmethod
    def _missing_(cls, value: object) -> "SyncState | None":
        if not isinstance(value, str):
            return None
        member = str.__new__(cls, value)
        member._name_ = "UNKNOWN"
        member._value_ = value
        return member
