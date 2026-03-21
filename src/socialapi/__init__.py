"""Official Python SDK for SocialAPI -- unified social media inbox API."""

from socialapi._async_client import AsyncSocialAPI
from socialapi._client import SocialAPI
from socialapi._exceptions import (
    AuthenticationError,
    ConflictError,
    InternalError,
    NotFoundError,
    NotSupportedError,
    PlanLimitError,
    PlatformRateLimitError,
    RateLimitError,
    SocialAPIError,
    StorageQuotaError,
    ValidationError,
)
from socialapi._version import __version__

__all__ = [
    "AsyncSocialAPI",
    "AuthenticationError",
    "ConflictError",
    "InternalError",
    "NotFoundError",
    "NotSupportedError",
    "PlanLimitError",
    "PlatformRateLimitError",
    "RateLimitError",
    "SocialAPI",
    "SocialAPIError",
    "StorageQuotaError",
    "ValidationError",
    "__version__",
]
