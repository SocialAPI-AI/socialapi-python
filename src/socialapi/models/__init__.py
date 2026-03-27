from __future__ import annotations

from socialapi.models.accounts import (
    Account,
    ConnectAccountRequest,
    ConnectAccountResponse,
    ConnectOAuthResponse,
    OAuthExchangeRequest,
    OAuthExchangeResponse,
)
from socialapi.models.comments import (
    CommentCapabilities,
    CommentedPost,
    InboxComment,
    PrivateReplyRequest,
    ReplyToCommentRequest,
    ReplyToCommentResponse,
)
from socialapi.models.conversations import (
    Conversation,
    Message,
    SendMessageRequest,
    SendMessageResponse,
    UpdateConversationRequest,
)
from socialapi.models.feedback import SendFeedbackRequest
from socialapi.models.keys import APIKey, CreateKeyRequest, CreateKeyResponse
from socialapi.models.mentions import Mention, MentionAuthor, MentionContent, MentionMedia
from socialapi.models.posts import (
    Post,
    PostMetrics,
    PostTarget,
    PostTargetError,
    PostTargetMetrics,
    ValidationIssue,
    ValidationResult,
)
from socialapi.models.publishing import (
    CreatePostRequest,
    MediaUploadResponse,
    MediaUploadURL,
    PlatformConstraints,
    TargetRequest,
    UnpublishRequest,
    UpdatePostRequest,
    ValidatePostRequest,
)
from socialapi.models.reviews import (
    ReplyToReviewRequest,
    ReplyToReviewResponse,
    Review,
    UpdateReviewReplyRequest,
)
from socialapi.models.usage import AccountLimits, UsageResponse
from socialapi.models.users import UpdateUserRequest, User
from socialapi.models.webhooks import (
    CreateWebhookRequest,
    CreateWebhookResponse,
    UpdateWebhookRequest,
    Webhook,
)

__all__: list[str] = [
    # keys
    "APIKey",
    # accounts
    "Account",
    # usage
    "AccountLimits",
    # comments
    "CommentCapabilities",
    "CommentedPost",
    "ConnectAccountRequest",
    "ConnectAccountResponse",
    "ConnectOAuthResponse",
    # conversations
    "Conversation",
    "CreateKeyRequest",
    "CreateKeyResponse",
    # publishing
    "CreatePostRequest",
    # webhooks
    "CreateWebhookRequest",
    "CreateWebhookResponse",
    "InboxComment",
    "MediaUploadResponse",
    "MediaUploadURL",
    # mentions
    "Mention",
    "MentionAuthor",
    "MentionContent",
    "MentionMedia",
    "Message",
    "OAuthExchangeRequest",
    "OAuthExchangeResponse",
    "PlatformConstraints",
    # posts
    "Post",
    "PostMetrics",
    "PostTarget",
    "PostTargetError",
    "PostTargetMetrics",
    "PrivateReplyRequest",
    "ReplyToCommentRequest",
    "ReplyToCommentResponse",
    # reviews
    "ReplyToReviewRequest",
    "ReplyToReviewResponse",
    "Review",
    # feedback
    "SendFeedbackRequest",
    "SendMessageRequest",
    "SendMessageResponse",
    "TargetRequest",
    "UnpublishRequest",
    "UpdateConversationRequest",
    "UpdatePostRequest",
    "UpdateReviewReplyRequest",
    # users
    "UpdateUserRequest",
    "UpdateWebhookRequest",
    "UsageResponse",
    "User",
    "ValidatePostRequest",
    "ValidationIssue",
    "ValidationResult",
    "Webhook",
]
