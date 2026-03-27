from __future__ import annotations

from typing import TYPE_CHECKING, Any

from socialapi.models.users import User

if TYPE_CHECKING:
    from socialapi._base_client import BaseAsyncClient, BaseSyncClient


class Users:
    """Manage the authenticated user profile (sync)."""

    _client: BaseSyncClient

    def __init__(self, client: BaseSyncClient) -> None:
        self._client = client

    def get_me(
        self,
        *,
        timeout: float | None = None,
    ) -> User:
        """Get the authenticated user's profile.

        Args:
            timeout: Override the client-level timeout for this request.

        Returns:
            The current user.

        Raises:
            AuthenticationError: If the API key is invalid.
        """
        data = self._client._get("/v1/users/me", timeout=timeout)
        return User.model_validate(data)

    def update_me(
        self,
        *,
        onboarding: bool | None = None,
        use_case: str | None = None,
        referral: str | None = None,
        timeout: float | None = None,
    ) -> User:
        """Update the authenticated user's profile.

        Args:
            onboarding: Set to ``False`` to mark onboarding as complete.
            use_case: User's primary use case description.
            referral: How the user found SocialAPI.
            timeout: Override the client-level timeout for this request.

        Returns:
            The updated user.

        Raises:
            AuthenticationError: If the API key is invalid.
        """
        body: dict[str, Any] = {}
        if onboarding is not None:
            body["onboarding"] = onboarding
        if use_case is not None:
            body["use_case"] = use_case
        if referral is not None:
            body["referral"] = referral
        data = self._client._patch("/v1/users/me", json=body, timeout=timeout)
        return User.model_validate(data)

    def delete_me(
        self,
        *,
        timeout: float | None = None,
    ) -> None:
        """Delete the authenticated user's account and all associated data.

        Args:
            timeout: Override the client-level timeout for this request.

        Raises:
            AuthenticationError: If the API key is invalid.
        """
        self._client._delete("/v1/users/me", timeout=timeout)


class AsyncUsers:
    """Manage the authenticated user profile (async)."""

    _client: BaseAsyncClient

    def __init__(self, client: BaseAsyncClient) -> None:
        self._client = client

    async def get_me(
        self,
        *,
        timeout: float | None = None,
    ) -> User:
        """Get the authenticated user's profile.

        Args:
            timeout: Override the client-level timeout for this request.

        Returns:
            The current user.

        Raises:
            AuthenticationError: If the API key is invalid.
        """
        data = await self._client._get("/v1/users/me", timeout=timeout)
        return User.model_validate(data)

    async def update_me(
        self,
        *,
        onboarding: bool | None = None,
        use_case: str | None = None,
        referral: str | None = None,
        timeout: float | None = None,
    ) -> User:
        """Update the authenticated user's profile.

        Args:
            onboarding: Set to ``False`` to mark onboarding as complete.
            use_case: User's primary use case description.
            referral: How the user found SocialAPI.
            timeout: Override the client-level timeout for this request.

        Returns:
            The updated user.

        Raises:
            AuthenticationError: If the API key is invalid.
        """
        body: dict[str, Any] = {}
        if onboarding is not None:
            body["onboarding"] = onboarding
        if use_case is not None:
            body["use_case"] = use_case
        if referral is not None:
            body["referral"] = referral
        data = await self._client._patch("/v1/users/me", json=body, timeout=timeout)
        return User.model_validate(data)

    async def delete_me(
        self,
        *,
        timeout: float | None = None,
    ) -> None:
        """Delete the authenticated user's account and all associated data.

        Args:
            timeout: Override the client-level timeout for this request.

        Raises:
            AuthenticationError: If the API key is invalid.
        """
        await self._client._delete("/v1/users/me", timeout=timeout)
