from enum import StrEnum


class WebhookEventType(StrEnum):
    WEBHOOK_EVENT_ACCOUNT_CONNECTED = "account.connected"
    WEBHOOK_EVENT_ACCOUNT_DISCONNECTED = "account.disconnected"
    WEBHOOK_EVENT_ACCOUNT_UPDATED = "account.updated"
    WEBHOOK_EVENT_COMMENT_RECEIVED = "comment.received"
    WEBHOOK_EVENT_DM_DELETED = "dm.deleted"
    WEBHOOK_EVENT_DM_POSTBACK = "dm.postback"
    WEBHOOK_EVENT_DM_RECEIVED = "dm.received"
    WEBHOOK_EVENT_DM_REFERRAL = "dm.referral"
    WEBHOOK_EVENT_DM_SENT = "dm.sent"
    WEBHOOK_EVENT_DM_STATUS_DELIVERED = "dm.status.delivered"
    WEBHOOK_EVENT_DM_STATUS_FAILED = "dm.status.failed"
    WEBHOOK_EVENT_DM_STATUS_READ = "dm.status.read"
    WEBHOOK_EVENT_DM_STATUS_SENT = "dm.status.sent"
    WEBHOOK_EVENT_MENTION_RECEIVED = "mention.received"
    WEBHOOK_EVENT_PAGE_REMOVED = "page.removed"
    WEBHOOK_EVENT_POST_DELETED = "post.deleted"
    WEBHOOK_EVENT_POST_FAILED = "post.failed"
    WEBHOOK_EVENT_POST_PARTIAL = "post.partial"
    WEBHOOK_EVENT_POST_PUBLISHED = "post.published"
    WEBHOOK_EVENT_POST_RETRIED = "post.retried"
    WEBHOOK_EVENT_POST_SCHEDULED = "post.scheduled"
    WEBHOOK_EVENT_POST_UNPUBLISHED = "post.unpublished"
    WEBHOOK_EVENT_POST_UPDATED = "post.updated"
    WEBHOOK_EVENT_REVIEW_RECEIVED = "review.received"
    WEBHOOK_EVENT_REVIEW_UPDATED = "review.updated"

    def __str__(self) -> str:
        return str(self.value)

    # Override (templates/str_enum.py.jinja): a value added to the API after this
    # SDK was released decodes as a pseudo-member instead of raising.
    @classmethod
    def _missing_(cls, value: object) -> "WebhookEventType | None":
        if not isinstance(value, str):
            return None
        member = str.__new__(cls, value)
        member._name_ = "UNKNOWN"
        member._value_ = value
        return member
