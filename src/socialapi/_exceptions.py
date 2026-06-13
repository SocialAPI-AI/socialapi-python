from __future__ import annotations

from typing import Any, cast

import httpx  # noqa: TC002


class SocialAPIError(Exception):
    """Base exception for all SocialAPI SDK errors."""

    message: str

    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message


class APIStatusError(SocialAPIError):
    """An HTTP error response (4xx/5xx) was received from the API.

    Attributes:
        status_code: HTTP status code.
        message: Human-readable error message from the nested ``error.message`` JSON field.
        code: Machine-readable error code from the nested ``error.code`` JSON field, if present.
        request_id: The ``request_id`` from the response envelope, if present.
        response: The raw ``httpx.Response`` for further inspection.
        body: Parsed JSON body, if available.

    The API emits a nested error envelope::

        {
            "error": {"code": "account.not_found", "message": "Account not found", "meta": {...}},
            "request_id": "req_abc123"
        }

    Legacy flat responses (``{"error": "msg", "code": "..."}`` shape) are also accepted
    for back-compatibility.
    """

    status_code: int
    code: str | None
    request_id: str | None
    response: httpx.Response
    body: dict[str, Any] | None

    def __init__(
        self,
        message: str,
        *,
        status_code: int,
        code: str | None = None,
        request_id: str | None = None,
        response: httpx.Response,
        body: dict[str, Any] | None = None,
    ) -> None:
        super().__init__(message)
        self.status_code = status_code
        self.code = code
        self.request_id = request_id
        self.response = response
        self.body = body

    @classmethod
    def from_response(cls, response: httpx.Response) -> APIStatusError:
        """Build the most specific exception subclass from an httpx response.

        Parses both the nested envelope shape emitted by the API::

            {"error": {"code": "...", "message": "..."}, "request_id": "..."}

        and the legacy flat shape for back-compatibility::

            {"error": "msg", "code": "..."}
        """
        body: dict[str, Any] | None = None
        message = f"HTTP {response.status_code}"
        code: str | None = None
        request_id: str | None = None

        try:
            body = response.json()
            if isinstance(body, dict):
                request_id_raw: Any = body.get("request_id")
                if isinstance(request_id_raw, str):
                    request_id = request_id_raw
                err: Any = body.get("error")
                if isinstance(err, dict):
                    # Nested envelope: {"error": {"code": "...", "message": "..."}}
                    err_dict: dict[str, Any] = cast("dict[str, Any]", err)
                    msg_val: Any = err_dict.get("message")
                    if isinstance(msg_val, str) and msg_val:
                        message = msg_val
                    code_val: Any = err_dict.get("code")
                    if isinstance(code_val, str):
                        code = code_val
                elif isinstance(err, str):
                    # Legacy flat envelope: {"error": "msg", "code": "..."}
                    message = err
                    code_val2: Any = body.get("code")
                    if isinstance(code_val2, str):
                        code = code_val2
        except Exception:
            pass

        # Try exact code-specific mapping first
        error_class: type[APIStatusError] | None = None
        if code is not None:
            error_class = _ERROR_CODE_MAP.get(code)
            # Suffix-based dynamic matching for per-platform code families
            if error_class is None:
                if code.endswith(".rate_limit"):
                    error_class = PlatformRateLimitError
                elif code.endswith(".auth"):
                    error_class = AuthenticationError
        # Fall back to HTTP status code mapping
        if error_class is None:
            error_class = _STATUS_CODE_MAP.get(response.status_code, APIStatusError)
        return error_class(
            message,
            status_code=response.status_code,
            code=code,
            request_id=request_id,
            response=response,
            body=body,
        )

    def __repr__(self) -> str:
        return f"{type(self).__name__}(status_code={self.status_code}, code={self.code!r}, message={self.message!r})"


class BadRequestError(APIStatusError):
    """400 Bad Request -- invalid parameters, missing metadata, or unsupported platform."""


class UnsupportedPlatformError(BadRequestError):
    """400 Bad Request -- unsupported platform."""


class MissingMetadataError(BadRequestError):
    """400 Bad Request -- missing required metadata."""


class AuthenticationError(APIStatusError):
    """401 Unauthorized -- invalid API key, expired token, or missing credentials."""


class InvalidTokenError(AuthenticationError):
    """401 Unauthorized -- invalid token."""


class InvalidCredentialsError(AuthenticationError):
    """401 Unauthorized -- invalid credentials."""


class ForbiddenError(APIStatusError):
    """403 Forbidden -- access denied (e.g. brand limit reached)."""


class NotFoundError(APIStatusError):
    """404 Not Found -- the requested resource does not exist."""


class AccountNotFoundError(NotFoundError):
    """404 Not Found -- the connected account does not exist."""


