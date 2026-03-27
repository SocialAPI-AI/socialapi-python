from __future__ import annotations

from typing import TYPE_CHECKING, Any

from socialapi.models.invites import Invite, InviteListItem

if TYPE_CHECKING:
    from socialapi._base_client import BaseAsyncClient, BaseSyncClient


class Invites:
    """Manage brand invites (sync)."""

    _client: BaseSyncClient

    def __init__(self, client: BaseSyncClient) -> None:
        self._client = client

    def create(
        self,
        *,
        brand_id: str,
        platform: str,
        expires_in_days: int = 7,
        timeout: float | None = None,
    ) -> Invite:
        """Create a single-use invite link for a brand.

        Args:
            brand_id: The brand to create the invite for.
            platform: Platform to connect (e.g. ``"facebook"``).
            expires_in_days: Days until the invite expires.
            timeout: Override the client-level timeout for this request.

        Returns:
            The created invite with token and URL.

        Raises:
            BadRequestError: If fields are missing or invalid.
            NotFoundError: If the brand does not exist.
            ConflictError: If an active invite already exists for this brand/platform.
            AuthenticationError: If the API key is invalid.
        """
        body: dict[str, Any] = {
            "brand_id": brand_id,
            "platform": platform,
            "expires_in_days": expires_in_days,
        }
        data = self._client._post("/v1/invites", json=body, timeout=timeout)
        return Invite.model_validate(data)

    def list(
        self,
        brand_id: str,
        *,
        timeout: float | None = None,
    ) -> list[InviteListItem]:
        """List invites for a brand.

        Args:
            brand_id: The brand ID.
            timeout: Override the client-level timeout for this request.

        Returns:
            A list of invites (active and expired/used).

        Raises:
            BadRequestError: If brand_id is missing.
            NotFoundError: If the brand does not exist.
            AuthenticationError: If the API key is invalid.
        """
        data = self._client._get("/v1/invites", params={"brand_id": brand_id}, timeout=timeout)
        raw_items: list[Any] = data.get("data", [])
        return [InviteListItem.model_validate(item) for item in raw_items]

    def revoke(
        self,
        invite_id: str,
        *,
        timeout: float | None = None,
    ) -> None:
        """Revoke an invite so it cannot be redeemed.

        Args:
            invite_id: The invite ID.
            timeout: Override the client-level timeout for this request.

        Raises:
            NotFoundError: If the invite does not exist or is already used.
            AuthenticationError: If the API key is invalid.
        """
        self._client._delete(f"/v1/invites/{invite_id}", timeout=timeout)


class AsyncInvites:
    """Manage brand invites (async)."""

    _client: BaseAsyncClient

    def __init__(self, client: BaseAsyncClient) -> None:
        self._client = client

    async def create(
        self,
        *,
        brand_id: str,
        platform: str,
        expires_in_days: int = 7,
        timeout: float | None = None,
    ) -> Invite:
        """Create a single-use invite link for a brand.

        Args:
            brand_id: The brand to create the invite for.
            platform: Platform to connect (e.g. ``"facebook"``).
            expires_in_days: Days until the invite expires.
            timeout: Override the client-level timeout for this request.

        Returns:
            The created invite with token and URL.

        Raises:
            BadRequestError: If fields are missing or invalid.
            NotFoundError: If the brand does not exist.
            ConflictError: If an active invite already exists for this brand/platform.
            AuthenticationError: If the API key is invalid.
        """
        body: dict[str, Any] = {
            "brand_id": brand_id,
            "platform": platform,
            "expires_in_days": expires_in_days,
        }
        data = await self._client._post("/v1/invites", json=body, timeout=timeout)
        return Invite.model_validate(data)

    async def list(
        self,
        brand_id: str,
        *,
        timeout: float | None = None,
    ) -> list[InviteListItem]:
        """List invites for a brand.

        Args:
            brand_id: The brand ID.
            timeout: Override the client-level timeout for this request.

        Returns:
            A list of invites (active and expired/used).

        Raises:
            BadRequestError: If brand_id is missing.
            NotFoundError: If the brand does not exist.
            AuthenticationError: If the API key is invalid.
        """
        data = await self._client._get("/v1/invites", params={"brand_id": brand_id}, timeout=timeout)
        raw_items: list[Any] = data.get("data", [])
        return [InviteListItem.model_validate(item) for item in raw_items]

    async def revoke(
        self,
        invite_id: str,
        *,
        timeout: float | None = None,
    ) -> None:
        """Revoke an invite so it cannot be redeemed.

        Args:
            invite_id: The invite ID.
            timeout: Override the client-level timeout for this request.

        Raises:
            NotFoundError: If the invite does not exist or is already used.
            AuthenticationError: If the API key is invalid.
        """
        await self._client._delete(f"/v1/invites/{invite_id}", timeout=timeout)
