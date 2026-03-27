from __future__ import annotations

from enum import StrEnum

# ---------------------------------------------------------------------------
# Default client configuration
# ---------------------------------------------------------------------------

DEFAULT_BASE_URL: str = "https://api.social-api.ai"
DEFAULT_TIMEOUT: float = 30.0
DEFAULT_MAX_RETRIES: int = 2
USER_AGENT_PREFIX: str = "socialapi-python"
API_KEY_ENV_VAR: str = "SOCIALAPI_API_KEY"
BASE_URL_ENV_VAR: str = "SOCIALAPI_BASE_URL"


# ---------------------------------------------------------------------------
# Platform identifiers
# ---------------------------------------------------------------------------


class Platform(StrEnum):
    """Supported social media platforms."""

    INSTAGRAM = "instagram"
    FACEBOOK = "facebook"
    THREADS = "threads"
    TIKTOK = "tiktok"
    GOOGLE = "google"
    LINKEDIN = "linkedin"


# ---------------------------------------------------------------------------
# Post status state machine
# ---------------------------------------------------------------------------


class PostStatus(StrEnum):
    """Post lifecycle states."""

    DRAFT = "draft"
    SCHEDULED = "scheduled"
    PUBLISHING = "publishing"
    PUBLISHED = "published"
    PARTIAL = "partial"
    FAILED = "failed"
    CANCELLED = "cancelled"


# ---------------------------------------------------------------------------
# Post target delivery status
# ---------------------------------------------------------------------------


class TargetStatus(StrEnum):
    """Per-platform target delivery states."""

    PENDING = "pending"
    PUBLISHING = "publishing"
    PUBLISHED = "published"
    FAILED = "failed"


# ---------------------------------------------------------------------------
# Visibility options
# ---------------------------------------------------------------------------


class Visibility(StrEnum):
    """Post visibility options."""

    PUBLIC = "public"
    PRIVATE = "private"
    CONNECTIONS_ONLY = "connections_only"


# ---------------------------------------------------------------------------
# Moderation actions
# ---------------------------------------------------------------------------


class ModerationAction(StrEnum):
    """Comment moderation operations."""

    HIDE = "hide"
    UNHIDE = "unhide"
    DELETE = "delete"


# ---------------------------------------------------------------------------
# Conversation status
# ---------------------------------------------------------------------------


class ConversationStatus(StrEnum):
    """DM conversation states."""

    ACTIVE = "active"
    ARCHIVED = "archived"


# ---------------------------------------------------------------------------
# Message direction
# ---------------------------------------------------------------------------


class MessageDirection(StrEnum):
    """Message flow direction."""

    INCOMING = "incoming"
    OUTGOING = "outgoing"


# ---------------------------------------------------------------------------
# Webhook event types
# ---------------------------------------------------------------------------


class WebhookEvent(StrEnum):
    """Subscribable webhook event types."""

    COMMENT_RECEIVED = "comment.received"
    DM_RECEIVED = "dm.received"
    REVIEW_RECEIVED = "review.received"
    MENTION_RECEIVED = "mention.received"


# ---------------------------------------------------------------------------
# Post target error categories
# ---------------------------------------------------------------------------


class ErrorCategory(StrEnum):
    """Structured error categories for failed post targets."""

    VALIDATION = "validation"
    AUTH = "auth"
    RATE_LIMIT = "rate_limit"
    PLATFORM = "platform"
    INTERNAL = "internal"


class ErrorCausedBy(StrEnum):
    """Who is responsible for the error."""

    USER = "user"
    PLATFORM = "platform"
    INTERNAL = "internal"
