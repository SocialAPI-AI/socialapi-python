"""Retry logic with exponential backoff and jitter."""

from __future__ import annotations

import random
from typing import TYPE_CHECKING

from socialapi._constants import INITIAL_RETRY_DELAY, MAX_RETRY_DELAY

if TYPE_CHECKING:
    import httpx


class RetryHandler:
    """Handles retry logic for failed requests.

    Implements exponential backoff with full jitter for 5xx errors,
    platform rate limits (429), and network/timeout errors.
    Does not retry plan limit errors (429 ``rate_limit_exceeded``)
    or other 4xx errors.

    Args:
        max_retries: Maximum number of retry attempts.
    """

    def __init__(self, max_retries: int) -> None:
        self._max_retries = max_retries

    @property
    def max_retries(self) -> int:
        """Return the configured maximum number of retries."""
        return self._max_retries

    # ------------------------------------------------------------------
    # Public helpers
    # ------------------------------------------------------------------

    def should_retry(
        self,
        response: httpx.Response | None,
        attempt: int,
        *,
        is_network_error: bool = False,
    ) -> bool:
        """Determine whether the request should be retried.

        Args:
            response: The HTTP response, or ``None`` for network errors.
            attempt: The current attempt number (0-indexed).
            is_network_error: Whether the failure was a network/timeout error.

        Returns:
            ``True`` if the request should be retried.
        """
        if attempt >= self._max_retries:
            return False

        if is_network_error:
            return True

        if response is None:
            return False

        error_code = self._extract_error_code(response)
        return self.is_retryable_status(response.status_code, error_code)

    def is_retryable_status(self, status_code: int, error_code: str | None = None) -> bool:
        """Check whether a status code / error code combination is retryable.

        Args:
            status_code: The HTTP status code.
            error_code: The machine-readable error code from the response body.

        Returns:
            ``True`` if the error is retryable.
        """
        # 5xx errors are always retryable.
        if status_code >= 500:
            return True

        # 429: only retry platform rate limits, never plan limits.
        if status_code == 429:
            return error_code != "rate_limit_exceeded"

        return False

    def calculate_delay(self, attempt: int, response: httpx.Response | None = None) -> float:
        """Calculate the delay before the next retry attempt.

        Uses exponential backoff with full jitter, capped at
        ``MAX_RETRY_DELAY``. Respects the ``Retry-After`` header
        when present.

        Args:
            attempt: The current attempt number (0-indexed).
            response: The HTTP response (may contain ``Retry-After``).

        Returns:
            The delay in seconds before the next attempt.
        """
        # Honour Retry-After header if present.
        if response is not None:
            retry_after = response.headers.get("Retry-After")
            if retry_after is not None:
                try:
                    return max(0.0, float(retry_after))
                except (ValueError, TypeError):
                    pass

        # Exponential backoff: base * 2^attempt, capped.
        base_delay = min(INITIAL_RETRY_DELAY * (2**attempt), MAX_RETRY_DELAY)
        # Full jitter: uniform random in [0, base_delay].
        return random.uniform(0, base_delay)

    # ------------------------------------------------------------------
    # Internal
    # ------------------------------------------------------------------

    @staticmethod
    def _extract_error_code(response: httpx.Response) -> str | None:
        """Try to parse the ``code`` field from a JSON error body.

        Args:
            response: The HTTP response.

        Returns:
            The error code string, or ``None`` if parsing fails.
        """
        try:
            body = response.json()
            code = body.get("code")
            return str(code) if code is not None else None
        except Exception:
            return None