class ConflictError(APIStatusError):
    """409 Conflict -- e.g. account already linked."""


class AccountAlreadyLinkedError(ConflictError):
    """409 Conflict -- account is already linked."""


class GoneError(APIStatusError):
    """410 Gone -- the resource is no longer available, e.g. an expired invite."""


class StorageQuotaExceededError(APIStatusError):
    """413 Payload Too Large -- storage quota exceeded."""


class RateLimitError(APIStatusError):
    """429 Too Many Requests -- API or platform rate limit exceeded."""


class PlatformRateLimitError(RateLimitError):
    """429 Too Many Requests -- platform-specific rate limit exceeded."""


class InternalServerError(APIStatusError):
    """500 Internal Server Error -- unexpected server failure."""


class NotSupportedError(APIStatusError):
    """501 Not Implemented -- the platform does not support this operation."""


class APIConnectionError(SocialAPIError):
    """A network-level failure prevented the request from completing.

    This covers DNS resolution errors, connection refused, TLS failures,
    and any other transport-layer problem.
    """

    request: httpx.Request | None

    def __init__(self, message: str, *, request: httpx.Request | None = None) -> None:
        super().__init__(message)
        self.request = request


class APITimeoutError(APIConnectionError):
    """The request timed out before receiving a complete response."""


# ---------------------------------------------------------------------------
# Internal mapping: HTTP status code -> exception class
# ---------------------------------------------------------------------------

_STATUS_CODE_MAP: dict[int, type[APIStatusError]] = {
    400: BadRequestError,
    401: AuthenticationError,
    403: ForbiddenError,
    404: NotFoundError,
    409: ConflictError,
    410: GoneError,
    413: StorageQuotaExceededError,
    429: RateLimitError,
    500: InternalServerError,
    501: NotSupportedError,
}

# ---------------------------------------------------------------------------
# Internal mapping: error code -> exception class (more specific)
# ---------------------------------------------------------------------------
#
# Keys are the real dot-notation codes emitted by the API (see core/api/connectors/base/errors.go).
# Legacy underscore keys are kept for back-compatibility but are secondary.
# Per-platform suffix families (*.rate_limit, *.auth) are handled dynamically in
# from_response() since they cannot be enumerated here.

_ERROR_CODE_MAP: dict[str, type[APIStatusError]] = {
    # --- account codes ---
    "account.not_found": AccountNotFoundError,
    "account.already_linked": AccountAlreadyLinkedError,
    "account.reconnection_required": ForbiddenError,
    "account.unsupported_platform": UnsupportedPlatformError,
    # --- resource / generic not-found ---
    "resource.not_found": NotFoundError,
    "resource.not_supported": NotSupportedError,
    # --- validation codes ---
    "validation.field_required": MissingMetadataError,
    # --- media codes ---
    "media.not_found": NotFoundError,
    "media.in_use": ConflictError,
    # --- brand codes ---
    "brand.not_found": NotFoundError,
    "brand.limit_reached": ForbiddenError,
    # --- billing codes ---
    "billing.storage_quota": StorageQuotaExceededError,
    # --- invite codes ---
    "invite.expired": GoneError,
    "invite.invalid": BadRequestError,
    # --- conversation / post codes ---
    "conversation.not_found": NotFoundError,
    "post.not_found": NotFoundError,
    "post.state_invalid": ConflictError,
    "post.no_retryable_deliveries": BadRequestError,
    # --- BYOK codes ---
    "byok.credentials_missing": ForbiddenError,
    "byok.credentials_invalid": AuthenticationError,
    "byok.credentials_forbidden": ForbiddenError,
    "byok.test_rate_limited": RateLimitError,
    # --- system codes ---
    "system.internal": InternalServerError,
    # --- HTTP fiber wrapper codes ---
    "http.400": BadRequestError,
    "http.401": AuthenticationError,
    "http.403": ForbiddenError,
    "http.404": NotFoundError,
    "http.409": ConflictError,
    "http.429": RateLimitError,
    "http.500": InternalServerError,
    "http.501": NotSupportedError,
    # --- legacy underscore keys (back-compat, kept harmless) ---
    "unsupported_platform": UnsupportedPlatformError,
    "missing_metadata": MissingMetadataError,
    "invalid_token": InvalidTokenError,
    "invalid_credentials": InvalidCredentialsError,
    "account_not_found": AccountNotFoundError,
    "account_already_linked": AccountAlreadyLinkedError,
    "platform_rate_limit": PlatformRateLimitError,
    "storage_quota_exceeded": StorageQuotaExceededError,
    "rate_limit_exceeded": RateLimitError,
    "not_supported": NotSupportedError,
    "not_found": NotFoundError,
    "unauthorized": AuthenticationError,
}
