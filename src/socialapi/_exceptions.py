"""Exception hierarchy for the SocialAPI SDK."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    import httpx


class SocialAPIError(Exception):
    """Base exception for all SocialAPI errors.

    Attributes:
        message: Human-readable error message from the API.
        code: Machine-readable error code from the API.
        status_code: HTTP status code of the response.
        response: The raw httpx.Response object.
    """

    message: str
    code: str
    status_code: int
    response: httpx.Response

    def __init__(
        self,
        message: str,
        *,
        code: str,
        status_code: int,
        response: httpx.Response,
    ) -> None:
        super().__init__(message)
        self.message = message
        self.code = code
        self.status_code = status_code
        self.response = response

    def __repr__(self) -> str:
        return f"{type(self).__name__}(message={self.message!r}, code={self.code!r}, status_code={self.status_code})"


class AuthenticationError(SocialAPIError):
    """Raised for 401 errors (unauthorized, invalid_token, invalid_credentials)."""


class ValidationError(SocialAPIError):
    """Raised for 400 errors (bad_request, unsupported_platform, missing_metadata)."""


class NotFoundError(SocialAPIError):
    """Raised for 404 errors (not_found, account_not_found)."""


class ConflictError(SocialAPIError):
    """Raised for 409 errors (account_already_linked)."""


class StorageQuotaError(SocialAPIError):
    """Raised for 413 errors (storage_quota_exceeded)."""


class RateLimitError(SocialAPIError):
    """Raised for 429 errors. Base class for plan and platform rate limits."""


class PlanLimitError(RateLimitError):
    """Raised when the monthly resource limit is exceeded (rate_limit_exceeded)."""


class PlatformRateLimitError(RateLimitError):
    """Raised when the upstream platform's rate limit is hit (platform_rate_limit)."""


class InternalError(SocialAPIError):
    """Raised for 500 errors (internal_error)."""


class NotSupportedError(SocialAPIError):
    """Raised for 501 errors (not_supported, not_implemented)."""


# ---------------------------------------------------------------------------
# Mapping tables
# ---------------------------------------------------------------------------

ERROR_CODE_MAP: dict[str, type[SocialAPIError]] = {
    "unauthorized": AuthenticationError,
    "invalid_token": AuthenticationError,
    "invalid_credentials": AuthenticationError,
    "not_found": NotFoundError,
    "account_not_found": NotFoundError,
    "bad_request": ValidationError,
    "unsupported_platform": ValidationError,
    "missing_metadata": ValidationError,
    "account_already_linked": ConflictError,
    "storage_quota_exceeded": StorageQuotaError,
    "rate_limit_exceeded": PlanLimitError,
    "platform_rate_limit": PlatformRateLimitError,
    "not_supported": NotSupportedError,
    "not_implemented": NotSupportedError,
    "internal_error": InternalError,
}

STATUS_CODE_MAP: dict[int, type[SocialAPIError]] = {
    400: ValidationError,
    401: AuthenticationError,
    404: NotFoundError,
    409: ConflictError,
    413: StorageQuotaError,
    429: RateLimitError,
    500: InternalError,
    501: NotSupportedError,
}


def raise_for_status(response: httpx.Response) -> None:
    """Parse an error response and raise the appropriate exception.

    Attempts to parse the JSON body ``{"error": "...", "code": "..."}``
    from the response. Falls back to a generic ``SocialAPIError`` when
    JSON parsing fails or the error code is unrecognized.

    Args:
        response: The httpx response to inspect.

    Raises:
        SocialAPIError: Or a more specific subclass based on the error code
            and HTTP status code.
    """
    if response.is_success:
        return

    message = "Unknown error"
    code = "unknown"

    try:
        body: dict[str, Any] = response.json()
        message = body.get("error", message)
        code = body.get("code", code)
    except Exception:
        message = response.text or message

    # Prefer error-code-based mapping for precision.
    exc_cls = ERROR_CODE_MAP.get(code)
    if exc_cls is None:
        exc_cls = STATUS_CODE_MAP.get(response.status_code, SocialAPIError)

    raise exc_cls(
        message,
        code=code,
        status_code=response.status_code,
        response=response,
    )
