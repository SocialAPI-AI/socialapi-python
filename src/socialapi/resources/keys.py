from __future__ import annotations

from typing import TYPE_CHECKING, Any

from socialapi.models.keys import APIKey, CreateKeyResponse

if TYPE_CHECKING:
    from socialapi._base_client import BaseAsyncClient, BaseSyncClient


class Keys:
    """Manage API keys (sync)."""

    _client: BaseSyncClient

    def __init__(self, client: BaseSyncClient) -> None:
        self._client = client

    def list(
        self,
        *,
        timeout: float | None = None,
    ) -> list[APIKey]:
        """List all API keys for the current user.

        Args:
            timeout: Override the client-level timeout for this request.

        Returns:
            A list of API keys (secrets are never included).

        Raises:
            AuthenticationError: If the API key is invalid.
        """
        data = self._client._get("/v1/keys", timeout=timeout)
        raw_items: list[Any] = data.get("data", [])
        return [APIKey.model_validate(item) for item in raw_items]

    def create(
        self,
        *,
        name: str,
        timeout: float | None = None,
    ) -> CreateKeyResponse:
        """Create a new API key.

        Args:
            name: Human-readable name for the key.
            timeout: Override the client-level timeout for this request.

        Returns:
            The new key details including the raw secret (shown once).

        Raises:
            AuthenticationError: If the API key is invalid.
        """
        data = self._client._post("/v1/keys", json={"name": name}, timeout=timeout)
        return CreateKeyResponse.model_validate(data)

    def revoke(
        self,
        key_id: str,
        *,
        timeout: float | None = None,
    ) -> None:
        """Revoke (delete) an API key.

        Args:
            key_id: The key ID to revoke.
            timeout: Override the client-level timeout for this request.

        Raises:
            NotFoundError: If the key does not exist.
            AuthenticationError: If the API key is invalid.
        """
        self._client._delete(f"/v1/keys/{key_id}", timeout=timeout)


class AsyncKeys:
    """Manage API keys (async)."""

    _client: BaseAsyncClient

    def __init__(self, client: BaseAsyncClient) -> None:
        self._client = client

    async def list(
        self,
        *,
        timeout: float | None = None,
    ) -> list[APIKey]:
        """List all API keys for the current user.

        Args:
            timeout: Override the client-level timeout for this request.

        Returns:
            A list of API keys (secrets are never included).

        Raises:
            AuthenticationError: If the API key is invalid.
        """
        data = await self._client._get("/v1/keys", timeout=timeout)
        raw_items: list[Any] = data.get("data", [])
        return [APIKey.model_validate(item) for item in raw_items]

    async def create(
        self,
        *,
        name: str,
        timeout: float | None = None,
    ) -> CreateKeyResponse:
        """Create a new API key.

        Args:
            name: Human-readable name for the key.
            timeout: Override the client-level timeout for this request.

        Returns:
            The new key details including the raw secret (shown once).

        Raises:
            AuthenticationError: If the API key is invalid.
        """
        data = await self._client._post("/v1/keys", json={"name": name}, timeout=timeout)
        return CreateKeyResponse.model_validate(data)

    async def revoke(
        self,
        key_id: str,
        *,
        timeout: float | None = None,
    ) -> None:
        """Revoke (delete) an API key.

        Args:
            key_id: The key ID to revoke.
            timeout: Override the client-level timeout for this request.

        Raises:
            NotFoundError: If the key does not exist.
            AuthenticationError: If the API key is invalid.
        """
        await self._client._delete(f"/v1/keys/{key_id}", timeout=timeout)
