"""Client configuration."""

from __future__ import annotations

from dataclasses import dataclass, field

from socialapi._constants import DEFAULT_BASE_URL, DEFAULT_MAX_RETRIES, DEFAULT_TIMEOUT


@dataclass(frozen=True)
class ClientConfig:
    """Configuration for the SocialAPI client.

    Attributes:
        api_key: The API key for authentication.
        base_url: The base URL of the SocialAPI server.
        timeout: Request timeout in seconds.
        max_retries: Maximum number of retries for failed requests.
    """

    api_key: str
    base_url: str = field(default=DEFAULT_BASE_URL)
    timeout: float = field(default=DEFAULT_TIMEOUT)
    max_retries: int = field(default=DEFAULT_MAX_RETRIES)
