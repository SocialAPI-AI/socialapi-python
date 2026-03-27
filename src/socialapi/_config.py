from __future__ import annotations

from dataclasses import dataclass

from socialapi._constants import DEFAULT_BASE_URL, DEFAULT_MAX_RETRIES, DEFAULT_TIMEOUT


@dataclass(frozen=True)
class ClientConfig:
    """Immutable configuration for ``SocialAPI`` and ``AsyncSocialAPI`` clients.

    Attributes:
        api_key: Bearer token sent with every request.
        base_url: API root URL (no trailing slash).
        timeout: Request timeout in seconds.
        max_retries: Maximum number of automatic retries (0 disables retries).
        debug: When ``True``, log request/response details via the ``socialapi`` logger.
    """

    api_key: str
    base_url: str = DEFAULT_BASE_URL
    timeout: float = DEFAULT_TIMEOUT
    max_retries: int = DEFAULT_MAX_RETRIES
    debug: bool = False
