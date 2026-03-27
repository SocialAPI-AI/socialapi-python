from __future__ import annotations

from typing import Any

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
        message: Human-readable error message from the ``error`` JSON field.
        code: Machine-readable error code from the ``code`` JSON field, if present.
        response: The raw ``httpx.Response`` for further inspection.
        body: Parsed JSON body, if available.
    """

    status_code: int
    code: str | None
    response: httpx.Response
    body: dict[str, Any] | None

    def __init__(
        self,
        message: str,
        *,
        status_code: int,
        code: str | None = None,
        response: httpx.Response,
        body: dict[str, Any] | None = None,
    ) -> None:
        super().__init__(message)
        self.status_code = status_code
        self.code = code
        self.response = response
        self.body = body

    @classmethod
    def from_response(cls, response: httpx.Response) -> APIStatusError:
        """Build the most specific exception subclass from an httpx response."""
        body: dict[str, Any] | None = None
        message = f"HTTP {response.status_code}"
        code: str | None = None

        try:
            body = response.json()
            if isinstance(body, dict):
                message = body.get("error", message)
                code = body.get("code")
        except Exception:
            pass

        error_class = _STATUS_CODE_MAP.get(response.status_code, APIStatusError)
        return error_class(
            message,
            status_code=response.status_code,
            code=code,
            response=response,
            body=body,
        )

    def __repr__(self) -> str:
        return f"{type(self).__name__}(status_code={self.status_code}, code={self.code!r}, message={self.message!r})"


class BadRequestError(APIStatusError):
    """400 Bad Request — invalid parameters, missing metadata, or unsupported platform."""


class AuthenticationError(APIStatusError):
    """401 Unauthorized — invalid API key, expired token, or missing credentials."""


class NotFoundError(APIStatusError):
    """404 Not Found — the requested resource does not exist."""


class ConflictError(APIStatusError):
    """409 Conflict — e.g. account already linked."""


class StorageQuotaExceededError(APIStatusError):
    """413 Payload Too Large — storage quota exceeded."""


class RateLimitError(APIStatusError):
    """429 Too Many Requests — API or platform rate limit exceeded."""


class InternalServerError(APIStatusError):
    """500 Internal Server Error — unexpected server failure."""


class NotSupportedError(APIStatusError):
    """501 Not Implemented — the platform does not support this operation."""


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
    404: NotFoundError,
    409: ConflictError,
    413: StorageQuotaExceededError,
    429: RateLimitError,
    500: InternalServerError,
    501: NotSupportedError,
}
