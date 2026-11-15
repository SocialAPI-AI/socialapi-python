from enum import StrEnum


class ApiEndpointsCreateWebhookRequestEventsItem(StrEnum):
    ACCOUNT_CONNECTED = "account.connected"
    ACCOUNT_DISCONNECTED = "account.disconnected"
    ACCOUNT_UPDATED = "account.updated"
    COMMENT_RECEIVED = "comment.received"
    DM_DELETED = "dm.deleted"
    DM_POSTBACK = "dm.postback"
    DM_RECEIVED = "dm.received"
    DM_REFERRAL = "dm.referral"
    DM_SENT = "dm.sent"
    DM_STATUS_DELIVERED = "dm.status.delivered"
    DM_STATUS_FAILED = "dm.status.failed"
    DM_STATUS_READ = "dm.status.read"
    DM_STATUS_SENT = "dm.status.sent"
    MENTION_RECEIVED = "mention.received"
    PAGE_REMOVED = "page.removed"
    POST_DELETED = "post.deleted"
    POST_FAILED = "post.failed"
    POST_PARTIAL = "post.partial"
    POST_PUBLISHED = "post.published"
    POST_RETRIED = "post.retried"
    POST_SCHEDULED = "post.scheduled"
    POST_UNPUBLISHED = "post.unpublished"
    POST_UPDATED = "post.updated"
    REVIEW_RECEIVED = "review.received"
    REVIEW_UPDATED = "review.updated"

    def __str__(self) -> str:
        return str(self.value)

    # Override (templates/str_enum.py.jinja): a value added to the API after this
    # SDK was released decodes as a pseudo-member instead of raising.
    @classmethod
    def _missing_(cls, value: object) -> "ApiEndpointsCreateWebhookRequestEventsItem | None":
        if not isinstance(value, str):
            return None
        member = str.__new__(cls, value)
        member._name_ = "UNKNOWN"
        member._value_ = value
        return member
