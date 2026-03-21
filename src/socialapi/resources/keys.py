"""API keys resource."""

from __future__ import annotations

from typing import TYPE_CHECKING

from socialapi.models.keys import CreateKeyResponse, KeysListResponse
from socialapi.models.shared import OKResponse

if TYPE_CHECKING:
    from socialapi._async_client import AsyncSocialAPI
    from socialapi._client import SocialAPI


class Keys:
    """Synchronous API keys resource.

    Provides methods for listing, creating, and revoking API keys.
    """

    def __init__(self, client: SocialAPI) -> None:
        self._client = client

    def list(self) -> KeysListResponse:
        """List all API keys for the authenticated user.

        Returns:
            A KeysListResponse containing the API key summaries.

        Raises:
            AuthenticationError: If the API key is invalid.
        """
        return self._client._get("/v1/keys", response_model=KeysListResponse)

    def create(self, name: str) -> CreateKeyResponse:
        """Create a new API key.

        Args:
            name: A descriptive name for the new key.

        Returns:
            A CreateKeyResponse containing the new key details including the raw key.

        Raises:
            ValidationError: If the name is empty or invalid.
        """
        return self._client._post("/v1/keys", json_data={"name": name}, response_model=CreateKeyResponse)

    def revoke(self, key_id: str) -> OKResponse:
        """Revoke an API key.

        Args:
            key_id: The ID of the key to revoke.

        Returns:
            An OKResponse indicating the key was revoked.

        Raises:
            NotFoundError: If the key is not found.
        """
        return self._client._delete(f"/v1/keys/{key_id}", response_model=OKResponse)


class AsyncKeys:
    """Asynchronous API keys resource.

    Provides methods for listing, creating, and revoking API keys.
    """

    def __init__(self, client: AsyncSocialAPI) -> None:
        self._client = client

    async def list(self) -> KeysListResponse:
        """List all API keys for the authenticated user.

        Returns:
            A KeysListResponse containing the API key summaries.

        Raises:
            AuthenticationError: If the API key is invalid.
        """
        return await self._client._get("/v1/keys", response_model=KeysListResponse)

    async def create(self, name: str) -> CreateKeyResponse:
        """Create a new API key.

        Args:
            name: A descriptive name for the new key.

        Returns:
            A CreateKeyResponse containing the new key details including the raw key.

        Raises:
            ValidationError: If the name is empty or invalid.
        """
        return await self._client._post("/v1/keys", json_data={"name": name}, response_model=CreateKeyResponse)

    async def revoke(self, key_id: str) -> OKResponse:
        """Revoke an API key.

        Args:
            key_id: The ID of the key to revoke.

        Returns:
            An OKResponse indicating the key was revoked.

        Raises:
            NotFoundError: If the key is not found.
        """
        return await self._client._delete(f"/v1/keys/{key_id}", response_model=OKResponse)
